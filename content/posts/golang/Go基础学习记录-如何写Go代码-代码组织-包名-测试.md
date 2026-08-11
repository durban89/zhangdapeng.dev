---
title: "Go基础学习记录 - 如何写Go代码 - 代码组织(包名、测试)"
date: "2025-07-30 14:59:18"
slug: "go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-bao-ming-ce-shi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(包名、测试)/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织(包名、测试).html"
  - "/Go基础学习记录-如何写Go代码-代码组织(包名、测试)/"
  - "/Go基础学习记录-如何写Go代码-代码组织(包名、测试).html"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-包名-测试/"
  - "/2025/07/30/Go基础学习记录-如何写Go代码-代码组织-包名-测试.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-bao-ming-ce-shi/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-bao-ming-ce-shi.html"
  - "/go-ji-chu-xue-xi-ji-lu-ru-he-xie-go-dai-ma-dai-ma-zu-zhi-bao-ming-ce-shi.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **包名**

Go源文件中的第一条语句必须是

```go
package name
```

其中name是包的导入默认名称。（包中的所有文件必须使用相同的名称。）

Go的惯例是程序包名称是导入路径的最后一个元素：导入为"crypto/rot13"的程序包应该命名为rot13。

可执行命令必须总是使用package main。

比如之前文章中提到的两个例子，一个是库一个是程序  
在程序hello.go中第一条语句是

```go
package main
```

在程序stringutil/reverse.go中的第一条语句是

```go
package stringutil
```

显然这里面hello.go是一个可以执行的，但是stringutil只是一个库，可以提供给类似hello.go这样的文件使用

没有要求软件包名称在链接到一个二进制文件的所有软件包中唯一，只需要导入的路径（它们的完整文件名）是唯一的。

详细Go的命名约定请参阅Effective Go[https://golang.org/doc/effective\_go.html#names]。

### **测试**

Go有一个由go test命令和测试包组成的轻量级测试框架。 通过创建名称以\_test.go结尾的文件来编写测试，其中包含名为TestXXX并带有签名func（t \* testing.T）的函数。 测试框架运行所有以这种方式命名的函数来进行测试; 如果函数调用失败，如t.Error或t.Fail，则认为测试失败。

下面创建文件将测试添加到stringutil包中  
$GOPATH/src/github.com/user/stringutil/reverse\_test.go里面的代码如下

```go
package stringutil

import "testing"

func TestReverse(t \*testing.T) {  
    cases := []struct {  
        in, want string  
    }{  
        {"Hello, world", "dlrow ,olleH"},  
        {"Hello, 世界", "界世 ,olleH"},  
        {"", ""},  
    }

    for \_, c := range cases {  
        got := Reverse(c.in)  
        if got != c.want {  
            t.Error("Reverse(%q) == %q, want %q", c.in, c.want)  
        }  
    }  
}
```

运行go test得到类似如下的内容

```bash
$ go test github.com/durban.zhang/stringutil
ok  	github.com/durban.zhang/stringutil	0.007s
```

与往常一样，如果您正在从软件包目录运行go工具，则可以省略软件包路径：

```bash
$ go test
PASS
ok  	github.com/durban.zhang/stringutil	0.007s
```
