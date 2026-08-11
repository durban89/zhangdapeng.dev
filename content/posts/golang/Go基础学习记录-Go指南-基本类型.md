---
title: "Go基础学习记录 - Go指南 - 基本类型"
date: "2025-07-30 14:59:31"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ji-ben-lei-xing"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-Go指南-基本类型/"
  - "/2025/07/30/Go基础学习记录-Go指南-基本类型.html"
  - "/Go基础学习记录-Go指南-基本类型/"
  - "/Go基础学习记录-Go指南-基本类型.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ji-ben-lei-xing/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ji-ben-lei-xing.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ji-ben-lei-xing.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **基本类型**

Go的基本类型有

* bool
* string
* int int8 int16 int32 int64
* uint uint8 uint16 uint32 uint64 uintptr
* byte // unit8的别名
* rune // int32的别名 表示一个Unicode码点
* float32 float64
* complex64 complex128

同导入一样，变量声明也可以"分组"成一个语法块.

int、uint和uintptr在32位系统上通常为32为宽，在63位系统上则为64位宽。当你需要一个整数值时应使用int类型，除非你有特殊的理由使用固定大小或无符号的整数类型。

```golang
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	Tobe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	const f = "%T(%v)\n"
	fmt.Printf(f, Tobe, Tobe)
	fmt.Printf(f, MaxInt, MaxInt)
	fmt.Printf(f, z, z)
}
```

运行结果类似如下

```bash
bool(false)
uint64(18446744073709551615)
complex128((2+3i))
```

---

### **零值**

没有明确初始值的变量声明会被赋予他们"零值"

零值包括

1. 数值类型为0
2. 布尔类型为false
3. 字符串为""(空字符串)

```golang
package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)
}
```

运行后输出如下

```bash
0 0 false ""
```
