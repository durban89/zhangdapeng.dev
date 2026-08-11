---
title: "Go基础学习记录 - 如何写Go代码 - 代码组织(概要、工作区、GOPATH环境变量)"
date: "2025-07-30 14:58:57"
slug: "go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-gai-yao-gong-zuo-qu-gopath-huan-jing-bian-liang"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(概要、工作区、GOPATH环境变量)/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(概要、工作区、GOPATH环境变量).html"
  - "/Go基础学习记录-如何写Go代码-代码组织(概要、工作区、GOPATH环境变量)/"
  - "/Go基础学习记录-如何写Go代码-代码组织(概要、工作区、GOPATH环境变量).html"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-概要-工作区-GOPATH环境变量/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-概要-工作区-GOPATH环境变量.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-gai-yao-gong-zuo-qu-gopath-hua/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-gai-yao-gong-zuo-qu-gopath.html"
  - "/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-gai-yao-gong-zuo-qu-gopath-huan-jing-.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

## **概要**

* Go程序员一般保持他们的Go代码在一个单独的工作区
* 一个工作区包含很多版本控制存储库
* 每个存储库包含一个或多个包
* 每个包包含一个或多个Go源码文件在一个单独的目录
* 关于包的路径，包的目录决定了它的 import path

请注意，这与其他编程环境不同，在这些编程环境中，每个项目都有一个单独的工作区，工作区与版本控制存储库紧密相关。

## **工作区**

工作空间是一个目录层次结构，其根目录包含三个目录，如下：

* src 包含Go源文件
* pkg 包含package objects
* bin 可执行的命令.

go tool 构建源码包并安装生成的二进制文件安装到pkg和bin目录

src子目录通常包含多个版本控制存储库（例如Git或Mercurial），用于跟踪一个或多个源包的开发。

为了了解工作区在实践中的结构，下面是一个例子：

```bash
bin/
    hello                          # command executable
    outyet                         # command executable
pkg/
    linux_amd64/
        github.com/golang/example/
            stringutil.a           # package object
src/
    github.com/golang/example/
        .git/                      # Git repository metadata
        hello/
            hello.go               # command source
        outyet/
            main.go                # command source
            main_test.go           # test source
        stringutil/
            reverse.go             # package source
            reverse_test.go        # test source
    golang.org/x/image/
        .git/                      # Git repository metadata
        bmp/
            reader.go              # package source
            writer.go              # package source
    ... (many more repositories and packages omitted) ...
```

上面的树结构展示了一个工作区包含了两个存储库(example 和 image)。example存储库包含了两个命令（hello和outyet）和一个库（stringutil）

image存储库包含了bmp包和许多其他的包。

典型的工作区包含许多由许多包和命令组成的源代码库。

大多数Go程序员将他们所有的Go源代码和依赖关系保存在一个工作区中。命令和库由不同类型的源代码包构建而成。

## **GOPATH环境变量**

GOPATH环境变量指定工作区的位置。

它默认为一个名为go的目录，位于主目录中，因此在Unix上是$HOME/go，在Plan 9上是$home/go，Windows上是％USERPROFILE％\go（通常为C:\Users\YourName\go）。

如果想在其他位置工作，则需要将GOPATH设置为该目录的路径。（另一个常见设置是设置GOPATH=$HOME）请注意，GOPATH不能与Go安装路径相同

go env GOPATH命令打印当前有效的GOPATH;如果环境变量未设置，它将打印默认位置。

为了方便起见，将工作区的bin子目录添加到PATH中：

```bash
$ export PATH=$PATH:$(go env GOPATH)/bin
```

为了简洁起见，脚本使用$GOPATH而不是$(go env GOPATH)。如果没有设置GOPATH，可以用这些命令替换$HOME/go，或者运行：

```bash
$ export GOPATH=$(go env GOPATH)
```

想要学习更过关于GOPATH环境变量的,可以到这里'go help gopath(https://golang.org/cmd/go/#hdr-GOPATH\_environment\_variable)'.

如果想要自定义工作区位置，可以到这里[GOPATH环境变量(https://golang.org/wiki/SettingGOPATH)]查看具体不同平台的设置方法：
