---
title: "Go基础学习记录 - Go指南 - 流程控制语句:defer"
date: "2025-07-31 10:06:43"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-defer"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:defer/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:defer.html"
  - "/Go基础学习记录-Go指南-流程控制语句:defer/"
  - "/Go基础学习记录-Go指南-流程控制语句:defer.html"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-defer/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-defer.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-defer/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-defer.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-defer.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **defer语句**

defer语句会将函数推迟到外层函数返回之后执行。推迟调用的函数其参数会立即求值，但直到外层函数返回前该函数都不会被调用。如下

```go
package main

import "fmt"

func main() {
    defer fmt.Println("world")
    fmt.Println("hello")
}
```

运行后输出结果如下

```bash
hello
world
```

### **defer 栈**

推迟的函数调用会被压入一个栈中。 当外层函数返回时，被推迟的函数会按照后进先出的顺序调用。

更多关于 defer 语句的信息， 官方文博可以看下，后面会做一篇关于defer深入的用法，当前还是做基础入门了解。  
defer栈的实例如下

```go
package main

import "fmt"

func main() {
    fmt.Println("第一段")

    for i := 0; i < 10; i++ {
        defer fmt.Println("第二段", i)
    }

    fmt.Println("第三段")
}
```

运行结果如下，可以看出执行的顺序

```bash
第一段
第三段
第二段 9
第二段 8
第二段 7
第二段 6
第二段 5
第二段 4
第二段 3
第二段 2
第二段 1
第二段 0
```
