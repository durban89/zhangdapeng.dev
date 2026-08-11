---
title: "Go基础学习记录 - 编写Web应用程序 - Web开发输入验证(四)"
date: "2025-08-01 09:22:17"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-si"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(四)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(四).html"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(四)/"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(四).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-四/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-四.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-si/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-si.html"
---
继续前面几篇文章的分享，本次分享下 -- 输入验证

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.4
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.4
```

这些我觉得 够清晰了。OK！

继续分享的输入验证的逻辑。

Web开发中最重要的原则之一是您不能信任客户端用户表单中的任何内容。  
您必须在使用之前验证所有传入数据。  
许多网站都受到这个问题的影响，这个问题既简单又至关重要。  
有两种方法可以验证常用的表单数据。  
第一个是前端的JavaScript验证，第二个是后端的服务器验证。  
本次继续上次分享，分享Web开发中的服务器端验证第四部分

## 单选按钮

如果我们想知道文章的开放状态是打开还是关闭，我们可以使用单选按钮，打开为1​，关闭为2。  
然而，当提交文章的时候发送了一个3的值，程序是否会抛出异常？肯定会，但是要如果处理。  
我们需要使用与下拉列表中相同的方法，以确保我们的单选按钮仅返回预期值，操作如下  
在edit.html添加如下代码

```html
<div class="checkbox">
  <label for="category">文章状态</label>
</div>
<div class="radio">
  <label>
    <input type="radio" name="openStatus" id="openStatus1" value="1" checked> 打开
  </label>
  <label>
    <input type="radio" name="openStatus" id="openStatus2" value="2"> 关闭
  </label>
</div>
```

在ArticleSave方法中使用以下代码来验证输入：

```go
if !helpers.ValidateInArray(openStatusSlice, openStatus) {
    fmt.Println("openStatus not in openStatusSlice")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
    return
}
```

并添加接收和输出的逻辑如下

```go
openStatus := r.FormValue("openStatus")
fmt.Println("openStatus: ", openStatus)
```

跟上次分享判断“分类”是一样的逻辑  
重新编译并运行项目，如果选择“打开”的话，提交后会在终端接收到如下输出

```bash
openStatus:  1
```

## 复选框

假设有一些用户兴趣的复选框，并且您不需要此处的无关值。  
您可以验证以下内容：

在这种情况下，清理与验证按钮和复选框输入略有不同，因为在这里我们从复选框中得到一个切片。实例操作如下：  
在edit.html添加如下代码

```html
<div class="checkbox">
  <label for="category">频道</label>
</div>
<div class="checkbox">
  <label>
    <input type="checkbox" name="channel" value="news"> 新闻
  </label>
  <label>
    <input type="checkbox" name="channel" value="technology"> 科技
  </label>
  <label>
    <input type="checkbox" name="channel" value="other"> 其他
  </label>
</div>
```

在ArticleSave方法中使用以下代码来验证输入：  
添加接收和输出的逻辑如下

```go
channel := r.FormValue("channel")
fmt.Println("channel: ", channel)
fmt.Println("channels: ", r.Form["channel"])
```

重新编译并运行项目，如果选择“新闻”、“科技”的话，提交后会在终端接收到如下输出

```bash
channel:  news
channels:  [news technology]
```

从输出可以看出，使用r.FormValue获取的值并不是我们提交后获取的值，反而r.Form["channel"]符合我们的要求，因此在以后的开发中，针对复选框的获取值的方式要留意下。

下面我们添加如下代码，对获取的值进行验证  
先添加一个帮助函数

```go
// ValidateSliceIntersection 交集
func ValidateSliceIntersection(sourceSlice []string, targetSlice []string) []string {
    var slice3 []string
    for _, slice1 := range sourceSlice {
        for _, slice2 := range targetSlice {
            if slice1 == slice2 {
                slice3 = append(slice3, slice2)
            }
        }
    }
    return slice3
}
```

在方法中调用

```go
chennelSlice := []string{"news", "technology", "other"}
a := helpers.ValidateSliceIntersection(channel, chennelSlice)
if len(a) == 0 {
    fmt.Println("channel is empty")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
    return
}
```

重新编译并运行项目，如果什么频道选项什么也不选的话，提交后会在终端接收到如下输出

```bash
channels:  []
channel is empty
```

如果感兴趣也可以试试选择“新闻”，“科技”后再试试

今天就分享到这里，如果你有更好的方法请在下方留言或者加群交流

项目更新地址

```bash
https://github.com/durban89/wiki_blog.git
tag: 1.0.5
```
