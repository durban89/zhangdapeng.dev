---
title: "Go基础学习记录 - 编写Web应用程序 - 重新调整项目目录结构（二）"
date: "2025-08-01 09:22:02"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu-lu-jie-gou-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（二）/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（二）.html"
  - "/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（二）/"
  - "/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（二）.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构-二/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-m.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu-lu-jie.html"
---
上篇文章整理了一部分的文件结构，本次再将剩余的一部分也处理下，其实很小的一部分，

将main中makeHandler函数处理掉，封装到我们看起来还算比较方便的归类中，创建文件

helpers/handler.go

```go
package helpers

import (
	"net/http"
	"regexp"
)

var validPath = regexp.MustCompile("^/(edit|save|view)/([a-zA-Z0-9]+)$")

// MakeHandler 处理路由函数
func MakeHandler(fn func(http.ResponseWriter, *http.Request, string)) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		// 这里我们将从Request中提取页面标题，并调用提供的处理程序'fn'
		m := validPath.FindStringSubmatch(r.URL.Path)
		if m == nil {
			http.NotFound(w, r)
			return
		}
		fn(w, r, m[2])
	}
}
```

这里说下我对go看法，其实go的机制并没有很完善，包管理其实一直是个大问题，按照我们正常的编写逻辑来说，应该不能像java之类的，先要编译完再运行，发现问题其实也需要一步一步去找，很头痛，这也是是为什么最近ReactNative一直很火的原因，热编译热启动热更新，都是为了我们的开发效率。然鹅go也是，虽然性能很好，但是包跟包之间的依赖似乎并不是很友好，我这里暂时按照自己的理解来，后面发现更可用的再进行更新。

下面修改main.go，引入我们需要的helper，main.go修改后的代码如下

```go
package main

import (
	"log"
	"net/http"

	"github.com/durban89/wiki/controllers"
	"github.com/durban89/wiki/helpers"
)

func main() {
	http.HandleFunc("/view/", helpers.MakeHandler(controllers.ArticleView))
	http.HandleFunc("/save/", helpers.MakeHandler(controllers.ArticleSave))
	http.HandleFunc("/edit/", helpers.MakeHandler(controllers.ArticleEdit))
	log.Fatal(http.ListenAndServe(":8090", nil))
}
```

是不是感觉清爽了很多。

下面再次进行编译并运行项目，项目正常启动运行正常。
