---
title: "Go基础学习记录之模板(template)[一]"
date: "2025-08-01 11:35:47"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之模板(template)[一]/"
  - "/2025/08/01/Go基础学习记录之模板(template)[一].html"
  - "/Go基础学习记录之模板(template)[一]/"
  - "/Go基础学习记录之模板(template)[一].html"
  - "/2025/08/01/Go基础学习记录之模板-template-一/"
  - "/2025/08/01/Go基础学习记录之模板-template-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-yi.html"
---
## **模板(一)**

## 什么是模板

希望您了解MVC(模型，视图，控制器)设计模型，其中模型处理数据，视图显示结果，最后，控制器处理用户请求。  
对于视图，许多动态语言通过在静态HTML文件中编写代码来生成数据。  
例如，JSP是通过插入`<%=...=>`，PHP是通过等插入`<php?...?>`来实现的。

以下演示了模板机制

```bash
Hello, my name is {NAME}  ----|
                              |------Hello, my name is Mary
NAME = "Mary"             ----|
```

Web应用程序响应客户端的大多数内容都是静态的，动态部分通常非常小。  
例如，如果您需要显示访问过页面的列表用户，则只有用户名是动态的。  
列表的样式保持不变。  
如您所见，模板对于重用静态内容非常有用。

### 在Go中使用模板

在Go中，我们有模板包来帮助处理模板。  
我们可以使用Parse，ParseFile和Execute等函数从纯文本或文件加载模板，然后评估动态部分

```go
func handler(w http.ResponseWriter, r *http.Request) {
    t := template.New("some template") // 创建一个模板
    t, _ = t.ParseFiles("templates/welcome.html", nil)  // 解析模板文件
    user := GetUser() // 获取当前用户信息
    t.Execute(w, user)  // 将模板和变量整合
}
```

正如您所看到的，它在Go中的模板中使用，加载和呈现数据非常容易，就像在其他编程语言中一样。  
为方便起见，我们将在示例中使用以下规则：

1. 使用Parse替换ParseFiles，因为Parse可以直接从字符串测试内容，因此我们不需要任何额外的文件。  
2. 对每个示例使用main，不要使用handler。  
3. 使用os.Stdout替换http.ResponseWriter，因为os.Stdout也实现了io.Writer接口。

### 将数据插入模板

我们刚刚向您展示了如何解析和呈现模板。  
下面让我们更进一步，将数据呈现给我们的模板。  
每个模板都是Go中的一个对象，那么我们如何将字段插入到模板中？

### *字段*

在Go中，您打算在模板中呈现的每个字段都应放在`{{}}`内。  
`{{.}}`是当前对象的简写，类似于Java或C++。  
如果要访问当前对象的字段，则应使用`{{.FieldName}}`。  
请注意，只能在模板中访问导出的字段。  
这是一个例子：

```go
package main

import (
    "html/template"
    "os"
)

type Person struct {
    UserName string
}

func main() {
    t := template.New("fieldname example")
    t, _ = t.Parse("hello {{.UserName}}!")
    p := Person{UserName: "Durban"}
    t.Execute(os.Stdout, p)
}
```

运行后得到的结果如下

```bash
hello Durban!
```

上面的例子正确地输出了hello Durban，但如果我们稍微修改一下我的结构，会出现以下错误：

```go
type Person struct {
    UserName string
    email    string  // 字段没有被导出
}

t, _ = t.Parse("hello {{.UserName}}! {{.email}}")
```

这部分代码将不会被编译，因为我们尝试访问尚未导出的字段。  
但是，如果我们尝试使用不存在的字段，Go只会输出一个空字符串而不是错误。

如果在模板中打印`{{.}}`，Go会输出此对象的格式化字符串，并在封面下调用fmt。

### *嵌套字段*

我们现在知道如何输出一个字段。  
如果该字段是一个对象，它也有自己的字段怎么办？  
我们如何在一个循环中打印它们？  
我们可以使用`{{with …}}…{{end}}`和`{{range …}}{{end}}`来达到这个目的。

`{{range}}`就像Go中的范围一样。  
`{{with}}`允许您编写相同的对象名称并使用```.```作为它的简写(类似于在VB中)。

比如下面的这个例子

```go
package main

import (
    "html/template"
    "os"
)

type Friend struct {
    Fname string
}

type Person struct {
    UserName string
    Emails   []string
    Friends  []*Friend
}

func main() {
    f1 := Friend{Fname: "durban1"}
    f2 := Friend{Fname: "durban2"}
    t := template.New("fieldname example")
    t, _ = t.Parse(`hello {{.UserName}}!
            {{range .Emails}}
                an email {{.}}
            {{end}}
            {{with .Friends}}
            {{range .}}
                my friend name is {{.Fname}}
            {{end}}
            {{end}}
            `)
    p := Person{UserName: "Durban",
        Emails:  []string{"[email protected]", "durban,[email protected]"},
        Friends: []*Friend{&f1, &f2}}
    t.Execute(os.Stdout, p)
}
```

编译运行后得到的结果类似如下

```bash
hello Durban!

                an email [email protected]

                an email durban,[email protected]

                my friend name is durban1

                my friend name is durban2
```

今天分享就到这里，请继续关注后续分享
