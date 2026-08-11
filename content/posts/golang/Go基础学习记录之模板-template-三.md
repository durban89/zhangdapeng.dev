---
title: "Go基础学习记录之模板(template)[三]"
date: "2025-08-01 11:35:54"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-san"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之模板(template)[三]/"
  - "/2025/08/01/Go基础学习记录之模板(template)[三].html"
  - "/Go基础学习记录之模板(template)[三]/"
  - "/Go基础学习记录之模板(template)[三].html"
  - "/2025/08/01/Go基础学习记录之模板-template-三/"
  - "/2025/08/01/Go基础学习记录之模板-template-三.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-san/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-san.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-san.html"
---
## Must

模板包有一个名为Must的函数，用于验证模板，如大括号，注释和变量的匹配。我们来看看Must的一个例子：

```go
package main

import (
    "fmt"
    "text/template"
)

func main() {
    t1 := template.New("first")
    template.Must(t1.Parse(" some static text /* and a comment */"))
    fmt.Println("第一个解析OK")

	t2 := template.New("second")
    template.Must(t2.Parse("some static text {{ .Name }}"))
    fmt.Println("第二个解析OK")

    fmt.Println("下一个解析失败")
    t3 := template.New("check parse error with Must")
    template.Must(t3.Parse(" some static text {{ .Name }"))
}
```

编译后运行得到如下结果

```bash
第一个解析OK
第二个解析OK
下一个解析失败
panic: template: check parse error with Must:1: unexpected "}" in operand
```

## 模板嵌套

就像在大多数Web应用程序中一样，模板的某些部分可以在其他模板中重用，例如博客的页眉和页脚。我们可以将header，content和footer声明为子模板，并使用以下语法在Go中声明它们：

```go
{{define "sub-template"}}content{{end}}
```

使用以下语法调用子模板：

```go
{{template "sub-template"}}
```

下面是一个完整的例子，假设我们有以下三个文件：header.html、content.html和footer.html在文件夹模板中，我们将读取文件夹并将文件名存储在字符串数组中，然后我们将使用解析文件。

main模板：

```html
{% raw %}
//header.html
{{define "header"}}
<html>
<head>
    <title>Something here</title>
</head>
<body>
{{end}}

//content.html
{{define "content"}}
{{template "header"}}
<h1>Nested here</h1>
<ul>
    <li>Nested usag</li>
    <li>Call template</li>
</ul>
{{template "footer"}}
{{end}}

//footer.html
{{define "footer"}}
</body>
</html>
{{end}}

// 使用子模板时，请确保已解析每个子模板文件
// 否则编译器在读取{{template "header"}}时不会理解要替换的内容

{% endraw %}
```

代码如下

```go
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"text/template"
	"strings"
)

var templates *template.Template

func main() {
	var allFiles []string
	files, err := ioutil.ReadDir("./templates")
	if err != nil {
		fmt.Println(err)
	}
	for _, file := range files {
		filename := file.Name()
		if strings.HasSuffix(filename, ".html") {
			allFiles = append(allFiles, "./templates/"+filename)
		}
	}

	templates, err = template.ParseFiles(allFiles...) // parses all .html files in the 'templates' folder

	if err != nil {
		fmt.Println(err)
	}

	s1 := templates.Lookup("header.html")
	s1.ExecuteTemplate(os.Stdout, "header", nil)
	fmt.Println()
	s2 := templates.Lookup("content.html")
	s2.ExecuteTemplate(os.Stdout, "content", nil)
	fmt.Println()
	s3 := templates.Lookup("footer.html")
	s3.ExecuteTemplate(os.Stdout, "footer", nil)
	fmt.Println()
	s3.Execute(os.Stdout, nil)
}
```

在这里我们可以看到template.ParseFiles将所有嵌套模板解析为缓存，并且{{define}}定义的每个模板都是相互独立的。它们保存在类似于map的地方，其中模板名称是键，值是模板主体。然后我们可以使用ExecuteTemplate来执行相应的子模板，这样页眉和页脚就是独立的，内容包含它们。请注意，如果我们尝试执行s1.Execute，则不会输出任何内容，因为没有可用的默认子模板。

***在看下下面这个例子***

```go
// 视图渲染
t, err := template.ParseFiles(append(config.CommonTemplatesFiles, config.TemplateDir+"/update.html")...)

if err != nil {
	http.Error(w, err.Error(), http.StatusInternalServerError)
	return
}

err = t.ExecuteTemplate(w, "update.html", struct {
	Autokid int64
	Title   string
	Content string
}{
	Autokid: autokid,
	Title:   title,
	Content: content.String,
})

if err != nil {
	http.Error(w, err.Error(), http.StatusInternalServerError)
	return
}
```

