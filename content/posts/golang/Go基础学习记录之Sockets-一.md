---
title: "Go基础学习记录之Sockets(一)"
date: "2025-08-01 11:36:02"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-sockets-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之Sockets(一)/"
  - "/2025/08/01/Go基础学习记录之Sockets(一).html"
  - "/Go基础学习记录之Sockets(一)/"
  - "/Go基础学习记录之Sockets(一).html"
  - "/2025/08/01/Go基础学习记录之Sockets-一/"
  - "/2025/08/01/Go基础学习记录之Sockets-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-sockets-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-sockets-yi.html"
---
## Sockets(套接字)

一些网络应用程序开发人员说较低的应用程序层都是关于套接字编程的。  
对于所有情况，这可能并非如此，但许多现代Web应用程序确实使用套接字来发挥其优势。  
你有没有想过当你上网时浏览器如何与网络服务器通信？  
或者MSN如何在聊天室中将您和您的朋友连接在一起，实时传递每条消息？  
许多像这样的服务使用套接字来传输数据。  
正如您所看到的，套接字在今天的网络编程中占有重要地位，下面来学习如何在Go中使用套接字。

### 什么是Sockets(套接字)

套接字源自Unix，并且鉴于Unix的基本"一切都是文件"的哲学，一切都可以通过"打开->写入/读取->关闭"来操作。  
套接字是这种哲学的一种实现。  
套接字具有打开套接字的函数调用，就像打开文件一样。  
这将返回套接字的int描述符，然后可以将其用于创建连接，传输数据等操作。  
常用的两种类型的套接字是流套接字（SOCK\_STREAM）和数据报套接字（SOCK\_DGRAM）。  
流套接字是面向连接的，如TCP，而数据报套接字不建立连接，如UDP。

### 套接字通信

在我们了解套接字如何相互通信之前，我们需要弄清楚如何确保每个套接字都是唯一的，否则建立一个可靠的通信通道已经不可能了。  
我们可以为每个进程提供一个独特的PID，它在本地服务于我们的目的，但是无法通过网络工作。  
幸运的是，TCP/IP帮助我们解决了这个问题。  
网络层的IP地址在主机网络中是唯一的，并且"协议+端口"在主机应用程序中也是唯一的。  
因此，我们可以使用这些原则来制作独特的套接字。  

{% img https://cdn.xiaorongmao.com/up/golang_web_39_1.png "" %}

基于TCP/IP的应用程序都以某种方式在其代码中使用套接字API。  
鉴于网络应用程序在现代变得越来越普遍，难怪一些开发人员说"一切都是关于套接字"。

### 套接字基础知识

我们知道套接字有两种类型，即TCP套接字和UDP套接字。  
TCP和UDP是协议，如上所述，我们还需要一个IP地址和端口号来拥有一个唯一的套接字。

### *IPv4*

全球互联网使用TCP/IP作为其协议，其中IP是网络层和TCP/IP的核心部分。  
IPv4表示其版本为4;  
迄今为止，基础设施发展已超过30年。  
IPv4地址中的位数为32，这意味着2^32个设备能够唯一地连接到 Internet。  
由于互联网的快速发展，近年来IP地址已经缺货。  
地址格式：127.0.0.1,172.122.121.111。

### *IPv6*

IPv6是下一版本或下一代互联网。  
它正在开发用于解决IPv4固有的许多问题。  
使用IPv6的设备的地址长度为128位，因此我们永远不必担心唯一地址的短缺。  
从这个角度来看，使用IPv6可以为地球上的每平方米提供超过1000个IP地址。  
还可以改进诸如对等连接，服务质量(QoS)，安全性，多播等的其他问题。  
地址格式：2002:c0e8:82e7:0:0:0:c0e8:82e7。

### *Go中的IP类型*

Go中的网络包提供了许多用于网络编程的类型，功能和方法。  
IP的定义如下：

```go
type IP []byte
```

函数`ParseIP（s string）IP`是将IPv4或IPv6格式转换为IP：

```go
package main

import (
    "fmt"
    "net"
    "os"
)

func main() {
    if len(os.Args) != 2 {
        fmt.Fprintf(os.Stderr, "Usage: %s ip-addr\n", os.Args[0])
        os.Exit(1)
    }
    name := os.Args[1]
    addr := net.ParseIP(name)
    if addr == nil {
        fmt.Println("Invalid address")
    } else {
        fmt.Println("The address is ", addr.String())
    }
    os.Exit(0)
}
```

它返回给定IP地址的相应IP格式。
