---
title: "Nodejs的安装、测试及hello world"
date: "2025-06-09 16:19:55"
slug: "nodejs-de-an-zhuang-ce-shi-ji-hello-world"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/09/Nodejs的安装、测试及hello-world/"
  - "/2025/06/09/Nodejs的安装、测试及hello-world.html"
  - "/Nodejs的安装、测试及hello-world/"
  - "/Nodejs的安装、测试及hello-world.html"
  - "/2025/06/09/Nodejs的安装-测试及hello-world/"
  - "/2025/06/09/Nodejs的安装-测试及hello-world.html"
  - "/2025/06/09/nodejs-de-an-zhuang-ce-shi-ji-hello-world/"
  - "/2025/06/09/nodejs-de-an-zhuang-ce-shi-ji-hello-world.html"
  - "/nodejs-de-an-zhuang-ce-shi-ji-hello-world.html"
---
### [安装：](#1)

现在地址：http://www.nodejs.org/download/

可以根据自己的系统类型，选择对应的安装文件，进行安装

### [测试](#2)

写一个简单的hello world

```js
var http = require('http');
http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World\n');
}).listen(8124);
console.log('Server running at http://127.0.0.1:8124/');
```
使用浏览器，输入url地址`http://127.0.0.1:8124/`，可以看到输出Hello World字符串，如果没有说明出现问题了。
