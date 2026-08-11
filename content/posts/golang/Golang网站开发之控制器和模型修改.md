---
title: "Golang网站开发之控制器和模型修改"
date: "2025-08-04 11:39:24"
slug: "golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-he-mo-xing-xiu-gai"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之控制器和模型修改/"
  - "/2025/08/04/Golang网站开发之控制器和模型修改.html"
  - "/Golang网站开发之控制器和模型修改/"
  - "/Golang网站开发之控制器和模型修改.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-he-mo-xing-xiu-gai/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-he-mo-xing-xiu-gai.html"
  - "/golang-wang-zhan-kai-fa-zhi-kong-zhi-qi-he-mo-xing-xiu-gai.html"
---
看过我前面几篇文章有关于网站开发中控制器和模型层的相关逻辑的话，可能会觉得，代码有点复杂，不是太符合Golang语言的特点，同时也不具有方便的使用特性，最近有闲暇的时候，继续看了一些关于Golang的基础只是，对之前的逻辑进行了下改进，主要分以下几个部分

1、修改路由（router）

2、修改控制器（controller）

3、修改模型（model）

下面具体看下做了哪些修改

### 修改路由

本来之前是要加入一些路由的请求方法，后来也没有想到很好的方式，于是就想还是将这种判断方式加入控制器层去做比较好，但是后来找打了这个加路由请求方式的方法后，觉得还是在路由这一层做个判断比较好。

第一步就是定义接口，实现路由的具体判断逻辑，代码如下

```go
package router

import (
	"net/http"
	"strings"
)

// Method 接口
type Method interface {
	GET(path string, handler func(w http.ResponseWriter, r *http.Request))
	POST(path string, handler func(w http.ResponseWriter, r *http.Request))
	DELETE(path string, handler func(w http.ResponseWriter, r *http.Request))
	PUT(path string, handler func(w http.ResponseWriter, r *http.Request))
	ALL(path string, handler func(w http.ResponseWriter, r *http.Request))
}

// GET 操作
func GET(path string, handler func(w http.ResponseWriter, r *http.Request)) {
	http.HandleFunc(path, func(w http.ResponseWriter, r *http.Request) {
		if strings.ToLower(r.Method) == "get" {
			handler(w, r)
			return
		}

		http.NotFound(w, r)
		return
	})
}

// POST 操作
func POST(path string, handler func(w http.ResponseWriter, r *http.Request)) {
	http.HandleFunc(path, func(w http.ResponseWriter, r *http.Request) {
		if strings.ToLower(r.Method) == "post" {
			handler(w, r)
			return
		}

		http.NotFound(w, r)
		return
	})
}

// DELETE 操作
func DELETE(path string, handler func(w http.ResponseWriter, r *http.Request)) {
	http.HandleFunc(path, func(w http.ResponseWriter, r *http.Request) {
		if strings.ToLower(r.Method) == "delete" {
			handler(w, r)
			return
		}

		http.NotFound(w, r)
		return
	})
}

// PUT 操作
func PUT(path string, handler func(w http.ResponseWriter, r *http.Request)) {
	http.HandleFunc(path, func(w http.ResponseWriter, r *http.Request) {
		if strings.ToLower(r.Method) == "put" {
			handler(w, r)
			return
		}

		http.NotFound(w, r)
		return
	})
}

// ALL 操作
func ALL(path string, handler func(w http.ResponseWriter, r *http.Request)) {
	http.HandleFunc(path, func(w http.ResponseWriter, r *http.Request) {
		handler(w, r)
		return
	})
}
```

从上面的代码可以看出，是存在重复的代码的，应该是有优化的方式的，暂时我是没有想到

然后看下调用方式

```go
package router

import (
	"github.com/durban89/wiki/controllers/article"
)

// Routes 操作
func Routes() {
	// 文章
	GET("/articles/update/", article.Update)
	GET("/articles/view/", article.View)
	GET("/articles/", article.Item)
}
```

有木有感觉清爽了很多，同时也由于控制器层做了修改，这样的调用方式，就感觉一目了然，很清爽

### 修改控制器（controller）

