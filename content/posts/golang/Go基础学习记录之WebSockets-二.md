---
title: "Go基础学习记录之WebSockets(二)"
date: "2025-08-01 11:36:18"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-websockets-er"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Go基础学习记录之WebSockets(二)/"
  - "/2025/08/01/Go基础学习记录之WebSockets(二).html"
  - "/Go基础学习记录之WebSockets(二)/"
  - "/Go基础学习记录之WebSockets(二).html"
  - "/2025/08/01/Go基础学习记录之WebSockets-二/"
  - "/2025/08/01/Go基础学习记录之WebSockets-二.html"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-websockets-er/"
  - "/2025/08/01/go-ji-chu-xue-xi-ji-lu-zhi-websockets-er.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-websockets-er.html"
---
## Go中的WebSocket

go标准库不支持WebSockets。  
然而，websocket包是go.net的一个子包，并且正式维护和支持。  
使用go get来安装这个包：

```bash
go get golang.org/x/net/websocket
```

WebSockets同时具有客户端和服务器端。  
让我们看一个简单的例子，用户在客户端输入一些信息并通过WebSocket将其发送到服务器，然后服务器将信息推送回客户端。客户端代码如下：

```html
<html>
<head>Test Websocket</head>
<body>
  <script type="text/javascript">
    var sock = null;
    var wsuri = "ws://127.0.0.1:1234";

    window.onload = function() {

      console.log("onload");

      sock = new WebSocket(wsuri);

      sock.onopen = function() {
        console.log("connected to " + wsuri);
      }

      sock.onclose = function(e) {
        console.log("connection closed (" + e.code + ")");
      }

      sock.onmessage = function(e) {
        console.log("message received: " + e.data);
      }
    };

    function send() {
        var msg = document.getElementById('message').value;
        sock.send(msg);
    };
  </script>
  <h1>WebSocket Echo Test</h1>
  <form>
    <p>
      Message: <input id="message" type="text" value="Hello, world!">
    </p>
  </form>
  <button onclick="send();">Send Message</button>
</body>
</html>
```

如您所见，使用客户端JavaScript函数建立连接非常容易。  
在成功完成上述握手过程后触发onopen事件。  
它告诉客户端已成功创建连接。  
尝试打开连接的客户端通常绑定到四个事件：

1）onopen：连接建立后触发。  
2）onmessage：收到消息后触发。  
3）onerror：发生错误后触发。  
4）onclose：连接关闭后触发。

服务器端代码如下：

```go
package main

import (
    "golang.org/x/net/websocket"
    "fmt"
    "log"
    "net/http"
)

func Echo(ws *websocket.Conn) {
    var err error

    for {
        var reply string

        if err = websocket.Message.Receive(ws, &reply); err != nil {
            fmt.Println("Can't receive")
            break
        }

        fmt.Println("Received back from client: " + reply)

        msg := "Received:  " + reply
        fmt.Println("Sending to client: " + msg)

        if err = websocket.Message.Send(ws, msg); err != nil {
            fmt.Println("Can't send")
            break
        }
    }
}

func main() {
    http.Handle("/", websocket.Handler(Echo))

    if err := http.ListenAndServe(":1234", nil); err != nil {
        log.Fatal("ListenAndServe:", err)
    }
}
```

当客户端发送用户输入信息时，服务器接收它，并再次使用发送返回响应。

通过上面的例子，我们可以看到WebSockets的客户端和服务器端实现非常方便。  
我们可以直接在Go中使用net包。  
随着HTML5的快速发展，WebSockets将在现代Web开发中扮演更重要的角色;  
我们都应该至少对它们有点熟悉。
