---
title: "Go基础学习记录 - Go指南 - 类型选择"
date: "2025-07-31 10:26:07"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-xuan-ze"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-类型选择/"
  - "/2025/07/31/Go基础学习记录-Go指南-类型选择.html"
  - "/Go基础学习记录-Go指南-类型选择/"
  - "/Go基础学习记录-Go指南-类型选择.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-xuan-ze/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-xuan-ze.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-lei-xing-xuan-ze.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **类型选择**

类型选择 是一种按顺序从几个类型断言中选择分支的结构。

类型选择与一般的 switch 语句相似，不过类型选择中的 case 为类型（而非值）， 它们针对给定接口值所存储的值的类型进行比较。

```go
switch v := i.(type) {
case T:
    // v 的类型为 T
case S:
    // v 的类型为 S
default:
    // 没有匹配，v 与 i 的类型相同
}
```

类型选择中的声明与类型断言 i.(T) 的语法相同，只是具体类型 T 被替换成了关键字 type 。此选择语句判断接口值 i 保存的值类型是 T 还是 S 。 在 T 或 S 的情况下，变量 v 会分别按 T 或 S 类型保存 i 拥有的值。 在默认（即没有匹配）的情况下，变量 v 与 i 的接口类型和值相同，具体使用如下

```go
package main

import "fmt"

func do(i interface{}) {
    switch v := i.(type) {
    case int: // int类型
        fmt.Printf("Twice %v is %v\n", v, v*2)
    case string: // string类型
        fmt.Printf("%q is %v bytes long\n", v, len(v))
    default:
        fmt.Printf("I don't know about type %T!\n", v)
    }
}

func main() {
    do(21)
    do("hello")
    do(true)
}
```

运行后得到的结果如下

```bash
Twice 21 is 42
"hello" is 5 bytes long
I don't know about type bool!
```
