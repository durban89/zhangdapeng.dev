---
title: "Nodejs的加载html页面和远程获取页面进行匹配操作"
date: "2025-06-17 15:51:17"
slug: "nodejs-de-jia-zai-html-ye-mian-he-yuan-cheng-huo-qu-ye-mian-jin-xing-pi-pei-cao-zuo"
categories: ["技术"]
tags: ["NodeJS", "JavaScript"]
aliases:
  - "/2025/06/17/Nodejs的加载html页面和远程获取页面进行匹配操作/"
  - "/2025/06/17/Nodejs的加载html页面和远程获取页面进行匹配操作.html"
  - "/Nodejs的加载html页面和远程获取页面进行匹配操作/"
  - "/Nodejs的加载html页面和远程获取页面进行匹配操作.html"
  - "/2025/06/17/nodejs-de-jia-zai-html-ye-mian-he-yuan-cheng-huo-qu-ye-mian-jin-xing-pi-pei-cao-zuo/"
  - "/2025/06/17/nodejs-de-jia-zai-html-ye-mian-he-yuan-cheng-huo-qu-ye-mian-jin-xing-pi-pei-cao-zuo.html"
  - "/nodejs-de-jia-zai-html-ye-mian-he-yuan-cheng-huo-qu-ye-mian-jin-xing-pi-pei-cao-zuo.html"
---
1，nodejs 的加载html页面

```javascript
function detail(response, query_param){
	fs.readFile('./sina_weibo.html','utf-8',function(err, data) {//读取内容
        if(err) throw err;
        response.setHeader('content-type', 'text/html;charset=utf-8');
		response.writeHead(200, {"Content-Type": "text/plain"});
		response.write(data);
		response.end();
    });
	
}
```

2，远程获取页面并进行匹配的操作

```javascript
function blog(response, query_param){
    // fs.readFile('./sina_weibo.html','utf-8',function(err, data) {//读取内容
    //     if(err) throw err;
    //     return data;
    // });

	response.setHeader('content-type', 'text/html;charset=utf-8');
	response.writeHead(200, {"Content-Type": "text/plain"});
    var options = { 
        host: '10.211.55.5', 
        port: 8006, 
        path: '/detail'
    };
    
    var html = '追加变量的变量 ';
    http.get(options, function(res) { 
        res.on('data', function(data) { 
            console.log("data here = " + data);
            // collect the data chunks to the variable named "html" 
            html += data; 
            html += "这里在获取数据";
        }).on('end', function() { 
            // the whole of webpage data has been collected. parsing time! 
            var title = $(html).find('div h3 span').each(function($this){ 
                var a = $(this).children('a').attr('href'); 
                var b = $(this).children('a').text();
                console.log(b + ":" + options.host + a); 
                html += b + ":" + options.host + a;
                response.write(html);
            });
            html += "这里在循环数据";
        });
        html += '结束';
    });
	response.end();
}
```

执行上面的方法，在nodejs里面需要加入几个模块

```javascript
var querystring = require("querystring");
var fs = require("fs");
var http = require('http');
var $ = require('jquery');
```

如果没有安装jquery的话，执行下面的命令

```javascript
npm install jquery
```

如果没有安装npm 的话，建议去google一下吧