这个是实战中的例子，是我在开发的一个web框架中使用到的

```go
t, err := template.ParseFiles(append(config.CommonTemplatesFiles, config.TemplateDir+"/update.html")...)
```

这段代码表示加载了一个页面需要的子模板，我将共用的模板放在了config.CommonTemplatesFiles这个变量中，这个时候在update.html中需要用的子模板就会被加载进来。

```go
t.ExecuteTemplate(w, "update.html", nil)
```

这段代码是用来指定默认的模板的，不然不会输入任何内容，这里在使用的时候切记。

当您不想使用{{define}}时，您只需创建一个带有子模板名称的文本文件，例如\_head.html是一个子模板，您将在项目中使用该模板然后创建此模板文件夹在templates文件夹中，并使用普通语法。基本上创建了查找缓存，以便每次提交请求时都不会读取文件，因为如果这样做，那么您将浪费大量资源来读取除非重写代码库之外不会更改的文件，在每个HTTP GET请求期间解析模板文件没有意义，因此该技术用于我们解析文件一次然后在缓存上执行Lookup()以在我们需要它来显示数据时执行模板。

一组中的模板彼此了解，但您必须为每一组解析它们。

有时你想要模板化上下文，例如你有一个\_head.html，你可能有一个标题，你必须根据你要加载的数据来填充这个标题，例如对于待办事项列表管理器你可以有三个待定的类别`pending`, `completed`, `deleted`。对于这个假设你有一个像这样的if条件语句

```html
<title>{{if eq .Navigation "pending"}} Tasks
    {{ else if eq .Navigation "completed"}}Completed
    {{ else if eq .Navigation "deleted"}}Deleted
    {{ else if eq .Navigation "edit"}} Edit
    {{end}}
</title>
```

注意：

Go模板遵循波兰表示法，同时执行比较，您首先给操作员，比较值和要比较的值。其他部分非常简单

通常我们使用`{{range}}`运算符循环遍历我们传递给模板的上下文变量，同时执行如下：

```go
// present in views package
context := db.GetTasks("pending") // true when you want non deleted notes
homeTemplate.Execute(w, context)
```

我们从数据库中获取上下文对象作为struct对象，假如定义如下

```go
// Task is the struct used to identify tasks
type Task struct {
       Id      int
    Title   string
    Content string
    Created string
}
// Context is the struct passed to templates
type Context struct {
    Tasks      []Task
    Navigation string
    Search     string
    Message    string
}

// present in database package
var task []types.Task
var context types.Context
context = types.Context{Tasks: task, Navigation: status}

// This line is in the database package where the context is returned back to the view.
```

我们在模板中使用任务数组和导航，我们看到了如何在模板中使用导航，我们将看到我们将如何在模板中使用实际任务数组。

在`{{if .Tasks}}`中，我们首先检查在执行时传递给模板的上下文对象的Tasks字段是否为空。如果它不是空的，那么我们将通过该数组来填充Task的标题和内容。以下示例在循环模板中的数组时非常重要，我们从Range运算符开始，然后我们可以将该结构的任何成员作为`{{.Name}}`，我的任务结构有一个标题和一个内容，（请注意大写字母T和C，它们是导出的名称，除非您想将它们设为私有，否则它们需要大写）。

```html
{{ range .Tasks }}
    {{ .Title }}
    {{ .Content }}
{{ end }}
```

此代码块将打印Task数组的每个标题和内容。以下是github.com/thewhitetulip/Tasks home.html模板的完整示例。

```html
<div class="timeline">
{{ if .Tasks}} {{range .Tasks}}
<div class="note">
    <p class="noteHeading">{{.Title}}</p>
    <hr>
    <p class="noteContent">{{.Content}}</p>
    </ul>
    </span>
</div>
{{end}} {{else}}
<div class="note">
    <p class="noteHeading">No Tasks here</p>
    <p class="notefooter">
    Create new task<button class="floating-action-icon-add" > here </button> </p>
</div>
{{end}}
```

模板函数和嵌套模板中打印数据的技术将动态数据与模板相结合。通过了解模板，我们可以得出结论，讨论MVC架构的V（View）部分。在接下来的学习分享中，将分享MVC的M（模型）和C（控制器）方面。
