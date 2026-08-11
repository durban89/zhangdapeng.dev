---
title: "Go基础学习记录之模板输出数组"
date: "2025-08-01 10:32:20"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-shu-chu-shu-zu"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之模板输出数组/"
  - "/2025/08/01/Go基础学习记录之模板输出数组.html"
  - "/Go基础学习记录之模板输出数组/"
  - "/Go基础学习记录之模板输出数组.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-shu-chu-shu-zu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-shu-chu-shu-zu.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-shu-chu-shu-zu.html"
---
以前使用PHP的Twig模板，后面又有使用过Flask的Jinja2模板，还可以比较容易入手，至少会有个for，一看就知道什么，也知道如何调用

到了Golang这边比较迷糊了，不过还好，官方也有说明，自己也搜索了下，这里记录下，很简单比如我们有个视图，代码大概如下

```go
{{range .Data}}
<div class="blog-post">
<h2 class="blog-post-title">{{ .autokid }} - {{ .title }} blog post</h2>
<p class="blog-post-meta">January 1, 2014 by <a href="#">Mark</a></p>
</div>
{{end}}
```

从上面的代码分析下，需要传一个带有Data的数据，那传递过来的参数里面至少要有个Data，如下

```go
err = t.Execute(w, struct {
    Data []models.SelectResult
}{
    Data: qr,
})
```

注意这里的Data，实际上根据项目的需求来，可以换成自己需要的，我这里的是以之前的文章【Go基础学习记录之Web开发的博客文章列表展示功能】为例，只是单独拿出来方便知识点聚焦

其实多用用还是很简单的。
