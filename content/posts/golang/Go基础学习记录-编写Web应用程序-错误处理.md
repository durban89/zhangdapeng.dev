---
title: "Go基础学习记录 - 编写Web应用程序 - 错误处理"
date: "2025-08-01 09:21:39"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-cuo-wu-chu-li"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-错误处理/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-错误处理.html"
  - "/Go基础学习记录-编写Web应用程序-错误处理/"
  - "/Go基础学习记录-编写Web应用程序-错误处理.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-cuo-wu-chu-li/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-cuo-wu-chu-li.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-cuo-wu-chu-li.html"
---
## **错误处理**

前面的分享加了两个功能，一个是编辑功能，一个保存功能

在我们的程序中有几个地方其实是忽略了错误的处理。  
这是不好的做法，尤其是因为这样的做法发生错误时，程序会出现意外行为。  
更好的解决方案是处理错误并向用户返回错误消息。  
这样，如果出现问题，服务器将完全按照我们想要的方式运行，并且可以通知用户。  
首先，让我们处理renderTemplate中的错误：

```go
func renderTemplate(w http.ResponseWriter, templateName string, p *Page) {
    t, err := template.ParseFiles("template/" + templateName + ".html")

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    err = t.Execute(w, p)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
}
```

http.Error函数发送指定的HTTP响应代码（在本例中为“内部服务器错误”）和错误消息。  
将这个放在一个单独的功能中的决定已经取得了成效。  
现在让我们修复saveHandler：

```go
func saveHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/save/"):]
    body := r.FormValue("body")
    p := &Page{
        Title: title,
        Body:  []byte(body),
    }
    err := p.save()
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
    }

    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

p.save()期间发生的任何错误都将报告给用户
