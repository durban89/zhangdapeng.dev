---
title: "Go基础学习记录之部署和维护(二)"
date: "2025-08-04 18:07:19"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之部署和维护(二)/"
  - "/2025/08/04/Go基础学习记录之部署和维护(二).html"
  - "/Go基础学习记录之部署和维护(二)/"
  - "/Go基础学习记录之部署和维护(二).html"
  - "/2025/08/04/Go基础学习记录之部署和维护-二/"
  - "/2025/08/04/Go基础学习记录之部署和维护-二.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-er/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-er.html"
---
### 错误和崩溃

一旦我们的网络应用程序上线，很可能会出现一些无法预料的错误。 下面列出了应用程序日常操作过程中可能出现的一些常见错误示例：

* 数据库错误：与访问数据库服务器或存储数据相关的错误。以下是您可能遇到的一些数据库错误：
* 连接错误：表示无法建立与网络数据库服务器的连接，提供的用户名或密码不正确，或者数据库不存在。
* 查询错误：SQL查询的非法或错误使用可能会引发错误，例如此错误。通过严格的测试可以避免这些类型的错误。
* 数据错误：数据库约束违规，例如尝试插入具有重复主键的字段。在将应用程序部署到生产环境之前，还可以通过严格的测试来避免这些类型的错误。
* 应用程序运行时错误：这些类型的错误差异很大，几乎涵盖了运行时可能出现的所有错误代码。可能的应用程序错误如下：
* 文件系统和权限错误：当应用程序尝试读取不存在或无权读取的文件时，或者当它尝试写入不允许写入的文件时，将发生此类错误。如果应用程序读取具有意外格式的文件，也会发生文件系统错误，例如配置文件应该是INI格式，而是结构化为JSON。
* 第三方应用程序错误：这些错误发生在与其他第三方应用程序或服务交互的应用程序中。例如，如果应用程序在调用Twitter的API之后发布推文，很明显Twitter的服务必须启动并运行才能使我们的应用程序完成其任务。我们还必须确保在调用中为这些第三方接口提供适当的参数，否则它们也会返回错误。
* HTTP错误：这些错误差别很大，并且基于用户请求。最常见的是404 Not Found错误，当用户尝试访问应用程序中不存在的资源时会出现错误。另一个常见的HTTP错误是401 Unauthorized错误（访问请求的资源需要身份验证），403 Forbidden错误（用户完全拒绝访问此资源）和503 Service Unavailable错误（表示内部程序错误）。
* 操作系统错误：这些类型的错误发生在操作系统层，并且可能在操作系统资源过度分配时发生，从而导致崩溃和系统不稳定。此级别的另一个常见情况是操作系统磁盘充满容量，无法写入。这自然会产生许多错误。
* 网络错误：网络错误通常有两种形式：一种是用户向应用程序发出请求并且网络断开连接，从而破坏其处理和响应阶段。这些错误不会导致应用程序崩溃，但会影响用户对网站的访问;另一种是应用程序尝试从断开连接的网络读取数据，导致读取失败。在进行网络调用以避免此类问题时，明智的测试尤为重要，这可能会导致应用程序崩溃。

### 错误处理目标

在实施错误处理之前，我们必须清楚我们要实现的目标。通常，错误处理系统应完成以下操作：

* 用户错误通知：发生系统或用户错误时，导致当前用户请求无法完成，应通知受影响的用户此问题。例如，对于因用户请求而导致的错误，我们会显示统一的错误页面（404.html）。当发生系统错误时，我们使用自定义错误页面为用户提供有关发生的事情的反馈 - 例如，系统暂时不可用（error.html）。
* 记录错误：发生系统错误时（通常，当函数返回非零错误变量时），应使用前面描述的记录系统将事件记录到日志文件文件中。如果是致命错误，还应通过电子邮件通知系统管理员。但一般情况下，大多数404错误都不能保证发送电子邮件通知;将事件记录到日志中供以后仔细检查通常就足够了。
* 回滚当前请求操作：如果用户请求导致服务器错误，那么我们需要能够回滚当前操作。让我们看一个例子：系统将用户提交的表单保存到其数据库，然后将此数据提交给第三方服务器。但是，第三方服务器断开连接，我们无法与它建立连接，从而导致错误。在这种情况下，应从数据库中删除先前存储的表单数据（应通知void），并且应用程序应通知用户系统错误。
* 确保应用程序可以从错误中恢复：我们知道任何程序都很难保证100％的正常运行时间，因此我们需要为程序失败的情况做好准备。例如，如果我们的程序崩溃，我们首先需要记录错误，通知相关各方，然后立即启动并重新运行程序。这样，我们的应用程序可以继续提供服务，同时系统管理员会调查并修复问题的原因。

### 如何处理错误

