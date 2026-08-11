---
title: "Go基础学习记录 - 编写Web应用程序 - XSS"
date: "2025-08-01 09:22:20"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-xss"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-XSS/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-XSS.html"
  - "/Go基础学习记录-编写Web应用程序-XSS/"
  - "/Go基础学习记录-编写Web应用程序-XSS.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-xss/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-xss.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-xss.html"
---
继续前几篇的分享，本次分享下 -- XSS

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.5
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.5
```

这些我觉得 够清晰了。OK！

继续分享XSS的分享。

## 转义提交的数据

今天的网站有更多的动态内容，以改善用户体验，这意味着我们必须根据每个人的行为提供动态信息。不幸的是，动态网站容易受到称为“跨站点脚本”（称为“XSS”）的恶意攻击。静态网站不容易受到跨站点脚本的影响。攻击者经常向有漏洞的网站注入JavaScript，VBScript，ActiveX或Flash等恶意脚本。一旦他们成功注入脚本，用户信息就会被盗，您的网站就会充斥着垃圾邮件。攻击者还可以将用户设置更改为他们想要的任何内容。  
如果我们希望防止此类攻击，则应结合以下两种方法：  
1、验证用户的所有数据，我在上几篇文章中已经讨论过。  
2、小心处理将发送给客户端的数据，以防止任何注入的脚本在浏览器上运行。  
那么我们如何在Go中做这两件事呢？  
幸运的是，html/template包有一些有用的函数来转义数据，如下所示：

* func HTMLEscape(w io.Writer, b []byte) 转义 b 到 w.
* func HTMLEscapeString(s string) string 返回一个转义后的字符串
* func HTMLEscaper(args ...interface{}) string 从多个参数中转义后返回一个字符串。

让我们通过例子来演示下  
这里我在ArticleSave方法中加入如下代码

```go
fmt.Println("username:", template.HTMLEscapeString(r.Form.Get("author"))) // print at server side
fmt.Println("password:", template.HTMLEscapeString(r.Form.Get("author")))
template.HTMLEscape(w, []byte(r.Form.Get("author"))) // responded to clients
```

如果有人试图将作者中输入为`*<script>alert()</script>*`，我们将分别在终端和浏览器中看到以下内容：  
终端显示如下

```bash
author:  &lt;script&gt;alert()&lt;/script&gt;
author:  &lt;script&gt;alert()&lt;/script&gt;
```

浏览器显示如下

```bash
&lt;script&gt;alert()&lt;/script&gt;
```

如果你在测试的时候建议先运行下面这段代码

```go
fmt.Println("username:", template.HTMLEscapeString(r.Form.Get("author"))) // print at server side
fmt.Println("password:", template.HTMLEscapeString(r.Form.Get("author")))
```

然后在注释掉上面的在运行下面这段代码

```go
template.HTMLEscape(w, []byte(r.Form.Get("author"))) // responded to clients
```

这样操作后后逻辑就比较清晰

## 转义后的JavaScript

html/template包中的函数可帮助您转义所有HTML标记。  
如果您只想将`*<script>alert()</script>*`打印到浏览器怎么办？  
您应该使用text/template。  
这里我没修改下我们项目的Page结构体，添加一个Script，如下

```go
type Page struct {
  Title  string
  Body   []byte
  Script string
}
```

然后需改ArticleView函数，在ArticleView中添加如下代码

```go
p.Script = "<script>alert('Web站开发实例')</script>"
helpers.RenderTemplate(w, "view", p)
```

然后在view.html添加如下代码

```html
{{.Script}}
```

重新编译项目应运行，当我们访问view路由的时候，会看到类似如下的输出

```html
<script>alert('Web站开发实例')</script>
```

我们还可以使用template.HTML类型：如果变量内容的类型为template.HTML，则不会对其进行转义。  
这里我没修改下我们项目的Page结构体，添加一个Script，如下

```go
type Page struct {
  Title  string
  Body   []byte
  Script string
  Html   template.HTML
}
```

然后需改ArticleView函数，在ArticleView中添加如下代码

```go
p.Html = template.HTML("<script>alert('Web站开发实例')</script>")
```

然后在view.html添加如下代码

```html
{{.Html}}
```

重新编译项目应运行，当我们访问view路由的时候，会看到类似如下的输出

```html
<script>alert('Web站开发实例')</script>
```

并且会有一个弹唱出现，其实就是调用了alert()函数

今天就分享到这里，如果你有更好的方法请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.6
```
