---
title: "Golang网站开发之模版的template和block的使用"
date: "2025-08-04 18:08:15"
slug: "golang-wang-zhan-kai-fa-zhi-mo-ban-de-template-he-block-de-shi-yong"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之模版的template和block的使用/"
  - "/2025/08/04/Golang网站开发之模版的template和block的使用.html"
  - "/Golang网站开发之模版的template和block的使用/"
  - "/Golang网站开发之模版的template和block的使用.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-mo-ban-de-template-he-block-de-shi-yong/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-mo-ban-de-template-he-block-de-shi-yong.html"
  - "/golang-wang-zhan-kai-fa-zhi-mo-ban-de-template-he-block-de-shi-yong.html"
---
从Go 1.6版本开始，有一个新的语法叫做*block*，这个语法的使用类似于*template*语法的使用，但是不同的是*block*会有一个默认值，而*template*没有默认值

下面来演示下，具体说的是什么意思

下面有两个页面：分别是首页和关于我页面 我将用这两个页面解释下*template*是如何工作的，并且如何使用新语法*block*来改变*template*语法

> content模板

每个页面都会使用这个模版

> 首页模版(home.tmpl)

```html
{{define "title"}}Home{{end}}
{{define "content"}}This is the Home page.{{end}}
```

> 关于我页面模板(about.tmpl)

```html
{{define "title"}}About{{end}}
{{define "content"}}This is the About page.{{end}}
```

> Base模板 一个基础模板(base.tmpl):

```html
<title>{{template "title" .}}</title>
<body>{{template "content" .}}</body>
```

> 渲染模版

在这个例子中，Base模板(base.tmpl)作为ParseFiles()第一个参数，content模板作为第二个参数。如果你转换了顺序的话，将不会展示任何东西，所以顺序很重要。

渲染首页的代码

```go
t, err := template.ParseFiles("base.tmpl", "home.tmpl")
if err != nil {
	log.Fatal(err)
}

if err := t.Execute(os.Stdout, nil); err != nil {
	log.Fatal(err)
}
```

首页渲染的结果

```html
<title>Home</title>
<body>This is the home page</body>
```

关于我页面渲染的代码

```go
t, err := template.ParseFiles("base.tmpl", "about.tmpl")
if err != nil {
	log.Fatal(err)
}

if err := t.Execute(os.Stdout, nil); err != nil {
	log.Fatal(err)
}
```

关于我渲染页面的结果

```html
<title>About</title>
<body>This is the about page.</body>
```

> Template语法的限制

假设你的网站有500个content模板。为了在base.tmpl中添加一个footer部分的话，你必须修改所有这些500个content模板并且要添加对应的定义，否则你将得到一个类似下面的错误

```bash
no such template "footer"
```

> 新语法

现在我们来将*template*语法修改为*block*语法。不需要修改任何content模板的代码，只需要修改Base模板(base.tmpl)，想下面这样：

```html
<title>{{block "title" .}}Default Title{{end}}</title>
<body>{{block "content" .}}This is the default body.{{end}}</body>
```

如果你的content模板没有任何匹配的定义，将会显示默认的内容。现在在build没有定义content的模板将不会再报错。

文章参考：http://www.josephspurrier.com/how-to-use-template-blocks-in-go-1-6/
