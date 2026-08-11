---
title: "Go基础学习记录 - Go指南 - 常量、数值常量"
date: "2025-07-30 15:28:41"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-chang-liang-shu-zhi-chang-liang"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-Go指南-常量、数值常量/"
  - "/2025/07/30/Go基础学习记录-Go指南-常量、数值常量.html"
  - "/Go基础学习记录-Go指南-常量、数值常量/"
  - "/Go基础学习记录-Go指南-常量、数值常量.html"
  - "/2025/07/30/Go基础学习记录-Go指南-常量-数值常量/"
  - "/2025/07/30/Go基础学习记录-Go指南-常量-数值常量.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-chang-liang-shu-zhi-chang-liang/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-chang-liang-shu-zhi-chang-liang.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-chang-liang-shu-zhi-chang-liang.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **常量**

常量的声明与变量类似，只不过是使用 const 关键字。

常量可以是字符、字符串、布尔值或数值。

常量不能用 := 语法声明。

演示如下

```go
package main

import "fmt"

const Pi = 3.14

func main() {
	const world = "世界"
	fmt.Println("Hello", world)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}
```

运行后输出如下

```bash
Hello 世界
Happy 3.14 Day
Go rules? true
```

### **数值常量**

数值常量是高精度的 值 。

一个未指定类型的常量由上下文来决定其类型。

再尝试一下输出 needInt(Big) 吧。

（int 类型最大可以存储一个 64 位的整数，有时会更小。）

（int 可以存放最大64位的整数，根据平台不同有时会更少。）

演示如下

```go
package main

import "fmt"

const (
	Big   = 1 << 100
	Small = Big >> 99
)

func needInt(x int) int {
	return x*10 + 1
}

func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Big))
	fmt.Println(needFloat(Small))
	// fmt.Println(needInt(Big))
}
```

运行后输出如下

```bash
21
1.2676506002282295e+29
0.2
```
