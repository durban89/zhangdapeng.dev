---
title: "Go基础学习记录 - Go指南 - 结构体"
date: "2025-07-31 10:06:49"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-gou-ti"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-结构体/"
  - "/2025/07/31/Go基础学习记录-Go指南-结构体.html"
  - "/Go基础学习记录-Go指南-结构体/"
  - "/Go基础学习记录-Go指南-结构体.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-gou-ti/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-gou-ti.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-gou-ti.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **结构体**

一个结构体(struct)就是一个字段的集合。(而type声明就是定义类型的)。详细的介绍可以看下面的实例

```go
package main

import "fmt"

// Rectangle 长方形
type Rectangle struct {
  width  int
  height int
}

func main() {
  fmt.Println(Rectangle{3, 4})
}
```

运行后输出如下

```bash
{3 4}
```

### **结构体字段**

结构体字段使用点号来访问。

```go
package main

import "fmt"

// Rectangle 长方形
type Rectangle struct {
  width  int
  height int
}

func main() {
  rectangle := Rectangle{3, 4}
  rectangle.width = 4
  fmt.Println(rectangle.width)
}
```

运行后输出如下

```bash
4
```

### **结构体指针**

结构体字段可以通过结构体指针来访问。

如果有一个指向结构体的指p，那么可以通过(\*p).X 来访问其字段X。不过这么写太啰嗦了，所以语言也允许我们使用隐式间接引用，直接写 p.X 就可以。

```go
package main

import "fmt"

// Rectangle 长方形
type Rectangle struct {
  width  int
  height int
}

func main() {
  rectangle := Rectangle{3, 4}
  p := &rectangle
  p.width = 1e9
  fmt.Println(rectangle)
}
```

运行后输出如下

```bash
{1000000000 4}
```

### **结构体文法**

结构体文法通过直接列出字段的值来新分配一个结构体。

使用Name:语法可以仅列出部分字段。(字段名的顺序无关)

特殊的前缀 & 返回一个指向结构体的指针。如下

```go
package main

import "fmt"

// Rectangle 长方形
type Rectangle struct {
  width  int
  height int
}

var (
  a = Rectangle{3, 4}     // Rectangle类型
  b = Rectangle{width: 1} // height:0 是隐含的
  c = Rectangle{}         // width:0和height:0是隐含的
  d = &Rectangle{5, 6}    // &Rectangle类型
)

func main() {
  fmt.Println(a, b, c, d)
}
```

运行后结果如下

```bash
{3 4} {1 0} {0 0} &{5 6}
```
