---
title: "Go基础学习记录 - Go指南 - 指针与函数"
date: "2025-07-31 10:25:56"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-yu-han-shu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-指针与函数/"
  - "/2025/07/31/Go基础学习记录-Go指南-指针与函数.html"
  - "/Go基础学习记录-Go指南-指针与函数/"
  - "/Go基础学习记录-Go指南-指针与函数.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-yu-han-shu/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-yu-han-shu.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-zhi-zhen-yu-han-shu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **指针与函数**

简单记录下指针与函数，修改下上篇文章[[Go基础学习记录 - Go指南 - 指针接收者](https://www.xiaorongmao.com/blog/23)]的代码，将方法改为函数，实例[实例1]代码如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area Rectangle的面积
func Area(v Rectangle) float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func Scale(v *Rectangle, f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v)
    Scale(&v, 10)
    fmt.Println(v)
    fmt.Println(Area(v))
}
```

执行后结果如下

```bash
{3 4}
{30 40}
1200
```

然后将Scale中第一个参数的\*去掉，实例[实例2]代码如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area Rectangle的面积
func Area(v Rectangle) float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func Scale(v Rectangle, f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v)
    Scale(v, 10)
    fmt.Println(v)
    fmt.Println(Area(v))
}
```

运行后得到的结果如下

```bash
{3 4}
{3 4}
12
```

通过上面的两个例子的对比我们知道如果通过函数而不是方法的方式实现上篇文章的一样的效果的话，传递到参数需要接收一个指针

### **方法与指针重定向**

上面的两个实例中，实例1中

```go
Scale(v *Rectangle, f float64)
```

在调用的时候第一个参数必须传递一个指针，如果传递的不是指针，结果有异常，会遇到类似如下的错误

```javascript
cannot use v (type Rectangle) as type *Rectangle in argument to Scale
```

但是如果是上篇文章中，以指针为接收者的方法被调用时，接收者既能为值又能为指针，实例代码如下

```go
package main

import (
    "fmt"
)

// Rectangle 长方形
type Rectangle struct {
    width, height float64
}

// Area Rectangle的面积
func (v Rectangle) Area() float64 {
    return v.width * v.height
}

// Scale 用给定的值调整比例
func (v *Rectangle) Scale(f float64) {
    v.width = v.width * f
    v.height = v.height * f
}

func main() {
    v := Rectangle{3, 4}
    fmt.Println(v)
    v.Scale(10)
    fmt.Println(v)
    fmt.Println(v.Area())
    fmt.Println("=========== 分隔线 ============")
    p := &Rectangle{3, 4}
    fmt.Println(p)
    p.Scale(10)
    fmt.Println(p)
    fmt.Println(p.Area())
}
```

运行后输出结果如下

```bash
{3 4}
{30 40}
1200
=========== 分隔线 ============
&{3 4}
&{30 40}
1200
```

从上面p和v的对比就能看出最终的Area得出的值是一致的  
对于语句 v.Scale(10) ，即便 v 是个值而非指针，带指针接收者的方法也能被直接调用。 也就是说，由于 Scale 方法有一个指针接收者，为方便起见，Go 会将语句 v.Scale(10) 解释为 (&v).Scale(5)

如果在实例中在增加如下代码

```go
// ScaleFunc 用给定的值调整比例
func (v Rectangle) ScaleFunc(f float64) {
    v.width = v.width * f
    v.height = v.height * f
}
```

这个时候我们在调用的时候，如下代码

```go
m := &Rectangle{3, 4}
fmt.Println(m)
m.ScaleFunc(10)
fmt.Println(m)
fmt.Println(m.Area())
```

和下面的这段代码

```go
m := Rectangle{3, 4}
fmt.Println(m)
m.ScaleFunc(10)
fmt.Println(m)
fmt.Println(m.Area())
```

运行的结果是一致的

但是函数的话，如果接受的参数是指的话，必须传递值，如果传递指针程序会出异常。如果将ScaleFunc方法替换为函数，如下代码

```go
// ScaleFunc 用给定的值调整比例
func ScaleFunc(v Rectangle, f float64) {
    v.width = v.width * f
    v.height = v.height * f
}
```

```go
fmt.Println(ScaleFunc(v))  // OK
fmt.Println(ScaleFunc(&v)) // 编译错误！
```
