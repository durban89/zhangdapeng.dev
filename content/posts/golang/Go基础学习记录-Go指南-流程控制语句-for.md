---
title: "Go基础学习记录 - Go指南 - 流程控制语句:for"
date: "2025-07-31 10:06:34"
slug: "go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-for"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:for/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句:for.html"
  - "/Go基础学习记录-Go指南-流程控制语句:for/"
  - "/Go基础学习记录-Go指南-流程控制语句:for.html"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-for/"
  - "/2025/07/31/Go基础学习记录-Go指南-流程控制语句-for.html"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-for/"
  - "/2025/07/31/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-for.html"
  - "/go-ji-chu-xue-xi-ji-lu-go-zhi-nan-liu-cheng-kong-zhi-yu-ju-for.html"
---
### **环境**

> go version go1.10.1 darwin/amd64

### **for循环**

Go 只有一种循环结构： for 循环。

基本的 for 循环由三部分组成，它们用分号隔开：

> 初始化语句：在第一次迭代前执行
>
> 条件表达式：在每次迭代前求值
>
> 后置语句：在每次迭代的结尾执行

初始化语句通常为一句短变量声明，该变量声明仅在 for 语句的作用域中可见。

注意：和 C、Java、JavaScript 之类的语言不同，Go 的 for 语句后面没有小括号，大括号 { } 则是必须的。演示如下

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}

	fmt.Println(sum)
}
```

运行后结果如下

```bash
45
```

初始化语句和后置语句是可选的。演示如下

```go
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}

	fmt.Println(sum)
}
```

运行后结果如下

```bash
1024
```

可能这里有疑惑

```go
for sum < 1000 {
    sum += sum
}
```

实际上这里可以等价于如下

```go
for ; sum < 1000; {
    sum += sum
}
```

### **for 是 Go 中的 “while”**

此时你可以去掉分号：C 的 while 在 Go 中叫做 for 。跟上面是类似的

```go
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}

	fmt.Println(sum)
}
```

在go中可以用for当做while来使用

### **无限循环**

如果省略循环条件，该循环就不会结束，因此无限循环可以写得很紧凑。演示如下

```go
package main

func main() {
	for {
	}
}
```

### **for range循环 - 数组循环**

```go
package main

import "fmt"

func main() {
	fruits:=[]string{"苹果", "香蕉", "橘子"}

	for i,fruit:=range fruits{
		fmt.Println(i,fruit)
	}
}
```

### **for range循环 - 字典循环**

```go
package main

import "fmt"

func main() {
	fruits := map[string]int{"苹果":15,"香蕉":20,"橘子":36}

	for fruit,price := range fruits{
		fmt.Println(fruit,price)
	}
}
```
