---
title: "Go基础学习记录 - Go指南 - 错误"
date: "2025-07-31 10:26:13"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-cuo-wu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-错误/"
  - "/2025/07/31/Go基础学习记录-Go指南-错误.html"
  - "/Go基础学习记录-Go指南-错误/"
  - "/Go基础学习记录-Go指南-错误.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-cuo-wu/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-cuo-wu.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-cuo-wu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **错误**

Go 程序使用 error 值来表示错误状态。

与 fmt.Stringer 类似， error 类型是一个内建接口：

```go
type error interface {
    Error() string
}
```

(与 fmt.Stringer 类似， fmt 包在打印值时也会满足 error 。)

通常函数会返回一个 error 值，调用它的代码应当判断这个错误是否等于 nil 来进行错误处理。

```go
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Printf("couldn't convert number: %v\n", err)
    return
}

fmt.Println("Converted integer:", i)
```

error 为 nil 时表示成功；非 nil 的 error 表示失败。如下实例

```go
package main

import (
    "fmt"
    "time"
)

type CustomError struct {
    When time.Time
    What string
}

func (e CustomError) Error() string {
    return fmt.Sprintf("时间 %v, %s", e.When, e.What)
}

func run() error {
    return &CustomError{
        time.Now(),
        "Running Wrong",
    }
}

func main() {
    if err := run(); err != nil {
        fmt.Println(err)
    }
}
```

注意这里要实现的方法

```go
func (e CustomError) Error() string {
    return fmt.Sprintf("时间 %v, %s", e.When, e.What)
}
```

只有实现了这个才符合接口的定义

### **练习：错误**

从之前的练习中[https://www.xiaorongmao.com/blog/12]复制 Sqrt 函数，修改它使其返回 error 值。  
之前实现的函数如下

```go
func Sqrt(x float64) float64 {
    z := float64(1)
    for n := 0; n < 10; n++ {
        z = z - ((z*z - x) / (2 * z))
    }

    return z
}
```

Sqrt 接受到一个负数时，应当返回一个非 nil 的错误值。复数同样也不被支持。

创建一个新的类型

```go
type ErrNegativeSqrt float64
```

并为其实现

```go
func (e ErrNegativeSqrt) Error() string
```

方法使其拥有 error 值，通过 ErrNegativeSqrt(-2).Error() 调用该方法应返回 "cannot Sqrt negative number: -2" 。

```go
package main

import (
    "fmt"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
    return fmt.Sprintf("cannot Sqrt negative number: %v", float64(e))
}

func Sqrt(x float64) (float64, error) {
    if x < 0 {
        return x, ErrNegativeSqrt(x)
    }

    z := float64(1)
    for n := 0; n < 10; n++ {
        z = z - ((z*z - x) / (2 * z))
    }

    return z, nil
    // return 0, nil
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(Sqrt(-2))
}
```

运行后得到的结果如下

```bash
1.414213562373095 <nil>
-2 cannot Sqrt negative number: -2
```

注意： 在 Error 方法内调用 fmt.Sprintf(e) 会让程序陷入死循环。可以通过先转换 e 来避免这个问题：fmt.Sprintf(float64(e)) 。这是为什么呢？  
暂时并没有找到官方的权威回复，找到的也只说如果e被调用的时候，实际上是调用了e.Error()，这样就会不断的调用e.Error()从而导致死循环
