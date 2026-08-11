---
title: "Go基础学习记录之错误处理"
date: "2025-08-04 11:39:09"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-cuo-wu-chu-li"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之错误处理/"
  - "/2025/08/04/Go基础学习记录之错误处理.html"
  - "/Go基础学习记录之错误处理/"
  - "/Go基础学习记录之错误处理.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-cuo-wu-chu-li/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-cuo-wu-chu-li.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-cuo-wu-chu-li.html"
---
## 错误处理

Go的主要设计考虑因素植根于以下思想：简单，清晰，简洁的语法（类似于C）和明确且不包含任何隐藏或意外事物的语句。 Go的错误处理方案以其实现的方式反映了所有这些原则。 如果您熟悉C语言，您将知道返回-1或NULL值以指示发生错误是很常见的。 但是，不熟悉C的API的用户将无法准确知道这些返回值的含义。 在C中，值0表示失败是否成功并不明确。 另一方面，Go明确定义了一个名为error的类型，其唯一目的是表达错误。 每当函数返回时，我们检查错误变量是否为nil以确定操作是否成功。 例如，os.Open函数失败，它将返回一个非零错误变量。

```go
func Open(name string) (file * File, err error)
```

这是我们如何在os.Open中处理错误的一个例子。 首先，我们尝试打开一个文件。 当函数返回时，我们通过将错误返回值与nil进行比较来检查它是否成功，如果它是非零值，则调用log.Fatal输出错误消息：

```go
f, err := os.Open("filename.ext")
if err != nil {
  log.Fatal(err)
}
```

与os.Open函数类似，Go的标准包中的函数都返回错误变量以便于错误处理。 本节将详细介绍错误类型的设计，并讨论如何正确处理Web应用程序中的错误。

### 错误类型

error是具有以下定义的接口类型：

```go
type error interface {
    Error() string
}
```

error是内置接口类型。 我们可以在下面的内置包中找到它的定义。 我们还有很多内部包在名为errorString的私有结构中使用错误，它实现了错误接口：

```go
// errorString is a trivial implementation of error.
type errorString struct {
    s string
}

func (e *errorString) Error() string {
    return e.s
}
```

您可以通过errors.New将常规字符串转换为errorString，以获得满足错误接口的对象。 其内部实施如下:

```go
// New returns an error that formats as the given text.
func New(text string) error {
    return &errorString{text}
}
```

以下示例演示了如何使用errors.New：

```go
func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return 0, errors.New("math: square root of negative number")
    }
    // implementation
}
```

在以下示例中，我们将负数传递给Sqrt函数。 检查err变量，我们使用简单的nil比较检查错误对象是否为非零。 比较的结果是正确的，因此调用fmt.Println（fmt包在处理错误调用时调用错误方法）以输出错误。

```go
f, err := Sqrt(-1)
if err != nil {
    fmt.Println(err)
}
```

### 自定义错误

通过以上描述，我们知道go错误是一个接口。 通过定义实现此接口的结构，我们可以实现它们的错误定义。 以下是JSON包中的示例：

```go
type SyntaxError struct {
    msg string // error description
    Offset int64 // where the error occurred
}

func (e * SyntaxError) Error() string {return e.msg}
```

发生语法错误时，不会在运行时打印错误的偏移字段，但使用类型断言错误类型，您可以打印所需的错误消息：

```go
if err := dec.Decode(&val); err != nil {
    if serr, ok := err.(*json.SyntaxError); ok {
        line, col := findLine(f, serr.Offset)
        return fmt.Errorf("%s:%d:%d: %v", f.Name(), line, col, err)
    }
    return err
}
```

应该注意，当函数返回自定义错误时，返回值设置为推荐的错误类型而不是自定义错误类型。 注意不要预先声明自定义错误类型的变量。 例如：

```go
func Decode() *SyntaxError {
    // error, which may lead to the caller's err != nil comparison to always be true.
    var err * SyntaxError // pre-declare error variable
    if an error condition {
        err = &SyntaxError{}
    }
    return err // error, err always equal non-nil, causes caller's err != nil comparison to always be true
}
```

有关详细说明，请参阅http://golang.org/doc/faq#nil\_error

上面的示例演示了如何实现简单的自定义错误类型。 但是，如果我们需要更复杂的错误处理呢？ 在这种情况下，我们必须参考net包方法：

