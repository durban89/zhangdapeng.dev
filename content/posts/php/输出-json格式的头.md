---
title: "输出 json格式的头"
date: "2025-06-19 13:55:02"
slug: "shu-chu-json-ge-shi-de-tou"
categories: ["技术"]
tags: ["JSON"]
aliases:
  - "/2025/06/19/输出-json格式的头/"
  - "/2025/06/19/输出-json格式的头.html"
  - "/输出-json格式的头/"
  - "/输出-json格式的头.html"
  - "/2025/06/19/shu-chu-json-ge-shi-de-tou/"
  - "/2025/06/19/shu-chu-json-ge-shi-de-tou.html"
  - "/shu-chu-json-ge-shi-de-tou.html"
---
标准写法的 application/json，人们有时候也习惯text/json，但是text/json不兼容的，建议你用标准application/json  
  
服务端 向 客户端 发送 JSON数据 时:  

Content-Type = 'application/json;charset=UTF-8'  
  
服务端 向 客户端 发送 JS 代码 时:  
  
Content-Type = 'text/javascript;charset=UTF-8'  
  
服务端 判断 客户端 提交的是否是 JSON数据 时 :

```bash
Content-Type = 'application/json;charset=UTF-8'
Content-Type = 'text/json;charset=UTF-8'
Content-Type = 'text/javascript;charset=UTF-8'
Content-Type = 'application/javascript;charset=UTF-8'
```

只要 Content-Type 满足上面4个条件中的 任意一个时,就可以认为提交的数据是 JSON数据
