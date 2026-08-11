---
title: "Go基础学习记录 - Go指南 - 方法"
date: "2025-07-31 10:25:49"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-fang-fa"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-方法/"
  - "/2025/07/31/Go基础学习记录-Go指南-方法.html"
  - "/Go基础学习记录-Go指南-方法/"
  - "/Go基础学习记录-Go指南-方法.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-fang-fa/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-fang-fa.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-fang-fa.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **方法**

Go 没有类。不过你可以为结构体类型定义方法。

方法就是一类带特殊的 接收者 参数的函数。

方法接收者在它自己的参数列表内，位于 func 关键字和方法名之间。

在此例中， Area 方法拥有一个名为 v ，类型为 Rectangle 的接收者。具体如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area 面积
func (r Rectangle) Area() float64 {
    return r.width * r.height
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v.Area())
}
```

### **方法即函数**

记住：方法只是个带接收者参数的函数。

上面代码中 Area 的写法就是个正常的函数，功能并没有什么变化。

### **方法接收者**

在Go的方法中，也可以为非结构体类型声明方法。非结构体如float64，即区别于struct的。

如下面的例子中，我们看到了一个带 Abs 方法的数值类型 CustomFloat 。方法接收者的类型只能是在同一包内定义的类型，如果方法的接收者类型是在其他包内定义的类型（如 int 之类的内建类型），是不能用来声明方法的。具体如下

```go
package main

import (
    "fmt"
)

// CustomFloat 自定义float64
type CustomFloat float64

// Abs 绝对值
func (f CustomFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

func main() {
    f := CustomFloat(-2)
    fmt.Println(f.Abs())
}
```
