---
title: "Golang小知识 - const和var的使用区别"
date: "2025-08-05 09:48:06"
slug: "golang-xiao-zhi-shi-const-he-var-de-shi-yong-qu-bie"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang小知识-const和var的使用区别/"
  - "/2025/08/05/Golang小知识-const和var的使用区别.html"
  - "/Golang小知识-const和var的使用区别/"
  - "/Golang小知识-const和var的使用区别.html"
  - "/2025/08/05/golang-xiao-zhi-shi-const-he-var-de-shi-yong-qu-bie/"
  - "/2025/08/05/golang-xiao-zhi-shi-const-he-var-de-shi-yong-qu-bie.html"
  - "/golang-xiao-zhi-shi-const-he-var-de-shi-yong-qu-bie.html"
---
Golang小知识 - const和var的使用区别

第一个举例

const和var声明的变量值为整型

```go
package main

import "fmt"

func main() {
	const (
		a = 1
		b = 2
		c = 3
	)

	fmt.Println(a+b == c)

	var (
		m = 1
		n = 2
		o = 3
	)

	fmt.Println(m+n == o)
}
```

运行结果如下

```bash
$ go build -o ./build/app
$ ./build/app
true
true
```

第二个举例

const和var声明的变量值为浮点型

```go
package main

import "fmt"

func main() {
	const (
		a = 0.1
		b = 0.2
		c = 0.3
	)

	fmt.Println(a+b == c)

	var (
		m = 0.1
		n = 0.2
		o = 0.3
	)

	fmt.Println(m+n == o)
}
```

运行结果如下

```bash
$ go build -o ./build/app
$ ./build/app
true
false
```
