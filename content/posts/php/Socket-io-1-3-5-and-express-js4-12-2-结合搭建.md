---
title: "Socket.io 1.3.5 and express.js 4.12.2 结合搭建"
date: "2025-06-30 15:15:45"
slug: "socketio-135-and-expressjs-4122-jie-he-da-jian"
categories: ["技术"]
tags: ["SocketIO", "ExpressJS"]
aliases:
  - "/2025/06/30/Socket.io-1.3.5-and-express.js-4.12.2-结合搭建/"
  - "/2025/06/30/Socket.io-1.3.5-and-express.js-4.12.2-结合搭建.html"
  - "/Socket.io-1.3.5-and-express.js-4.12.2-结合搭建/"
  - "/Socket.io-1.3.5-and-express.js-4.12.2-结合搭建.html"
  - "/2025/06/30/Socket-io-1-3-5-and-express-js4-12-2-结合搭建/"
  - "/2025/06/30/Socket-io-1-3-5-and-express-js4-12-2-结合搭建.html"
  - "/2025/06/30/socketio-135-and-expressjs-4122-jie-he-da-jian/"
  - "/2025/06/30/socketio-135-and-expressjs-4122-jie-he-da-jian.html"
  - "/socketio-135-and-expressjs-4122-jie-he-da-jian.html"
---
可以在app.js同目录下建立一个文件，如io.js

里面的代码如下：

```js
var io = require('socket.io')();
//这段代码可以随意自己修改，根据业务需求来定
io.on('connection', function (socket) {
  socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });
});
module.exports = io;
```

下一步就是修改bin/www这个文件（省略号代表还有其他的代码）

```js
var app = require('../app');

var io = require('../io');//这里引入刚才加的文件

var server = require('http').Server(app);

io.attach(server);//加入这段代码
server.listen(8080);
```

前端的代码需要这样写：

```html
<script src="/socket.io/socket.io.js"></script>
<script>
$(document).ready(function(){
    var socket = io();//这里是注意点
socket.on('news', function (data) {
console.log(data);
});
});
</script>
```

好了大功告成！


