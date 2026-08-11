---
title: "Go基础学习记录 - Go指南 - 并发系列之sync.Mutex"
date: "2025-07-31 10:27:01"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-syncmutex"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之sync.Mutex/"
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之sync.Mutex.html"
  - "/Go基础学习记录-Go指南-并发系列之sync.Mutex/"
  - "/Go基础学习记录-Go指南-并发系列之sync.Mutex.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-syncmutex/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-syncmutex.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-syncmutex.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **sync.Mutex**

上篇分享可以了解到Channels非常适合在各个goroutines进行通信。

但是如果我们并不需要通信呢？比如说，若我们只是想保证每次只有一个goroutines能够访问一个共享的变量，从而避免冲突

这里涉及的概念叫做 互斥（mutual exclusion） ，我们通常使用 互斥锁 （Mutex） 这一数据结构来提供这种机制。

Go 标准库中提供了 sync.Mutex 互斥锁类型及其两个方法：

```go
Lock
Unlock
```

下面实现一个简单的实例演示，如下

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

// SafeCounter 的并发使用是安全的。
type SafeCounter struct {
    v   map[string]int
    mux sync.Mutex
}

// Inc 增加给定 key 的计数器的值。
func (c *SafeCounter) Inc(key string) {
    c.mux.Lock()
    // Lock 之后同一时刻只有一个 goroutine 能访问 c.v
    c.v[key]++
    c.mux.Unlock()
}

// Value 返回给定 key 的计数器的当前值。
func (c *SafeCounter) Value(key string) int {
    c.mux.Lock()
    // Lock 之后同一时刻只有一个 goroutine 能访问 c.v
    defer c.mux.Unlock()
    return c.v[key]
}

func main() {
    c := SafeCounter{v: make(map[string]int)}
    for i := 0; i < 1000; i++ {
        go c.Inc("somekey")
    }

    time.Sleep(time.Second)
    fmt.Println(c.Value("somekey"))
}
```

我们可以通过在代码前调用 Lock 方法，在代码后调用 Unlock 方法来保证一段代码的互斥执行。 如上面代码中的Inc方法。

我们也可以用 defer 语句来保证互斥锁一定会被解锁。如上面代码中的Value方法。
