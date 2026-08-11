---
title: "Go基础学习记录 - Go指南 - 类型断言"
date: "2025-07-31 10:26:04"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-duan-yan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-类型断言/"
  - "/2025/07/31/Go基础学习记录-Go指南-类型断言.html"
  - "/Go基础学习记录-Go指南-类型断言/"
  - "/Go基础学习记录-Go指南-类型断言.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-duan-yan/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-duan-yan.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-duan-yan.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **类型断言**

类型断言 提供了访问接口值底层具体值的方式。

```go
t := i.(T)
```

该语句断言接口值 i 保存了具体类型 T ，并将其底层类型为 T 的值赋予变量 t 。

若 i 并未保存 T 类型的值，该语句就会触发一个异常。

为了 判断 一个接口值是否保存了一个特定的类型， 类型断言可返回两个值：其底层值以及一个报告断言是否成功的布尔值。

```go
t, ok := i.(T)
```

若 i 保存了一个 T ，那么 t 将会是其底层值，而 ok 为 true 。

否则， ok 将为 false 而 t 将为 T 类型的零值，程序并不会产生异常。

请注意这种语法和读取一个映射时的相同之处。示例如下

```go
package main

import "fmt"

func main() {
    var i interface{} = "hello"

    s := i.(string)
    fmt.Println(s)

    s, ok := i.(string)
    fmt.Println(s, ok)

    f, ok := i.(float64)
    fmt.Println(f, ok)

    f = i.(float64) // panic
    fmt.Println(f)
}
```

稍微解释下

```go
f = i.(float64) // panic
fmt.Println(f)
```

这里就是讲的意思就是 保存的类型值不是一个string而是一个float，从

```go
var i interface{} = "hello"
```

这里可以看出，接口的类型值是一个string，这个时候给予float64的话，导致类型不符合而报错
