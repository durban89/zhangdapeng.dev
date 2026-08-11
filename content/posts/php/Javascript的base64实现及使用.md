---
title: "Javascript的base64实现及使用"
date: "2025-07-10 11:52:44"
slug: "javascript-de-base64-shi-xian-ji-shi-yong"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/07/10/Javascript的base64实现及使用/"
  - "/2025/07/10/Javascript的base64实现及使用.html"
  - "/Javascript的base64实现及使用/"
  - "/Javascript的base64实现及使用.html"
  - "/2025/07/10/javascript-de-base64-shi-xian-ji-shi-yong/"
  - "/2025/07/10/javascript-de-base64-shi-xian-ji-shi-yong.html"
  - "/javascript-de-base64-shi-xian-ji-shi-yong.html"
---
实例及实现原理如下

```js
var uploadKey = 'avatar/20191212/userid-1.png';

// key 进行base64处理
// 第一步使用encodeURIComponent() 函数把字符串作为 URI 组件进行编码
// 第二步使用unescape() 函数对通过 escape() 编码的字符串进行解码
// 第三步使用btoa() 方法用于创建一个 base-64 编码的字符串。该方法使用 "A-Z", "a-z", "0-9", "+", "/" 和 "=" 字符来编码字符串。base64 解码使用方法是 atob() 。

var key = btoa(unescape(encodeURIComponent(uploadKey)));

var url = "http://upload.qiniup.com/putb64/12" + '/key/' + key;
```

运行上面代码结果如下

```bash
> var uploadKey = 'avatar/20191212/userid-1.png';
< undefined
> var key = btoa(unescape(encodeURIComponent(uploadKey)));
< undefined
> var url = "http://upload.qiniup.com/putb64/12"+'/key/'+key; 
< undefined
> console.log(url)
  VM7861:1 http://upload.qiniup.com/putb64/12/key/YXZhdGFyLzIwMTkxMjEyL3VzZXJpZC0xLnBuZw==
> undefined
```

参考如下 https://stackoverflow.com/questions/246801/how-can-you-encode-a-string-to-base64-in-javascript

我们分解执行下

```bash
> var a = encodeURIComponent(uploadKey)
< undefined
> console.log(a)
< avatar%2F20191212%2Fuserid-1.png
> undefined
< var b = unescape(a);
> undefined
< console.log(b)
  avatar/20191212/userid-1.png
> undefined
< var c = btoa(b)
> undefined
< console.log(c)
  YXZhdGFyLzIwMTkxMjEyL3VzZXJpZC0xLnBuZw==
> undefined
```
