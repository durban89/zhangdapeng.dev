---
title: "Go基础学习记录之CSRF攻击(二)"
date: "2025-08-04 11:38:40"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-csrf-gong-ji-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之CSRF攻击(二)/"
  - "/2025/08/04/Go基础学习记录之CSRF攻击(二).html"
  - "/Go基础学习记录之CSRF攻击(二)/"
  - "/Go基础学习记录之CSRF攻击(二).html"
  - "/2025/08/04/Go基础学习记录之CSRF攻击-二/"
  - "/2025/08/04/Go基础学习记录之CSRF攻击-二.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-csrf-gong-ji-er/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-csrf-gong-ji-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-csrf-gong-ji-er.html"
---
## CSRF攻击

### 如何防止CSRF攻击

通过上篇文章[]的介绍，您可能会有点害怕。  
但恐惧是件好事。  
它将迫使您自行了解如何防止此类漏洞发生在您身上。

可以在Web应用程序的服务器端和客户端上采取针对CSRF攻击的预防措施。  
但是，CSRF攻击在服务器端最有效地受到阻碍。

有许多方法可以防止服务器端的CSRF攻击。  
大多数方法来自以下两个方面：

1. 保持正确使用GET，POST和cookies。  
2. 包括带有非GET请求的伪随机数

在前面几章关于REST的介绍中，我们了解了大多数Web应用程序是如何基于GET和POST HTTP请求的，并且这些cookie与这些请求一起被包含在内。  
我们通常根据以下原则设计应用程序：

1. GET通常用于在不更改任何数据的情况下查看信息。  
2. POST用于下订单，更改资源属性或执行其他任务

我现在将使用Go语言来说明如何限制对资源方法的访问：

```go
controller.Get("/user/:uid", FetchUser)
controller.Post("/user/:uid", UpdateUser)
```

由于我们已经规定修改只能使用POST，因此当发出GET方法而不是POST时，我们可以拒绝响应请求。  
根据上段代码，可以防止利用GET作为CSRF漏洞的攻击。  
这足以阻止所有可能的CSRF攻击吗？  
当然不是，因为POST也可以伪造。

我们需要实现第二步，即（在非GET请求的情况下）增加请求中包含的伪随机数的长度。  
这通常涉及以下步骤：

* 对于每个用户，生成具有伪随机值的唯一cookie令牌。所有表单必须包含相同的伪随机值。这个提议是最简单的，因为从理论上讲，攻击者无法读取第三方cookie。攻击者可能提交的任何表单都将无法通过验证过程而不知道随机值是什么。
* 不同的表单包含不同的伪随机值，正如我们在第4.4节“如何防止多表单提交”中所介绍的那样。我们可以重用该部分中的相关代码来满足我们的需求：

生成随机数令牌：

```go
h := md5.New()
io.WriteString(h, strconv.FormatInt(crutime, 10))
io.WriteString(h, "ganraomaxxxxxxxxx")
token := fmt.Sprintf("%x", h.Sum(nil))

t, _ := template.ParseFiles("login.html")
t.Execute(w, token)
```

输出令牌：

```html
<input type="hidden" name="token" value="{{.}}">
```

验证令牌：

```go
r.ParseForm()
token := r.Form.Get("token")
if token! = "" {
    // Verification token of legitimacy
} Else {
    // Error token does not exist
}
```

我们可以使用上面的代码来保护我们的POST。  
您可能想知道，根据我们的理论，恶意第三方是否可能以某种方式找出我们的秘密令牌价值？  
事实上，破解它基本上是不可能的 - 使用强力方法计算正确的字符串值需要大约2到11次。

### 小结

跨站点请求伪造（也称为CSRF）是一种非常危险的Web安全威胁。  
它在网络安全圈中被称为“沉睡的巨人”安全问题;  
正如您所知，CSRF攻击具有相当的声誉。  
本次分享不仅介绍了跨站点请求伪造本身，还介绍了此漏洞背后的因素。  
最后提出了一些防止此类攻击的建议和方法。  
作为读者，我希望本次分享能够激励您编写更好，更安全的Web应用程序。