在前面的分享中，我们使用一些示例解决了错误处理和设计的过程。 让我们更详细地讨论这些示例，并查看其他一些错误处理方案：

* 通知用户错误：

发生错误时，我们可以向用户显示两种错误页面：404.html和error.html。 以下是错误页面的源代码可能如下所示的示例：

```html
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Page Not Found
  </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <div class="container">
    <div class="row">
      <div class="span10">
        <div class="hero-unit">
          <h1> 404! </h1>
          <p>{{.ErrorInfo}}</p>
        </div>
      </div>
      <!--/span-->
    </div>
  </div>
</body>

</html>
```

另一个示例

```html
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>system error page
  </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body>
  <div class="container">
    <div class="row">
      <div class="span10">
        <div class="hero-unit">
          <h1> system is temporarily unavailable ! </h1>
          <p>{{.ErrorInfo}}</p>
        </div>
      </div>
      <!--/span-->
    </div>
  </div>
</body>

</html>
```

404错误处理逻辑，在发生系统错误时：

```go
func (p *MyMux) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path == "/" {
        sayhelloName(w, r)
        return
    }
    NotFound404(w, r)
    return
}

func NotFound404(w http.ResponseWriter, r *http.Request) {
    log.Error(" page not found")              //error logging
    t, _ = t.ParseFiles("tmpl/404.html", nil) //parse the template file
    ErrorInfo := " File not found "           //Get the current user information
    t.Execute(w, ErrorInfo)                   //execute the template merger operation
}

func SystemError(w http.ResponseWriter, r *http.Request) {
    log.Critical(" System Error")                      //system error triggered Critical, then logging will not only send a message
    t, _ = t.ParseFiles("tmpl/error.html", nil)        //parse the template file
    ErrorInfo := " system is temporarily unavailable " //Get the current user information
    t.Execute(w, ErrorInfo)                            //execute the template merger operation
}
```

### 如何处理异常

我们知道许多其他语言都尝试过捕获用于捕获异常情况的关键字，但实际上，可以预期会发生许多错误而不需要异常处理，并且可以将其视为错误。 出于这个原因，Go函数通过设计返回错误。 例如，如果找不到文件或os.Open返回错误，这些函数不会出现混乱; 另一个例子，如果网络连接在数据写操作期间断开连接，则net.Conn系列Write函数将返回错误而不是恐慌。 在大多数应用程序中都会出现这些错误状态，并且Go特别通过返回错误变量使操作失败时使其显式化。 看一下上面的例子，我们可以清楚地看到可能发生的错误。

但是，应该使用恐慌的情况。例如，在几乎不可能发生故障的操作中，或者在无法返回错误并且操作无法继续的某些情况下，应该使用恐慌。例如，尝试获取x[j]处的数组值的程序，但索引j超出范围。代码的这一部分将导致程序恐慌，这种性质的其他关键的，意外的错误也会引起恐慌。默认情况下，恐慌会杀掉有问题的进程（goroutine），允许调度goroutine的代码有机会从错误中恢复。这样，发生错误的函数以及之后的所有后续代码将不会继续执行。 Go的恐慌是故意设计的，考虑到这种行为，这与典型的错误处理不同;恐慌真的只是异常处理。在下面的示例中，我们希望User[UID]将从User数组返回一个用户名，但我们使用的UID超出范围并引发异常。如果我们没有立即处理这个问题的恢复机制，那么该进程将被终止，并且恐慌将在堆栈中传播，直到我们的程序最终崩溃。为了使我们的应用程序能够健壮并且能够抵御这些类型的运行时错误，我们需要在某些地方实现恢复机制。

```go
func GetUser(uid int) (username string) {
    defer func() {
        if x := recover(); x != nil {
            username = ""
        }
    }()

    username = User[uid]
    return
}
```

以上描述了错误和异常之间的差异。 那么，当我们开发Go应用程序时，我们何时使用其中一个？ 规则很简单：如果定义了预期可能失败的函数，则返回错误变量。 当调用另一个包的函数时，如果它被很好地实现，除非发生了真正的异常（无论是否已实现恢复逻辑），否则不必担心它会发生混乱。 恐慌和恢复只应在包内部使用，以处理无法保证程序状态或发生程序员错误的特殊情况。 外部API应显式返回错误值。

### 小结

本篇文章分享中概述了Web应用程序应如何处理各种错误，如网络，数据库和操作系统错误等。 我们概述了几种有效处理运行时错误的技术，例如：显示用户友好的错误通知，回滚操作，记录和警告系统管理员。 最后，我们解释了如何正确处理错误和异常。 错误的概念经常与异常的概念混淆，但在Go中，两者之间存在明显的区别。 出于这个原因，我们已经讨论了在Web应用程序中处理错误和异常的原则。
