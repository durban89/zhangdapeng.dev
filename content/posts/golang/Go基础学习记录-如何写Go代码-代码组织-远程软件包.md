---
title: "Go基础学习记录 - 如何写Go代码 - 代码组织(远程软件包)"
date: "2025-07-30 14:59:22"
slug: "go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-yuan-cheng-ruan-jian-bao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(远程软件包)/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(远程软件包).html"
  - "/Go基础学习记录-如何写Go代码-代码组织(远程软件包)/"
  - "/Go基础学习记录-如何写Go代码-代码组织(远程软件包).html"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-远程软件包/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-远程软件包.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-yuan-cheng-ruan-jian-bao/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-yuan-cheng-ruan-jian-bao.html"
  - "/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-yuan-cheng-ruan-jian-bao.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **Remote packages 远程包**

导入路径描述了如何获取通过诸如使用Git或Mercurial等版本控制系统的源码包

go tool使用此属性自动从远程存储库获取包。

例如，官网文档中描述的示例也保存在GitHub[github.com/golang/example]上托管的Git存储库中。

如果您在存储库的导入路径中包含存储库URL，那么将自动获取，构建并安装它，代码如下

```bash
$ go get github.com/golang/example/hello
$ $GOPATH/bin/hello
Hello, Go examples!
```

如果工作空间中不存在指定的包，则get将其放在GOPATH指定的第一个工作空间内。（如果包已经存在，请跳过远程提取，其行为与go install相同。）

发出上述go get命令后，工作空间目录树现在应该类似如下：

```bash
bin/
    hello                           # command executable
pkg/
    darwin_amd64/
        github.com/golang/example/
            stringutil.a            # package object
        github.com/durban.zhang/
            stringutil.a            # package object
src/
    github.com/golang/example/
	.git/                       # Git repository metadata
        hello/
            hello.go                # command source
        stringutil/
            reverse.go              # package source
            reverse_test.go         # test source
    github.com/durban.zhang/
        hello/
            hello.go                # command source
        stringutil/
            reverse.go              # package source
            reverse_test.go         # test source
```

在GitHub上托管的hello命令依赖于同一个存储库中的stringutil包。

hello.go文件中的导入使用相同的导入路径约定，因此go get命令也能够定位和安装相关软件包。

```go
import "github.com/golang/example/stringutil"
```

此约定是使Go包可供其他人使用的最简单方法。

Go Wiki和godoc.org提供了外部Go项目的列表。

有关通过go tool使用远程存储库的更多信息，请参阅go help importpath。

基本上关于Golang的如何写go代码的，基本上官方就这些，只是这些还是不够的，还无法进行实际的应用，之后的文章会以下面的路程进行记录

* 订阅golang-announce邮件列表，以便在发布新的稳定版Go时收到通知。
* 请参阅Effective Go提供有关编写清晰，习惯性Go代码的提示。
* 以Go的旅程学习语言本身。
* 访问文档页面获取关于Go语言及其库和工具的深入文章。
