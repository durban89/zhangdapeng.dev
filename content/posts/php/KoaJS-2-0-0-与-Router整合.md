---
title: "KoaJS 2.0.0 与 Router整合"
date: "2025-07-02 11:31:43"
slug: "koajs-200-yu-router-zheng-he"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/02/KoaJS-2.0.0-与-Router整合/"
  - "/2025/07/02/KoaJS-2.0.0-与-Router整合.html"
  - "/KoaJS-2.0.0-与-Router整合/"
  - "/KoaJS-2.0.0-与-Router整合.html"
  - "/2025/07/02/KoaJS-2-0-0-与-Router整合/"
  - "/2025/07/02/KoaJS-2-0-0-与-Router整合.html"
  - "/2025/07/02/koajs-200-yu-router-zheng-he/"
  - "/2025/07/02/koajs-200-yu-router-zheng-he.html"
  - "/koajs-200-yu-router-zheng-he.html"
---
最近koajs更新了一个很重要的版本，就是2.0.0,虽然这个版本是一个还在开发中的版本，但是已经可以下载使用了，当然，我用来下，唉，遗憾的是，虽然koa更新了，但是对应的中间插件并没有更新，这个是为什么呢，其他中间件的人不积极呗，只能试用了下，最重要的一个就是，Router这个中间件，既然也没有更新，不兼容最新版本的koa，好吧，还有在issue中发现了两点，已经有人根据koa-router，自己写了一个koa-66,使用完还不错，下面正式记录一下：

安装 koa@2.0.0-alpha.2

```javascript
cnpm install koa@2.0.0-alpha.2 --save
```

安装koa-66

```bash
cnpm install koa-66 --save
```

安装完了看个示例吧,app.js代码如下

```javascript
'use strict';
const Koa = require('koa');
const app = new Koa();
const co = require('co');
const Router = require('koa-66');
// const router = new Router();
const mountRouter = new Router();
const Controller = require('./router');
app.use((ctx, next) => {
  const start = new Date;
  return next().then(() => {
    const ms = new Date - start;
    console.log(`${ctx.method} ${ctx.url} - ${ms}`);
  });
});
// app.use((ctx) => {
//   ctx.body = 'Hello World!';
// });
mountRouter.mount('/blog', Controller.router);
app.use(mountRouter.routes());
app.listen(3002);
```

router.js代码如下：

```javascript
/**
 * Created by durban on 15/10/17.
 */
const Router = require('koa-66');
const router = new Router();
router.get('/home', (ctx, next) => {
  return next().then(() => {
    console.log(ctx);
    console.log(ctx.req);
    ctx.body = 'Router Hello World!';
  });
});
router.get('/views/:id', (ctx,next) => {
  return next().then(() => {
    console.log(ctx.params);
    ctx.body = 'views';
  });
});
router.get('/about', (ctx, next) => {
  return next().then(() => {
    ctx.body = 'about';
  });
});
module.exports.router = router;
```

好了，运行app.js,开始测试吧，终于搞定了router的代码不用跟app.js写在一起了。

当然这里的node版本是最新的版本v4.2.1。


