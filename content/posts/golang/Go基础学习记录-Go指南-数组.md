---
title: "Go基础学习记录 - Go指南 - 数组"
date: "2025-07-31 10:06:52"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-shu-zu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-数组/"
  - "/2025/07/31/Go基础学习记录-Go指南-数组.html"
  - "/Go基础学习记录-Go指南-数组/"
  - "/Go基础学习记录-Go指南-数组.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-shu-zu/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-shu-zu.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-shu-zu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **数组**

类型[n]T表示拥有n个T类型的值的数组。

表达式

```go
var a [10]int
```

会将变量a声明为拥有有10个整数的数组。

数组的长度是其类型的一部分，因此数组不能改变大小。 这看起来是个限制，不过没关系， Go 提供了更加便利的方式来使用数组。示例如下

```go
package main

import "fmt"

func main() {
    var fruit [3]string
    fruit[0] = "Apple"
    fruit[1] = "Banana"
    fruit[2] = "Orange"
    fmt.Println(fruit[0], fruit[1], fruit[2])
    fmt.Println(fruit)

    score := [6]int{90, 89, 87, 68, 100, 99}
    fmt.Println(score)
}
```

运行后得到的结果如下

```bash
Apple Banana Orange
[Apple Banana Orange]
[90 89 87 68 100 99]
```
