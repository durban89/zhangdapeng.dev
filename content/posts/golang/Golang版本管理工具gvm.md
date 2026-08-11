---
title: "Golang版本管理工具gvm"
date: "2025-08-04 18:08:01"
slug: "golang-ban-ben-guan-li-gong-ju-gvm"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang版本管理工具gvm/"
  - "/2025/08/04/Golang版本管理工具gvm.html"
  - "/Golang版本管理工具gvm/"
  - "/Golang版本管理工具gvm.html"
  - "/2025/08/04/golang-ban-ben-guan-li-gong-ju-gvm/"
  - "/2025/08/04/golang-ban-ben-guan-li-gong-ju-gvm.html"
  - "/golang-ban-ben-guan-li-gong-ju-gvm.html"
---
如果你是做开发的，那么版本的兼容性有时候很重要，但是如何才能做到多个版本共存呢，建议使用gvm

### 安装

具体的安装方式官网已经有了一个很好的介绍了，请点击(这里)[<https://github.com/moovweb/gvm>]

bash的安装方式，执行下面这个命令

```bash
bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

zsh的安装方式

```bash
zsh < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

安装完之后建议先安装go1.4这个版本，主要是因为go1.5+之后的版本已经移除了c编译直接用go替换了，如果没有安装go的话是没有办法安装后面的版本的，这块的记忆间隔时间比较久了，如果可以直接安装最新版本的话我会继续来更新此处的记录。

安装命令如下

```bash
gvm install go[版本号]
```

如果安装慢的话，建议加个代理，毕竟人家在国外，有时候访问要绕很远才能访问到

卸载命令如下

```bash
go implode
```

这个命令会完全的移除gvm和所有安装的包和go版本，**所以使用的时候小心**

### 正确的使用方式

gvm既然作为一个版本管理器，就会有一个问题，就是我们的一个项目，在运行的时候，具体选择哪个版本来运行，以及测试的时候需要确定使用哪个版本来运行的问题

那么既然gvm作为一个管理版本的工具，gvm就有这个功能提供给我们使用

比如我们的项目在`~/go/src/wiki-blog`的目录下面

然后运行下面代码

```bash
$ go version
go version go1.13.1 darwin/amd64
cd ~/go/src/wiki-blog
$ gvm linkthis
/xxx/xxx/.gvm/pkgsets/go1.13.1/global/src/wiki-blog -> /xxx/xxx/go/src/wiki-blog
```

从上面的执行看出来，当前的go版本是1.13.1，所以link之后，会将我们的项目软连接到`/xxx/xxx/.gvm/pkgsets/go1.13.1/global/src`目录下面。

```bash
$ ll /xxx/xxx/.gvm/pkgsets/go1.13.1/global/src
lrwxr-xr-x  1 durban  staff    29B 12 27 17:51 wiki-web -> /xxx/xxx/go/src/wiki-web
```

最后开发的时候我们进入`/xxx/xxx/go/src/wiki-blog`目录，运行和编译的时候依然不会有任何影响，如果我们后面增加了一个新的版本

```bash
$ gvm install go1.13.5
Updating Go source...
Installing go1.13.5...
* Compiling...
go1.13.5 successfully installed!
```

只要我们安装版本后，并执行命令`gvm use go1.13.5 --default` 然后再次执行命令

```bash
$ go version
go version go1.13.5 darwin/amd64

cd ~/go/src/wiki-blog
$ gvm linkthis
/xxx/xxx/.gvm/pkgsets/go1.13.5/global/src/wiki-blog -> /xxx/xxx/go/src/wiki-blog
```

会将我们的项目软连接到`/xxx/xxx/.gvm/pkgsets/go1.13.5/global/src`目录下面。

```bash
$ ll /xxx/xxx/.gvm/pkgsets/go1.13.5/global/src
lrwxr-xr-x  1 durban  staff    29B 12 27 17:51 wiki-blog -> /xxx/xxx/go/src/wiki-blog
```

然后需要进行依赖包的安装，gvm并不会将前一个版本的代码库移植到新的代码库中。 所以这里**强调**，一定在有依赖包管理的情况下再进行安装使用，不然别轻易切换版本，不过现在*go mod*也是不错的选择。 另外在进行`go linkthis`的时候一定是在src的下面的一级目录（即src当前目录），不要再深入二级之后的目录去执行，不然映射的路径会有问题的。

> 不过这里奇怪的是，src作为一个源码目录的标识是不是挺不方便的
