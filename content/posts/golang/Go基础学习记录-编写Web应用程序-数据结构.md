---
title: "Go基础学习记录 - 编写Web应用程序 - 数据结构"
date: "2025-08-01 09:21:15"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-jie-gou"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据结构/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-数据结构.html"
  - "/Go基础学习记录-编写Web应用程序-数据结构/"
  - "/Go基础学习记录-编写Web应用程序-数据结构.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-jie-gou/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-jie-gou.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shu-ju-jie-gou.html"
---
## **编写Web应用的前提介绍**

在编写一样的时候我们会经历下面几个部分

* 创建一个数据结构，并定义一个加载数据和存储数据的方法
* 使用net/http包来构建Web应用
* 使用html/template包处理HTML模板
* 使用正则regexp包来校验用户的输入
* 使用闭包closures

假设你已经掌握了如下知识:

* 已经有了编写程序的经验
* 了解web基础的web技术，包括(HTTP,HTML)
* 会一些UNIX/DOS命令行知识

## **应用程序搭建**

需要使用FreeBSD，Linux，OS X或Windows机器来运行Go。如果还不会安装的话请转到(Go基础学习记录 - 安装)[https://www.xiaorongmao.com/blog/2]

在GOPATH中创建一个新目录并cd到目录中：

```bash
mkdir wiki
cd wiki
```

比如我的项目目录路径如下

```bash
/xxx/xxx/go/src/github.com/durban.zhang/wiki
```

创建一个名为wiki.go的文件，并用您喜欢的编辑器中打开它，并添加以下行：

```go
package main

import (
    "fmt"
    "io/ioutil"
)
```

我们从Go标准库导入fmt和ioutil包。后面，当实现其他功能时，我们将向此导入声明添加更多包。

## **数据结构**

首先从定义数据结构开始。wiki由一系列互连的页面组成，每个页面都有一个Title和一个Body（页面内容）。  
在这里，我们将Page定义为一个结构，其中两个字段代表标题和正文。如下

```go
type Page struct {
    Title string
    Body  []byte
}
```

[]byte 表示"字节切片"。Body元素使用[]byte而不是字符串，是因为我们将使用的io库，它所期望的类型是[]byte。  
Page结构描述了页面数据将如何存储在内存中。如果要将数据持久的进行存储的话，需要在Page上创建一个一个save方法来解决这个问题。如下

```go
func (p *Page) save() error {
    filename := p.Title + ".txt"
    return ioutil.WriteFile(filename, p.Body, 0600)
}
```

这是一个名为save的方法，它将接收器p作为指向Page的指针。它不接受任何参数，并返回类型错误的值。

此方法将Page的Body保存为文本文件。为简单起见，将使用Title作为文件名。  
save方法返回一个错误值，因为这是WriteFile的返回类型（一个将字节切片写入文件的标准库函数）。  
save方法返回错误值，让应用程序在写入文件时出错。  
如果一切顺利，Page.save（）将返回nil（指针，接口和其他类型的零值）。  
作为WriteFile的第三个参数传递的八进制整数文字0600表示应该仅为当前用户创建具有读写权限的文件。除了保存页面，我们还想加载页面。方法如下：

```go
func loadPage(title string) (*Page, error) {
    filename := title + ".txt"
    body, error := ioutil.ReadFile(filename)
    if error != nil {
        return nil, error
    }

    return &Page{Title: title, Body: body}, nil
}
```

函数loadPage从title参数构造文件名，将文件的内容读入新的变量体，并返回指向使用正确的标题和正文值构造的Page文本的指针。

此函数在调用者调用的时候可以通过检查第二个参数，如果是nil那么它已经成功加载了一个Page。如果不是，则调用者可以处理错误

此时，我们有一个简单的数据结构，能够保存到文件并从中加载。  
还需要编写一个主函数来测试我们编写的内容，如下：

```go
func main() {
    p1 := &Page{
        Title: "Test Title",
        Body:  []byte("Test Body"),
    }
    p1.save()
    p2, _ := loadPage("Test Title")
    fmt.Println(string(p2.Body))
}
```

编译并执行此代码后，将创建一个名为TestPage.txt的文件，其中包含p1的内容。  
然后将该文件读入struct p2，并将其Body元素打印到屏幕上。  
可以像下面这样编译并运行

```bash
$go build wiki.go
$./wiki
Test Body
```
