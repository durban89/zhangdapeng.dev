---
title: "Go基础学习记录 - 编写Web应用程序 - Web开发表单处理"
date: "2025-08-01 09:22:05"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-biao-dan-chu-li"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发表单处理/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发表单处理.html"
  - "/Go基础学习记录-编写Web应用程序-Web开发表单处理/"
  - "/Go基础学习记录-编写Web应用程序-Web开发表单处理.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-biao-dan-chu-li/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-biao-dan-chu-li.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-biao-dan-chu-li.html"
---
前面的文章分享的部分功能都能正常使用，本次分享分析下里面的细节部分 -- 表单处理

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.0
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.0
```

这些我觉得 够清晰了。OK！继续我们的表单处理逻辑。这里我一个templates/edit.html为例

```html
<form action="/save/{{.Title}}" method="POST">
  <div class="form-group">
    <textarea class="form-control" name="body" rows="20" cols="80">{{printf "%s" .Body}}</textarea>
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

此表单将提交到服务器上的`/save/{{.Title}}`。  
用户单击Submit按钮后，数据将被发送到服务器路由器注册的save处理程序。  
然后我们需要知道它是使用POST方法还是GET。这里很明显是POST  
使用http包很容易找到。  
让我们看看save页面上的表单数据处理  
打开文件controllers/article.go 找到ArticleSave方法。这个方法是处理save请求的，找到

```go
body := r.FormValue("body")
```

这里只接收了一个body参数，如果有其他参数的话，获取方式是一样的，这里为了测试我们修改下form表单的代码添加一个作者信息，如下

```html
<form action="/save/{{.Title}}" method="POST">
  <div class="form-group">
    <label for="author">作者</label>
    <input class="form-control" name="author" id="author" value=""/>
  </div>
  <div class="form-group">
    <label for="body">文章内容</label>
    <textarea class="form-control" name="body" id="body" rows="20" cols="80">{{printf "%s" .Body}}</textarea>
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

还要修改下ArticleSave函数，如下

```go
func ArticleSave(w http.ResponseWriter, r *http.Request, title string) {
    body := r.FormValue("body")
    author := r.FormValue("author")
    method := r.Method

    fmt.Println("author ", author)
    fmt.Println("method: ", method)

    p := &helpers.Page{
        Title: title,
        Body:  []byte(body),
    }

    err := p.Save()

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

主要是加了如下部分内容

```go
author := r.FormValue("author")
method := r.Method

fmt.Println("author ", author)
fmt.Println("method: ", method)
```

这里多加了一个method的输出，为了后续逻辑做铺垫。比如如果是get请求的话，我们就不做处理，或者返回一个错误信息

重新编译项目并启动，请求save/后在终端会看到如下输出

```javascript
author  作者名称
method:  POST
```

这里的例子我使用的是FormValue，还有另外一个组合也可以使用，如下

```go
r.ParseForm()
r.Form["author"]
```

这种方式获取到的值是一个数组，打印出来的话类似如下

```bash
[作者名称]
```

当使用r.FormValue的时候会自动执行r.ParseForm()，并且r.FormValue的获取的只是其中一个值，如果我们提交过来的数据是一个数组的话，只用r.FormValue的话会有问题request.Form的类型是url.Value。  
它使用格式key = value保存数据，如下演示

```go
v := url.Values{}
v.Set("name", "Ava")
v.Add("friend", "Jess")
v.Add("friend", "Sarah")
v.Add("friend", "Zoe")

fmt.Println(v.Encode()) // == "name=Ava&friend=Jess&friend=Sarah&friend=Zoe"
fmt.Println(v.Get("name"))
fmt.Println(v.Get("friend"))
fmt.Println(v["friend"])
```

好了，关于表单的分享暂时就这些

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.1
```
