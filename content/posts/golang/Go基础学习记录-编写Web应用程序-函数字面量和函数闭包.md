---
title: "Go基础学习记录 - 编写Web应用程序 - 函数字面量和函数闭包"
date: "2025-08-01 09:21:52"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-han-shu-zi-mian-liang-he-han-shu-bi-bao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-函数字面量和函数闭包/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-函数字面量和函数闭包.html"
  - "/Go基础学习记录-编写Web应用程序-函数字面量和函数闭包/"
  - "/Go基础学习记录-编写Web应用程序-函数字面量和函数闭包.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-han-shu-zi-mian-liang-he-han-shu/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-han-shu-zi-mian-liang-he-han.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-han-shu-zi-mian-liang-he-han-shu-bi-bao.html"
---
### **函数字面量和函数闭包**

在每个处理程序中捕获错误条件会引入大量重复的代码。  
如果我们可以将每个处理程序包装在执行此验证和错误检查的函数中，该怎么办？  
Go的函数文字提供了一种强大的抽象功能，可以帮助我们。  
首先，我们重新编写每个处理程序的函数定义以接受标题字符串：

```go
func viewHandler(w http.ResponseWriter, r *http.Request, title string)
func editHandler(w http.ResponseWriter, r *http.Request, title string)
func saveHandler(w http.ResponseWriter, r *http.Request, title string)
```

现在让我们定义一个包含上述类型函数的包装函数，并返回一个http.HandlerFunc类型的函数（适合传递给函数http.HandleFunc）：

```go
func makeHandler(fn func(http.ResponseWriter, *http.Request, string)) http.HandleFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // 这里我们将从Request中提取页面标题，并调用提供的处理程序'fn'
    }
}
```

返回的函数称为闭包，因为它包含在其外部定义的值。 在这种情况下，变量fn（makeHandler的单个参数）由闭包函数包含。变量fn将是saveHandler，editHandler或viewHandler程序之一。

现在我们可以从getTitle获取代码并在此处使用它（稍作修改）：

```go
func makeHandler(fn func(http.ResponseWriter, *http.Request, string)) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // 这里将从Request中提取页面标题，并调用提供的处理程序'fn'
        m := validPath.FindStringSubmatch(r.URL.Path)
        if m == nil {
            http.NotFound(w, r)
            return
        }
        fn(w, r, m[2])
    }
}
```

makeHandler返回的闭包是一个带有http.ResponseWriter和http.Request（换句话说，http.HandlerFunc）的函数。  
闭包从请求路径中提取标题，并使用TitleValidator正则表达式对其进行验证。  
如果标题无效，则会使用http.NotFound函数将错误写入ResponseWriter。  
如果标题有效，则将使用ResponseWriter，Request和title作为参数调用封闭的处理函数fn。  
现在，在使用http包注册之前，我们可以使用makeHandler在main中包装处理函数：

```go
func main() {
    http.HandleFunc("/view/", makeHandler(viewHandler))
    http.HandleFunc("/save/", makeHandler(saveHandler))
    http.HandleFunc("/edit/", makeHandler(editHandler))
    log.Fatal(http.ListenAndServe(":8090", nil))
}
```

最后，从处理函数中删除对getTitle的调用，使它们更简单：

```go
func viewHandler(w http.ResponseWriter, r *http.Request, title string) {
    p, err := loadPage(title)
    if err != nil {
        http.Redirect(w, r, "/edit/"+title, http.StatusFound)
        return
    }

    renderTemplate(w, "view", p)
}

func editHandler(w http.ResponseWriter, r *http.Request, title string) {
    p, err := loadPage(title)
    if err != nil {
        p = &Page{Title: title}
    }

    renderTemplate(w, "edit", p)
}

func saveHandler(w http.ResponseWriter, r *http.Request, title string) {
    body := r.FormValue("body")
    p := &Page{
        Title: title,
        Body:  []byte(body),
    }

    err := p.save()

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

修改完之后重新打包，看下我们的处理逻辑是否能正常运行

```bash
$ go install
$ wiki
```

运行正常。  
我当前的运行目录如下，稍后下面将分享下实践的的代码

```bash
.
├── LICENSE
├── README.md
├── data
│   ├── test.txt
│   ├── test1.txt
│   └── testdd.txt
├── main.go
└── template
    ├── edit.html
    └── view.html
```

本实例结束实践项目地址

```bash
https://github.com/durban89/wiki_blog.git
```

国内用户如果打不开的话可以到这里

```bash
https://gitee.com/durban/wiki_blog.git
```
