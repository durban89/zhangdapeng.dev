---
title: "Go基础学习记录之部署和维护(一)"
date: "2025-08-04 11:39:21"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之部署和维护(一)/"
  - "/2025/08/04/Go基础学习记录之部署和维护(一).html"
  - "/Go基础学习记录之部署和维护(一)/"
  - "/Go基础学习记录之部署和维护(一).html"
  - "/2025/08/04/Go基础学习记录之部署和维护-一/"
  - "/2025/08/04/Go基础学习记录之部署和维护-一.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-yi/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-bu-shu-he-wei-hu-yi.html"
---
到目前为止，已经分享了在Go中开发，调试和测试Web应用程序的基础知识。然而，正如人们常说的那样：最后10％的开发需要90％的时间。在本次分享中，我们将强调最后10％的应用程序开发，以便真正制作可靠和高质量的Web应用程序。在第一部分中，我们将研究生产服务如何生成日志以及记录自身的过程。第二部分将描述处理运行时错误，以及如何在发生错误时对其进行管理，以便最大限度地减少对最终用户的影响。在第三部分中，我们讨论了部署独立Go程序的主题，这一开始可能很棘手。您可能知道，Go程序不能像使用C语言一样使用守护程序编写。我们将讨论如何在Go中管理后台进程。最后，我们的第四部分和最后一部分将介绍在Go中备份和恢复应用程序数据的过程。我们将看一些技术，以确保在发生崩溃时，我们将能够保持数据的完整性。

### 日志

我们希望构建能够跟踪整个执行过程中发生的事件的Web应用程序，将它们组合到一个位置，以便以后轻松访问，当我们不可避免地需要执行调试或优化任务时。Go提供了一个简单的日志包，我们可以用它来帮助我们实现简单的日志记录功能。可以使用Go的fmt软件包打印日志，该软件包称为内部错误处理函数，用于一般错误日志记录。但是，Go的标准包仅包含用于记录的基本功能。如果您的需求更加复杂，我们可以使用许多第三方日志工具来补充它（类似于log4j和log4cpp的工具，如果您曾经不得不处理Java或C ++中的日志记录）。Go中一个流行的，功能齐全的开源日志工具是seelog日志框架。让我们来看看如何使用seelog在Go应用程序中执行日志记录。

seelog简介

Seelog是Go的日志框架，它提供了一些简单的功能来实现日志记录任务，如过滤和格式化。其主要特点如下：

* 通过XML动态配置;您可以动态加载配置参数，而无需重新编译程序
* 支持热更新，无需重启应用程序即可动态更改配置
* 支持多输出流，可以同时将日志输出管道输出到多个流，例如文件流，网络流等。
* 支持不同的日志输出

  + 命令行输出
  + 文件输出
  + 缓存输出
  + 支持日志轮换
  + SMTP邮件

以上只是seelog功能的部分列表。要充分利用seelog的所有功能，请查看其官方维基，其中详细说明了您可以使用它做什么。让我们看看我们如何在项目中使用seelog：

首先安装seelog：

```bash
go get -u github.com/cihub/seelog
```

然后让我们写一个简单的例子：

```go
package main

import log "github.com/cihub/seelog"

func main() {
    defer log.Flush()
    log.Info("Hello from Seelog!")
}
```

编译并运行该程序。如果您在应用程序日志中看到来自seelog的Hello，则已成功安装seelog并且运行正常。

使用seelog自定义日志处理

Seelog支持自定义日志处理。以下代码段基于其程序包的自定义日志处理部分：

```go
package logs

import (
    "errors"
    "fmt"
    seelog "github.com/cihub/seelog"
    "io"
)

var Logger seelog.LoggerInterface

func loadAppConfig() {
    appConfig := `
<seelog minlevel="warn">
    <outputs formatid="common">
        <rollingfile type="size" filename="/data/logs/roll.log" maxsize="100000" maxrolls="5"/>
        <filter levels="critical">
            <file path="/data/logs/critical.log" formatid="critical"/>
            <smtp formatid="criticalemail" senderaddress="[email protected]" sendername="ShortUrl API" hostname="smtp.gmail.com" hostport="587" username="mailusername" password="mailpassword">
                <recipient address="[email protected]"/>
            </smtp>
        </filter>
    </outputs>
    <formats>
        <format id="common" format="%Date/%Time [%LEV] %Msg%n" />
        <format id="critical" format="%File %FullPath %Func %Msg%n" />
        <format id="criticalemail" format="Critical error on our server!\n    %Time %Date %RelFile %Func %Msg \nSent by Seelog"/>
    </formats>
