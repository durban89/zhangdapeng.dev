---
title: "Go基础学习记录 - Go指南 - Stringer"
date: "2025-07-31 10:26:10"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-stringer"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-Stringer/"
  - "/2025/07/31/Go基础学习记录-Go指南-Stringer.html"
  - "/Go基础学习记录-Go指南-Stringer/"
  - "/Go基础学习记录-Go指南-Stringer.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-stringer/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-stringer.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-stringer.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **Stringer**

fmt 包中定义的 Stringer 是最普遍的接口之一。

```go
type Stringer interface {
    String() string
}
```

Stringer 是一个可以用字符串描述自己的类型。fmt 包（还有很多包）都通过此接口来打印值。

```go
package main

import "fmt"

type Person struct {
    Name string
    Age  int
}

func (p Person) String() string {
    return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func main() {
    a := Person{"Durban Zhang", 42}
    z := Person{"Skuran Ma", 42}
    fmt.Println(a, z)
}
```

### **练习：Stringer**

通过让 IPAddr 类型实现 fmt.Stringer 来打印点号分隔的地址。例如，IPAddr{1, 2, 3, 4} 应当打印为 "1.2.3.4" 。  
这个实现还是比较简单的，如果上面的例子看懂了这个实现起来根本不费力气。

```go
package main

import "fmt"

type IPAddr [4]byte

// TODO: Add a "String() string" method to IPAddr.

func (ip IPAddr) String() string {
    return fmt.Sprintf("%v.%v.%v.%v", ip[0],ip[1],ip[2],ip[3])
}

func main() {
    hosts := map[string]IPAddr{
        "loopback":  {127, 0, 0, 1},
        "googleDNS": {8, 8, 8, 8},
    }
    for name, ip := range hosts {
        fmt.Printf("%v: %v\n", name, ip)
    }
}
```
