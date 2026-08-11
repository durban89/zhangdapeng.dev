---
title: "Golang小知识 - go关键字创建并发执行"
date: "2025-08-05 09:48:12"
slug: "golang-xiao-zhi-shi-go-guan-jian-zi-chuang-jian-bing-fa-zhi-xing"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang小知识-go关键字创建并发执行/"
  - "/2025/08/05/Golang小知识-go关键字创建并发执行.html"
  - "/Golang小知识-go关键字创建并发执行/"
  - "/Golang小知识-go关键字创建并发执行.html"
  - "/2025/08/05/golang-xiao-zhi-shi-go-guan-jian-zi-chuang-jian-bing-fa-zhi-xing/"
  - "/2025/08/05/golang-xiao-zhi-shi-go-guan-jian-zi-chuang-jian-bing-fa-zhi-xing.html"
  - "/golang-xiao-zhi-shi-go-guan-jian-zi-chuang-jian-bing-fa-zhi-xing.html"
---
Golang小知识 - go关键字创建并发执行

go如何在实际代码中实现并发执行

下面示例如下

```go
package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int) {
	fmt.Println("worker", len(jobs))

	for j := range jobs {
		fmt.Println("wodker", id, "started job", j)
	}
}

func main() {
	const jobsNum = 5
	jobs := make(chan int, jobsNum)

	for w := 1; w <= 3; w++ {
		go worker(w, jobs)
	}

	for j := 1; j <= jobsNum; j++ {
		jobs <- j
	}

	close(jobs)

	time.Sleep(time.Second * 4)
}
```

这里可以看出来

```go
go worker(w, jobs)
```

这里的代码创建了三个并行的操作

我运行下看看运行结果，运行三次的结果如下

第一次运行结果

```bash
$ go run main.go
worker 5
wodker 1 started job 1
wodker 1 started job 2
wodker 1 started job 3
wodker 1 started job 4
wodker 1 started job 5
worker 0
worker 0
```

第二次运行结果

```bash
$ go run main.go
worker 5
worker 5
wodker 2 started job 2
wodker 2 started job 3
wodker 2 started job 4
wodker 2 started job 5
wodker 1 started job 1
worker 5
```

第三次运行结果

```bash
$ go run main.go
worker 5
wodker 3 started job 1
wodker 3 started job 2
worker 5
wodker 1 started job 4
wodker 1 started job 5
wodker 3 started job 3
worker 5
```

从运行的结果可以看出每次运行的结果都不一样

我们可以理解为启动的三个并行函数，都获得了 chan

`for...range` 执行的时候先从chan中获取数据的先执行 这个先后顺序是根据计算机内部调用的来决定的。
