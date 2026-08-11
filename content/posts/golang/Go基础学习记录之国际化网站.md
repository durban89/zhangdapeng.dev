---
title: "Go基础学习记录之国际化网站"
date: "2025-08-04 11:39:06"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-guo-ji-hua-wang-zhan"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之国际化网站/"
  - "/2025/08/04/Go基础学习记录之国际化网站.html"
  - "/Go基础学习记录之国际化网站/"
  - "/Go基础学习记录之国际化网站.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-guo-ji-hua-wang-zhan/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-guo-ji-hua-wang-zhan.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-guo-ji-hua-wang-zhan.html"
---
### **国际化网站**

上一篇文章[[Go基础学习记录之本地化资源](https://www.xiaorongmao.com/blog/112)]介绍了如何处理本地化资源，即使用区域设置配置文件。  
那么，如果我们需要处理多个本地化资源，如文本翻译，时间和日期，数字等，我们该怎么办？  
本篇文章将逐一解决这些问题。

### 管理多个区域设置包

在开发应用程序时，您需要做的第一件事就是决定是否要支持多种语言。  
如果您决定支持多种语言，则需要开发组织结构，以便将来添加更多语言。  
我们可以这样做的一种方法是将所有相关的语言环境文件放在一个config/locales目录或类似的东西中。  
我们假设你想要支持中文和英文。  
在这种情况下，您将把en.json和zh.json语言环境文件放入上述文件夹中。  
他们的内容可能如下所示：

// zh.json

```json
{
  "zh":
  {
    "submit": "提交",
    "create": "创建"
  }
}
```

// en.json

```json
{
  "en":
  {
    "submit": "Submit",
    "create": "Create"
  }
}
```

我们决定使用一些第三方Go软件包来帮助我们将我们的Web应用程序国际化。  
在go-i18n的情况下，我们首先必须注册config/locales目录来加载我们所有的语言环境文件：

```go
Tr := i18n.NewLocale()
Tr.LoadPath("config/locales")
```

这个包很容易使用。  
我们可以测试它的工作原理如下：

```go
fmt.Println(Tr.Translate("submit"))
//Output "submit"
Tr.SetLocale("zn")
fmt.Println(Tr.Translate("submit"))
//Outputs "递交"
```

### 自动加载本地包

我们刚刚描述了如何自动加载自定义语言包。  
事实上，go-i18n库预先加载了一堆默认格式信息，如时间和货币格式。  
用户可以覆盖和自定义这些默认配置以满足其需求。  
请考虑以下过程：

```go
//Load the default configuration files, which are placed below in `go-i18n/locales`

//File should be named zh.json, en-json, en-US.json etc., so we can continuously support more languages

func (il *IL) loadDefaultTranslations(dirPath string) error {
    dir, err := os.Open(dirPath)
    if err != nil {
        return err
    }
    defer dir.Close()

    names, err := dir.Readdirnames(-1)
    if err != nil {
        return err
    }

    for _, name := range names {
        fullPath := path.Join(dirPath, name)

        fi, err := os.Stat(fullPath)
        if err != nil {
            return err
        }

        if fi.IsDir() {
            if err := il.loadTranslations(fullPath); err != nil {
                return err
            }
        } else if locale := il.matchingLocaleFromFileName(name); locale != "" {
            file, err := os.Open(fullPath)
            if err != nil {
                return err
            }
            defer file.Close()

            if err := il.loadTranslation(file, locale); err != nil {
                return err
            }
        }
    }

    return nil
}
```

使用上面的代码加载我们的所有默认翻译，然后我们可以使用以下代码来选择和使用区域设置：

```go
fmt.Println(Tr.Time(time.Now()))
//Output: 2009年1月08日 星期四 20:37:58 CST

fmt.Println(Tr.Time(time.Now(),"long"))
//Output: 2009年1月08日

fmt.Println(Tr.Money(11.11))
//Output: ¥11.11
```

### 模板mapfunc

上面，我们介绍了一种管理和集成多种语言包的方法。  
我们实现的一些功能基于逻辑层，例如："Tr.Translate"，"Tr.Time"，"Tr.Money"等。  
在逻辑层中，我们可以使用这些函数（在提供所需参数之后）来应用您的翻译，在渲染时将结果直接输出到模板层。  
如果我们想直接在模板层中使用这些功能，我们该怎么办？  
如果您忘记了，我们在本书前面提到Go模板支持自定义模板功能。  
以下代码显示了mapfunc的实现方式：

1. 文字信息

下面是一个实现mapfunc的简单文本转换函数。  
它使用Tr.Translate执行适当的翻译：

```go
func I18nT(args ...interface{}) string {
    ok := false
    var s string
    if len(args) == 1 {
        s, ok = args[0].(string)
    }
    if !ok {
        s = fmt.Sprint(args...)
    }
    return Tr.Translate(s)
}
```

我们注册这样的函数：

```go
t.Funcs(template.FuncMap{"T": I18nT})
```

然后从您的模板中使用它：

```go
{{.V.Submit | T}}
```

2. 日期和时间

日期和时间调用Tr.Time函数执行其翻译。  
mapfunc实现如下：

```go
func I18nTimeDate(args ...interface{}) string {
    ok := false
    var s string
    if len(args) == 1 {
        s, ok = args[0].(string)
    }
    if !ok {
        s = fmt.Sprint(args...)
    }
    return Tr.Time(s)
}
```

像这样注册函数：

```go
t.Funcs(template.FuncMap{"TD": I18nTimeDate})
```

然后从您的模板中使用它：

3. 货币信息

货币使用Tr.Money功能转换货币。  
mapFunc实现如下：

```go
func I18nMoney(args ...interface{}) string {
    ok := false
    var s string
    if len(args) == 1 {
        s, ok = args[0].(string)
    }
    if !ok {
        s = fmt.Sprint(args...)
    }
    return Tr.Money(s)
}
```

像这样注册函数：

```go
t.Funcs(template.FuncMap{"M": I18nMoney})
```

然后从您的模板中使用它：

```go
{{.V.Money | M}}
```

### 小结

在本次分享中，我们学习了如何在Web应用程序中实现多语言包。  
我们通过自定义语言包看到，我们不仅可以轻松地将我们的应用程序国际化，还可以促进其他语言的添加（通过使用配置文件）。  
默认情况下，go-i18n软件包将提供一些常用的时间，货币等配置，使用起来非常方便。  
我们了解到，这些函数也可以使用映射函数直接从我们的模板中使用;  
每个翻译的字符串都可以直接传送到我们的模板。  
这使我们的Web应用程序能够以最小的努力适应多种语言。
