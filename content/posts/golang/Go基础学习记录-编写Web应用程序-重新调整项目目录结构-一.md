---
title: "Go基础学习记录 - 编写Web应用程序 - 重新调整项目目录结构（一）"
date: "2025-08-01 09:21:59"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu-lu-jie-gou-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（一）/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（一）.html"
  - "/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（一）/"
  - "/Go基础学习记录-编写Web应用程序-重新调整项目目录结构（一）.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构-一/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重新调整项目目录结构-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-m.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-xin-tiao-zheng-xiang-mu-mu-lu-jie.html"
---
### **重新调整项目目录结构**

前面的一些文章介绍，完全可以做一个简单的Web应用，但是如果用过PHP或者是Python等语言的框架开发Web应用的时候会发现，从结构目录上来说完全是一个成熟的架构了，但是对于Golang来说，似乎并没有什么成熟的架构，网上大多数现成的架构，也都是很随意，比如最流行的*Beego，大概看了下，功能很齐全，可以直接上手使用，但是对于像我习惯MVC方式的，*这不得不让我觉得，这样的写代码方式，似乎有些让我不习惯很习惯，下面让我来踩踩坑，做个适合自己开发的架构。

首先我们把前面文章中的视图做下整理，将view.html和edit.html，转移到templates文件夹，以后这个文件夹就是我们自己放模板的文件夹。同时我们将view.html和edit.html进行下UI，我这边使用了Bootstrap4.0版本，代码分别如下

templates/view.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{{.Title}}</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body>
    <div class="container">
      <div class="col-md-12">
        <div class="text-center">
          <h1> {{.Title}}</h1>
        </div>

        <p>[<a href="/edit/{{.Title}}">edit</a>]</p>
        <div>{{printf "%s" .Body}}</div>
      </div>
    </div>

    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

templates/edit.html

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Editing {{.Title}}</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>

  <body>
    <div class="container">
      <div class="col-md-12">
        <div class="text-center">
          <h1>Editing:【 {{.Title}}】</h1>
        </div>
        <form action="/save/{{.Title}}" method="POST">
          <div class="form-group">
            <textarea class="form-control" name="body" rows="20" cols="80">{{printf "%s" .Body}}</textarea>
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
```

同时修改templates

有原来的

```go
var templates = template.Must(template.ParseFiles("template/edit.html", "template/view.html"))
```

修改为

```go
var templates = template.Must(template.ParseFiles("templates/edit.html", "templates/view.html"))
```

重新编译并运行代码

```bash
$ go install
$ wiki
```

完美，一切正常。（正常不代表没问题），后面继续
