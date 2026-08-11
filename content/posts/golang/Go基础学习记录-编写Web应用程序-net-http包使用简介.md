---
title: "Go基础学习记录 - 编写Web应用程序 - net/http包使用简介"
date: "2025-08-01 09:21:21"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-nethttp-bao-shi-yong-jian-jie"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-net/http包使用简介/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-net/http包使用简介.html"
  - "/Go基础学习记录-编写Web应用程序-net/http包使用简介/"
  - "/Go基础学习记录-编写Web应用程序-net/http包使用简介.html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-net-http包使用简介/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-net-http包使用简介.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-nethttp-bao-shi-yong-jian-jie/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-nethttp-bao-shi-yong-jian-ji.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-nethttp-bao-shi-yong-jian-jie.html"
---
### **net/http包构建Web应用简介**

下面是一个简单的Web服务器的完整工作示例：

```go
package main

import (
    "fmt"
    "log"
    "net/http"
)

// 相应处理
func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "=======> %s", r.URL.Path[1:])
}

func main() {
    // 路由处理 接收"/"后 交给handler处理
    http.HandleFunc("/", handler)
    // 启动服务
    log.Fatal(http.ListenAndServe(":8090", nil))
}
```

main函数以对http.HandleFunc的调用开始，它告诉http包使用处理程序处理对web根目录（"/"）的所有请求。  
然后调用http.ListenAndServe，指定它应该在接口（":8090"）上侦听端口8090。(暂时不要担心它的第二个参数，nil)此函数将一直阻塞，直到程序终止。

ListenAndServe仅在发生意外错误时返回错误信息。为了记录该错误，我们使用log.Fatal包装函数调用。  
handler函数的类型为http.HandlerFunc。它需要一个http.ResponseWriter和一个http.Request作为其参数。  
http.ResponseWriter值组装HTTP服务器的响应;通过向它写入值，我们将数据发送到HTTP客户端。  
http.Request是表示客户端HTTP请求的数据结构。  
r.URL.Path是请求URL的路径组件。  
尾部[1:]表示"从第1个字符到结尾创建路径的子片段"。  
这会从路径名中删除前导"/"。  
如果您运行此程序并访问URL：

```bash
http://localhost:8090/monkeys
```

该程序将显示一个页面，其中包含如下内容：

```bash
=======> monkeys
```
