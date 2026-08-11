---
title: "Go基础学习记录之阻止Session劫持(Preventing session hijacking)"
date: "2025-08-01 11:35:25"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-zu-zhi-session-jie-chi-preventing-session-hijacking"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之阻止Session劫持(Preventing-session-hijacking)/"
  - "/2025/08/01/Go基础学习记录之阻止Session劫持(Preventing-session-hijacking).html"
  - "/Go基础学习记录之阻止Session劫持(Preventing-session-hijacking)/"
  - "/Go基础学习记录之阻止Session劫持(Preventing-session-hijacking).html"
  - "/2025/08/01/Go基础学习记录之阻止Session劫持-Preventing-session-hijacking/"
  - "/2025/08/01/Go基础学习记录之阻止Session劫持-Preventing-session-hijacking.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zu-zhi-session-jie-chi-preventing-session-hijacking/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-zu-zhi-session-jie-chi-preventing-session-hijacking.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-zu-zhi-session-jie-chi-preventing-session-hijacking.html"
---
## 阻止Session劫持(Preventing session hijacking)

Session劫持是一种常见且严重的安全威胁。在与服务器通信时，客户端使用Session ID进行验证和其他目的。不幸的是，恶意第三方有时可以跟踪这些通信并找出客户端Session ID。  
本次分享，将向您展示如何为教育目的劫持Session。

### Session劫持过程

以下代码是count变量的计数器：

```go
// WelcomeLogin 欢迎登录页
func WelcomeLogin(w http.ResponseWriter, r *http.Request) {
    session, err := appSession.SessionStart(w, r)
    if err != nil {
        fmt.Fprintf(w, "session error")
        return
    }

    count := session.Get("count")
    if count == nil {
        session.Set("count", 1)
    } else {
        session.Set("count", count.(int)+1)
    }

    t, err := template.ParseFiles(config.TemplateDir + "/login.html")

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    err = t.Execute(w, session.Get("count"))

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
}
```

login.html的内容如下：

```html
Hi. Now count:{{.}}
```

保持刷新直到数字变为10，然后打开浏览器的cookie管理器（我在这里使用firefox）。您应该能够看到以下信息：

{% img https://cdn.xiaorongmao.com/up/golang_web_30_1.png!/fh/500 "" %}

 
这一步非常重要：打开另一个浏览器(我在这里使用chrome)，将URL复制到新浏览器，打开一个cookie模拟器来创建一个新的cookie并输入与我们在第一个浏览器中看到的cookie完全相同的值。

刷新页面，您将看到以下内容：

{% img https://cdn.xiaorongmao.com/up/golang_web_30_2.png!/fh/500 "" %}

在这里，我们看到我们可以在不同浏览器之间劫持Session，并且在一个浏览器中执行的操作可以影响另一个浏览器中页面的状态。  
因为HTTP是无状态的，所以无法知道来自chrome的Session ID是否被模拟，并且firefox也无法知道它的Session ID已被劫持。

### 防止Session劫持

通过上面劫持Session的简单示例，可以看到它非常危险，因为它允许攻击者做任何他们想做的事情。那么我们如何防止会话劫持？第一步是仅在cookie中设置Session ID，而不是在URL重写中设置。另外，我们应该将httponly cookie属性设置为true。这限制了客户端脚本获得对Session ID的访问权限。使用这些技术，XSS无法访问cookie，也不会像我们演示的那样从cookie管理器获取会话ID。  
第二步是为每个请求添加一个令牌。与我们在前面部分中处理重复表单提交的方式类似，我们添加一个包含令牌的隐藏字段。当请求发送到服务器时，我们可以验证此令牌以证明请求是唯一的。

```go
h := md5.New()
salt:="xiaorongmao%^7&8888"
io.WriteString(h,salt+time.Now().String())
token:=fmt.Sprintf("%x",h.Sum(nil))
if r.Form["token"]!=token{
    // ask to log in
}
session.Set("token",token)
```

### Session ID超时

另一种解决方案是为每个Session添加创建时间，并用新的Session ID替换过期的Session ID。这可以防止在某些情况下Session劫持，例如劫持时间太晚。

```go
createtime := session.Get("createtime")
if createtime == nil {
    session.Set("createtime", time.Now().Unix())
} else if (createtime.(int64) + 60) < (time.Now().Unix()) {
    appSession.SessionDestroy(w, r)
    session = appSession.SessionStart(w, r)
}
```

我们设置一个值来保存创建时间并检查它是否已过期（我在这里设置了60秒）。此步骤通常可以阻止会话劫持尝试。通过组合上面提到的两个解决方案，将能够防止大多数Session劫持尝试成功。一方面，频繁重置的Session ID将导致攻击者总是过期且无用的Session ID;另一方面，通过在cookie上设置httponly属性并确保只能通过cookie传递Session ID，可以减轻所有基于URL的攻击。最后，我们在Cookie上设置MaxAge = 0，这意味着Session ID不会保存在浏览器历史记录中。
