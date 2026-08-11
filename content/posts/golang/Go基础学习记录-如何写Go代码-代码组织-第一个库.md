---
title: "Go基础学习记录 - 如何写Go代码 - 代码组织(第一个库)"
date: "2025-07-30 14:59:15"
slug: "go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-di-yi-ge-ku"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(第一个库)/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(第一个库).html"
  - "/Go基础学习记录-如何写Go代码-代码组织(第一个库)/"
  - "/Go基础学习记录-如何写Go代码-代码组织(第一个库).html"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-第一个库/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-第一个库.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-di-yi-ge-ku/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-di-yi-ge-ku.html"
  - "/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-di-yi-ge-ku.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **第一个库**

写一个库然后在上篇文章中的代码中调用

第一步选择一个包路径然后创建包目录

上篇文章我使用的是这个目录github.com/durban.zhang，这里的话创建一个目录$GOPATH/src/github.com/durban.zhang/stringutil

```bash
$ mkdir $GOPATH/src/github.com/durban.zhang/stringutil
```

然后创建一个文件reverse.go，里面的内容如下

```go
package stringutil

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}

	return string(r)
}
```

写好后使用go build编译

```bash
go build github.com/durban.zhang/stringutil
```

或者，如果在当前目录的话，可以直接

```bash
go build
```

go build不会产生一个 output 文件，如果想要这样做的话，必须使用go install，产生的文件会在工作区的pkg目录。

确认stringutil包建立之后，修改hello.go，文件应该在\*$GOPATH/src/github.com/durban.zhang/hello\*这个目录下面,hello.go里面的内容修改如下

```go
package main

import (
	"fmt"

	"github.com/user/stringutil"
)

func main() {
	fmt.Printf(stringutil.Reverse("!oG ,olleH"))
}
```

每当go工具安装一个包或二进制文件时，它也会安装它所具有的任何依赖关系。

所以当你安装hello程序

```bash
$ go install github.com/durban.zhang/hello
```

stringutil包将会自动被安装

运行后会得到如下

```bash
$ hello
Hello, Go!
```

经过前面的操作后,工作区的目录结构应该会类似如下

```bash
bin/
    hello                 # command executable
pkg/
    darwin_amd64/          # this will reflect your OS and architecture
        github.com/durban.zhang/
            stringutil.a  # package object
src/
    github.com/durban.zhang/
        hello/
            hello.go      # command source
        stringutil/
            reverse.go    # package source
```

请注意，go install将stringutil.a对象放置在映射其源目录的pkg/darwin\_amd64内的目录中。这是为了将来的调用工具可以找到包对象并避免不必要地重新编译包。

darwin\_amd64部分可以帮助交叉编译，并且会反映您系统的操作系统和体系结构。

Go命令可执行文件是静态链接的;包对象不需要显示的来运行Go程序。
