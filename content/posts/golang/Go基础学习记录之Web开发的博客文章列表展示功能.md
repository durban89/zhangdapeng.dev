---
title: "Go基础学习记录之Web开发的博客文章列表展示功能"
date: "2025-08-01 10:32:17"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-wen-zhang-lie-biao-zhan-shi-gong-neng"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Web开发的博客文章列表展示功能/"
  - "/2025/08/01/Go基础学习记录之Web开发的博客文章列表展示功能.html"
  - "/Go基础学习记录之Web开发的博客文章列表展示功能/"
  - "/Go基础学习记录之Web开发的博客文章列表展示功能.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-wen-zhang-lie-biao-zhan-shi-gong-neng/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-wen-zhang-lie-biao-zhan-shi-gong-nen.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-web-kai-fa-de-bo-ke-wen-zhang-lie-biao-zhan-shi-gong-neng.html"
---
每次我都会将自己实践的代码放到github上并且都会打一个tag，方便后面用的同学使用，这里我以下面分支的代码进行实践分享

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.5
```

本次分享继续之前的Model层，之前的Model层重构，零零散散的总算是完成了，今天继续添加一下文章列表展示功能，虽然说是一个简单的列表展示，但是也还是耗费了很长的时间

过程很简单，先简单说下，后面说下具体的难点

## 第一步、添加控制层

添加一个控制器函数ArticleItem，用来展示调用文章的列表数据并给到前端进行展示。代码如下

```go
// ArticleItem 列表
func ArticleItem(w http.ResponseWriter, r *http.Request) {
	var blogModel models.BlogModel

	var autokid int64
	var title string
	selectField := models.SelectValues{
		"autokid": &autokid,
		"title":   &title,
	}

	where := models.WhereValues{}

	qr, err := blogModel.Query(selectField, where, 0, 10)

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
		Data []models.SelectResult
	}{
		Data: qr,
	})

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}
```

## 第二步、View层修改

这里我们需要添加一个视图文件` templates/item.html` ，里面的代码如下

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>列表</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link
      rel="stylesheet"
      href="https://fezvrasta.github.io/bootstrap-material-design/docs/4.0/examples/blog/blog.css"
      crossorigin="anonymous" />
  </head>

  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-9">

          <h3 class="pb-3 mb-4 font-italic border-bottom">
            From the Firehose
          </h3>

          {{range .Data}}
          <div class="blog-post">
            <h2 class="blog-post-title">{{ .autokid }} - {{ .title }} blog post</h2>
            <p class="blog-post-meta">January 1, 2014 by <a href="#">Mark</a></p>
          </div>
          {{end}}

          <nav class="blog-pagination">
            <a class="btn btn-outline-primary" href="#">Older</a>
            <a class="btn btn-outline-secondary disabled" href="#">Newer</a>
          </nav>
        </div>
        <div class="col-md-3">
          RightSidebar
        </div>
      </div>
    </div>

    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

  </body>
</html>
```

## 第三步、路由添加

修改 `routes/routes.go` 文件如下路由

```go
{
    Path: "/item/",
    Fn:   controllers.ArticleItem,
},
```

添加后重新编译并访问/item就会看到如下类似的输出

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1536507943/xiaorongmao/golang_web_22_1.png "" %}


以上就是具体逻辑的输出，不过这里主要说下难点

> 如何在模板中对数组类型的数据进行输出，如下方式操作

```go
{{range .Data}}
<div class="blog-post">
<h2 class="blog-post-title">{{ .autokid }} - {{ .title }} blog post</h2>
<p class="blog-post-meta">January 1, 2014 by <a href="#">Mark</a></p>
</div>
{{end}}
```

这个是刚才的视图文件中可以找到

并且我们在控制层也要有对应的参数传递，如下

```go
err = t.Execute(w, struct {
    Data []models.SelectResult
}{
    Data: qr,
})
```

> Model层查询功能工作失败，由于反射机制使用错误，现已更改如下，前面的文章也会相应做修改

```go
for k, v := range s {
	var ref = reflect.ValueOf(v)
	var refv = ref.Elem()

	if refv.Kind() == reflect.Int64 {
		tmpResult[k] = refv.Int()
	} else if refv.Kind() == reflect.String {
		tmpResult[k] = refv.String()
	}

	i++
}
```

这里主要是进行判断然后将值进行对应类型的转换，不然跟之前的调用方式，其实赋值的只是一个指针的地址，当循环到最后一个的时候，全部的值都会编程一个值，这个时候就会看到获取到的列表每组数值都是一样的。

今天分享就到这里，如果对反射机制不是很理解的话，可以去搜下，以前没觉得golang有多火，其实只要搜索下某个相关知识点那就回发现，很多文章在介绍次相关的知识。

---

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.1.6
```
