---
title: "Go基础学习记录 - Go指南 - 流程控制语句:switch"
date: "2025-07-31 10:06:39"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-switch"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:switch/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:switch.html"
  - "/Go基础学习记录-Go指南-流程控制语句:switch/"
  - "/Go基础学习记录-Go指南-流程控制语句:switch.html"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-switch/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-switch.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-switch/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-switch.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-switch.html"
---
环境

> go version go1.10.1 darwin/amd64

### **switch语句**

Go的switch流程控制语句的使用如下

```go
package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Println("Run Switch Control")
    switch os := runtime.GOOS; os {
    case "darwin":
        fmt.Println("OS X")
    case "linux":
        fmt.Println("Linux")
    default:
        fmt.Printf("%s", os)
    }
}
```

### **switch 的求值顺序**

switch 的 case 语句从上到下顺次执行，直到匹配成功时停止。

```go
switch i {
  case 0:
  case f():
}
```

在 i==0 时 f 不会被调用。看如下例子

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("什么时候是周六?")
    today := time.Now().Weekday()
    switch time.Saturday {
    case today + 0:
        fmt.Println("今天")
    case today + 1:
        fmt.Println("明天")
    case today + 2:
        fmt.Println("后天")
    default:
        fmt.Println("还要过几天")
    }
}
```

### **没有条件的 switch**

没有条件的 switch 同 switch true 一样。这种形式能将一长串 if-then-else 写得更加清晰。实例如下

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("早上好")
    case t.Hour() < 17:
        fmt.Println("下午好")
    default:
        fmt.Println("晚上好")
    }
}
```
