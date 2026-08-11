---
title: "Golang小知识 - 别名的使用"
date: "2025-08-05 09:48:00"
slug: "golang-xiao-zhi-shi-bie-ming-de-shi-yong"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang小知识-别名的使用/"
  - "/2025/08/05/Golang小知识-别名的使用.html"
  - "/Golang小知识-别名的使用/"
  - "/Golang小知识-别名的使用.html"
  - "/2025/08/05/golang-xiao-zhi-shi-bie-ming-de-shi-yong/"
  - "/2025/08/05/golang-xiao-zhi-shi-bie-ming-de-shi-yong.html"
  - "/golang-xiao-zhi-shi-bie-ming-de-shi-yong.html"
---
初学者肯定知道 import 的作用

比如导入fmt包，只需要

```go
import (
	"fmt"
)
```

但是

```go
import (
	'fmt'
)
```

是不可以的，build的时候会报错的

```bash
$ go build -o ./build/app
can't load package: package .:
main.go:4:2: illegal rune literal
```

但是别名要如何使用

举个例子

```go
import (
	"fmt"
	a "fmt"
	b "fmt"
	c "fmt"
)
```

意思就是说我可以将`fmt`这个包名改名为`a`或者`b`或者`c`调用的时候要怎么用

举个例子

```go
func main() {
	fmt.Println("a string")
	a.Println("A")
	b.Println("B")
	c.Println("C")
}
```

在继续往下看答案之前，先想象下结果

结果如下

```bash
a string
A
B
C
```

小知识点每天掌握一点点，了解更深一点。
