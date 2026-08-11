---
title: "Go基础学习记录之Sockets(三)"
date: "2025-08-01 11:36:08"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-sockets-san"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Sockets(三)/"
  - "/2025/08/01/Go基础学习记录之Sockets(三).html"
  - "/Go基础学习记录之Sockets(三)/"
  - "/Go基础学习记录之Sockets(三).html"
  - "/2025/08/01/Go基础学习记录之Sockets-三/"
  - "/2025/08/01/Go基础学习记录之Sockets-三.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-san/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-san.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-sockets-san.html"
---
## TCP Server(TCP 服务端)

上篇文章中的介绍我们已经渔鸥了一个TCP客户端。  
现在我们使用net包来编写TCP服务器。  
在服务器端，我们需要将服务绑定到特定的非活动端口，并侦听任何传入的客户端请求。

用到的函数如下

```go
func ListenTCP(net string, laddr *TCPAddr) (l *TCPListener, err os.Error)
func (l *TCPListener) Accept() (c Conn, err os.Error)
```

这里要求的参数与我们之前使用的DialTCP函数所需的参数相同。  
让我们使用端口7777实现时间同步服务，示例代码如下：

```go
package main

import (
    "fmt"
    "net"
    "os"
    "time"
)

func main() {
    service := ":7777"
    tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
    checkError(err)
    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)
    for {
        conn, err := listener.Accept()
        if err != nil {
            continue
        }
        daytime := time.Now().String()
        conn.Write([]byte(daytime)) // don't care about return value
        conn.Close()                // we're finished with this client
    }
}
func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
        os.Exit(1)
    }
}
```

服务启动后，它会等待客户端请求。  
当它收到客户端请求时，它接受它并向客户端返回包含有关当前时间信息的响应。  
值得注意的是，当for循环中发生错误时，服务将继续运行而不是退出。  
服务器将错误记录到服务器错误日志，而不是崩溃。  
但是，上面的代码仍然不够好。  
我们没有使用goroutines，这将允许我们接受同时请求。  
我们现在就这样做：

```go
package main

import (
    "fmt"
    "net"
    "os"
    "time"
)

func main() {
    service := ":1200"
    tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
    checkError(err)
    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)
    for {
        conn, err := listener.Accept()
        if err != nil {
            continue
        }
        go handleClient(conn)
    }
}

func handleClient(conn net.Conn) {
    defer conn.Close()
    daytime := time.Now().String()
    conn.Write([]byte(daytime)) // don't care about return value
    // we're finished with this client
}

func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
        os.Exit(1)
    }
}
```

通过将我们的业务流程与handleClient函数分离出来，并使用go关键字，我们已经在服务中实现了并发性。  
这是对goroutines的强大和简单性的一个很好的证明。你们中的一些人可能会想到以下内容：这个服务器没有做任何有意义的事情。  
如果我们需要通过单个连接发送不同时间格式的多个请求，该怎么办？我们怎么做？

```go
package main

import (
    "fmt"
    "net"
    "os"
    "time"
    "strconv"
)

func main() {
    service := ":1200"
    tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
    checkError(err)
    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)
    for {
        conn, err := listener.Accept()
        if err != nil {
            continue
        }
        go handleClient(conn)
    }
}

func handleClient(conn net.Conn) {
    conn.SetReadDeadline(time.Now().Add(2 * time.Minute)) // set 2 minutes timeout
    request := make([]byte, 128) // set maximum request length to 128B to prevent flood based attacks
    defer conn.Close()  // close connection before exit
    for {
        read_len, err := conn.Read(request)

        if err != nil {
            fmt.Println(err)
            break
        }

        if read_len == 0 {
            break // connection already closed by client
        } else if string(request[:read_len]) == "timestamp" {
            daytime := strconv.FormatInt(time.Now().Unix(), 10)
            conn.Write([]byte(daytime))
        } else {
            daytime := time.Now().String()
            conn.Write([]byte(daytime))
        }
    }
}

func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
        os.Exit(1)
    }
}
```

在这个例子中，我们使用conn.Read()来不断读取客户端请求。  
我们无法关闭连接，因为客户端可能会发出多个请求。  
由于我们使用conn.SetReadDeadline()设置的超时，连接在我们分配的时间段后自动关闭。  
到期时间结束后，我们的程序会从for循环中断。  
请注意，需要创建具有最大大小限制的请求，以防止泛洪攻击。
