---
title: "Go基础学习记录 - 包、变量和函数"
date: "2025-07-30 14:59:27"
slug: "go-ji-chu-xue-xi-ji-lu-bao-bian-liang-he-han-shu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/30/Go基础学习记录-包、变量和函数/"
  - "/2025/07/30/Go基础学习记录-包、变量和函数.html"
  - "/Go基础学习记录-包、变量和函数/"
  - "/Go基础学习记录-包、变量和函数.html"
  - "/2025/07/30/Go基础学习记录-包-变量和函数/"
  - "/2025/07/30/Go基础学习记录-包-变量和函数.html"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-bao-bian-liang-he-han-shu/"
  - "/2025/07/30/go-ji-chu-xue-xi-ji-lu-bao-bian-liang-he-han-shu.html"
  - "/go-ji-chu-xue-xi-ji-lu-bao-bian-liang-he-han-shu.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### 

### **包**

每个 Go 程序都是由包构成的。程序从 main 包开始运行。如下代码通过导入路径 "fmt" 和 "math/rand" 来使用这两个包。

按照约定，包名与导入路径的最后一个元素一致。例如，"math/rand" 包中的源码均以 package rand 语句开始。

```go
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```

此代码用圆括号组合了导入，这是“分组”形式的导入语句。

### **包的导入**

导入也可以编写多个导入语句，例如：

```go
package main

import "fmt"
import "math"

func main() {
	fmt.Println("Now you have %g problems.", math.Sqrt(7))
}
```

上面代码中

```go
import "fmt"
import "math"
```

这部分，fmt和math分开导入

不过使用分组导入语句是更好的形式。

### **包的导出名字**

在 Go 中，如果一个名字以大写字母开头，那么它就是已导出的。 例如， Pizza 就是个已导出名， Pi 也同样，它导出自 math 包。

pizza 和 pi 并未以大写字母开头，所以它们是未导出的。

在导入一个包时，只能引用其中已导出的名字。任何“未导出”的名字在该包外均无法访问。

执行如下代码，观察错误输出。

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.pi)
}
```

执行后输出类似如下的错误

```bash
example/export.go:9:14: cannot refer to unexported name math.pi
example/export.go:9:14: undefined: math.pi
```

将 math.pi 改名为 math.Pi 再试着执行一次。代码如下

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Pi)
}
```

执行后输出结果如下

```bash
3.141592653589793
```

### **变量声明**

var 语句用于声明一个变量列表

就像如下代码中看到的一样， var 语句可以出现在包或函数级别。

```go
package main

import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}
```

执行后会得到类似如下输出的结果

```bash
false false false 0
```

### **变量初始化**

变量声明可以包含初始值，每个变量对应一个。

如果初始化值已存在，则可以省略类型；变量会从初始值中获得类型。如下

```go
package main

import "fmt"

var i, j int = 1, 2

func main() {
	var a, b, c = true, false, "no!"
	fmt.Println(i, j, a, b, c)
}
```

运行后得到类似如下结果

```bash
1 2 true false no!
```

### **短变量声明**

在函数中，简洁赋值语句 := 可在类型明确的地方代替 var 声明。

函数外的每个语句都必须以关键字开始（ var 、 func 等等）， 因此 := 结构不能在函数外使用。如下

```go
package main

import "fmt"

k := 3

func main() {
	var i, j int = 1, 2
	k := 3
	a, b, c := true, false, "no"

	fmt.Println(i,j,k,a,b,c)
}
```

运行后会得到如下输出

```bash
example/variables_small_init.go:5:1: syntax error: non-declaration statement outside function body
```

当把函数外的k := 3去掉后运行得到类似如下结果

```bash
1 2 3 true false no
```

### **函数**

函数可以没有参数或接受多个参数。在如下代码中， add 接受两个 int 类型的参数。注意类型在变量名之后。

```go
package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(1, 2))
}
```

当连续两个或多个函数的已命名形参类型相同时，除最后一个类型以外，其它都可以省略。如下

```go
package main

import "fmt"

func add(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(1, 2))
}
```

将

```bash
x int, y int
```

改为

```bash
x, y int
```

### **函数多值返回**

函数可以返回任意数量的返回值。如下swap函数返回了两个字符串。

```go
package main

import "fmt"

func swap() (string, string) {
	return "1", "2"
}

func main() {
	a, b := swap()
	fmt.Println(a, b)
}
```

### **命名返回值**

Go 的返回值可被命名，它们会被视作定义在函数顶部的变量。返回值的名称应当具有一定的意义，它可以作为文档使用。没有参数的 return 语句返回已命名的返回值。也就是`直接`返回。直接返回语句应当仅用在下面这样的短函数中。在长的函数中它们会影响代码的可读性。如下

```go
package main

import "fmt"

func add(sum int) (x, y int) {
	x = sum + 1
	y = sum + 2
	return
}

func main() {
	fmt.Println(add(1))
}
```
