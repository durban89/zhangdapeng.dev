---
title: "Go基础学习记录 - Go指南 - 接口"
date: "2025-07-31 10:26:02"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-kou"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-接口/"
  - "/2025/07/31/Go基础学习记录-Go指南-接口.html"
  - "/Go基础学习记录-Go指南-接口/"
  - "/Go基础学习记录-Go指南-接口.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-kou/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-kou.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-jie-kou.html"
---
**环境**

> go version go1.10.1 darwin/amd64

### **接口**

接口类型 是由一组方法签名定义的集合。接口类型的值可以保存任何实现了这些方法的值。实例演示如下

```go
package main

import (
    "fmt"
    "math"
)

// Rectangle 长方形接口
type Rectangle interface {
    Area() float64
}

func main() {
    var a Rectangle
    f := MyFloat(-math.Sqrt2)
    v := Square{3}

    a = f  // a MyFloat 实现了 Rectangle
    a = &v // a *Square 实现了 Rectangle

    // 下面一行，v 是一个 Square（而不是 *Square）
    // 所以没有实现 Rectangle
    // a = v

    fmt.Println(a.Area())
}

// MyFloat 自定义的类型
type MyFloat float64

// Area Area方法
func (f MyFloat) Area() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

// Square 正方形
type Square struct {
    width float64
}

// Area 面积
func (v *Square) Area() float64 {
    return v.width * v.width
}
```

注意：

```go
a = v
```

这行代码会报错的  
原因是，由于 Area 方法只为 \*Square （指针类型）定义， 因此 Square （值类型）并未实现 Rectangle。

### **接口与隐式实现**

类型通过实现一个接口的所有方法来实现该接口。 既然无需专门显式声明，也就没有“implements“关键字。

隐式接口从接口的实现中解耦了定义，这样接口的实现可以出现在任何包中，无需提前准备。

因此，也就无需在每一个实现上增加新的接口名称，这样同时也鼓励了明确的接口定义。

### **接口值**

在内部，接口值可以看做包含值和具体类型的元组，如下

```go
(value, type)
```

接口值保存了一个具体底层类型的具体值。接口值调用方法时会执行其底层类型的同名方法。实例演示如下

```go
package main

import (
    "fmt"
    "math"
)

type I interface {
    M()
}

type T struct {
    S string
}

func (t *T) M() {
    fmt.Println(t.S)
}

type F float64

func (f F) M() {
    fmt.Println(f)
}

func main() {
    var i I

    i = &T{"Hello"}
    describe(i)
    i.M()

    i = F(math.Pi)
    describe(i)
    i.M()
}

func describe(i I) {
    fmt.Printf("(%v, %T)\n", i, i)
}
```

运行后得到的结果如下

```bash
(&{Hello}, *main.T)
Hello
(3.141592653589793, main.F)
3.141592653589793
```

### **底层值为 nil 的接口值**

即便接口内的具体值为 nil，方法仍然会被 nil 接收者调用。

在一些语言中，这会触发一个空指针异常，但在 Go 中通常会写一些方法来优雅地处理它（如本例中的 M 方法）。注意： 保存了 nil 具体值的接口其自身并不为 nil 。实例演示如下

```go
package main

import "fmt"

type I interface {
    M()
}

type T struct {
    S string
}

func (t *T) M() {
    if t == nil {
        fmt.Println("<nil>")
        return
    }

    fmt.Println(t.S)
}

func main() {
    var i I

    var t *T

    i = t

    describe(i)
    i.M()

    i = &T{"Hello"}
    describe(i)
    i.M()
}

func describe(i I) {
    fmt.Printf("(%v, %T)", i, i)
}
```

运行后得到的结果如下

```bash
(<nil>, *main.T)<nil>
(&{Hello}, *main.T)Hello
```

### **nil 接口值**

nil 接口值既不保存值也不保存具体类型。为 nil 接口调用方法会产生运行时错误，因为接口的元组内并未包含能够指明该调用哪个 具体 方法的类型。实例演示如下

```go
package main

import "fmt"

type I interface {
    M()
}

func main() {
    var i I

    describe(i)
    i.M()

}

func describe(i I) {
    fmt.Println("(%v, %T)", i, i)
}
```

运行后结果输出如下

```bash
(%v, %T) <nil> <nil>
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x108d66b]

goroutine 1 [running]:
main.main()
    /Users/durban/go/src/github.com/durban.zhang/example/example.go:13 +0x2b
exit status 2
```

### **空接口**

指定了零个方法的接口值被称为 空接口：

```go
interface{}
```

空接口可保存任何类型的值。 （因为每个类型都至少实现了零个方法。）空接口被用来处理未知类型的值。 例如，fmt.Print 可接受类型为 interface{} 的任意数量的参数。如下实例演示

```go
package main

import "fmt"

func main() {
    var i interface{}

    describe(i)

    i = 42
    describe(i)

    i = "Hello"
    describe(i)
}

func describe(i interface{}) {
    fmt.Printf("(%v, %T)\n", i, i)
}
```

运行后输出结果如下

```bash
(<nil>, <nil>)
(42, int)
(Hello, string)
```
