---
title: "Go基础学习记录 - Go指南 - 选择值或指针作为接收者"
date: "2025-07-31 10:25:59"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-xuan-ze-zhi-huo-zhi-zhen-zuo-wei-jie-shou-zhe"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-选择值或指针作为接收者/"
  - "/2025/07/31/Go基础学习记录-Go指南-选择值或指针作为接收者.html"
  - "/Go基础学习记录-Go指南-选择值或指针作为接收者/"
  - "/Go基础学习记录-Go指南-选择值或指针作为接收者.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-xuan-ze-zhi-huo-zhi-zhen-zuo-wei-jie-shou-zhe/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-xuan-ze-zhi-huo-zhi-zhen-zuo-wei-jie-shou-zhe.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-xuan-ze-zhi-huo-zhi-zhen-zuo-wei-jie-shou-zhe.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### 选择值或指针作为接收者

使用指针接收者的原因有二：

首先，方法能够修改其接收者指向的值。

其次，这样可以避免在每次调用方法时复制该值。若值的类型为大型结构体时，这样做会更加高效。

下面看下面的代码演示

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
func (v *Rectangle) Area() float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func (v *Rectangle) Scale(f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := &Rectangle{3, 4}
    fmt.Printf("调整比例之前 : %+v, Area: %v\n", v, v.Area())
    v.Scale(5)
    fmt.Printf("调整比例之后 : %+v, Area: %v\n", v, v.Area())
}
```

运行后得到的结果如下

```bash
调整比例之前 : &{width:3 height:4}, Area: 12
调整比例之后 : &{width:15 height:20}, Area: 300
```

在实例中， Scale 和 Area 接收者的类型为 \*Rectangle ，即便 Area 并不需要修改其接收者。

通常来说，所有给定类型的方法都应该有值或指针接收者，但并不应该二者混用。
