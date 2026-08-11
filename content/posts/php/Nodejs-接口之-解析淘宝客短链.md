---
title: "Nodejs 接口之 解析淘宝客短链"
date: "2025-07-03 11:07:37"
slug: "nodejs-jie-kou-zhi-jie-xi-tao-bao-ke-duan-lian"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-接口之-解析淘宝客短链/"
  - "/2025/07/03/Nodejs-接口之-解析淘宝客短链.html"
  - "/Nodejs-接口之-解析淘宝客短链/"
  - "/Nodejs-接口之-解析淘宝客短链.html"
  - "/2025/07/03/nodejs-jie-kou-zhi-jie-xi-tao-bao-ke-duan-lian/"
  - "/2025/07/03/nodejs-jie-kou-zhi-jie-xi-tao-bao-ke-duan-lian.html"
  - "/nodejs-jie-kou-zhi-jie-xi-tao-bao-ke-duan-lian.html"
---
给你一个淘宝客的短链，如果获取他跳转后的地址，这是我最近在做个一个程序，使用node开发总体来说还是挺简答的。

大概说下流程

第一步：解析出这个短链最终的真实地址

我的第一个想法是，是不是需要啥啥接口才可以哇。但是我又想，这也太麻烦了，如果我访问了这个链接是不是就可以得到真实的链接了。好，到网上找到了一个request库，还是有实例哦，简单的不要不要的，赶紧弄了下，果然是有结果的。

```js
var r = request(url, function(err, res, body) {
  var uri = res.request.uri.href;
  console.log(uri);
}
```

可以了。地址拿到了，用浏览器打开试试，结果还是有问题，这个地址不是产品的真实地址，还是要做一个跳转的，好吧。

我又想，这个页面究竟是个啥，打开一看，其实里面就是个js函数，执行了就简单了，这个对于node来说真实小菜一碟哇。

突然让我想起来urllib这个库，嗯，不错很好用的。

开始用的时候，直接请求就以为能得到结果了，结果不是的，还需要在请求中加上referer，哈哈，也许是个漏洞吧，这样我就能解析出真实的地址了。

那先解决第一个问题就是node如何营造一个dom的环境，玩过dom的人肯定知道jsdom啦，然后在进行urllib请求根据302跳转获取到。

```js
jsdom.env(uri, function(err, window) {
  //都有window了，想干嘛就干嘛吧
}
```

之后就是获取最终headers里面的location

```js
var urlRes = urllib.request(real_jump_address, {
  method: 'GET',
  headers: {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Upgrade-Insecure-Requests': 1,
    'Host': 's.click.taobao.com',
    'Referer': uri
  }
}, function(err, data, res) {
  if (err) {
    throw err; // you need to handle error
  }
  // console.log(res.statusCode);
  console.log(res.headers.location);
  // data is Buffer instance
  // console.log('body ', data.toString());
});
```


