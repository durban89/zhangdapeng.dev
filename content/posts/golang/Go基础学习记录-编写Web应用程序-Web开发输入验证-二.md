---
title: "Go基础学习记录 - 编写Web应用程序 - Web开发输入验证(二)"
date: "2025-08-01 09:22:11"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(二)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(二).html"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(二)/"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(二).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-二/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-er/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-er.html"
---
继续前面几篇文章的分享，本次分享下 -- 输入验证

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

***项目地址***

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.2
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.2
```

这些我觉得 够清晰了。OK！

继续分享的输入验证的逻辑。

Web开发中最重要的原则之一是您不能信任客户端用户表单中的任何内容。  
您必须在使用之前验证所有传入数据。  
许多网站都受到这个问题的影响，这个问题既简单又至关重要。  
有两种方法可以验证常用的表单数据。  
第一个是前端的JavaScript验证，第二个是后端的服务器验证。  
本次继续上次分享，分享Web开发中的服务器端验证第二部分

## 中文

有时我们需要用户输入他们的中文名称，我们必须验证他们都使用中文而不是随机字符。  
对于中文验证，正则表达式是唯一的方法。如下示例演示

```go
if m, _ := regexp.MatchString("^[\\x{4e00}-\\x{9fa5}]+$", r.Form.Get("author")); m {
    fmt.Println("含有中文")
}
```

当提交的时候我们给author赋值"我是中文"，然后点击Submit提交，会看到输出如下内容

```bash
author: [我是中文]
含有中文
```

## 英文字母

有时我们需要用户只输入英文字母。  
例如，我们需要某人的英文名称，比如astaxie而不是asta谢谢。  
我们可以轻松使用正则表达式来执行验证。如下示例演示

```go
if m, _ := regexp.MatchString("^[a-zA-Z]+$", r.Form.Get("author")); m {
    fmt.Println("含有英文字母")
}
```

当提交的时候我们给author赋值"English"，然后点击Submit提交，会看到输出如下内容

```bash
author: [English]
含有英文字母
```

## **邮箱地址**

如果您想知道用户是否输入了有效的电子邮件地址，可以使用以下正则表达式：

```go
if m, _ := regexp.MatchString(`^([\w\.\_]{2,10})@(\w{1,}).([a-z]{2,4})$`, r.Form.Get("author")); m {
    fmt.Println("正确的邮箱地址")
}
```

当提交的时候我们给author赋值"xxx@xxx"，然后点击Submit提交，会看到输出如下内容

```bash
author: [xxx@xxx]
正确的邮箱地址
```

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.3
```
