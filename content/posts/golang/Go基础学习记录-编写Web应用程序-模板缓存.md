---
title: "Go基础学习记录 - 编写Web应用程序 - 模板缓存"
date: "2025-08-01 09:21:45"
slug: "go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-mu-ban-huan-cun"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-模板缓存/"
  - "/2025/08/01/Go基础学习记录-编写Web应用程序-模板缓存.html"
  - "/Go基础学习记录-编写Web应用程序-模板缓存/"
  - "/Go基础学习记录-编写Web应用程序-模板缓存.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-mu-ban-huan-cun/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-mu-ban-huan-cun.html"
  - "/go-ji-chu-xue-xi-ji-lu-bian-xie-web-ying-yong-cheng-xu-mu-ban-huan-cun.html"
---
### **模板缓存**

renderTemplate函数中的代码效率是比较低的，每次呈现页面时，renderTemplate都会调用ParseFiles。 更好的处理方法是在程序初始化时调用ParseFiles一次，将所有模板解析为单个\* Template。 然后我们可以使用ExecuteTemplate方法呈现特定模板。

首先，我们创建一个名为templates的全局变量，并使用ParseFiles对其进行初始化。

```go
var templates = template.Must(template.ParseFiles("template/edit.html", "template/view.html"))
```

函数template.Must是一个方便的包装器，当传递非零错误值时会发生异常，否则返回\*模板不变。  
如果模板无法加载，唯一明智的做法就是退出程序。  
ParseFiles函数接受任意数量的用于标识模板文件的字符串参数，并将这些文件解析为以基本文件名命名的模板。  
如果我们要为程序添加更多模板，我们会将它们的名称添加到ParseFiles调用的参数中。  
然后我们修改renderTemplate函数以使用适当模板的名称调用templates.ExecuteTemplate方法：

```go
func renderTemplate(w http.ResponseWriter, templateName string, p *Page) {
    fmt.Println(templates)
    err := templates.ExecuteTemplate(w, templateName+".html", p)

    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
}
```

请注意，模板名称是模板文件名，因此我们必须将".html"附加到tmpl参数。  
尤其注意的是，templates在初始化的时候我是将模板放在了一个文件夹下面，但是在renderTemplate中使用的时候只要传递文件名就好了，对应的路径都不需要拼接。
