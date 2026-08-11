---
title: "KoaJS-2 实现验证码验证"
date: "2025-07-02 16:00:26"
slug: "koajs-2-shi-xian-yan-zheng-ma-yan-zheng"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/02/KoaJS-2-实现验证码验证/"
  - "/2025/07/02/KoaJS-2-实现验证码验证.html"
  - "/KoaJS-2-实现验证码验证/"
  - "/KoaJS-2-实现验证码验证.html"
  - "/2025/07/02/koajs-2-shi-xian-yan-zheng-ma-yan-zheng/"
  - "/2025/07/02/koajs-2-shi-xian-yan-zheng-ma-yan-zheng.html"
  - "/koajs-2-shi-xian-yan-zheng-ma-yan-zheng.html"
---
首先安装验证码插件

这里推荐使用ccap，这个插件是我在寻找过程中，觉得能跟koa搭配比较好的一个插件，其他的要不就是需要express，要不就是需要安装其他一系列比较大的类库。

```bash
npm install ccap --save
```

如何使用？

```js
const ccap = require('ccap')();
home.get('/home', (ctx, next) => {
  return next().then(() => {
    ctx.body = ctx.session.captcha;
  });
});
home.get('/captcha', (ctx, next) => {
  return next().then(() => {
    let ary = ccap.get();
    let txt = ary[0];
    let buf = ary[1];
    ctx.body = buf;
    ctx.type = 'image/png';
    ctx.session.captcha = txt;
  });
});
```