以前认为跟其他语言可以类似的做到在controller下放一个文件就可以方便的调用控制器的方法，但是在Golang实际上不建议这样做的，Golang给我的理解是功能就要以一个单独的包存在，包与包之间是不能冲突的，但是实际上我们一个控制器会用到的方法，在另外一个控制器也可能用得到，所以以分包的方式反而会容易解决很多问题，比如下面的模型修改也是类似的。controllers目录下的文件结构如下

```bash
.
├── article
│   └── article.go
├── welcome
    └── welcome.go
```

这样的话我可以在article.go和welcome.go写同样的方法而不会相互冲突，同时最大的好处是我能为每个单独的控制器也单元测试，这个是最主要的。 分开有时让我们的代码看起来更加清晰 看下article.go的中的部分代码

```go
package article

import (
	"fmt"
	"html/template"
	"net/http"
	"time"

	"github.com/durban89/wiki/config"
	"github.com/durban89/wiki/helpers"
	"github.com/durban89/wiki/models"
	"github.com/durban89/wiki/models/article"
)

// Update 更新文章
func Update(w http.ResponseWriter, r *http.Request) {
	http.NotFound(w, r)
	return
}

// View 文章详情
func View(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")

	if id == "" {
		http.NotFound(w, r)
		return
	}

	// model 数据检索查询
	var articleModel article.Article

	var autokid int64
	var title string
	selectField := models.SelectValues{
		"autokid": &autokid,
		"title":   &title,
	}

	where := models.WhereValues{
		"autokid": models.WhereCondition{
			Operator: "=",
			Value:    id,
		},
	}

	err := articleModel.QueryOne(selectField, where)

	if err != nil {
		fmt.Println(err)
		http.NotFound(w, r)
		return
	}

	// 视图渲染
	t, err := template.ParseFiles(config.TemplateDir + "/view.html")

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	err = t.Execute(w, struct {
		Autokid int64
		Title   string
		Body    string
		Script  string
		Html    string
	}{
		Autokid: autokid,
		Title:   title,
		Body:    "dddd",
		Script:  "",
		Html:    "",
	})

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	return
}

// Item 列表
func Item(w http.ResponseWriter, r *http.Request) {
	var siteName string
	cookie, err := r.Cookie("site_name_cookie")

	if err != nil {
		expired := time.Now().Add(365 * 24 * time.Hour)
		cookie := http.Cookie{
			Name:    "site_name_cookie",
			Value:   "gowhich_cookie",
			Expires: expired,
		}

		http.SetCookie(w, &cookie)
	} else {
		siteName = cookie.Value
	}

	var articleModel article.Article

	var autokid int64
	var title string
	selectField := models.SelectValues{
		"autokid": &autokid,
		"title":   &title,
	}

	where := models.WhereValues{}

	qr, err := articleModel.Query(selectField, where, 0, 10)

	if err != nil {
		fmt.Println(err)
		http.NotFound(w, r)
		return
	}

	t, err := template.ParseFiles(config.TemplateDir + "/item.html")

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	err = t.Execute(w, struct {
		Data   []models.SelectResult
		Cookie string
	}{
		Data:   qr,
		Cookie: siteName,
	})

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}
```

### 修改模型（model）

根据上面的控制器修改的逻辑，模型的修改的逻辑也是类似的。models目录下的文件结构类似如下

```bash
.
├── article
│   └── article.go
```

看下 article.go中的内容

```go
package article

import (
	"github.com/durban89/wiki/models"
)

var tableName = "article"

// Article 模型
type Article struct {
	models.ModelProperty
}

// Property 属性
type Property struct {
	Autokid string
	Title   string
}
```

如果看过我之前的文章应该会多多少少了解了我在models中做的事情，其实这里的逻辑涉及到一个继承的概念

```go
// Article 模型
type Article struct {
	models.ModelProperty
}
```

主要是上面这段代码

最后想说的是，通过这样的修改布局，创建模型和控制器的话，代码就会很舒畅，有种似曾相识的感觉。

代码库如下，本篇文章中涉及到的都在这里的

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.2.1
```
