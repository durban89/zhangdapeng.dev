---
title: "Go基础学习记录 - Go指南 - 并发系列之Channels"
date: "2025-07-31 10:26:43"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-channels"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之Channels/"
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之Channels.html"
  - "/Go基础学习记录-Go指南-并发系列之Channels/"
  - "/Go基础学习记录-Go指南-并发系列之Channels.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-channels/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-channels.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-channels.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **Channels**

信道是带有类型的管道，你可以通过它用信道操作符 <- 来发送或者接收值。

```go
ch <- v    // 将 v 发送至信道 ch。
v := <-ch  // 从 ch 接收值并赋予 v。
```

("箭头"就是数据流的方向。)

和映射与切片一样，信道在使用前必须创建：

```go
ch := make(chan int)
```

默认情况下，发送和接收操作在另一端准备好之前都会阻塞。这使得goroutines可以在没有显式的锁或竞态变量的情况下进行同步。以下示例对切片中的数进行求和，将任务分配给两个goroutines。 一旦两个goroutines完成了它们的计算，它就能算出最终的结果。

```go
package main

import "fmt"

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {

        sum += v
    }
    c <- sum // 将和送入 c
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}

    c := make(chan int)
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    x, y := <-c, <-c // 从 c 中接收

    fmt.Println(x, y, x+y)
}
```

运行后结果如下

```bash
-5 17 12
```

### **带缓冲的Channels**

Channels可以是 带缓冲的，将缓冲长度作为第二个参数提供给 make 来初始化一个带缓冲的Channels：

```go
ch := make(chan int, 100)
```

仅当Channels的缓冲区填满后，向其发送数据时才会阻塞。当缓冲区为空时，接受方会阻塞。修改示例填满缓冲区，然后看看会发生什么。  
运行正常实例如下

```go
package main

import "fmt"

func main() {
    ch := make(chan int, 2)
    ch <- 1
    ch <- 2
    fmt.Println(<-ch)
    fmt.Println(<-ch)
}
```

运行后得到如下

```bash
1
2
```

运行异常的实例如下

```go
package main

import "fmt"

func main() {
    ch := make(chan int, 1)
    ch <- 1
    ch <- 2
    fmt.Println(<-ch)
    fmt.Println(<-ch)
}
```

运行后得到如下

```bash
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
    /xxx/xxx/go/src/github.com/xxx/example/example.go:8 +0x73
exit status 2
```
