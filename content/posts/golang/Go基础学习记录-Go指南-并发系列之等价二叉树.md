---
title: "Go基础学习记录 - Go指南 - 并发系列之等价二叉树"
date: "2025-07-31 10:26:58"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-deng-jia-er-cha-shu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之等价二叉树/"
  - "/2025/07/31/Go基础学习记录-Go指南-并发系列之等价二叉树.html"
  - "/Go基础学习记录-Go指南-并发系列之等价二叉树/"
  - "/Go基础学习记录-Go指南-并发系列之等价二叉树.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-deng-jia-er-cha-shu/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-deng-jia-er-cha-shu.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-bing-fa-xi-lie-zhi-deng-jia-er-cha-shu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **等价二叉树**

不同二叉树的叶节点上可以保存相同的值序列。例如，以下两个二叉树都保存了序列 1，1，2，3，5，8，13 。

![等价二叉树](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1533046337/xiaorongmao/xiaorongmao_image_19_1.png)

在大多数语言中，检查两个二叉树是否保存了相同序列的函数都相当复杂。 我们将使用 Go 的并发和信道来编写一个简单的解法。

本例使用跟官方一致的 tree 包，它定义了类型：

```go
type Tree struct {
    Left  *Tree
    Value int
    Right *Tree
}
```

现在我们要实现的内容下

1. 实现 Walk 函数。

2. 测试 Walk 函数。

函数 tree.New(k) 用于构造一个随机结构的二叉树，它保存了值 k 、 2k 、 3k ... 10k 。

创建一个新的信道 ch 并且对其进行步进：

```go
go Walk(tree.New(1), ch)
```

然后从信道中读取并打印 10 个值。应当是数字 `1, 2, 3, ..., 10` 。

3. 用 Walk 实现 Same 函数来检测 t1 和 t2 是否存储了相同的值。

4. 测试 Same 函数。

> Same(tree.New(1), tree.New(1)) 应当返回 true。  
> Same(tree.New(1), tree.New(2)) 应当返回 false。

[Tree的文档](https://godoc.org/golang.org/x/tour/tree#Tree)实现方式如下

```go
package main

import (
    "fmt"
    "golang.org/x/tour/tree"
)

// Walk 步进 tree t 将所有的值从 tree 发送到 channel ch。
func Walk(t *tree.Tree, ch chan int) {
    walkTree(t, ch)
    close(ch)
}

func walkTree(t *tree.Tree, ch chan int) {
    if t != nil {
        walkTree(t.Left, ch)
        ch <- t.Value
        walkTree(t.Right, ch)
    }
}

// Same 检测树 t1 和 t2 是否含有相同的值。
func Same(t1, t2 *tree.Tree) bool {
    ch1 := make(chan int)
    ch2 := make(chan int)
    go Walk(t1, ch1)
    go Walk(t2, ch2)

    for i := range ch1 {
        if i != <-ch2 {
            return false
        }
    }

    return true
}

func main() {
    // 测试Walk
    ch := make(chan int, 10)
    go Walk(tree.New(1), ch)
    for i := range ch {
        fmt.Println(i)
    }

    fmt.Println(Same(tree.New(1), tree.New(1)))
    fmt.Println(Same(tree.New(1), tree.New(2)))
}
```

运行后结果如下

```bash
1
2
3
4
5
6
7
8
9
10
true
false
```
