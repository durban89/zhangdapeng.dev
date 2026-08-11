---
title: "Go基础学习记录 - Go指南 - 指针接收者"
date: "2025-07-31 10:25:52"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-jie-shou-zhe"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-指针接收者/"
  - "/2025/07/31/Go基础学习记录-Go指南-指针接收者.html"
  - "/Go基础学习记录-Go指南-指针接收者/"
  - "/Go基础学习记录-Go指南-指针接收者.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-jie-shou-zhe/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-jie-shou-zhe.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-jie-shou-zhe.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **指针接收者**

Go可以为指针接收者声明方法。这意味着对于某类型 T ，接收者的类型可以用 \*T 的语法。 （此外， T 不能是像 \*int 这样的指针。）示例如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area Rectangle的面积
func (v Rectangle) Area() float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func (v *Rectangle) Scale(f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v)
    v.Scale(10)
    fmt.Println(v)
    fmt.Println(v.Area())
}
```

运行后得到如下结果

```bash
{3 4}
{30 40}
1200
```

例如，这里为 \*Rectangle 定义了 Scale 方法。

指针接收者的方法可以修改接收者指向的值（就像 Scale 在这做的）。 由于方法经常需要修改它的接收者，指针接收者比值接收者更常用。试着移除 Scale 函数声明中的 \* ，观察此程序的行为如何变化。如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area Rectangle的面积
func (v Rectangle) Area() float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func (v Rectangle) Scale(f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v)
    v.Scale(10)
    fmt.Println(v)
    fmt.Println(v.Area())
}
```

运行后得到如下结果

```bash
{3 4}
{3 4}
12
```

若使用值接收者，那么 Scale 方法会对原始 Rectangle 值的副本进行操作。 （对于函数的其它参数也是如此。） Scale 方法必须用指针接受者来更改 main 函数中声明的 Rectangle 的值。
