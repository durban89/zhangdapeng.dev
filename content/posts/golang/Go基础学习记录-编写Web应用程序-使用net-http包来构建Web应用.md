---
title: "Go基础学习记录 - 编写Web应用程序 - 使用net/http包来构建Web应用"
date: "2025-08-01 09:21:26"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shi-yong-nethttp-bao-lai-gou-jian-web-ying-yong"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-使用net/http包来构建Web应用/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-使用net/http包来构建Web应用.html"
  - "/Go基础学习记录-编写Web应用程序-使用net/http包来构建Web应用/"
  - "/Go基础学习记录-编写Web应用程序-使用net/http包来构建Web应用.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-使用net-http包来构建Web应用/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-使用net-http包来构建Web应用.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shi-yong-nethttp-bao-lai-gou-jia/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shi-yong-nethttp-bao-lai-gou.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-shi-yong-nethttp-bao-lai-gou-jian-web-y.html"
---
### **使用net/http来构建Web应用**

要使用net/http包，必须导入：

```go
import (
    "fmt"
    "io/ioutil"
    "net/http" // 注意这里
)
```

让我们创建一个允许用户查看Wiki页面的处理程序viewHandler。它将处理前缀为"/view/"的URL。

```go
func viewHandler(w http.ResponseWriter, r *http.Request) {
    title := r.URL.Path[len("/view/"):]
    p, _ := loadPage(title)
    fmt.Fprintf(w, "<h1>%s</h1><div>%s</div>", p.Title, p.Body)
}
```

再次注意，使用`\_`来忽略loadPage的错误返回值。  
这样做是为了简单起见，通常被认为是不好的做法。  
后面会讨论这个问题。  
首先，此函数从r.URL.Path中提取页面标题，r.URL.Path是请求URL的路径组件。  
使用[len("/view/"):]重新切片路径以删除请求路径的前导"/view/"组件。  
这是因为路径总是以"/view/"开头，这不是页面标题的一部分。  
然后，该函数加载页面数据，使用一串简单的HTML格式化页面，并将其写入w，即http.ResponseWriter。  
要使用此处理程序，我们重写main函数以使用viewHandler初始化http以处理path /view/下的任何请求。

```go
func main() {
    http.HandleFunc("/view/", viewHandler)
    log.Fatal(http.ListenAndServe(":8090", nil))
}
```

我们创建一些页面数据(作为test.txt)，编译我们的代码，并尝试提供维基页面。  
在编辑器中打开test.txt文件，并在其中保存字符串"I Like Gowhich"（不带引号）。

```bash
$ go build wiki.go
$ ./wiki
```

运行此Web服务器后，访问 http://localhost:8090/view/test 应显示一个标题为"test"的页面，其中包含"I Like Gowhich"字样。  
但是访问其他页面的时候，则程序会报错。这个问题我们后面慢慢解决
