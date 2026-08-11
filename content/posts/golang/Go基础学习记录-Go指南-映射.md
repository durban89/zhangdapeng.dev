---
title: "Go基础学习记录 - Go指南 - 映射"
date: "2025-07-31 10:25:28"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ying-she"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-映射/"
  - "/2025/07/31/Go基础学习记录-Go指南-映射.html"
  - "/Go基础学习记录-Go指南-映射/"
  - "/Go基础学习记录-Go指南-映射.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ying-she/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ying-she.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-ying-she.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

## **映射**

### **映射将键映射到值。**

映射的零值为nil，nil映射既没有键，也不能添加键。make函数会返回给定类型的映射，并将其初始化备用。如下演示

```go
package main

import "fmt"

// Rectangle width height
type Rectangle struct {
  width, height float64
}

var m map[string]Rectangle

func main() {
  m = make(map[string]Rectangle)
  m["one"] = Rectangle{
    40.68433, 74.39967,
  }
  fmt.Println(m["one"])
}
```

### **映射的语法**

映射的语法与结构体相似，不过必须有键名。

```go
package main

import "fmt"

// Rectangle width height
type Rectangle struct {
  width, height float64
}

var m = map[string]Rectangle{
  "one": Rectangle{
    40.68433, 74.39967,
  },
  "two": Rectangle{
    37.42202, 122.08408,
  },
}

func main() {
  fmt.Println(m)
}
```

### **映射的语法 特殊情况**

若顶级类型只是一个类型名，则可以在语法的元素中省略它。

```go
package main

import "fmt"

// Rectangle width height
type Rectangle struct {
  width, height float64
}

var m = map[string]Rectangle{
  "one": {40.68433, 74.39967},
  "two": {37.42202, 122.08408},
}

func main() {
  fmt.Println(m)
}
```

### **修改映射**

在映射m中插入或修改元素：

```go
m[key] = elem
```

获取元素：

```go
elem = m[key]
```

删除元素：

```go
delete(m, key)
```

通过双赋值检测某个键是否存在：

```go
elem, ok = m[key]
```

若 key 在 m 中， ok 为 true ；否则， ok 为 false 。  
若 key 不在映射中，那么 elem 是该映射元素类型的零值。  
同样的，当从 映射 中读取某个不存在的键时，结果是 映射 的元素类型的零值。  
注 ：若 elem 或 ok 还未声明，可以使用短变量声明：

```go
elem, ok := m[key]
```

下面看个详细的实例演示

```go
package main

import "fmt"

func main() {
  m := make(map[string]int)

  m["Q"] = 42
  fmt.Println("The value:", m["Q"])

  m["Q"] = 48
  fmt.Println("The value:", m["Q"])

  delete(m, "Q")
  fmt.Println("The value:", m["Q"])

  v, ok := m["Q"]
  fmt.Println("The value:", v, "status:", ok)
}
```

运行后结果如下

```bash
The value: 42
The value: 48
The value: 0
The value: 0 status: false
```

### **练习：映射**

实现 WordCount 。它应当返回一个映射，其中包含每个字符串 s 中"单词"的个数。函数 wc.Test 会对此函数执行一系列测试用例，并输出成功还是失败。  
[strings.Fields](https://go-zh.org/pkg/strings/#Fields) 很有帮助。  
这个是官网的例子，下面是我的实现方式，有兴趣的可以实现下

```go
package main

import "strings"
import (
  "golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
  var x = make(map[string]int)
  for _,n := range strings.Fields(s) {
    x[n] += 1
  }
  return x
}

func main() {
  wc.Test(WordCount)
}
```

运行后输出结果如下

```bash
PASS
 f("I am learning Go!") = 
  map[string]int{"I":1, "am":1, "learning":1, "Go!":1}
PASS
 f("The quick brown fox jumped over the lazy dog.") = 
  map[string]int{"brown":1, "fox":1, "dog.":1, "The":1, "jumped":1, "over":1, "the":1, "lazy":1, "quick":1}
PASS
 f("I ate a donut. Then I ate another donut.") = 
  map[string]int{"I":2, "ate":2, "a":1, "donut.":2, "Then":1, "another":1}
PASS
 f("A man a plan a canal panama.") = 
  map[string]int{"A":1, "man":1, "a":2, "plan":1, "canal":1, "panama.":1}
```

PASS代表通过测试，给自己点个"赞"
