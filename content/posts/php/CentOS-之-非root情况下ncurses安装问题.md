---
title: "CentOS 之 非root情况下ncurses安装问题"
date: "2025-07-03 17:37:38"
slug: "centos-zhi-fei-root-qing-kuang-xia-ncurses-an-zhuang-wen-ti"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/03/CentOS-之-非root情况下ncurses安装问题/"
  - "/2025/07/03/CentOS-之-非root情况下ncurses安装问题.html"
  - "/CentOS-之-非root情况下ncurses安装问题/"
  - "/CentOS-之-非root情况下ncurses安装问题.html"
  - "/2025/07/03/centos-zhi-fei-root-qing-kuang-xia-ncurses-an-zhuang-wen-ti/"
  - "/2025/07/03/centos-zhi-fei-root-qing-kuang-xia-ncurses-an-zhuang-wen-ti.html"
  - "/centos-zhi-fei-root-qing-kuang-xia-ncurses-an-zhuang-wen-ti.html"
---
最近使用主机发现，没有root权限，然后想用zsh，发现没有root权限也是安装不了，但是安装zsh又需要ncurses，但是网上都是一些yum之类的命令，但是yum只能root用哇，苦于无奈，只能安装在自己的目录下使用了。具体过程如下。

### 系统版本：

```bash
$ lsb_release -a
```

> LSB Version:    :core-4.1-amd64:core-4.1-noarch  
> Distributor ID: CentOS  
> Description:    CentOS Linux release 7.3.1611 (Core)  
> Release:        7.3.1611  
> Codename:       Core

### 源码包下载

http://ftp.gnu.org/pub/gnu/ncurses/  
这里可以找到需要的版本

正常安装

```bash
./configure --prefix=$HOME
```

会遇到一个问题，如下

> /usr/bin/ld: /usr/lib/libncurses.a(lib\_addch.o): relocation R\_X86\_64\_32 against `a local symbol' can not be used when making a   
> shared object; recompile with -fPIC /usr/lib/libncurses.a: could not read symbols: Bad value   
> collect2: ld returned 1 exit status   
> make[1]: \*\*\* [http://www.cnblogs.com/.ext/x86\_64-linux/curses.so] Error 1   
> make[1]: Leaving directory `/home/deploy/tmp/ruby-   
> enterprise-1.8.6-20081215/source/ext/curses'   
> make: \*\*\* [all] Error 1

从错误中可以定位到可能是ncurses这个静态链接库的问题，从网上找了很久，解决方法如下在安装ncurses时如下方法安装：

```bash
$./configure --prefix=$HOME --with-shared --without-debug --enable-widec
$make && make install
```
