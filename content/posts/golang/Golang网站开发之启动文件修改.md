---
title: "Golang网站开发之启动文件修改"
date: "2025-08-04 18:07:37"
slug: "golang-wang-zhan-kai-fa-zhi-qi-dong-wen-jian-xiu-gai"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之启动文件修改/"
  - "/2025/08/04/Golang网站开发之启动文件修改.html"
  - "/Golang网站开发之启动文件修改/"
  - "/Golang网站开发之启动文件修改.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-qi-dong-wen-jian-xiu-gai/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-qi-dong-wen-jian-xiu-gai.html"
  - "/golang-wang-zhan-kai-fa-zhi-qi-dong-wen-jian-xiu-gai.html"
---
这几天重新温习了一下Golang，再次进行我的小博客“wiki”进行开发，发现网上似乎多了很多针对web的使用方式的介绍，尤其是http这个库，于是之前一直想解决的问题也有了着落

先看下之前的main.go启动的代码，如下

```go
func main() {
	router.Routes()

	err := http.ListenAndServe(":8090", nil)

	if err != nil {
		log.Println("Server Start Failed")
	} else {
		log.Println("Listening on 0.0.0.0:8090")
	}
}
```

现在的代码如下

```go
func main() {
	// 路由
	router.Routes()

	var addr = flag.String("addr", ":8090", "The addr of the application")

	log.Println("Starting web server on", *addr)

	if err := http.ListenAndServe(*addr, nil); err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}
```

这里说下我这段代码是要做什么？

正常来说，启动一个server的话，启动成功了，我们输入下信息，代表我们的server是正常启动的，但是前面第一段代码，并没有达到我的理想要求，什么都没有输出

后面一段代码提前输出了，并且在失败的时候会输出另外一段日志信息，这个虽说取巧了，但是也算是合理。这个问题我查了另外几片文章

> https://juejin.im/post/5d390b1ae51d455071250bf7#heading-9
>
> https://echorand.me/posts/golang-dissecting-listen-and-serve/
>
> https://github.com/gin-gonic/gin/blob/master/gin.go

建议从上到下的看下，其实ListenAndServe是可以传第二个参数的，不过要实现对应的DefaultServeMuX的功能，比如ServeHttp这个功能，这个有简单的做法也有复杂的做法，后面我如果需要了，实现后再记录，不过可以看下第三个链接，里面有它实现的逻辑，可以参考下，感觉很完善。
