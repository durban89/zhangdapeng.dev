---
title: "Go基础学习记录之本地化资源"
date: "2025-08-04 11:39:03"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-ben-di-hua-zi-yuan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之本地化资源/"
  - "/2025/08/04/Go基础学习记录之本地化资源.html"
  - "/Go基础学习记录之本地化资源/"
  - "/Go基础学习记录之本地化资源.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-ben-di-hua-zi-yuan/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-ben-di-hua-zi-yuan.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-ben-di-hua-zi-yuan.html"
---
### 本地化资源

上一篇文章[[Go基础学习记录之国际化和本地化(一)](https://www.xiaorongmao.com/blog/111)]介绍了如何设置区域设置。  
在设置了语言环境之后，我们需要解决存储与特定语言环境相对应的信息的问题。  
此信息可包括：文本内容，时间和日期，货币值，图片，特定文件和其他视图资源。  
在Go中，所有这些上下文信息都以JSON格式存储在我们的后端，当特定区域的用户访问我们的网站时，可以调用并注入我们的视图。  
例如，英文和中文内容将分别存储在en.json和zh-CN.json文件中。

### 本地化的文本内容

纯文本是在Web应用程序中表示信息的最常用方式，大部分本地化内容可能采用此形式。  
目标是提供与区域表达一致的文本内容，并为您网站的外国用户感到自然。  
一种解决方案是创建区域设置，本地语言字符串及其本地对应项的嵌套映射。  
当客户端请求包含某些文本内容的页面时，我们首先检查他们所需的语言环境，然后从相应的地图中检索相应的字符串。  
以下代码段是此过程的一个简单示例：

```go
package main

import "fmt"

var locales map[string]map[string]string

func main() {
    locales = make(map[string]map[string]string, 2)
    en := make(map[string]string, 10)
    en["pea"] = "pea"
    en["bean"] = "bean"
    locales["en"] = en
    cn := make(map[string]string, 10)
    cn["pea"] = "豌豆"
    cn["bean"] = "毛豆"
    locales["zh-CN"] = cn
    lang := "zh-CN"
    fmt.Println(msg(lang, "pea"))
    fmt.Println(msg(lang, "bean"))
}

func msg(locale, key string) string {
    if v, ok := locales[locale]; ok {
        if v2, ok := v[key]; ok {
            return v2
        }
    }
    return ""
}
```

上面的示例为不同的区域设置（在本例中为中文和英文区域设置）设置翻译字符串的映射。  
我们将cn翻译映射到相同的英语键值，以便我们可以用中文重建我们的英文文本信息。  
如果我们想将文本切换到我们可能实现的任何其他语言环境，那么设置一个lang变量就很简单了。

简单的键值替换有时可能不足以满足我们的需求。  
例如，如果我们有一个短语，例如“我30岁”，其中30是变量，我们将如何本地化它？  
在这些情况下，我们可以结合使用fmt.Printf函数来实现所需的结果：

```go
en["how old"] = "I am %d years old"
cn["how old"] = "我今年%d岁了"

fmt.Printf(msg(lang, "how old"), 30)
```

上面的示例代码仅用于演示;  
实际的语言环境数据通常以JSON格式存储在我们的数据库中，允许我们执行一个简单的json.Unmarshal来使用我们的字符串翻译映射语言环境。

### 本地化的日期和时间

由于我们的时区惯例，世界某个地区的时间可能与另一个地区的时间不同。  
类似地，表示时间的方式也可以从区域设置到区域设置。  
例如，一个中国环境可能会读到2012年10月24日星期三23时11分13秒CST，而英文版可能是：周三10月24日23:11:13 CST 2012.不仅语言有变化，  
但格式也有差异。  
因此，在本地化日期和时间时，我们需要解决以下两点：

1. 时区  
2. 格式化问题

`$GOROOT/lib/time/package/timeinfo.zip`目录包含与时区定义相对应的语言环境。  
为了获得与用户当前语言环境相对应的时间，我们首先应该使用`time.LoadLocation(name string)`来获取与我们的语言环境对应的Location对象，并传入表示Asia/Shanghai或America/Chicago等语言环境的字符串。  
然后，我们可以将此Location对象与Time对象（通过调用time.Now获得）一起使用，以使用Time对象的In方法获取最终时间。  
下面详细介绍了这个过程（这个例子使用了上面例子中的一些变量）：

```go
en["time_zone"] = "America/Chicago"
cn["time_zone"] = "Asia/Shanghai"

loc, _ := time.LoadLocation(msg(lang, "time_zone"))
t := time.Now()
t = t.In(loc)
fmt.Println(t.Format(time.RFC3339))
```

我们可以用类似的方式处理文本格式以解决我们的时间格式问题：

```go
en["date_format"]="%Y-%m-%d %H:%M:%S"
cn["date_format"]="%Y年%m月%d日 %H时%M分%S秒"

fmt.Println(date(msg(lang,"date_format"),t))

func date(fomat string, t time.Time) string{
    year, month, day = t.Date()
    hour, min, sec = t.Clock()
    //Parsing the corresponding %Y%m%d%H%M%S and then returning the information
    //%Y replaced by 2012
    //%m replaced by 10
    //%d replaced by 24
}
```

### 本地化货币价值

显然，货币也因地区而异。  
我们可以像处理日期那样对待它：

```go
en["money"] ="USD %d"
cn["money"] ="￥%d元"

fmt.Println(date(msg(lang,"date_format"),100))

func money_format(fomat string, money int64) string{
    return fmt.Sprintf(fomat, money)
}
```

### 视图和资源的本地化

我们可以使用不同的图像，css，js和其他静态资源来提供自定义视图，具体取决于当前的区域设置。  
实现此目的的一种方法是将这些文件组织到各自的区域设置中。  
这是一个例子：

```bash
views
|--en  //English Templates
    |--images     //store picture information
    |--js         //JS files 
    |--css        //CSS files
    index.tpl     //User Home
    login.tpl     //Log Home
|--zh-CN //Chinese Templates
    |--images
    |--js
    |--css
    index.tpl
    login.tpl
```

使用此目录结构，我们可以像这样呈现特定于语言环境的视图：

```go
s1, _ := template.ParseFiles("views" + lang + "index.tpl")
VV.Lang = lang
s1.Execute(os.Stdout, VV)
```

index.tpl文件中引用的资源可以按如下方式处理：

```html
// js file
<script type="text/javascript" src="views/{{.VV.Lang}}/js/jquery/jquery-1.8.0.min.js"></script>
// css file
<link href="views/{{.VV.Lang}}/css/bootstrap-responsive.min.css" rel="stylesheet">
// Picture files
<img src="views/{{.VV.Lang}}/images/btn.png">
```

通过动态视图和我们对资源进行本地化的方式，我们将能够轻松添加更多区域设置。

### 小结

本篇分享介绍如何使用和存储本地资源。  
我们了解到我们可以使用转换函数和字符串插值，并且看到映射可以是存储特定于语言环境的数据的有效方法。  
对于后者，我们可以在需要时简单地提取相应的区域设置信息 - 如果它是我们期望的文本内容，我们的映射翻译和习语可以直接传送到输出。  
如果它像时间或货币那样更复杂，我们只需使用fmt.Printf函数预先格式化它。  
本地化我们的视图和资源是最简单的情况，只需将我们的文件组织到各自的语言环境中，然后从它们的语言环境相对路径引用它们。