</seelog>
`
    logger, err := seelog.LoggerFromConfigAsBytes([]byte(appConfig))
    if err != nil {
        fmt.Println(err)
        return
    }
    UseLogger(logger)
}

func init() {
    DisableLog()
    loadAppConfig()
}

// DisableLog disables all library log output
func DisableLog() {
    Logger = seelog.Disabled
}

// UseLogger uses a specified seelog.LoggerInterface to output library log.
// Use this func if you are using Seelog logging system in your app.
func UseLogger(newLogger seelog.LoggerInterface) {
    Logger = newLogger
}
```

以上实现了三个主要功能：

* DisableLog

初始化禁用seelog的全局变量Logger，主要是为了防止记录器被重复初始化

* LoadAppConfig

根据配置文件初始化seelog的配置设置。在我们的示例中，我们从内存中的字符串中读取配置，当然，您也可以从XML文件中读取它。在配置中，我们设置以下参数：

* Seelog

minlevel参数是可选的。如果已配置，将记录大于或等于指定级别的日志记录级别。可选的maxlevel参数类似地用于配置所需的最大日志记录级别。

* Outputs

配置输出目的地。在我们的特定情况下，我们将记录数据引导到两个输出目的地。第一个是滚动日志文件，我们不断保存最新的日志记录数据窗口。第二个目标是过滤日志，仅记录严重级别错误。我们还将其配置为在发生这些类型的错误时通过电子邮件提醒我们。

* Formats

定义各种日志记录格式。您可以使用自定义格式或预定义格式 - 可以在seelog的wiki上找到预定义格式的完整列表

* UseLogger

将当前记录器设置为我们的日志处理器

上面，我们定义并配置了一个自定义日志处理包。以下代码演示了我们如何使用它：

```go
package main

import (
    "net/http"
    "project/logs"
    "project/configs"
    "project/routes"
)

func main() {
    addr, _ := configs.MainConfig.String("server", "addr")
    logs.Logger.Info("Start server at:%v", addr)
    err := http.ListenAndServe(addr, routes.NewMux())
    logs.Logger.Critical("Server err:%v", err)
}
```

邮件通知

上面的示例说明了如何使用seelog设置电子邮件通知。如您所见，我们使用以下smtp配置：

```html
<smtp formatid="criticalemail" senderaddress="xxx@xxx" sendername="ShortUrl API" hostname="smtp.gmail.com" hostport="587" username="mailusername" password="mailpassword">
    <recipient address="xxx@xxx"/>
</smtp>
```

我们通过critalemail配置设置警报消息的格式，提供我们的邮件服务器参数以便能够接收它们。我们还可以将通知程序配置为使用收件人配置向其他用户发送警报。为每个额外的收件人添加一行是一件简单的事情。

要测试此代码是否正常工作，您可以向应用程序添加假的关键消息，如下所示：

```go
logs.Logger.Critical("test Critical message")
```

完成测试后，不要忘记删除它，或者当您的应用程序上线时，您的收件箱可能会充斥着电子邮件通知。

现在，只要我们的应用程序在线时记录关键消息，您和指定的收件人就会收到通知电子邮件。然后，您和您的团队可以及时处理并纠正这种情况。

使用应用程序日志

对于日志，每个应用程序的用例可能会有所不同。例如，有些人使用日志进行数据分析，其他人则进行性能优化。某些日志用于分析用户行为以及人们如何与您的网站进行互动。当然，有些日志只是用于记录应用程序事件作为查找问题的辅助数据。

例如，假设我们需要跟踪用户登录系统的尝试。这涉及将成功和不成功的登录尝试记录到我们的日志中。我们通常使用"Info"日志级别来记录这些类型的事件，而不是像"warn"那样更严重的事件。如果您使用的是linux类型的系统，则可以使用grep命令从日志中方便地查看所有不成功的登录尝试，如下所示：

```bash
# cat /data/logs/roll.log | grep "failed login"
2012-12-11 11:12:00 WARN : failed login attempt from 11.22.33.44 username password
```

这样，我们可以在应用程序日志中轻松找到相应的信息，这可以帮助我们在需要时执行统计分析。 此外，我们还需要考虑高流量Web应用程序生成的日志大小。 这些日志有时会不可预测地增长。 要解决此问题，我们可以使用logrotate配置设置seelog，以确保单个日志文件不会占用过多的磁盘空间。

### 小结

在本次分享中，我们已经了解了seelog的基础知识以及如何使用它构建自定义日志记录系统。 我们看到我们可以轻松地将seelog配置为我们需要的强大的日志处理系统，使用它为我们提供可靠的数据源以供分析。 通过日志分析，我们可以优化我们的系统，并在问题出现时轻松找到问题的根源。 此外，seelog还提供各种默认日志级别。 我们可以将minlevel配置与日志级别结合使用，以轻松设置测试或发送自动通知消息。
