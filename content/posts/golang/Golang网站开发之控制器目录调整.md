---
title: "Golang网站开发之控制器目录调整"
date: "2025-08-04 18:07:40"
slug: "golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-mu-lu-tiao-zheng"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之控制器目录调整/"
  - "/2025/08/04/Golang网站开发之控制器目录调整.html"
  - "/Golang网站开发之控制器目录调整/"
  - "/Golang网站开发之控制器目录调整.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-mu-lu-tiao-zheng/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-mu-lu-tiao-zheng.html"
  - "/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-mu-lu-tiao-zheng.html"
---
Golang代码看的多了，你会更加理解其中的目录结果的部署，跟我们之前的后段语言，比如PHP还是有区别的。

比如我们命名一个控制文件的时候，叫做BlogController.php，然后里面会有create、update、delete等一些方法。我之前的博客wiki架构也采用了类似的方式，但是在golang中你会发现一些奇怪的问题，如目录看起来重叠

```bash
$ tree controllers/
controllers/
├── article
│   ├── article.go
│   └── save.go
├── article.go
├── json.go
├── upload.go
├── welcome
│   └── welcome.go
└── welcome.go
```

你会发现article/article.go，明明一个目录已经叫article了为什么，里面的文件还有一个叫article.go，感觉有些重复。之后从其文件的函数，以及golang的库函数可以发现，基本上一个函数一个文件，而且对应的函数文件会有一个函数的测试文件，这样在看目录的时候就很清楚。于是我将我的目录做了如下调整

```bash
$ tree controllers/
controllers/
├── article
│   ├── create.go
│   ├── delete.go
│   ├── error.go
│   ├── item.go
│   ├── save.go
│   ├── update.go
│   └── view.go
├── article.go
├── json.go
├── upload.go
├── welcome
│   └── welcome.go
└── welcome.go
```

在看下controller/article.go目录，是不是很清晰。

此时此刻，我觉得，这个golang可以不用什么框架的，针对自己项目的需求，自己搭建一个符合自己项目需求的框架，性能才会更好。
