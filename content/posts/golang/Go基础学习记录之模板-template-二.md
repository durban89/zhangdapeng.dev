---
title: "Go基础学习记录之模板(template)[二]"
date: "2025-08-01 11:35:51"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之模板(template)[二]/"
  - "/2025/08/01/Go基础学习记录之模板(template)[二].html"
  - "/Go基础学习记录之模板(template)[二]/"
  - "/Go基础学习记录之模板(template)[二].html"
  - "/2025/08/01/Go基础学习记录之模板-template-二/"
  - "/2025/08/01/Go基础学习记录之模板-template-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-er/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-mu-ban-template-er.html"
---
## 条件语句

如果需要检查模板中的条件，可以像使用常规Go程序一样使用if-else语法。如果管道为空，则默认值if为false。以下示例显示如何在模板中使用if-else：

```go
package main

import (
    "os"
    "text/template"
)

func main() {
    tEmpty := template.New("template test")
    tEmpty = template.Must(tEmpty.Parse("Empty pipeline if demo: {{if ``}} will not be outputted. {{end}}\n"))
    tEmpty.Execute(os.Stdout, nil)

    tWithValue := template.New("template test")
    tWithValue = template.Must(tWithValue.Parse("Not empty pipeline if demo: {{if `anything`}} will be outputted. {{end}}\n"))
    tWithValue.Execute(os.Stdout, nil)

    tIfElse := template.New("template test")
    tIfElse = template.Must(tIfElse.Parse("if-else demo: {{if `anything`}} if part {{else}} else part.{{end}}\n"))
    tIfElse.Execute(os.Stdout, nil)
}
```

重新编译运行后结果如下

```bash
Empty pipeline if demo: 
Not empty pipeline if demo:  will be outputted. 
if-else demo:  if part
```

如您所见，在模板中使用if-else很容易。注意你不能在if中使用条件表达式，例如`.Mail =="[email protected]"`只接受布尔值。

## 管道"|"

Unix用户应该熟悉管道运算符，比如 `ls | grep "gowhich"` 。此命令过滤文件，仅显示包含单词gowhich的文件。我喜欢Go模板的一件事是它们支持管道。 `{{}}` 中的任何内容都可以是管道数据。我们上面使用的电子邮件可能会使我们的应用程序容易受到XSS攻击。我们如何使用管道来解决这个问题？

```html
{{. | html}}
```

我们可以使用此方法将电子邮件正文转义为HTML。它与编写Unix命令非常相似，并且可以方便地用于模板函数。

## 模板变量

有时我们需要在模板中使用局部变量。我们可以将它们与with，range和if关键字一起使用，它们的范围介于这些关键字和{{end}}之间。下面是一个声明全局变量的示例：

```html
$variable := pipeline
```

其他的示例如下

```html
{{with $x := "output" | printf "%q"}}{{$x}}{{end}}
{{with $x := "output"}}{{printf "%q" $x}}{{end}}
{{with $x := "output"}}{{$x | printf "%q"}}{{end}}
```

## 模板函数

Go使用fmt包来格式化模板中的输出，但有时我们需要做其他事情。例如，考虑以下场景：假设我们想在我们的电子邮件地址中用`at`替换`@`，就像将`[email protected]`变为`durban.zhangatgmail.com`一样。此时，我们必须编写一个自定义函数。每个模板函数都有一个唯一的名称，并与Go程序中的一个函数相关联，如下所示：

```go
type FuncMap map[string]interface{}
```

假设我们的Go程序中有一个与其EmailDealWith对应函数关联的emailDeal模板函数。我们可以使用以下代码来注册这个函数：

```go
t = t.Funcs(template.FuncMap{"emailDeal": EmailDealWith})
```

EmailDealWith的定义如下

```go
func EmailDealWith(args …interface{}) string
```

具体实例如下

```go
package main

import (
    "fmt"
    "html/template"
    "os"
    "strings"
)

type Friend struct {
    Fname string
}

type Person struct {
    UserName string
    Emails   []string
    Friends  []*Friend
}

func EmailDealWith(args ...interface{}) string {
    ok := false
    var s string
    if len(args) == 1 {
        s, ok = args[0].(string)
    }
    if !ok {
        s = fmt.Sprint(args...)
    }
    // find the @ symbol
    substrs := strings.Split(s, "@")
    if len(substrs) != 2 {
        return s
    }
    // replace the @ by " at "
    return (substrs[0] + " at " + substrs[1])
}

func main() {
    f1 := Friend{Fname: "durban1"}
    f2 := Friend{Fname: "durban2"}
    t := template.New("fieldname example")
    t = t.Funcs(template.FuncMap{"emailDeal": EmailDealWith})
    t, _ = t.Parse(`hello {{.UserName}}!
                {{range .Emails}}
                    an emails {{.|emailDeal}}
                {{end}}
                {{with .Friends}}
                {{range .}}
                    my friend name is {{.Fname}}
                {{end}}
                {{end}}
                `)
    p := Person{UserName: "Durban",
        Emails:  []string{"[email protected]", "[email protected]"},
        Friends: []*Friend{&f1, &f2}}
    t.Execute(os.Stdout, p)
}
```

编译后运行得到的结果如下

```bash
hello Durban!

                    an emails durban.zhang at gmail.com

                    an emails durban.zhang at 126.com

                    my friend name is durban1

                    my friend name is durban2
```

以下是内置模板函数的列表：

```go
var builtins = FuncMap{
    "and":      and,
    "call":     call,
    "html":     HTMLEscaper,
    "index":    index,
    "js":       JSEscaper,
    "len":      length,
    "not":      not,
    "or":       or,
    "print":    fmt.Sprint,
    "printf":   fmt.Sprintf,
    "println":  fmt.Sprintln,
    "urlquery": URLQueryEscaper,
}
```

今天的学习分享就到这里，继续关注。
