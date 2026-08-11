---
title: "CocoaPods安装"
date: "2025-06-30 11:49:10"
slug: "cocoapods-an-zhuang"
categories: ["技术"]
tags: ["CocoaPods"]
aliases:
  - "/2025/06/30/CocoaPods安装/"
  - "/2025/06/30/CocoaPods安装.html"
  - "/CocoaPods安装/"
  - "/CocoaPods安装.html"
  - "/2025/06/30/cocoapods-an-zhuang/"
  - "/2025/06/30/cocoapods-an-zhuang.html"
  - "/cocoapods-an-zhuang.html"
---
CocoaPods安装

在安装CocoaPods之前，首先要在本地安装好Ruby环境。至于如何在Mac中安装好Ruby环境，请google一下。

假如你在本地已经安装好Ruby环境，那么下载和安装CocoaPods将十分简单，只需要一行命令。

```bash
sudo gem install cocoapods
```

在终端中敲入这个命令之后，会发现半天没有任何反应。可能原因是因为那堵墙阻挡了cocoapods.org

我们可以用淘宝的Ruby镜像来访问cocoapods。按照下面的顺序在终端中敲入依次敲入命令：

```bash
$ gem sources --remove https://rubygems.org/
//等有反应之后再敲入以下命令
$ gem sources -a http://ruby.taobao.org/
```

为了验证你的Ruby镜像是并且仅是taobao，可以用以下命令查看：

```bash
$ gem sources -l
```

只有在终端中出现下面文字才表明你上面的命令是成功的：

*** CURRENT SOURCES ***

http://ruby.taobao.org/

这时候，你再次在终端中运行：

```bash
$ sudo gem install cocoapods
```

等上十几秒钟，CocoaPods就可以在你本地下载并且安装好了，不再需要其他设置。

//===============================

如果你说我安装的时候遇到了类似ruby报错的信息，你可以尝试这个命令：

```bash
rvm requirements
```

执行完后，可以再试一下，如果还是有问题的话，留言我们一起探讨一下。

