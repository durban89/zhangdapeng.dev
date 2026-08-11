---
title: "Golang中template的使用注意事项（ParseFiles和ExecuteTemplate）"
date: "2025-08-04 18:08:11"
slug: "golang-zhong-template-de-shi-yong-zhu-yi-shi-xiang-parsefiles-he-executetemplate"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang中template的使用注意事项（ParseFiles和ExecuteTemplate）/"
  - "/2025/08/04/Golang中template的使用注意事项（ParseFiles和ExecuteTemplate）.html"
  - "/Golang中template的使用注意事项（ParseFiles和ExecuteTemplate）/"
  - "/Golang中template的使用注意事项（ParseFiles和ExecuteTemplate）.html"
  - "/2025/08/04/Golang中template的使用注意事项-ParseFiles和ExecuteTemplate/"
  - "/2025/08/04/Golang中template的使用注意事项-ParseFiles和ExecuteTemplate.html"
  - "/2025/08/04/golang-zhong-template-de-shi-yong-zhu-yi-shi-xiang-parsefiles-he-executetemplate/"
  - "/2025/08/04/golang-zhong-template-de-shi-yong-zhu-yi-shi-xiang-parsefiles-he-executetemplate.html"
  - "/golang-zhong-template-de-shi-yong-zhu-yi-shi-xiang-parsefiles-he-executetemplate.html"
---
最近在开发博客网站，在渲染模板这块用的稍微多一些，但是遇到的问题也会多一些，每次遇到问题都能更加的了解一些，所以没事多写点东西，尤其是自己开发一些功能

先看下 ParseFiles(filenames ...string) 提示：至少要传入一个文件

如下使用方式

```go
var TemplatesFiles []string{
	"template/index.html",
	"template/login.html",
	"template/logout.html"
}

t, err := template.ParseFiles(TemplatesFiles...)

var name = "index.html"

t.ExecuteTemplate(w, name, nil)
```

当我再加一个模板文件的时候，如下

```go
var TemplatesFiles []string{
	"template/index.html",
	"template/login.html",
	"template/logout.html",
	"template/auth/profile.html" // 多加的文件
}

t, err := template.ParseFiles(TemplatesFiles...)

var name = "auth/profile.html"

t.ExecuteTemplate(w, name, nil)
```

提示我找不到“auth/profile.html”这个文件

首先我们看下官方文档`func (t *Template) ParseFiles(filenames ...string) (*Template, error)`

这个函数的描述有下面一句话

> When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

官方有一个这样的描述，我英文不好，但是我看下另外一个方法`func ParseFiles(filenames ...string) (*Template, error)`

其下面有另外一个描述

> When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results. For instance, ParseFiles("a/foo", "b/foo") stores "b/foo" as the template named "foo", while "a/foo" is unavailable.

有个例子ParseFiles("a/foo", "b/foo")，最后我们存储"b/foo"作为模版名字"foo"，从这里看出来模板的名字存储的值为"foo"，并不是"b/foo"，并且只能存储最后一个名字为"foo"的文件。

所以我们修改下前面的代码

```go
var TemplatesFiles []string{
	"template/index.html",
	"template/login.html",
	"template/logout.html",
	"template/auth/profile.html" // 多加的文件
}

t, err := template.ParseFiles(TemplatesFiles...)

var name = "profile.html"

t.ExecuteTemplate(w, name, nil)
```

将`auth/profile.html`改为`profile.html`即可

也就是说存储的是一个文件名，不是一个文件的路径名，就算文件包括了文件路径名，也不会以包含路径的方式来命名模板的名字。

所以这里使用的时候会有一些限制，而且注意模板的命名使用规则

文件名尽量不要重名，重名的话再使用ParseFiles解析的时候，也不要传入文件名相同的文件，否则会默认忽略前面的文件。
