---
title: "Golang知识点：interface与string之间的转换"
date: "2025-08-04 18:07:54"
slug: "golang-zhi-shi-dian-interface-yu-string-zhi-jian-de-zhuan-huan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang知识点：interface与string之间的转换/"
  - "/2025/08/04/Golang知识点：interface与string之间的转换.html"
  - "/Golang知识点：interface与string之间的转换/"
  - "/Golang知识点：interface与string之间的转换.html"
  - "/2025/08/04/golang-zhi-shi-dian-interface-yu-string-zhi-jian-de-zhuan-huan/"
  - "/2025/08/04/golang-zhi-shi-dian-interface-yu-string-zhi-jian-de-zhuan-huan.html"
  - "/golang-zhi-shi-dian-interface-yu-string-zhi-jian-de-zhuan-huan.html"
---
简单总结下*interface与string之间的转换*方式，新手可以尝试下，方便以后使用中查询

### 第一种*interface与string之间的转换*方式如下

```go
var x interface{} = "abc"
str := fmt.Sprintf("%v", x)
```

### 第二种*interface与string之间的转换*方式如下

```go
var x interface{} = []int{1, 2, 3}
str := fmt.Sprintf("%v", x)
fmt.Println(str) // "[1 2 3]"
```

### 第三种*interface与string之间的转换*方式如下

map的类型是`map[string]interface{}`的时候需要需要添加`.(string)`，使用方式如下

```go
value := arguments["key"].(string)
```

### 第四种*interface与string之间的转换*方式如下

最新版本的`Docopt`会返回一个Opts对象，这个对象有一个转换方法，使用方式如下

```go
value, err := arguments.String("key")
```

参考如下：

https://yourbasic.org/golang/interface-to-string/  

https://stackoverflow.com/questions/27137521/how-to-convert-interface-to-string
