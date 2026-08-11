---
title: "JavaScript实现 邮箱登陆跳转"
date: "2025-06-27 10:59:13"
slug: "javascript-shi-xian-you-xiang-deng-lu-tiao-zhuan"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/JavaScript实现-邮箱登陆跳转/"
  - "/2025/06/27/JavaScript实现-邮箱登陆跳转.html"
  - "/JavaScript实现-邮箱登陆跳转/"
  - "/JavaScript实现-邮箱登陆跳转.html"
  - "/2025/06/27/javascript-shi-xian-you-xiang-deng-lu-tiao-zhuan/"
  - "/2025/06/27/javascript-shi-xian-you-xiang-deng-lu-tiao-zhuan.html"
  - "/javascript-shi-xian-you-xiang-deng-lu-tiao-zhuan.html"
---
javascript实现 邮箱登陆跳转，代码如下

```js
<script type="text/javascript">
var hash={
    'qq.com': 'http://mail.qq.com',
    'gmail.com': 'http://mail.google.com',
    'sina.com': 'http://mail.sina.com.cn',
    '163.com': 'http://mail.163.com',
    '126.com': 'http://mail.126.com',
    'yeah.net': 'http://www.yeah.net/',
    'sohu.com': 'http://mail.sohu.com/',
    'tom.com': 'http://mail.tom.com/',
    'sogou.com': 'http://mail.sogou.com/',
    '139.com': 'http://mail.10086.cn/',
    'hotmail.com': 'http://www.hotmail.com',
    'live.com': 'http://login.live.com/',
    'live.cn': 'http://login.live.cn/',
    'live.com.cn': 'http://login.live.com.cn',
    '189.com': 'http://webmail16.189.cn/webmail/',
    'yahoo.com.cn': 'http://mail.cn.yahoo.com/',
    'yahoo.cn': 'http://mail.cn.yahoo.com/',
    'eyou.com': 'http://www.eyou.com/',
    '21cn.com': 'http://mail.21cn.com/',
    '188.com': 'http://www.188.com/',
    'foxmail.coom': 'http://www.foxmail.com'
};

$(function(){
    $(".mail").each(function() {
        var url = $(this).text().split('@')[1];
        for (var j in hash){
            $(this).attr("href", hash[url]);
        }
    });
})
</script>
```

js弹出新窗口而不会被浏览器阻止的方法

```html
<form id="emailForm" action="mail.qq.com" method="get" target="_blank">
    <input type="hidden" id="isHidden" value="yiwo"/>
</form>
<script type="text/javascript">
function(){
  $("#emailForm").attr("action","http://" + gotoEmail($("#regEmail").val()));
  $("#emailForm").submit();
  window.location.href="index.action";}
  
</script>
```

