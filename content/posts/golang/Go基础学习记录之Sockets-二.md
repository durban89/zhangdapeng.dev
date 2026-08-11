---
title: "Go基础学习记录之Sockets(二)"
date: "2025-08-01 11:36:05"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-sockets-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Sockets(二)/"
  - "/2025/08/01/Go基础学习记录之Sockets(二).html"
  - "/Go基础学习记录之Sockets(二)/"
  - "/Go基础学习记录之Sockets(二).html"
  - "/2025/08/01/Go基础学习记录之Sockets-二/"
  - "/2025/08/01/Go基础学习记录之Sockets-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-er/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-sockets-er.html"
---
## TCP socket

当我们知道如何通过网络端口访问Web服务时，我们可以做些什么？  
作为客户，我们可以向指定的网络端口发送请求并获得响应;  
作为服务器，我们需要将服务绑定到指定的网络端口，等待客户端的请求并提供响应。  
在Go的网络包中，有一种称为TCPConn的类型，可以促进这种客户端/服务器交互。  
这种类型有两个关键函数，如下：

```go
func (c *TCPConn) Write(b []byte) (n int, err os.Error)
func (c *TCPConn) Read(b []byte) (n int, err os.Error)
```

客户端或服务器可以使用TCPConn来读取和写入数据。

我们还需要一个TCPAddr来表示TCP地址信息：

```go
type TCPAddr struct {
    IP IP
    Port int
}
```

我们使用ResolveTCPAddr函数在Go中获取TCPAddr：

```go
func ResolveTCPAddr(net, addr string) (*TCPAddr, os.Error)
```

net的参数可以是"tcp4"，"tcp6"或"tcp"之一，它们分别表示仅IPv4，仅IPv6，以及IPv4或IPv6。  
addr可以是域名或IP地址，例如"www.google.com:80"或"127.0.0.1:22"

## TCP客户端

Go客户端使用net包中的DialTCP函数创建TCP连接，该连接返回TCPConn对象;  
在建立连接之后，服务器具有与当前连接相同类型的连接对象，并且客户端和服务器可以开始彼此交换数据。  
通常，客户端通过TCPConn向服务器发送请求，并从服务器响应中接收信息;  
服务器读取并解析客户端请求，然后返回反馈。  
在客户端或服务器关闭之前，此连接将保持有效。  
创建连接的函数如下：

```go
func DialTCP(net string, laddr, raddr *TCPAddr) (c *TCPConn, err os.Error)
```

net的参数可以是"tcp4"，"tcp6"或"tcp"之一，它们分别表示仅IPv4，仅IPv6，以及IPv4或IPv6。  
laddr表示本地地址，在大多数情况下将其设置为nil。  
raddr代表远程地址。

让我们编写一个简单的示例来模拟请求基于HTTP请求连接到服务器的客户端。  
我们需要一个简单的HTTP请求标头：

```bash
"HEAD / HTTP/1.0\r\n\r\n"
```

服务器响应信息格式如下所示：

```bash
HTTP/1.0 200 OK
ETag: "-9985996"
Last-Modified: Thu, 25 Mar 2010 17:51:10 GMT
Content-Length: 18074
Connection: close
Date: Sat, 28 Aug 2010 00:43:48 GMT
Server: nginx/1.13.10
```

客户端代码：

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net"
    "os"
)

func main() {
    if len(os.Args) != 2 {
        fmt.Fprintf(os.Stderr, "Usage: %s host:port ", os.Args[0])
        os.Exit(1)
    }
    service := os.Args[1]
    tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
    checkError(err)
    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    checkError(err)
    _, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
    checkError(err)
    result, err := ioutil.ReadAll(conn)
    checkError(err)
    fmt.Println(string(result))
    os.Exit(0)
}
func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
        os.Exit(1)
    }
}
```

在上面的示例中，我们使用用户输入作为net.ResolveTCPAddr的服务参数来获取tcpAddr。  
将tcpAddr传递给DialTCP函数，我们创建了一个TCP连接，即conn。  
然后我们可以使用conn向服务器发送请求信息。  
最后，我们使用ioutil.ReadAll从conn中读取所有内容，其中包含服务器响应。

待续...
