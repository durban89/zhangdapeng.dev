---
title: "Go基础学习记录 - 安装"
date: "2025-07-30 14:58:45"
slug: "go-ji-chu-xue-xi-ji-lu-an-zhuang"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-安装/"
  - "/2025/07/30/Go基础学习记录-安装.html"
  - "/Go基础学习记录-安装/"
  - "/Go基础学习记录-安装.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-an-zhuang/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-an-zhuang.html"
  - "/go-ji-chu-xue-xi-ji-lu-an-zhuang.html"
---
**安装**  
在mac下安装很简单，直接执行

```bash
brew install go
```

官方称  
如果你是从老版本升级的话，必须移除已经存在的版本

> If you are upgrading from an older version of Go you must first remove the existing version.

**测试是否安装成功**  
检查Go是否安装成功，可以通过创建一个workspace写个小程序来测试，具体如下创建workspace目录, $HOME/go. (如果你想用一个不同的目录，就需要设置GOPATH环境变量)  
下一步在workspace目录创建一个目录src/hello, 在src/hello目录创建一个名称为hello.go的文件，里面的内容如下:

```go
package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
}
```

然后使用Go工具进行构建

```bash
$ cd $HOME/go/src/hello
$ go build
```

上面的命令将创建一个名称为hello的可执行文件。  
执行他可看到如下输出

```bash
$ ./hello
Hello world
```

如果你看到"hello, world"信息，说明你的Go安装是可以正常工作的。

你可以运行"go install"安装其他的Go包到workspace的bin目录或者运行"go clean -i"去移除已经安装的包

在离开去写Go代码之前请先去阅读下如何写Go代码文档，里面描述了许多基础的观念关于Go tools

### **最终Golang环境**

> go version go1.10.1 darwin/amd64
