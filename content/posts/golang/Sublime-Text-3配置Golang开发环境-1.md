---
title: "Sublime Text 3配置Golang开发环境（1）"
date: "2025-08-04 18:07:34"
slug: "sublime-text-3-pei-zhi-golang-kai-fa-huan-jing-1"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Sublime-Text-3配置Golang开发环境（1）/"
  - "/2025/08/04/Sublime-Text-3配置Golang开发环境（1）.html"
  - "/Sublime-Text-3配置Golang开发环境（1）/"
  - "/Sublime-Text-3配置Golang开发环境（1）.html"
  - "/2025/08/04/Sublime-Text-3配置Golang开发环境-1/"
  - "/2025/08/04/Sublime-Text-3配置Golang开发环境-1.html"
  - "/2025/08/04/sublime-text-3-pei-zhi-golang-kai-fa-huan-jing-1/"
  - "/2025/08/04/sublime-text-3-pei-zhi-golang-kai-fa-huan-jing-1.html"
  - "/sublime-text-3-pei-zhi-golang-kai-fa-huan-jing-1.html"
---
### 为什么不建议使用Gosublime

看下使用流程 首先安装GoSublime

这个默认的作用只是起到了格式化和高亮代码的作用

如果格式化不起作用的话，可以试试安装下`gofmt`这个包 不过gofmt是默认就安装的

如果想要在写代码的过程中自动导入和删除需要的包的话，先要安装下`goimports`，

```bash
go get -u golang.org/x/tools/cmd/goimports
```

然后在添加配置

```bash
"fmt_cmd" :[ "goimports"],
```

但是会遇到下面两个问题

> 不能变量自动补全没有办法提示 函数自动补全功能没有办法提示

如果谁能告诉我解决办法，我万分感谢，毕竟安装一个就能搞定我很开心

### 完整篇 - 推荐使用

这个方法虽然要自己单独去安装每个插件，但是效果很好用

参考地址： https://www.alexedwards.net/blog/streamline-your-sublime-text-and-go-workflow

1、安装golang工具整合插件

打开Sublime Text 3按下快捷键 `Ctrl/Cmd+Shift+P`.

选择`Package Control: Install Package`命令.

输入`Golang Build`然后会车.

> 如何使用

打开`Tools > Build System` 菜单然后选择`Go`

这个时候打开命令面板，就可以输入下面的命令进行操作了

```bash
Build with: Go
Build with: Go - Run (see Cancelling a Build below)
Build with: Go - Test
Build with: Go - Benchmark
Build with: Go - Install
Build with: Go - Cross-Compile (Interactive)
Build with: Go - Clean
```

详情地址请参考：https://github.com/golang/sublime-build/blob/master/docs/usage.md

2、安装自动格式化和自动导入插件

打开Sublime Text 3按下快捷键 `Ctrl/Cmd+Shift+P`.

选择`Package Control: Install Package`命令.

输入`Gofmt`然后会车.

装完插件后，终端运行

```bash
$ go get golang.org/x/tools/cmd/goimports
$ which goimports
/home/xxx/Code/go/bin/goimports
```

安装完之后打开Preferences > Package Settings > Gofmt > Settings - User

然后添加如下配置

```bash
{
  "cmds": [
    ["goimports"]
  ],
  "format_on_save": true
}
```

重启sublime text，打开.go文件，编写代码保存，则自动格式化，并导入需要的包，如果提示config之类的错误

打开Preferences > Package Settings > Golang Config > Settings - User

然后添加如下配置

```bash
{
    "PATH": "/Users/xxx/.gvm/pkgsets/go1.13.1/global/bin",
    "GOPATH": "/Users/xxx/.gvm/pkgsets/go1.13.1/global"
}
```

参考文档：https://github.com/golang/sublime-config/blob/master/docs/user.md

然后重新打开.go文件在保存试试

3、安装代码高亮提示插件

安装 `SublimeLinter 3` 请点击[*这里*](https://packagecontrol.io/packages/SublimeLinter)

安装 `SublimeLinter-golangcilint` 请点击[*这里*](https://packagecontrol.io/packages/SublimeLinter-golangcilint)

安装 `golangci-lint helper` 请点击[*这里*](https://github.com/golangci/golangci-lint#install)

我是通过此方式安装的golangci-linter

```bash
curl -sfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.21.0
```

很多文章有介绍这个如何使用，但是我经过这个流程搭建完，依旧不起作用

于是我改用了golint，使用步骤如下：

安装 `SublimeLinter 3` 请点击[*这里*](https://packagecontrol.io/packages/SublimeLinter)

安装 `SublimeLinter-golint` 请点击[*这里*](https://packagecontrol.io/packages/SublimeLinter-golint)

安装 `golint` 请点击[*这里*](https://github.com/golang/lint)

4、安装代码自动补全插件【这个暂时查到要使用gocode，安装完之后，流程复杂，操作高深，不喜欢，后面遇到再更新】
