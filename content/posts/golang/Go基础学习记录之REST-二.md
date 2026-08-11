---
title: "Go基础学习记录之REST(二)"
date: "2025-08-04 11:38:25"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-rest-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之REST(二)/"
  - "/2025/08/04/Go基础学习记录之REST(二).html"
  - "/Go基础学习记录之REST(二)/"
  - "/Go基础学习记录之REST(二).html"
  - "/2025/08/04/Go基础学习记录之REST-二/"
  - "/2025/08/04/Go基础学习记录之REST-二.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-rest-er/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-rest-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-rest-er.html"
---
## RESTful实现

Go没有直接支持REST，但由于RESTful Web应用程序都是基于HTTP的，我们可以使用net/http包来自己实现它。  
当然，在我们能够完全实现REST之前，我们首先需要做一些修改。

REST使用不同的方法来处理资源，具体取决于该资源所需的交互。  
许多现有应用程序声称是RESTful但它们实际上并不实现REST。  
我将这些应用程序分为几个级别，取决于它们实现的HTTP方法。

{% img https://cdn.xiaorongmao.com/up/golang_web_46_1.png "" %}

上图显示了当前在REST中实现的三个级别。  
在开发自己的应用程序时，您可能不会选择遵循REST的所有规则和约束，因为有时它的规则不适合所有情况。  
RESTful Web应用程序使用每个HTTP方法，包括DELETE和PUT，但在许多情况下，HTTP客户端只能发送GET和POST请求。

1. HTML标准允许客户端通过链接和表单发送GET和POST请求。没有AJAX支持，不可能发送PUT或DELETE请求。  
2. 一些防火墙拦截PUT和DELETE请求，客户端必须使用POST才能实现它们。完全RESTful服务负责查找原始HTTP方法并恢复它们。

我们可以通过在POST请求中添加隐藏的\_method字段来模拟PUT和DELETE请求，但是这些请求必须在处理之前在服务器端进行转换。  
在Go中轻松实现标准RESTful接口，如以下示例所示：

```go
package main

import (
  "fmt"
  "log"
  "net/http"

  "github.com/julienschmidt/httprouter"
)

func Index(w http.ResponseWriter, r *http.Request, _ httprouter.Params) {
  fmt.Fprint(w, "Welcome!\n")
}

func Hello(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
  fmt.Fprintf(w, "hello, %s!\n", ps.ByName("name"))
}

func getuser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
  uid := ps.ByName("uid")
  fmt.Fprintf(w, "you are get user %s", uid)
}

func modifyuser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
  uid := ps.ByName("uid")
  fmt.Fprintf(w, "you are modify user %s", uid)
}

func deleteuser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
  uid := ps.ByName("uid")
  fmt.Fprintf(w, "you are delete user %s", uid)
}

func adduser(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
  // uid := r.FormValue("uid")
  uid := ps.ByName("uid")
  fmt.Fprintf(w, "you are add user %s", uid)
}

func main() {
  router := httprouter.New()
  router.GET("/", Index)
  router.GET("/hello/:name", Hello)

  router.GET("/user/:uid", getuser)
  router.POST("/adduser/:uid", adduser)
  router.DELETE("/deluser/:uid", deleteuser)
  router.PUT("/moduser/:uid", modifyuser)

  log.Fatal(http.ListenAndServe(":8080", router))
}
```

此示例代码向您展示如何编写非常基本的REST应用程序。我们的资源是用户，我们对不同的方法使用不同的功能。在这里，我们导入了一个名为github.com/julienschmidt/httprouter的第三方软件包。我们已经介绍了如何在前面的章节中实现自定义路由器--julienschmidt/httprouter包实现了一些非常方便的路由器映射规则，这使得它非常便于实现RESTful架构。如您所见，REST要求您为同一资源的不同HTTP方法实现不同的逻辑。

### 总结

REST是一种Web架构风格，它基于过去WWW的成功经验：无状态，以资源为中心，充分利用HTTP和URI协议以及提供统一的接口。  
这些出色的设计考虑因素使REST成为最受欢迎的Web服务标准。  
从某种意义上说，通过强调URI并利用早期的Internet标准（如HTTP），REST为大型可扩展的Web应用程序铺平了道路。  
目前，Go对REST的支持仍然非常基础。  
但是，通过为每种类型的HTTP请求实现自定义路由规则和不同的请求处理程序，我们可以在Go webapps中实现RESTful架构。
