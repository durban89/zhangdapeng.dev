---
title: "Go基础学习记录 - 编写Web应用程序 - Web开发输入验证(三)"
date: "2025-08-01 09:22:14"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-san"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(三)/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证(三).html"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(三)/"
  - "/Go基础学习记录-编写Web应用程序-Web开发输入验证(三).html"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-三/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-Web开发输入验证-三.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-san/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-web-kai-fa-shu-ru-yan-zheng-san.html"
---
继续前面几篇文章的分享，本次分享下 -- 输入验证

为了保持项目的可学习性，我这里将之前分享的代码积累了下，放在github上，想要尽快入手学习的，可以直接clone我的代码，写代码不上手，都等于白搭，光看的话，对于我来说，我是不行的，没办法学会。

项目地址

```bash
https://github.com/durban89/wiki_blog
tag: 1.0.3
```

有些同学可能看不懂，怎么就只给了这些，完全不懂呀。我把使用的命令打出来，照着操作，就应该可以解决了

```bash
git clone https://github.com/durban89/wiki_blog /local/path
cd /local/path
git fetch origin
git checkout 1.0.3
```

这些我觉得 够清晰了。OK！

继续分享的输入验证的逻辑。

Web开发中最重要的原则之一是您不能信任客户端用户表单中的任何内容。  
您必须在使用之前验证所有传入数据。  
许多网站都受到这个问题的影响，这个问题既简单又至关重要。  
有两种方法可以验证常用的表单数据。  
第一个是前端的JavaScript验证，第二个是后端的服务器验证。  
本次继续上次分享，分享Web开发中的服务器端验证第三部分

## 验证整理

先将上次的验证分享进行下整理，上次验证主要包括中文、英文和邮箱，我们将这些小的功能整理到一个独立的文件中，方便我们后面调用  
创建helpers/strings.go，整理的后的代码如下，当然如果您有更好的建议或者方式也可以分享一下。

```go
package helpers

import (
    "regexp"
)

// ValidateInt 验证整数
func ValidateInt(str string) bool {
    if m, _ := regexp.MatchString("^[0-9]+$", str); m {
        return true
    }
    return false
}

// ValidateEmail 验证邮箱
func ValidateEmail(str string) bool {
    if m, _ := regexp.MatchString(`^([\w\.\_]{2,10})@(\w{1,}).([a-z]{2,4})$`, str); m {
        return true
    }

    return false
}

// ValidateChinese 验证中文
func ValidateChinese(str string) bool {
    if m, _ := regexp.MatchString("^[\\x{4e00}-\\x{9fa5}]+$", str); m {
        return true
    }

    return false
}

// ValidateEnglish 验证英文
func ValidateEnglish(str string) bool {
    if m, _ := regexp.MatchString("^[a-zA-Z]+$", str); m {
        return true
    }

    return false
}
```

## 下拉列表

假设我们需要一个来自下拉列表的项目，里面是文章的分类内容，但我们得到的是黑客捏造的值。我们如何防止这种情况发生？  
假设我们有以下 `<select>`：

```html
<select name="category">
  <option value="php">PHP</option>
  <option value="java">Python</option>
  <option value="golang">Golang</option>
</select>
```

这里我修改 edit.html 文件  
增加后部分内容如下

```html
<div class="form-group">
  <label for="category">分类</label>
  <select class="form-control" name="category">
    <option value="php">PHP</option>
    <option value="java">Python</option>
    <option value="golang">Golang</option>
  </select>
</div>
```

服务端修改ArticleSave方法，添加如下代码

```go
category := r.FormValue("category")
```

和

```go
fmt.Println("category ", category)
```

重新编译代码并重启项目，分类中我们选择Golang后提交，会在后台终端输入类似如下的输出

```bash
category  golang
```

如果仅仅是接收到了参数，如果黑客不是通过web端，而是模拟web提交数据的话，我们就会收到意想不到的结果，下面对这个输入进行下验证  
在helpers/strings.go中加入验证函数

```go
// ValidateInArray 元素是否在指定的数组中
func ValidateInArray(slice []string, str string) bool {
    for _, v := range slice {
        if v == str {
            return true
        }
    }

    return false
}
```

并在ArticleSave调用，进行验证

```go
slice := []string{"php", "java", "golang"}
if !helpers.ValidateInArray(slice, category) {
    fmt.Println("category not in slice")
    http.Redirect(w, r, "/view/"+title, http.StatusFound)
    return
}
```

为了测试我们在edit.html中加入一个不在"php", "java", "golang"中的元素"html"

重新编译代码并重启项目，分类中我们选择Html后提交，会在后台终端输入类似如下的输出

```bash
category not in slice
```

今天就分享到这里，如果你有更好的方法请在下方留言或者加群交流

项目更新地址

```go
https://github.com/durban89/wiki_blog.git
tag: 1.0.4
```