```go
package net

type Error interface {
    error
    Timeout() bool   // Is the error a timeout?
    Temporary() bool // Is the error temporary?
}
```

使用类型断言，我们可以检查我们的错误是否为net.Error类型，如以下示例所示。 这允许我们改进我们的错误处理 - 如果网络上发生临时错误，它将休眠1秒，然后重试该操作。

```go
if nerr, ok := err.(net.Error); ok && nerr.Temporary() {
    time.Sleep(1e9)
    continue
}

if err != nil {
    log.Fatal(err)
}
```

### 错误处理

Go处理错误并以类似C的方式检查函数的返回值，这与大多数其他主要语言的行为不同。 这使得代码更加明确和可预测，但也更加冗长。 为了减少错误处理代码的冗余，我们可以使用抽象错误处理函数，它们允许我们实现类似的错误处理行为：

```go
func init() {
    http.HandleFunc("/view", viewRecord)
}

func viewRecord(w http.ResponseWriter, r *http.Request) {
    c := appengine.NewContext(r)
    key := datastore.NewKey(c, "Record", r.FormValue("id"), 0, nil)
    record := new(Record)
    if err := datastore.Get(c, key, record); err != nil {
        http.Error(w, err.Error(), 500)
        return
    }
    if err := viewTemplate.Execute(w, record); err != nil {
        http.Error(w, err.Error(), 500)
    }
}
```

上面的示例演示了数据访问和模板调用如何检测到错误。 发生错误时，调用统一处理程序http.Error会向客户端返回500错误代码，并显示相应的错误数据。 但是当进行越来越多的HandleFunc调用时，错误处理逻辑代码将会增加。 我们可以自定义路由器以减少代码（有关更多详细信息，请参阅HTTP的文章）。

```go
type appHandler func(http.ResponseWriter, *http.Request) error

func (fn appHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    if err := fn(w, r); err != nil {
        http.Error(w, err.Error(), 500)
    }
}
```

上面我们定义了一个自定义路由器。 然后我们可以照常注册我们的处理程序：

```go
func init() {
    http.Handle("/view", appHandler(viewRecord))
}
```

然后可以通过以下代码处理/ view处理程序; 它比我们原来的实现简单得多不是吗？

```go
func viewRecord(w http.ResponseWriter, r *http.Request) error {
    c := appengine.NewContext(r)
    key := datastore.NewKey(c, "Record", r.FormValue("id"), 0, nil)
    record := new(Record)
    if err := datastore.Get(c, key, record); err != nil {
        return err
    }
    return viewTemplate.Execute(w, record)
}
```

除了打印出相应的错误代码之外，上面的错误处理程序示例将在发生任何错误时向用户返回500内部错误代码。 实际上，我们可以自定义返回的错误类型，以输出更加开发人员友好的错误消息，其中包含对调试有用的信息，如下所示：

```go
type appError struct {
    Error   error
    Message string
    Code    int
}
```

我们的自定义路由器可以相应更改：

```go
type appHandler func(http.ResponseWriter, *http.Request) *appError

func (fn appHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    if e := fn(w, r); e != nil { // e is *appError, not os.Error.
        c := appengine.NewContext(r)
        c.Errorf("%v", e.Error)
        http.Error(w, e.Message, e.Code)
    }
}
```

在我们完成修改自定义错误后，我们的逻辑可以更改如下：

```go
func viewRecord(w http.ResponseWriter, r *http.Request) *appError {
    c := appengine.NewContext(r)
    key := datastore.NewKey(c, "Record", r.FormValue("id"), 0, nil)
    record := new(Record)
    if err := datastore.Get(c, key, record); err != nil {
        return &appError{err, "Record not found", 404}
    }
    if err := viewTemplate.Execute(w, record); err != nil {
        return &appError{err, "Can't display record", 500}
    }
    return nil
}
```

如上所示，我们可以在视图中返回不同的错误代码和错误消息，具体取决于具体情况。 虽然我们的代码版本与前一版本的功能类似，但它更明确，并且其错误消息提示更易于理解。 所有这些因素都可以帮助您的应用程序在复杂性增加时更具可扩展性。

## 小结

容错是任何编程语言的一个非常重要的方面。 在Go中，它是通过错误处理实现的。 虽然Error只是一个接口，但它的实现方式可能有很多变化，我们可以根据具体情况自定义它。 通过介绍这些各种错误处理概念，我们希望您已经了解了如何在您自己的Web应用程序中实现更好的错误处理方案。
