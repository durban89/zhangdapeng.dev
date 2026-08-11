---
title: "Go基础学习记录 - Go指南 - 指针"
date: "2025-07-31 10:06:46"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-指针/"
  - "/2025/07/31/Go基础学习记录-Go指南-指针.html"
  - "/Go基础学习记录-Go指南-指针/"
  - "/Go基础学习记录-Go指南-指针.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **指针**

Go 具有指针。 指针保存了变量的内存地址。

类型 `\*T` 是指向 T 类型值的指针。其零值为 nil 。

```go
var p *int
```

& 操作符会生成一个指向其操作数的指针。

```go
i := 42
p = &i
```

\* 操作符表示指针指向的底层值。

```go
fmt.Println(*p) // 通过指针 p 读取 i
*p = 21         // 通过指针 p 设置 i
```

这也就是通常所说的"间接引用"或"重定向"。

与 C 不同，Go 没有指针运算。

示例如下

```go
package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i         // 指向i
	fmt.Println(*p) // 通过指针读取i的值
	*p = 21         // 通过指针设置i的值
	fmt.Println(i)  // 查看i的新值

	p = &j         // 指向j
	*p = *p / 37   // 通过指针对j进行除法计算
	fmt.Println(j) // 查看j的新值
}
```

可以从注释上理解下指针的用法
