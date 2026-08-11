---
title: "iframe无边框示例"
date: "2025-07-11 11:16:19"
slug: "iframe-wu-bian-kuang-shi-li"
categories: ["技术"]
tags: ["iframe"]
aliases:
  - "/2025/07/11/iframe无边框示例/"
  - "/2025/07/11/iframe无边框示例.html"
  - "/iframe无边框示例/"
  - "/iframe无边框示例.html"
  - "/2025/07/11/iframe-wu-bian-kuang-shi-li/"
  - "/2025/07/11/iframe-wu-bian-kuang-shi-li.html"
  - "/iframe-wu-bian-kuang-shi-li.html"
---
iframe无边框示例，网上很多帖子其实只告诉了我们一部分

```html
<iframe src="https://gowhich.com" id='other_ad' width="100%" height="568" scrolling="yes" frameborder="no" border="0" marginwidth="0" marginheight="0" allowtransparency="yes" style="border:0"></iframe>
```

如果单单只是这一部分的话，是不起作用的（在某些情况下）

其实主要原因是部分浏览器默认的margin和padding并没有设置为0，实际上还需要加一些css style

```html
<style>
  * {
    margin:0;
    padding:0;
  }

  html {
    font-size: 3.125vw;
  }
</style>
```

完整的示例代码如下

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset=UTF-8>
  <meta http-equiv=X-UA-Compatible>
  <meta name=format-detection content="telephone=no">
  <meta name=viewport content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,user-scalable=no">
  <link rel="shortcut icon" href="yours">
  <title>小游戏</title>
</head>
<style>
  * {
    margin:0;
    padding:0;
  }

  html {
    font-size: 3.125vw;
  }
</style>
<body style="background:#270f48">
  <div id="app" v-cloak>
    <iframe src="https://gowhich.com" id='other_ad' width="100%" height="568" scrolling="yes" frameborder="no" border="0" marginwidth="0" marginheight="0" allowtransparency="yes" style="border:0"></iframe>
  </div>
</body>
</html>
```
