---
title: "Go基础学习记录 - 编写Web应用程序 - 路由和程序启动的一些思考"
date: "2025-08-01 10:31:57"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-lu-you-he-cheng-xu-qi-dong-de-yi-xie-si-kao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-路由和程序启动的一些思考/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-路由和程序启动的一些思考.html"
  - "/Go基础学习记录-编写Web应用程序-路由和程序启动的一些思考/"
  - "/Go基础学习记录-编写Web应用程序-路由和程序启动的一些思考.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-lu-you-he-cheng-xu-qi-dong-de-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-lu-you-he-cheng-xu-qi-dong-d.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-lu-you-he-cheng-xu-qi-dong-de-yi-xie-si.html"
---
近段时间重新对我的Web应用程序进行了一些思考，首先程序启动的main.go文件中，暂时的路由添加没有太大的问题，但是根据以往的项目开发经验，如果这个系统对外分享的话，之后在做大项目的时候，会遇到添加很多路由的情况，然后就会发现文件变的越来越大，关键是路由还放在了main.go文件中，这个实在是太麻烦了，于是今天做了下少许的改动。

每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.12
```

1、改动main.go文件

将原来的

```go
http.HandleFunc("/view/", helpers.MakeHandler(controllers.ArticleView))
http.HandleFunc("/save/", helpers.MakeHandler(controllers.ArticleSave))
http.HandleFunc("/edit/", helpers.MakeHandler(controllers.ArticleEdit))
http.HandleFunc("/upload/", controllers.UploadHandler)
http.HandleFunc("/postFile/", controllers.PostFileHandler)
```

用下面的代码替换掉

```go
router.Routes()
```

这样我们将路由这一块的逻辑分到一个负责路由的文件来做处理，这样main.go文件就看起来很简洁。

2、添加router.go

创建文件`router/router.go,添加代码如下`

```go
package router

import (
	"net/http"

	"github.com/durban89/wiki/controllers"
)

// RouterMap 路由
type RouterMap struct {
	Path string
	Fn   func(http.ResponseWriter, *http.Request)
}

// RouterMaps 路由列表
var RouterMaps = []*RouterMap{
	{
		Path: "/view/",
		Fn:   controllers.ArticleViewWithID,
	},
	{
		Path: "/save/",
		Fn:   controllers.ArticleViewWithID,
	},
	{
		Path: "/edit/",
		Fn:   controllers.ArticleViewWithID,
	},
	{
		Path: "/upload/",
		Fn:   controllers.UploadHandler,
	},
	{
		Path: "/postFile/",
		Fn:   controllers.PostFileHandler,
	},
}

// Routes 操作
func Routes() {
	for i := 0; i < len(RouterMaps); i++ {
		cRoute := RouterMaps[i]
		http.HandleFunc(cRoute.Path, cRoute.Fn)
	}
}
```

从上面的代码可以看出来，路由的管理稍微好一些了，这也就达到了我们优化main.go文件的目的。

3、测试

在`controllers/article.go`文件中添加如下函数

```go
func ArticleViewWithID(w http.ResponseWriter, r *http.Request) {
	if strings.ToLower(r.Method) == "get" {
		var validPath = regexp.MustCompile("^/(view)/([a-zA-Z0-9]+)$")
		m := validPath.FindStringSubmatch(r.URL.Path)
		if m == nil {
			http.NotFound(w, r)
			return
		}

		// 获取文章标题或者文章ID
		fmt.Println(m[2:])

		fmt.Fprintf(w, "Welcome to the home page!")
		return
	}

	http.NotFound(w, r)
	return

}
```

添加完之后，重新编译项目并运行，一切正常。

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.0
```
