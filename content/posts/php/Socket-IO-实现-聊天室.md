---
title: "Socket IO 实现 聊天室"
date: "2025-06-30 11:49:19"
slug: "socket-io-shi-xian-liao-tian-shi"
categories: ["技术"]
tags: ["SocketIO"]
aliases:
  - "/2025/06/30/Socket-IO-实现-聊天室/"
  - "/2025/06/30/Socket-IO-实现-聊天室.html"
  - "/Socket-IO-实现-聊天室/"
  - "/Socket-IO-实现-聊天室.html"
  - "/2025/06/30/socket-io-shi-xian-liao-tian-shi/"
  - "/2025/06/30/socket-io-shi-xian-liao-tian-shi.html"
  - "/socket-io-shi-xian-liao-tian-shi.html"
---
没想到，自己写过的第一个聊天室，居然是用nodejs实现的【因为简单的啊】，使用起来很简单，要剖析里面的原理才是最重要的

先看代码：

html代码

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Socket.io</title>
        <link rel="stylesheet" type="text/css" href="css/main.css"/>
        <script src="//libs.useso.com/js/jquery/1.10.0/jquery.js"></script>
        <script src="/socket.io/socket.io.js"></script>
        <script src="js/chat.js"></script>
    </head>
    <body>
        <h1>Socket.io - Simple char Room</h1>
 
        <div>
            <span id="status">Connecting...</span>
            <input type="text" id="input" />
 
        </div>
        <div id="content"></div>
    </body>
</html>
```

js代码

```js
/**
 * Created by davidzhang on 14-10-22.
 */
$(function(){
    var content = $('#content');
    var status = $('#status');
    var input = $('#input');
    var myName = false;
 
    //建立socket链接
    socket = io.connect('http://localhost:3000');
 
    //收到server的连接确认
    socket.on('open',function(){
        status.text('Choose a name:');
    });
 
 
    //监听system事件，判断welcome或disconnect，打印系统消息
    socket.on('system',function(json){
        var p = '';
        if(json.type == 'welcome'){
 
            if(myName == json.text) {
                status.text(myName + ':').css('color', json.color);
            }
            p = '<p style="background:"'+json.color+'">system @ '+json.time+':Welcome ' + json.text + '</p>';
 
        }else if(json.type == 'disconnect'){
            p = '<p style="background:"'+json.color+'">system @ '+json.time+' : Bye ' + json.text + '</p>';
 
        }
 
        content.prepend(p);
 
    });
 
 
    //监听message事件，打印消息
    socket.on(message,function(json){
        var p = '<p<span style="color:"'+json.color+';">'+ json.author + '</span>@ ' + json.time +':' + json.text + '</p>';
        content.prepend(p);
    });
 
    input.keydown(function(e){
        if(e.keyCode == 13){
            var msg = $(this).val();
            if(!msg) return false;
            socket.send(msg);
            $(this).val('');if(myName==false){myName=msg}}})});
```

css代码

```css
* {padding:0px; margin:0px;}
body{font-family:tahoma; font-size:12px;margin:10px;}
p {line-height:18px;padding:2px;}
div {width:500px;}
#content {
    padding:5px;
    background:#ddd;
    border-radius:5px;
    border:1px solid #CCC;
    margin-top:10px;
}
#input {
    border-radius:2px;
    border:1px solid #ccc;
    margin-top:10px;
    padding:5px;
    width:380px;
}
#status {
    width:100px;
    display:block;
    float:left;
    margin-top:15px;
}
```

服务器端的代码

```js
var express = require('express');
var path = require("path");
var app = express();
var server = require("http").createServer(app);
var io = require("socket.io").listen(server);
 
//设置日志级别
io.set("log level", 1);
 
io.on('connection',function(socket){
    socket.emit("open");
 
    //构造客户端对象
    var client = {
        socket:socket,
        name:false,
        color:getColor()
    }
 
    socket.on('message',function(msg){
 
        var obj = {time:getTime(),color:client.color};
 
        if(!client.name){
            client.name = msg;
            obj['text'] = client.name;
            obj['author'] = 'System';
            obj['type'] = 'welcome';
            console.log(client.name + 'login');
 
            //返回欢迎语
            socket.emit('system',obj);
            //广播新用户已登录
            socket.broadcast.emit('system',obj);
        }else{
            obj['text'] = msg;
            obj['author'] = client.name;
            obj['type'] = 'message';
            console.log(client.name+'say:'+msg);
 
            //返回消息
            socket.emit('message',obj);
            //广播向其他用户消息
            socket.broadcast.emit('message',obj);
        }
 
    });
 
    socket.on('disconnect',function(){
        var obj = {
            time:getTime(),
            color:client.color,
            author:"System",
            text:client.name,
            type:'disconnect'
        };
 
        //广播用户已退出
        socket.broadcast.emit('system',obj);
        console.log(client.name+'Disconnect');
    });
});
 
//express 基本设置
app.configure(function(){
    app.set('port',process.env.PORT || 3000);
    app.set('views',__dirname + '/views');
    app.use(express.favicon());
    app.use(express.logger('dev'));
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(app.router);
    app.use(express.static(path.join(__dirname,'public')));
});
 
app.configure('development',function(){
    app.use(express.errorHandler());
});
 
//指定websocket的客户端的html文件
app.get('/',function(req,res){
    res.sendfile('views/chat.html');
});
 
server.listen(app.get('port'),function(){
    console.log('Express server listening on port '+app.get('port'));
});
 
var getTime=function(){
  var date = new Date();
  return date.getHours()+":"+date.getMinutes()+":"+date.getSeconds();
}
 
var getColor=function(){
  var colors = ['aliceblue','antiquewhite','aqua','aquamarine','pink','red','green',
                'orange','blue','blueviolet','brown','burlywood','cadetblue'];
  return colors[Math.round(Math.random() * 10000 % colors.length)];
}
```

这里的服务器是使用nodejs的express，当然里面使用的是nodejs的socket.io这个库，使用起来是很酷的，大家可以操作一下。

如果想需要真个代码的话，可以去这里

https://github.com/zhangda89/Socket-chat-Room

