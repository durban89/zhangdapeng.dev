---
title: "Go基础学习记录 - Go指南 - 切片"
date: "2025-07-31 10:06:55"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-qie-pian"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-切片/"
  - "/2025/07/31/Go基础学习记录-Go指南-切片.html"
  - "/Go基础学习记录-Go指南-切片/"
  - "/Go基础学习记录-Go指南-切片.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-qie-pian/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-qie-pian.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-qie-pian.html"
---
### **环境**

> ### go version go1.10.1 darwin/amd64

### **切片**

每个数组的大小都是固定的。 而切片则为数组元素提供动态大小的、灵活的视角。 在实践中，切片比数组更常用。

类型 []T 表示一个元素类型为 T 的切片。

以下表达式为数组 a 的前五个元素创建了一个切片。

```go
a[0:5]
```

演示如下

```go
package main

import "fmt"

func main() {
    fruit := []string{"apple", "banana", "orange"}

    var spliceFruit = fruit[1:3]
    fmt.Println(spliceFruit)
}
```

### **切片可以像数组一样，通过索引来引用数值**

切片并不存储任何数据， 它只是描述了底层数组中的一段。

更改切片的元素会修改其底层数组中对应的元素。与它共享底层数组的切片都会监听到这些修改。实例如下

```go
package main

import "fmt"

func main() {
    fruits := []string{
        "apple",
        "banana",
        "orange",
        "tomato",
        "peach",
    }

    fmt.Println(fruits)

    a := fruits[0:2]
    b := fruits[1:3]
    fmt.Println(a, b)

    b[0] = "XXX"
    fmt.Println(a, b)
    fmt.Println(fruits)
}
```

### **切片语法**

切片语法类似于没有长度的数组语法。

这是一个数组文语法：

```go
[3]bool{true, true, false}
```

下面这样则会创建一个和上面相同的数组，然后构建一个引用了它的切片：

```go
[]bool{true, true, false}
```

下面使用跟过的实例演示下

```go
package main

import "fmt"

func main() {
    aNum := []int{
        1,
        2,
        3,
        4,
        5,
    }
    fmt.Println(aNum)

    aBool := []bool{
        true,
        false,
        true,
        false,
        true,
    }
    fmt.Println(aBool)

    aStruct := []struct {
        i int
        b bool
    }{
        {1, true},
        {2, false},
        {3, true},
        {4, false},
        {5, true},
    }
    fmt.Println(aStruct)
}
```

运行后得到如下结果

```bash
[1 2 3 4 5]
[true false true false true]
[{1 true} {2 false} {3 true} {4 false} {5 true}]
```

### **切片的默认行为**

在进行切片时，你可以利用它的默认行为来忽略上下界。

切片下界的默认值为 0 ，上界则是该切片的长度。

对于数组

```go
var a [10]int
```

来说，以下切片是等价的：

```go
a[0:10]
a[:10]
a[0:]
a[:]
```

下面简单的看个实例

```go
package main

import "fmt"

func main() {
    s := []int{2, 3, 5, 7, 11, 13}

    s1 := s[1:4]
    fmt.Println(s1)

    s2 := s[:2]
    fmt.Println(s2)

    s3 := s[1:]
    fmt.Println(s3)
}
```

### **切片的长度与容量**

切片拥有长度和容量。  
切片的长度就是它所包含的元素个数。  
切片的容量是从它的第一个元素开始数，到其底层数组元素末尾的个数。  
切片s的长度和容量可通过表达式len(s)和cap(s)来获取。  
你可以通过重新切片来扩展一个切片，给它提供足够的容量。如下实例

```go
package main

import "fmt"

func main() {
    s := []int{2, 3, 5, 7, 11, 13}
    printSlice(s)

    s = s[:0]
    printSlice(s)

    s = s[:4]
    printSlice(s)

    s = s[2:]
    printSlice(s)
}

func printSlice(s []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
```

运行后输出结果如下

```bash
len=6 cap=6 [2 3 5 7 11 13]
len=0 cap=6 []
len=4 cap=6 [2 3 5 7]
len=2 cap=4 [5 7]
```

从上面的输出可以看出来，前三个输出在没有改变上界的时候，容量的值是没有变的，但是在设置了上界值之后容量就变化了，这个后面开发的时候要引起注意。

### **nil 切片**

切片的零值是 nil 。nil 切片的长度和容量为 0 且没有底层数组。实例演示如下

```go
package main

import "fmt"

func main() {
    var s []int
    fmt.Println(s, len(s), cap(s))
    if s == nil {
        fmt.Println("nil!")
    }
}
```

运行后结果如下

```bash
[] 0 0
nil!
```

### **用 make 创建切片**

切面可以用内建函数make来创建，这也是创建动态数组的方式。  
make函数会分配一个元素为零值的数组并返回一个引用了它的切片：

```go
a := make([]int, 5)  // len(a)=5
```

如果要指定它的容量，需向 make 传入第三个参数：

```go
b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```

再来看个详细的实例

```go
package main

import "fmt"

func main() {
    a := make([]int, 5)
    printSlice("a", a)

    b := make([]int, 0, 5)
    printSlice("b", b)

    c := b[:2]
    printSlice("c", c)

    d := c[2:5]
    printSlice("d", d)
}

func printSlice(s string, x []int) {
    fmt.Printf("%s len=%d cap=%d %v\n",
        s, len(x), cap(x), x)
}
```

### **切片的切片**

切片可包含任何类型，甚至包括其它的切片。如下详细实例

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    // Create a tic-tac-toe board.
    board := [][]string{
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
    }

    // The players take turns.
    board[0][0] = "X"
    board[2][2] = "O"
    board[1][2] = "X"
    board[1][0] = "O"
    board[0][2] = "X"

    for i := 0; i < len(board); i++ {
        fmt.Printf("%s\n", strings.Join(board[i], " "))
    }
}
```

运行后结果输出如下

```bash
X _ X
O _ X
_ _ O
```

### **向切片追加元素**

为切片追加新的元素是种常用的操作，为此Go提供了内建的append函数。 append内建函数的详情介绍请转到这里[https://go-zh.org/pkg/builtin/#append]。

> func append(s []T, vs ...T) []T

append 的第一个参数 s 是一个元素类型为 T 的切片， 其余类型为 T 的值将会追加到该切片的末尾。  
append 的结果是一个包含原切片所有元素加上新添加元素的切片。  
当 s 的底层数组太小，不足以容纳所有给定的值时，它就会分配一个更大的数组。 返回的切片会指向这个新分配的数组。实例演示如下

```go
package main

import "fmt"

func main() {
    var fruits []string
    printSlice(fruits)

    fruits = append(fruits, "Apple")
    printSlice(fruits)

    fruits = append(fruits, "Orange")
    printSlice(fruits)

    fruits = append(fruits, "Banana", "Peach", "Tomoto")
    printSlice(fruits)
}

func printSlice(s []string) {
    fmt.Printf("len=%d, cap=%d, %v \n", len(s), cap(s), s)
}
```

运行后输出结果如下

```bash
len=0, cap=0, [] 
len=1, cap=1, [Apple] 
len=2, cap=2, [Apple Orange] 
len=5, cap=5, [Apple Orange Banana Peach Tomoto] 
```
