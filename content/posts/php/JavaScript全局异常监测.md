---
title: "JavaScript全局异常监测"
date: "2025-07-14 14:44:50"
slug: "javascript-quan-ju-yi-chang-jian-ce"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/07/14/JavaScript全局异常监测/"
  - "/2025/07/14/JavaScript全局异常监测.html"
  - "/JavaScript全局异常监测/"
  - "/JavaScript全局异常监测.html"
  - "/2025/07/14/javascript-quan-ju-yi-chang-jian-ce/"
  - "/2025/07/14/javascript-quan-ju-yi-chang-jian-ce.html"
  - "/javascript-quan-ju-yi-chang-jian-ce.html"
---
JavaScript全局异常监测

在写代码的过程中一直遇到一个问题，就是如何来监测异常代码的处理

如果在开发中，可以使用chrome dev tools来监测代码异常，并能时刻监测代码的异常部分

但是在代码上线之后，如果监测代码就比较麻烦

这里提供一个监测全局的代码，虽然也很多网站有关于类似代码的分享

这里主要是记录下，防止忘记，找起来麻烦，关键是这个代码是我自己经过测试使用，比较完善的一个，也许别人也有其他版本

但是我这个版本我保证是可以用的

只需要放在`<script></script>`标签里面就可以了，如果需要将异常的代码信息上传到服务器，可以自己修改下，将`console.log`部分改成数据请求的代码就可以了

代码如下

```javascript
window.onerror = function(msg,url,l){
  txt="There was an error on this page.\n\n"
  txt+="Error: " + msg + "\n"
  txt+="URL: " + url + "\n"
  txt+="Line: " + l + "\n\n"
  txt+="Click OK to continue.\n\n"
  console.log(txt);
  return true
};
```
