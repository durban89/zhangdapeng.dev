---
title: "Go基础学习记录之WebSockets(一)"
date: "2025-08-01 11:36:14"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-websockets-yi"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之WebSockets(一)/"
  - "/2025/08/01/Go基础学习记录之WebSockets(一).html"
  - "/Go基础学习记录之WebSockets(一)/"
  - "/Go基础学习记录之WebSockets(一).html"
  - "/2025/08/01/Go基础学习记录之WebSockets-一/"
  - "/2025/08/01/Go基础学习记录之WebSockets-一.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-websockets-yi/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-websockets-yi.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-websockets-yi.html"
---
## WebSockets

WebSockets是HTML5的一个重要特性。  
它实现了基于浏览器的远程套接字，允许浏览器与服务器进行全双工通信。  
Firefox，Google Chrome和Safari等主流浏览器支持此WebSockets。

在WebSockets诞生之前，人们经常使用“滚动轮询”进行即时消息传递服务，这允许客户端定期发送HTTP请求。  
然后，服务器将最新数据返回给客户端。  
这种方法的缺点是它要求客户端不断向服务器发送许多请求，这会占用大量带宽。

WebSockets使用一种特殊的标头，可以将浏览器和服务器之间所需的握手次数减少到只有一次，以建立连接。  
此连接在其整个生命周期内将保持活动状态，您可以使用JavaScript从此连接写入或读取数据，如传统TCP套接字的情况。  
它解决了实时Web开发所涉及的许多问题，并且与传统HTTP相比具有以下优势：

1. 单个Web客户端只有一个TCP连接。  
2. WebSocket服务器可以将数据推送到Web客户端。  
3. 轻量级头，以减少数据传输开销。

WebSocket URL以ws：//或wss：//（SSL）开头。  
下图显示了WebSockets的通信过程。  
作为握手协议的一部分，将特定的HTTP报头发送到服务器，并建立连接。  
然后，服务器或客户端能够通过WebSocket通过JavaScript发送或接收数据。  
然后，事件处理程序可以使用此套接字异步接收数据。

{% img https://cdn.xiaorongmao.com/up/golang_web_43_1.png "" %}


## WebSocket原则

WebSocket协议实际上非常简单。  
成功完成初始握手后，建立连接。  
后续数据通信将以“\ x00”开头，以“\ xFF”结尾。  
客户端可以看到此前缀和后缀，因为WebSocket将中断两端，自动生成原始数据。

WebSocket连接由浏览器请求并由服务器响应，之后建立连接。  
这个过程通常被称为“握手”。

请考虑以下请求和响应：

{% img https://cdn.xiaorongmao.com/up/golang_web_43_2.png "" %}


“Sec-WebSocket-key”是随机生成的，正如您可能已经猜到的那样，它是base64编码的。  
服务器需要在接受请求后将此密钥附加到固定字符串：

```bash
258EAFA5-E914-47DA-95CA-C5AB0DC85B11
```

假设我们有f7cb4ezEAl6C3wRaU6JORA ==，那么我们有：

```bash
f7cb4ezEAl6C3wRaU6JORA==258EAFA5-E914-47DA-95CA-C5AB0DC85B11
```

使用sha1计算二进制值并使用base64对其进行编码。  
那么我们将：

```bash
rE91AJhfC+6JdVcVXOGJEADEJdQ=
```

使用此作为Sec-WebSocket-Accept响应头的值。
