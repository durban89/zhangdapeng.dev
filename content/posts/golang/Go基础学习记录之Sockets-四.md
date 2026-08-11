---
title: "Go基础学习记录之Sockets(四)"
date: "2025-08-01 11:36:11"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-sockets-si"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Sockets(四)/"
  - "/2025/08/01/Go基础学习记录之Sockets(四).html"
  - "/Go基础学习记录之Sockets(四)/"
  - "/Go基础学习记录之Sockets(四).html"
  - "/2025/08/01/Go基础学习记录之Sockets-四/"
  - "/2025/08/01/Go基础学习记录之Sockets-四.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-si/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-si.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-sockets-si.html"
---
## 控制TCP连接

控制TCP连接函数如下

```go
func DialTimeout(net, addr string, timeout time.Duration) (Conn, error)
```

设置连接超时。  
这些适用于客户端和服务器：

```go
func (c *TCPConn) SetReadDeadline(t time.Time) error
func (c *TCPConn) SetWriteDeadline(t time.Time) error
```

设置一个连接的写/读超时：

```go
func (c *TCPConn) SetKeepAlive(keepalive bool) os.Error
```

值得花些时间考虑一下您希望连接超时的时间长短。  
长连接可以减少创建连接所涉及的开销量，并且适用于需要频繁交换数据的应用程序。  
有关更多详细信息，请查阅Go的net包的官方文档。

## UDP sockets(UDP套接字)

UDP套接字和TCP套接字之间的唯一区别是处理服务器端多个请求的处理方法。  
这是因为UDP没有像Accept那样的功能。  
所有其他功能都有UDP对应物;  
在前面介绍的文章中，其中的功能用UDP代替TCP，具体函数如下：

```go
func ResolveUDPAddr(net, addr string) (*UDPAddr, os.Error)
func DialUDP(net string, laddr, raddr *UDPAddr) (c *UDPConn, err os.Error)
func ListenUDP(net string, laddr *UDPAddr) (c *UDPConn, err os.Error)
func (c *UDPConn) ReadFromUDP(b []byte) (n int, addr *UDPAddr, err os.Error
func (c *UDPConn) WriteToUDP(b []byte, addr *UDPAddr) (n int, err os.Error)
```

UDP客户端代码示例：

```go
package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    if len(os.Args) != 2 {
        fmt.Fprintf(os.Stderr, "Usage: %s host:port", os.Args[0])
        os.Exit(1)
    }
    service := os.Args[1]
    udpAddr, err := net.ResolveUDPAddr("udp4", service)
    checkError(err)
    conn, err := net.DialUDP("udp", nil, udpAddr)
    checkError(err)
    _, err = conn.Write([]byte("anything"))
    checkError(err)
    var buf [512]byte
    n, err := conn.Read(buf[0:])
    checkError(err)
    fmt.Println(string(buf[0:n]))
    os.Exit(0)
}

func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error ", err.Error())
        os.Exit(1)
    }
}
```

UDP服务器代码示例：

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
    udpAddr, err := net.ResolveUDPAddr("udp4", service)
    checkError(err)
    conn, err := net.ListenUDP("udp", udpAddr)
    checkError(err)
    for {
        handleClient(conn)
    }
}

func handleClient(conn *net.UDPConn) {
    var buf [512]byte
    _, addr, err := conn.ReadFromUDP(buf[0:])
    if err != nil {
        return
    }
    daytime := time.Now().String()
    conn.WriteToUDP([]byte(daytime), addr)
}

func checkError(err error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error ", err.Error())
        os.Exit(1)
    }
}
```
