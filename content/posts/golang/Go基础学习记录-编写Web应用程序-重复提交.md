---
title: "Go基础学习记录 - 编写Web应用程序 - 重复提交"
date: "2025-08-01 09:22:25"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-fu-ti-jiao"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重复提交/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-重复提交.html"
  - "/Go基础学习记录-编写Web应用程序-重复提交/"
  - "/Go基础学习记录-编写Web应用程序-重复提交.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-fu-ti-jiao/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-fu-ti-jiao.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-chong-fu-ti-jiao.html"
---
本次分享下 -- 表单的重复提交

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.6
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.6
```

这些我觉得 够清晰了。OK！

继续分享"重复提交"的分享。

## 重复提交

我不知道你有没有看到一些博客或BBS有多个帖子完全相同，但我可以告诉你，这是因为用户提交了重复的帖子导致的。  
有许多事情可能会导致重复提交;  
有时用户只需双击提交按钮，或者他们想在发布后修改一些内容，然后按后退按钮。  
在某些情况下，这是恶意用户的故意行为。  
很容易看出重复提交会如何导致许多问题。  
因此，我们必须使用有效的手段来预防它。  
解决方案是向表单添加一个带有唯一标记的隐藏字段，并在处理传入数据之前始终检查此标记。  
此外，如果您使用Ajax提交表单，请在提交表单后使用JavaScript禁用提交按钮。  
具体实例演示如下

### 第一步 首先修改下我们的edit.html

添加如下代码

```html
<input type="hidden" name="token" value="{{.Token}}">
```

### 第二步 修改我们的Page结构体

```go
type Page struct {
  Title  string
  Body   []byte
  Script string
  Html   template.HTML
  Token  string
}
```

### 第三步 添加Token

修改ArticleEdit函数，添加生成token的逻辑

```go
crutime := time.Now().Unix()
h := md5.New()
io.WriteString(h, strconv.FormatInt(crutime, 10))
token := fmt.Sprintf("%x", h.Sum(nil))
```

当我们重新编译程序并运行后，访问edit页面的时候，通过查看源代码的方式能够看到有如下代码

```html
<input type="hidden" name="token" value="f3072482bbf23a8cbf2eeef3dd489eaf">
```

您可以刷新页面，每次都会看到不同的token。  
这确保了每种形式都是独特的。

### 第四步 添加验证逻辑

我这里修改ArticleSave函数，并添加如下逻辑

```go
if token != "" {
  // check token validity
  fmt.Println("Token is empty")
} else {
  // give error if no token
  fmt.Println("To Validate Token")
}
```

我们使用MD5哈希（时间戳）生成令牌，并将其添加到客户端表单上的隐藏字段和服务器端的会话cookie（后面的分享中介绍）。  
然后我们可以使用此令牌来检查此表单是否已提交。

目前，您可以通过向表单添加令牌来防止许多重复提交攻击，但它无法阻止此类型的所有欺骗性攻击。  
还有许多工作需要完成

今天就分享到这里，如果你有更好的方法请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.7
```
