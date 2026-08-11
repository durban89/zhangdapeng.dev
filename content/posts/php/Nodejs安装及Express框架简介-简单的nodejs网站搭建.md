---
title: "Nodejs安装及Express框架简介-简单的nodejs网站搭建"
date: "2025-06-17 16:45:20"
slug: "nodejs-an-zhuang-ji-express-kuang-jia-jian-jie-jian-dan-de-nodejs-wang-zhan-da-jian"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/17/Nodejs安装及Express框架简介-简单的nodejs网站搭建/"
  - "/2025/06/17/Nodejs安装及Express框架简介-简单的nodejs网站搭建.html"
  - "/Nodejs安装及Express框架简介-简单的nodejs网站搭建/"
  - "/Nodejs安装及Express框架简介-简单的nodejs网站搭建.html"
  - "/2025/06/17/nodejs-an-zhuang-ji-express-kuang-jia-jian-jie-jian-dan-de-nodejs-wang-zhan-da-jian/"
  - "/2025/06/17/nodejs-an-zhuang-ji-express-kuang-jia-jian-jie-jian-dan-de-nodejs-wang-zhan-da-jian.html"
  - "/nodejs-an-zhuang-ji-express-kuang-jia-jian-jie-jian-dan-de-nodejs-wang-zhan-da-jian.html"
---
用node.js建博客(一) - node.js安装及Express框架简介

### [技术准备](#1):

[node.js](http://nodejs.org/) 写本文的时候我采用的版本是0.4.5, Win用户需要自行编译node.exe  
[npm](http://npmjs.org/) 类似Ruby中的RubyGems, node.js包依赖管理工具  
[express](http://expressjs.com/) 类似Ruby中的Sinatra, 一个简单的Web框架  
[markdown.js](https://github.com/evilstreak/markdown-js) node.js中的markdown解析器， 什么是markdown?? 用过GitHub的朋友应该知道，readme.md文件  
[prettify.js](https://code.google.com/p/google-code-prettify/) google-code-prettify, 提供在线的语法高亮支持，支持语法包括C-like, Java, Python, shell等大多数语言。

### [安装Nodejs](#2)

可以参考我的这篇文章：[http://www.gowhich.com/blog/40](https://www.gowhich.com/blog/40)

### [安装 npm](#3)

1）. Unix/Linux:

```bash
$ curl http://npmjs.org/install.sh | sh
```

安装完成后

```bash
$ npm -v
```

看看是否安装成功

2）. Windows:

待补充

### [Nodejs的express框架](#4)

如果你用过Ruby的Sinatra.rb, 会觉得Express非常熟悉。Express作者是参考sinatra, 写了一个基于node.js的实现。

1. 安装

由于这个有点特殊，需要为npm添加-g参数， 刚开始安装的时候没有加，导致不能使用epress 命令行参数

```bash
$ npm install -g express
$ epxress -v #看看是否安装成功
```

2. 创建一个express项目看看

```bash
$ express nodeblog
$ cd nodeblog
```

3. express目录结构

Express 目录结构

```ini
目录/文件             说明
./               根目录，我们的node.js代码都会方这个目录
package.json          npm依赖配置文件， 类似ruby中的Gemfile, java Maven中的pom.xml文件.
                一会需要在这里添加 markdownjs-js 项目依赖
app.js             项目的入口文件
public/
  javascript/
  stylesheets/
  images/           存放静态资源文件, jquery/prettify.js等静态库会方这里，当然自己编写的前端代码也可以放这里
views/             模板文件, express默认采用jade, 当然，你也可以使用自己喜欢的haml,JES, coffeeKup,
                jQueryTemplate等模板引擎
node_modules/          存放npm安装到本地依赖包，依赖包在package.json文件中声明，使用npm install指令安装
```

4. 运行程序看看

```bash
$ npm install
$ node app.js
```

访问http://localhost:3000/  
  
我们看看app.js文件:

```javascript
var express = require('express');  
var app = module.exports = express.createServer();  
  
// Express 程序配置  
app.configure(function(){  
  app.set('views', __dirname + '/views');  
  app.set('view engine', 'jade');  
  app.use(express.bodyParser());  
  app.use(express.methodOverride());  
  app.use(app.router);  
  app.use(express.static(__dirname + '/public'));  
});  
  
// url路由  
app.get('/', function(req, res){  
  res.render('index', {  
    title: 'Express'  
  });  
});  
  
app.listen(3000);
```

下面代码将url渲染到 index.jade文件, 并且传递title参数:

```javascript
app.get('/', function(req, res){  
  res.render('index', {  
    title: 'Express'  
  });  
});
```

其中传递变量title, 在views/layout.jade文件中有定义, 我们这里将title改成"Node Blog":

```javascript
app.get('/', function(req, res){ 
  res.render('index', {  
    title: 'Node Blog'  
  });  
});  
```

修改后效果如下所示:  
  
到这里， Express 入门介绍就到这里，进一步内容需要看参考资料中的相关文档

### [参考资料](#5):

jade GitHub仓库: https://github.com/visionmedia/jade

[《Express中文入门手册》](http://www.csser.com/tools/express-js/express-guide-reference-zh-CN.html)

[《markdown语法说明》](http://qingbo.net/picky/502-markdown-syntax.html)

[《google-code-prettify使用说明》](https://google-code-prettify.googlecode.com/svn/trunk/README.html)

[《使用node.js, markdownjs, prettify.js打造个人写作平台》](http://www.cnblogs.com/sanshi/archive/2011/03/16/1986468.html)

[《将node.js应用上传到vmc平台》](http://witcheryne.iteye.com/blog/1160111), 这是我前两天写的一篇， 关于如何将应用上传到vmc服务器，后面篇幅不会再做介绍。

http://witcheryne.iteye.com/blog/1165067
