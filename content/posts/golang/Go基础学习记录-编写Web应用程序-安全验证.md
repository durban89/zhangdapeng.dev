---
title: "Go基础学习记录 - 编写Web应用程序 - 安全验证"
date: "2025-08-01 09:21:48"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-an-quan-yan-zheng"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-安全验证/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-安全验证.html"
  - "/Go基础学习记录-编写Web应用程序-安全验证/"
  - "/Go基础学习记录-编写Web应用程序-安全验证.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-an-quan-yan-zheng/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-an-quan-yan-zheng.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-an-quan-yan-zheng.html"
---
## **安全验证**

前面加了很多功能，但是程序存在严重的安全漏洞，用户可以访问在服务器上读/写的任意路径。  
为了缓解这种情况，我们可以编写一个函数来使用正则表达式验证标题。  
首先，将"regexp"添加到导入列表中。  
然后我们可以创建一个全局变量来存储我们的验证表达式：

```go
var validPath = regexp.MustCompile("^/(edit|save|view)/([a-zA-Z0-9]+)$")
```

函数regexp.MustCompile将解析并编译正则表达式，并返回一个regexp.Regexp。  
MustCompile与Compile的区别在于，如果表达式编译失败，它将会出现异常，而Compile会将错误作为第二个参数返回。  
现在，让我们编写一个函数，该函数使用validPath表达式来验证路径并提取页面标题

```go
func getTitle(w http.ResponseWriter, r *http.Request) (string, error) {
    m := validPath.FindStringSubmatch(r.URL.Path)
    if m == nil {
        http.NotFound(w, r)
        return "", errors.New("无效的页面标题")
    }

    return m[2], nil // 标题是第二个子表达式中
}
```

如果标题有效，它将与nil错误值一起返回。  
如果标题无效，该函数将向HTTP连接写入“404 Not Found”错误，并向处理程序返回错误。  
要创建新错误，我们必须导入错误包。  
下面在每个处理程序中调用getTitle：

```go
func viewHandler(w http.ResponseWriter, r *http.Request) {
    title, err := getTitle(w, r)
    if err != nil {
        return
    }

    p, err := loadPage(title)
    if err != nil {
        http.Redirect(w, r, "/edit/"+title, http.StatusFound)
        return
    }

    renderTemplate(w, "view", p)
}

func editHandler(w http.ResponseWriter, r *http.Request) {
    title, err := getTitle(w, r)
    if err != nil {
        return
    }

    p, err := loadPage(title)
    if err != nil {
        p = &Page{Title: title}
    }

    renderTemplate(w, "edit", p)
}

func saveHandler(w http.ResponseWriter, r *http.Request) {
    title, err := getTitle(w, r)
    if err != nil {
        return
    }

    body := r.FormValue("body")
    p := &Page{
        Title: title,
        Body:  []byte(body),
    }

    err = p.save()

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
    }

    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

修改完之后，重新编译并运行程序，当访问非edit、view、save路由时，会出现异常错误提示
