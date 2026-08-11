---
title: "Go基础学习记录 - Go指南 - 流程控制语句:if/else"
date: "2025-07-31 10:06:36"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-ifelse"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:if/else/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:if/else.html"
  - "/Go基础学习记录-Go指南-流程控制语句:if/else/"
  - "/Go基础学习记录-Go指南-流程控制语句:if/else.html"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-if-else/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-if-else.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-ifelse/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-ifelse.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-ifelse.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **if/else**

Go 的 if 语句与 for 循环类似，表达式外无需小括号 ( ) ，而大括号 { } 则是必须的。  
演示如下

```go
package main

import (
    "fmt"
    "math"
)

func sqrt(x float64) string {
    if x < 0 {
        return sqrt(-x) + "i"
    }

    return fmt.Sprint(math.Sqrt(x))
}

func main() {
    fmt.Println(sqrt(2), sqrt(-4))
}
```

运行后结果输出如下

```bash
1.4142135623730951 2i
```

### **if 的简短语句**

同 for 一样， if 语句可以在条件表达式前执行一个简单的语句。  
该语句声明的变量作用域仅在 if 之内。  
演示如下

```go
package main

import (
    "fmt"
    "math"
)

func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    }

    return lim
}

func main() {
    fmt.Println(
        pow(3, 2, 10),
        pow(3, 3, 20),
    )
}
```

运行后结果输出如下

```bash
9 20
```

### **if 和 else**

在 if 的简短语句中声明的变量同样可以在任何对应的 else 块中使用。演示如下

```go
package main

import (
    "fmt"
    "math"
)

func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    } else {
        fmt.Printf("%g >= %g\n", v, lim)
    }

    return lim
}

func main() {
    fmt.Println(
        pow(3, 2, 10),
        pow(3, 3, 20),
    )
}
```

运行后执行结果类似如下

```bash
27 >= 20
9 20
```

### **练习：循环与函数**

官网提供了一个简单的练习题，关于函数和循环：用牛顿法实现平方根函数。

在练习题中，牛顿法是通过选择一个起点 z 然后重复以下过程来求 Sqrt(x) 的近似值：  
![xiaorongmao](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1530890520/xiaorongmao/Go%E5%9F%BA%E7%A1%80%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95_-_Go%E6%8C%87%E5%8D%97_-_%E6%B5%81%E7%A8%8B%E6%8E%A7%E5%88%B6%E8%AF%AD%E5%8F%A5-if_else_1.png)

为此只需重复计算 10 次，并且观察不同的值（1，2，3，……）是如何逐步逼近结果的。 然后，修改循环条件，使得当值停止改变（或改变非常小）的时候退出循环。观察迭代次数是否变化。最后对比下与 math.Sqrt的取值是否接近,这个希望读者自己实现以下，这里我把我的贴到下面，希望读者做完后在对比下。不一定我的就是最好的

```go
package main

import (
    "fmt"
    "math"
)

func Sqrt(x float64) float64 {
    z := float64(1)
    for n := 0; n < 10; n++ {
        z = z - ((z*z - x) / (2 * z))
    }

    return z
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(math.Sqrt(2))
}
```

运行后结果如下

```bash
1.414213562373095
1.4142135623730951
```
