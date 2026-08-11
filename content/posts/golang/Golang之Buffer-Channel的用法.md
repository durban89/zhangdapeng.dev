---
title: "Golang之Buffer Channel的用法"
date: "2025-08-05 11:36:58"
slug: "golang-zhi-buffer-channel-de-yong-fa"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang之Buffer-Channel的用法/"
  - "/2025/08/05/Golang之Buffer-Channel的用法.html"
  - "/Golang之Buffer-Channel的用法/"
  - "/Golang之Buffer-Channel的用法.html"
  - "/2025/08/05/golang-zhi-buffer-channel-de-yong-fa/"
  - "/2025/08/05/golang-zhi-buffer-channel-de-yong-fa.html"
  - "/golang-zhi-buffer-channel-de-yong-fa.html"
---
预设一个这样的场景

我要运行一个脚本 要一次运行多个 是并发的 但是我又想控制下并发量 不要太多

比如我一次要运行10个，但是最多运行3个创建能放10个脚本的变量jobs

```go
jobs := make(chan int, 10)

go func() {
    for i := 0; i < 10; i++ {
        jobs <- i + 1
    }
    close(jobs)
}()
```

创建最多能运行3个脚本的变量

```go
works := make(chan struct{}, 3)
```

开始运行脚本

```go
for job := range jobs {
    wg.Add(1)
    go func(job, i int) {
        works <- struct{}{} // 达到3个 就会阻塞卡住 等待执行完释放才能继续
        fmt.Printf("脚本 id %2d 开始运行 \n", job)

        // 模拟脚本运行过程
        duration := time.Second * time.Duration(job)
        time.Sleep(duration)

        <-works
        wg.Done()
    }(job, 1)
}
```

输出结果展示下

```bash
$ go run main.go
脚本 id 10 开始运行 
脚本 id  1 开始运行 
脚本 id  2 开始运行 
脚本 id  6 开始运行 
脚本 id  5 开始运行 
脚本 id  8 开始运行 
脚本 id  9 开始运行 
脚本 id  4 开始运行 
脚本 id  3 开始运行 
脚本 id  7 开始运行
```

完整代码贴出来

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func main() {
    jobs := make(chan int, 10)
    works := make(chan struct{}, 3)

    wg := sync.WaitGroup{}

    go func() {
        for i := 0; i < 10; i++ {
            jobs <- i + 1
        }
        close(jobs)
    }()

    for job := range jobs {
        wg.Add(1)
        go func(job, i int) {
            works <- struct{}{} // 达到3个 就会阻塞卡住 等待执行完释放才能继续
            fmt.Printf("脚本 id %2d 开始运行 \n", job)

            // 模拟脚本运行过程
            duration := time.Second * time.Duration(job)
            time.Sleep(duration)

            <-works
            wg.Done()
        }(job, 1)
    }

    wg.Wait()

}
```
