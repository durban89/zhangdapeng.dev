---
title: "Go基础学习记录 - 编写Web应用程序 - 添加编辑和保存功能（二）"
date: "2025-08-01 09:21:36"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong-neng-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（二）/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（二）.html"
  - "/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（二）/"
  - "/Go基础学习记录-编写Web应用程序-添加编辑和保存功能（二）.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能-二/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-添加编辑和保存功能-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-tian-jia-bian-ji-he-bao-cun-gong-neng-e.html"
---
## **添加编辑和保存功能**

继续上篇文章【[Go基础学习记录 - 编写Web应用程序 - 添加编辑和保存功能（一）](https://www.xiaorongmao.com/blog/43)】

如果将上篇文章的逻辑进行构建并运行，试图访问一个不存在的wiki，比如/view/APageThatDoesntExist，将看到包含HTML的空页面。  
这是因为它忽略了loadPage的错误返回值，并继续尝试填写没有数据的模板。  
相反，如果请求的页面不存在，它应该将客户端重定### 处理不存在的页面  
修改下viewHandler来达到我们的需求，如下

```go
func viewHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/view/"):]
    p, err := loadPage(title)
    if err != nil {
        http.Redirect(w, r, "/edit/"+title, http.StatusFound)
        return
    }

    renderTemplate(w, "view", p)
}
```

http.Redirect函数将HTTP状态代码http.StatusFound（302）和Location头添加到HTTP响应中。  
再次构建并运行程序，访问/view/APageThatDoesntExist，会跳转到/edit/APageThatDoesntExist。

### 保存页面功能  
根据上篇文章的流程，我们来添加下saveHandler函数的处理逻辑，它将处理位于编辑页面上的表单的提交。  
先在main中加入对应的逻辑，如下

```go
func main() {
    http.HandleFunc("/view/", viewHandler)
    http.HandleFunc("/edit/", editHandler)
    http.HandleFunc("/save/", saveHandler)
    log.Fatal(http.ListenAndServe(":8090", nil))
}
```

saveHandler实现处理程序如下：

```go
func saveHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/save/"):]
    body := r.FormValue("body")
    p := &Page{
        Title: title,
        Body:  []byte(body),
    }
    p.save()
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

页面标题（在URL中提供）和表单的唯一字段Body存储在新页面中。  
然后调用save()方法将数据写入文件，并将客户端重定向到/view/page。  
FormValue返回的值是string类型。  
我们必须将该值转换为[]byte，然后才能适应Page结构。  
我们使用[]byte(body)来执行转换。

到这里整个的编辑和存储就都完成了，我们可以再次进行构建程序，然后启动

```bash
$ go build wiki.go
$ ./wiki
```

访问view/pageTitle，不存在则进行创建，通过表单提交进行保存，还可以继续修改并保存。
