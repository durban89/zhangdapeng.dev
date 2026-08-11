---
title: "Go基础学习记录之Session和Cookie"
date: "2025-08-01 11:32:04"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-session-he-cookie"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Session和Cookie/"
  - "/2025/08/01/Go基础学习记录之Session和Cookie.html"
  - "/Go基础学习记录之Session和Cookie/"
  - "/Go基础学习记录之Session和Cookie.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-session-he-cookie/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-session-he-cookie.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-session-he-cookie.html"
---
## Session和Cookie

session和cookie是两个非常常见的Web概念，也很容易被误解。  
但是，它们对于页面授权以及收集页面统计信息非常重要。  
我们来看看这两个用例。

假设我们要抓取限制公共访问的页面，例如Twitter用户的主页。  
当然，您可以打开浏览器并输入用户名和密码来登录和访问该信息，但所谓的“网络爬行”意味着我们使用程序自动执行此过程而无需任何人为干预。  
因此，当我们使用浏览器登录时，我们必须找出幕后的真实情况。

当我们第一次收到登录页面并输入用户名和密码时，按下“登录”按钮后，浏览器会向远程服务器发送POST请求。  
服务器验证登录信息并返回HTTP响应后，浏览器重定向到用户主页。  
这里的问题是，服务器如何知道我们拥有所需网页的访问权限？  
由于HTTP是无状态的，因此服务器无法知道我们是否在最后一步中通过了验证。  
最简单也许最天真的解决方案是将用户名和密码附加到URL。  
这有效，但对服务器施加了太大的压力（服务器必须验证针对数据库的每个请求），并且可能对用户体验有害。  
实现此目标的另一种方法是使用cookie和session在服务器端或客户端保存用户的身份。  
简而言之，Cookie会在客户端的计算机上存储历史信息（包括用户登录信息）。  
每次用户访问同一网站时，客户端的浏览器都会发送这些cookie，自动完成用户的登录步骤。

另一方面，session在服务器端存储历史信息。  
服务器使用session ID来标识不同的session，并且服务器生成的session ID应始终是随机且唯一的。  
您可以使用cookie或URL参数来获取客户端的身份。

Cookie由浏览器维护。  
可以在Web服务器和浏览器之间进行通信时修改它们。  
当用户访问相应的网站时，Web应用程序可以访问cookie信息。  
在大多数浏览器设置中，有一个与cookie隐私相关的设置。  
打开它时，您应该能够看到类似于以下内容的内容。

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1536669103/golang_web_25_1.png "" %}

Cookie具有到期时间，并且有两种类型的Cookie以其生命周期区分：会话cookie和持久性cookie。  
如果您的应用程序未设置cookie到期时间，浏览器关闭后浏览器将不会将其保存到本地文件系统中。  
这些cookie称为会话cookie，这种类型的cookie通常保存在内存中而不是本地文件系统中。  
如果您的应用程序确实设置了到期时间(例如，setMaxAge(606024))，浏览器会将此cookie保存到本地文件系统，并且在达到分配的到期时间之前不会删除它。  
保存到本地文件系统的Cookie可以由不同的浏览器进程共享 - 例如，通过两个IE窗口;  
不同的浏览器使用不同的进程来处理保存在内存中的cookie。

## Cookie

### Set Cookie

Go使用net/http包中的SetCookie函数来设置cookie：

```go
http.SetCookie(w ResponseWriter, cookie *Cookie)
```

w是请求的响应，cookie是结构。让我们看看Cookie的结构：

```go
// A Cookie represents an HTTP cookie as sent in the Set-Cookie header of an
// HTTP response or the Cookie header of an HTTP request.
//
// See http://tools.ietf.org/html/rfc6265 for details.
type Cookie struct {
    Name  string
    Value string

    Path       string    // optional
    Domain     string    // optional
    Expires    time.Time // optional
    RawExpires string    // for reading cookies only    // MaxAge=0 means no 'Max-Age' attribute specified.
    // MaxAge<0 means delete cookie now, equivalently 'Max-Age: 0'
    // MaxAge>0 means Max-Age attribute present and given in seconds
    MaxAge   int
    Secure   bool
    HttpOnly bool
    Raw      string
    Unparsed []string // Raw text of unparsed attribute-value pairs
}
```

下面让我们实例演示一下

```go
expired := time.Now().Add(365 * 24 * time.Hour)
cookie := http.Cookie{
    Name:    "site_name",
    Value:   "gowhich",
    Expires: expired,
}

http.SetCookie(w, &cookie)
```

上面的示例显示了如何设置cookie。现在让我们看看如何获取已设置的cookie：

### Get Cookie

```go
var siteName string
cookie, err := r.Cookie("site_name")
if err != nil {
    siteName = cookie.Value
}
fmt.Println(siteName)
```

从请求中获取cookie非常方便。

## Session

session是一系列操作或消息。例如，您可以考虑在接听电话和挂起电话之间采取的动作。  
在网络协议方面，session更多地与浏览器和服务器之间的连接有关。  
session有助于存储服务器和客户端之间的连接状态，这有时可以采用数据存储结构的形式。  
session是服务器端机制，通常使用哈希表（或类似的东西）来保存传入的信息。  
当应用程序需要为客户端分配新会话时，服务器应检查是否存在具有唯一session ID的同一客户端的任何现有session。  
如果session ID已存在，则服务器将只返回同一session到客户端。  
另一方面，如果客户端不存在session ID，则服务器会创建一个全新的session（这通常发生在服务器删除了相应的sessionID，但用户已手动附加旧session时）。  
session本身并不复杂，但它的实现和部署是比较复杂的，所以你不能使用“一种方式来统治它们”。

总之，session和cookie的目的是相同的。  
它们都是为了克服HTTP的无状态，但它们使用不同的方法。  
session使用cookie在客户端保存session ID，并在服务器端保存所有其他信息。  
Cookie会在客户端保存所有客户端信息。  
您可能已经注意到cookie存在一些安全问题。  
例如，恶意第三方网站可能会破解和收集用户名和密码。

以下是两个常见的漏洞：

* appA为appB设置了一个意外的cookie。
* XSS攻击：appA使用JavaScript document.cookie访问appB的cookie。

看完本次分享后，您应该了解一些cookie和session的基本概念。你应该能够理解它们之间的差异，这样当不可避免地出现bug时你就不会自杀。
