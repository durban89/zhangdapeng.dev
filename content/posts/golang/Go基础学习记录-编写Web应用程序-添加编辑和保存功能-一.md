---
title: "Go基础学习记录 - 编写Web应用程序 - 添加编辑和保存功能（一）"
date: "2025-08-01 09:21:33"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong-neng-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（一）/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（一）.html"
  - "/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（一）/"
  - "/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（一）.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能-一/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong-neng-y.html"
---
### **添加编辑和保存功能**

如果我们做的web应该如上篇文章那样只是本地存储，会有很多bug等我们去修复，并且还不保证能顺畅的使用。  
现在创建两个新的处理程序：一个名为editHandler，用于显示"编辑页面"表单，另一个名为saveHandler，用于保存通过表单输入的数据。  
首先我们先来实现editHandler的处理逻辑，先在main中加入对应的逻辑，如下

```go
func main() {
    http.HandleFunc("/view/", viewHandler)
    http.HandleFunc("/edit/", editHandler)
    log.Fatal(http.ListenAndServe(":8090", nil))
}
```

函数editHandler加载页面（或者，如果它不存在，则创建一个空的Page结构），并显示一个HTML表单。如下

```go
func editHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/edit/"):]
    p, err := loadPage(title)
    if err != nil {
        p = &Page{Title: title}
    }
    fmt.Fprintf(w, "<h1>Editing %s</h1>"+
        "<form action=\"/save/%s\" method=\"POST\">"+
        "<textarea name=\"body\">%s</textarea><br>"+
        "<input type=\"submit\" value=\"Save\">"+
        "</form>", p.Title, p.Title, p.Body)
}
```

这个函数可以正常工作，但所有硬编码的HTML都很难看。当然，还有更好的方法。如下

### **html/template包**

html/template包是Go标准库的一部分。  
我们可以使用html/template将HTML保存在一个单独的文件中，这样我们就可以在不修改底层Go代码的情况下更改编辑页面的布局。  
首先，我们必须将html/template添加到导入列表中。我们也不会再使用fmt了，所以我们必须删除它。大快人心。

```go
import (
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "html/template" // 注意这里
)
```

让我们创建一个包含HTML表单的模板文件。打开一个名为edit.html的新文件，并添加以下行：

```html
<html>
  <head>
    <title>Editing {{.Title}}</title>
  </head>

  <body>
    <h1>Editing {{.Title}}</h1>
  </body>

  <form action="/save/{{.Title}}" method="POST">
    <div>
      <textarea name="body" rows="20" cols="80">{{printf "%s" .Body}}</textarea>
    </div>
    <div>
      <input type="submit" value="Save">
    </div>
  </form>
</html>
```

修改editHandler以使用模板，而不是硬编码的HTML：

```go
func editHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/edit/"):]
    p, err := loadPage(title)
    if err != nil {
        p = &Page{Title: title}
    }

    t, _ := template.ParseFiles("template/edit.html")

    t.Execute(w, p)
}
```

函数template.ParseFiles将读取edit.html的内容并返回\* template.Template。  
方法t.Execute执行模板，将生成的HTML写入http.ResponseWriter。  
.Title和.Body点标识符指的是p.Title和p.Body。  
模板指令用双花括号括起来。  
printf "％s" .Body指令是一个函数调用，它输出.Body作为字符串而不是字节流，与调用fmt.Printf相同。  
html/template包有助于保证模板操作只生成安全且正确的HTML。  
例如，它会自动转义任何大于符号（>），将其替换为＆gt;，以确保用户数据不会损坏表单HTML。  
由于我们现在正在处理模板，让我们为viewHandler创建一个名为view.html的模板，内容如下：

```html
<html>
  <head>
    <title>View {{.Title}}</title>
  </head>

  <body>
    <h1>{{.Title}}</h1>

    <p>[
      <a href="/edit/{{.Title}}">edit</a>]</p>

    <div>{{printf "%s" .Body}}</div>
  </body>
</html>
```

相应地修改viewHandler：

```go
func viewHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/view/"):]
    p, _ := loadPage(title)    t, _ := template.ParseFiles("template/view.html")
    t.Execute(w, p)
}
```

请注意，我们在两个处理程序中使用了几乎完全相同的模板代码。  
让我们通过将模板代码移动到它自己的函数来删除这个重复，创建如下函数

```go
func renderTemplate(w http.ResponseWriter, templateName string, p *Page) {
    t, _ := template.ParseFiles("template/" + templateName + ".html")

    t.Execute(w, p)
}
```

并修改处理程序以使用该函数,如下：

```go
func viewHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/view/"):]
    p, _ := loadPage(title)
    renderTemplate(w, "view", p)
}
```

```go
func editHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/edit/"):]
    p, err := loadPage(title)
    if err != nil {
        p = &Page{Title: title}
    }

    renderTemplate(w, "edit", p)
}
```

可以再次构建和测试我们的程序。
