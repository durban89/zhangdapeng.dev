---
title: "Go基础学习记录 - Go指南 - 函数值和函数的闭包"
date: "2025-07-31 10:25:46"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-han-shu-zhi-he-han-shu-de-bi-bao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-函数值和函数的闭包/"
  - "/2025/07/31/Go基础学习记录-Go指南-函数值和函数的闭包.html"
  - "/Go基础学习记录-Go指南-函数值和函数的闭包/"
  - "/Go基础学习记录-Go指南-函数值和函数的闭包.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-han-shu-zhi-he-han-shu-de-bi-bao/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-han-shu-zhi-he-han-shu-de-bi-bao.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-han-shu-zhi-he-han-shu-de-bi-bao.html"
---
### **环境**

> ### go version go1.10.1 darwin/amd64

### **函数值**

函数也是值。它们可以像其它值一样传递。函数值可以用作函数的参数或返回值。

```go
package main

import (
    "fmt"
    "math"
)

func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

func main() {
    hypot := func(x, y float64) float64 {
        return math.Sqrt(x*x + y*y)
    }
    fmt.Println(hypot(5, 12))

    fmt.Println(compute(hypot))
    fmt.Println(compute(math.Pow))
}
```

### **函数的闭包**

Go 函数可以是一个闭包。闭包是一个函数值，它引用了其函数体之外的变量。 该函数可以访问并赋予其引用的变量的值，换句话说，该函数被"绑定"在了这些变量上。

例如，函数 adder 返回一个闭包。每个闭包都被绑定在其各自的 sum 变量上。

```go
package main

import "fmt"

func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func main() {
    pos, neg := adder(), adder()
    for i := 0; i < 10; i++ {
        fmt.Println(
            pos(i),
            neg(-2*i),
        )
    }
}
```

运行后得到的结果如下

```bash
0 0
1 -2
3 -6
6 -12
10 -20
15 -30
21 -42
28 -56
36 -72
45 -90
```

### **练习：斐波纳契闭包**

让我们用函数做些好玩的事情。

实现一个 fibonacci 函数，它返回一个函数（闭包）， 该闭包返回一个斐波纳契数列 `(0, 1, 1, 2, 3, 5, ...)` 。实现如下，实现有点繁琐，应该有更好的实现方式

```go
package main

import "fmt"

// fibonacci 是一个返回int的值的函数
func fibonacci() func() int {
    f0, f1 := 0, 1
    n := 0
    return func() int {
        if n == 0 {
            n += 1
            return f0
        }

        if n == 1 {
            n += 1
            return f1
        }

        f2 := f1 + f0
        f0 = f1
        f1 = f2

        return f2
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
```

运行后输出结果如下

```bash
0
1
1
2
3
5
8
13
21
34
```
