---
title: "Go基础学习记录 - 编写Web应用程序 - Web开发输入验证(一)"
date: "2025-08-01 09:22:08"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(一)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(一).html"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(一)/"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(一).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-一/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-yi.html"
---
继续前面几篇文章的分享，本次分享下 -- 输入验证

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.1
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.1
```

这些我觉得 够清晰了。OK！

继续分享的输入验证的逻辑。

Web开发中最重要的原则之一是您不能信任客户端用户表单中的任何内容。  
您必须在使用之前验证所有传入数据。  
许多网站都受到这个问题的影响，这个问题既简单又至关重要。  
有两种方法可以验证常用的表单数据。  
第一个是前端的JavaScript验证，第二个是后端的服务器验证。  
本次只分享Web开发中的服务器端验证。

## **必填字段**

有时我们要求用户输入一些字段，但他们无法完成该字段。可以使用len函数来获取字段的长度，以确保用户输入了某些内容。在ArticleSave方法中加入如下代码

```go
if len(r.Form["author"][0]) == 0 {
    fmt.Println("author is empty")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

当提交的时候我们不给author赋值，然后点击Submit提交，会看到输出如下内容

```bash
author: []
author is empty
```

r.Form在空白时对待不同的表单元素类型。  
对于空文本框，文本区域和文件上传，它返回一个空字符串;  
对于单选按钮和复选框，它甚至不会创建相应的项目。  
相反，如果您尝试访问它，您将收到错误。  
因此，使用r.Form.Get()获取字段值更安全，因为如果该值不存在，它将始终返回空。  
另一方面，r.Form.Get()一次只能获得一个字段值，因此您需要使用r.Form来获取值的映射。我们修改下刚才那段代码如下

```go
if len(r.Form.Get("author")) == 0 {
    fmt.Println("author is empty")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
```

当提交的时候我们不给author赋值，然后点击Submit提交，会看到输出如下内容

```bash
author: []
author is empty
```

得到的结果跟上段代码是一致的

## **数字**

有时我们需要提交过来的数据是数字而不是字段值等其他文本。  
例如，假设我们只需要整数形式的用户年龄，即50或10，而不是“足够老”或“年轻人”。  
如果我们需要一个正数，我们可以先将值转换为int类型，然后再处理它。下面我们在ArticleSave方法中加入如下代码

```go
getint, err := strconv.Atoi(r.Form.Get("author"))
if err != nil {
    fmt.Println(err)
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
}
fmt.Println("getint:", getint)
```

当提交的时候我们给author赋值durban，然后点击Submit提交，会看到输出如下内容

```bash
author: [durban]
strconv.Atoi: parsing "durban": invalid syntax
```

当提交的时候我们给author赋值10，然后点击Submit提交，会看到输出如下内容

```bash
author: [10]
getint: 10
```

另一种方法是使用正则表达式。  
代码如下，我们将上面的代码段更换如下

```go
if m, _ := regexp.MatchString("^[0-9]+$", r.Form.Get("author")); !m {
    fmt.Println("非整数")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
    return
}
fmt.Println("get author:", r.Form.Get("author"))
```

当提交的时候我们给author赋值10，然后点击Submit提交，会看到输出如下内容

```bash
author: [10]
get author: 10
```

出于高性能目的，正则表达式效率不高，但简单的正则表达式通常足够快。  
如果您熟悉正则表达式，那么这是验证数据的一种非常方便的方法。  
请注意，Go使用[RE2]，因此支持所有UTF-8字符。

**RE2是一种快速，安全，线程友好的替代方法，用于回溯正则表达式引擎，如PCRE，Perl和Python中使用的那些。  
它是一个C ++库。**

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.2
```
