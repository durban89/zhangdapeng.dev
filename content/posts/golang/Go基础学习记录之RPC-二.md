---
title: "Go基础学习记录之RPC(二)"
date: "2025-08-04 11:38:33"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-rpc-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之RPC(二)/"
  - "/2025/08/04/Go基础学习记录之RPC(二).html"
  - "/Go基础学习记录之RPC(二)/"
  - "/Go基础学习记录之RPC(二).html"
  - "/2025/08/04/Go基础学习记录之RPC-二/"
  - "/2025/08/04/Go基础学习记录之RPC-二.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-rpc-er/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-rpc-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-rpc-er.html"
---
继续上篇文章[[Go基础学习记录之RPC(一)](https://www.xiaorongmao.com/blog/102)]

继续看下如何实践HTTP RPC、TCP RPC和JSON RPC

## HTTP RPC

HTTP服务器端代码：

```go
package main

import (
    "errors"
    "fmt"
    "net/http"
    "net/rpc"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

type Arith int

func (t *Arith) Multiply(args *Args, reply *int) error {
    *reply = args.A * args.B
    return nil
}

func (t *Arith) Divide(args *Args, quo *Quotient) error {
    if args.B == 0 {
        return errors.New("divide by zero")
    }
    quo.Quo = args.A / args.B
    quo.Rem = args.A % args.B
    return nil
}

func main() {

    arith := new(Arith)
    rpc.Register(arith)
    rpc.HandleHTTP()

    err := http.ListenAndServe(":1234", nil)
    if err != nil {
        fmt.Println(err.Error())
    }
}
```

我们注册了Arith的RPC服务，然后通过rpc.HandleHTTP在HTTP上注册了这个服务。  
之后，我们可以通过HTTP传输数据。客户端代码：

```go
package main

import (
    "fmt"
    "log"
    "net/rpc"
    "os"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage: ", os.Args[0], "server")
        os.Exit(1)
    }
    serverAddress := os.Args[1]

    client, err := rpc.DialHTTP("tcp", serverAddress+":1234")
    if err != nil {
        log.Fatal("dialing:", err)
    }
    // Synchronous call
    args := Args{17, 8}
    var reply int
    err = client.Call("Arith.Multiply", args, &reply)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d*%d=%d\n", args.A, args.B, reply)

    var quot Quotient
    err = client.Call("Arith.Divide", args, &quot)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d/%d=%d remainder %d\n", args.A, args.B, quot.Quo, quot.Rem)

}
```

我们分别编译客户端和服务器端代码，然后启动服务器和客户端。  
输入一些数据后，您将获得类似的内容。

```bash
$ ./http_c localhost
Arith: 17*8=136
Arith: 17/8=2 remainder 1
```

如您所见，我们为返回类型定义了一个结构。  
我们将它用作服务器端的函数参数类型，以及客户端client.Call上的第二个和第三个参数的类型。  
这个调用非常重要。  
它有三个参数，第一个是要调用的函数的名称，第二个是要传递的参数，最后一个是返回值（指针类型）。  
到目前为止，我们看到在Go中实现RPC非常容易。

## TCP RPC

让我们尝试基于TCP的RPC，这里是服务器端代码：

```go
package main

import (
    "errors"
    "fmt"
    "net"
    "net/rpc"
    "os"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

type Arith int

func (t *Arith) Multiply(args *Args, reply *int) error {
    *reply = args.A * args.B
    return nil
}

func (t *Arith) Divide(args *Args, quo *Quotient) error {
    if args.B == 0 {
        return errors.New("divide by zero")
    }
    quo.Quo = args.A / args.B
    quo.Rem = args.A % args.B
    return nil
}

func main() {

    arith := new(Arith)
    rpc.Register(arith)

    tcpAddr, err := net.ResolveTCPAddr("tcp", ":1234")
    checkError(err)

    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)

    for {
        conn, err := listener.Accept()
        if err != nil {
            continue
        }
        rpc.ServeConn(conn)
    }

}

func checkError(err error) {
    if err != nil {
        fmt.Println("Fatal error ", err.Error())
        os.Exit(1)
    }
}
```

HTTP RPC和TCP RPC之间的区别在于，如果我们使用TCP RPC，则必须自己控制连接，然后将连接传递给RPC进行处理。

你可能已经猜到了，这是一种阻塞模式。  
您可以自由地使用goroutine将此应用程序扩展为更高级的实验。

客户端代码：

```go
package main

import (
    "fmt"
    "log"
    "net/rpc"
    "os"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage: ", os.Args[0], "server:port")
        os.Exit(1)
    }
    service := os.Args[1]

    client, err := rpc.Dial("tcp", service)
    if err != nil {
        log.Fatal("dialing:", err)
    }
    // Synchronous call
    args := Args{17, 8}
    var reply int
    err = client.Call("Arith.Multiply", args, &reply)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d*%d=%d\n", args.A, args.B, reply)

    var quot Quotient
    err = client.Call("Arith.Divide", args, &quot)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d/%d=%d remainder %d\n", args.A, args.B, quot.Quo, quot.Rem)

}
```

客户端代码的唯一区别是HTTP客户端使用DialHTTP而TCP客户端使用Dial（TCP）。

## JSON RPC

JSON RPC将数据编码为JSON而不是gob。

让我们看一下服务器上Go JSON RPC的示例：

```go
package main

import (
    "errors"
    "fmt"
    "net"
    "net/rpc"
    "net/rpc/jsonrpc"
    "os"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

type Arith int

func (t *Arith) Multiply(args *Args, reply *int) error {
    *reply = args.A * args.B
    return nil
}

func (t *Arith) Divide(args *Args, quo *Quotient) error {
    if args.B == 0 {
        return errors.New("divide by zero")
    }
    quo.Quo = args.A / args.B
    quo.Rem = args.A % args.B
    return nil
}

func main() {

    arith := new(Arith)
    rpc.Register(arith)

    tcpAddr, err := net.ResolveTCPAddr("tcp", ":1234")
    checkError(err)

    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)

    for {
        conn, err := listener.Accept()
        if err != nil {
            continue
        }
        jsonrpc.ServeConn(conn)
    }

}

func checkError(err error) {
    if err != nil {
        fmt.Println("Fatal error ", err.Error())
        os.Exit(1)
    }
}
```

JSON RPC基于TCP，但尚不支持HTTP。  
客户端代码：

```go
package main

import (
    "fmt"
    "log"
    "net/rpc/jsonrpc"
    "os"
)

type Args struct {
    A, B int
}

type Quotient struct {
    Quo, Rem int
}

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage: ", os.Args[0], "server:port")
        log.Fatal(1)
    }
    service := os.Args[1]

    client, err := jsonrpc.Dial("tcp", service)
    if err != nil {
        log.Fatal("dialing:", err)
    }
    // Synchronous call
    args := Args{17, 8}
    var reply int
    err = client.Call("Arith.Multiply", args, &reply)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d*%d=%d\n", args.A, args.B, reply)

    var quot Quotient
    err = client.Call("Arith.Divide", args, &quot)
    if err != nil {
        log.Fatal("arith error:", err)
    }
    fmt.Printf("Arith: %d/%d=%d remainder %d\n", args.A, args.B, quot.Quo, quot.Rem)

}
```

## 小结

Go对HTTP，TPC和JSON RPC实现有很好的支持，这使我们可以轻松开发分布式Web应用程序;  
但是，令人遗憾的是Go没有内置的SOAP RPC支持，尽管一些开源的第三方软件包提供了这一功能。
