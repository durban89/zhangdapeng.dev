---
title: "Node超级简单实现聊天服务器"
date: "2025-06-27 14:14:22"
slug: "node-chao-ji-jian-dan-shi-xian-liao-tian-fu-wu-qi"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/27/Node超级简单实现聊天服务器/"
  - "/2025/06/27/Node超级简单实现聊天服务器.html"
  - "/Node超级简单实现聊天服务器/"
  - "/Node超级简单实现聊天服务器.html"
  - "/2025/06/27/node-chao-ji-jian-dan-shi-xian-liao-tian-fu-wu-qi/"
  - "/2025/06/27/node-chao-ji-jian-dan-shi-xian-liao-tian-fu-wu-qi.html"
  - "/node-chao-ji-jian-dan-shi-xian-liao-tian-fu-wu-qi.html"
---
Node超级简单实现聊天服务器

使用Nodejs是如此简单的实现了一个简单的聊天服务器

实现代码如下：

```js
var net = require('net');

var chatServer = net.createServer(),clientList = [];

chatServer.on("connection",function(client){
    client.name = client.remoteAddress + ":" + client.remotePort;
    client.write("Hi! "+client.name+" \n");
    clientList.push(client);

    client.on("data",function(data){
        //数据发送给客户端
        broadcast(data,client);
        // clientList[i].write(data);
    });

    client.on("end",function(){
        clientList.splice(clientList.indexOf(client),1);
    });

    client.on("error",function(e){
        console.log(e)
    });
});
chatServer.listen(9000)

function broadcast(message,client){
    var cleanup = [];
    for(var i=0;i<clientList.length;i++){
        if(client != clientList[i]){
            if(clientList[i].writable){
                clientList[i].write(client.name = "says:"+message);
            }else{
                cleanup.push[clientList[i]];
                clientList[i].destory();
            }
        }
    }
}
```

使用过程就是：

启动js

```bash
node chat.js
```

连接方式：telnet

```bash
telnet 127.0.0.1 9000
```

