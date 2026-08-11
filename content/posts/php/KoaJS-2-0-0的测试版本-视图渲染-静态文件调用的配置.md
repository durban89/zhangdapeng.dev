---
title: "KoaJS 2.0.0的测试版本-视图渲染、静态文件调用的配置"
date: "2025-07-02 11:31:52"
slug: "koajs-200-de-ce-shi-ban-ben-shi-tu-xuan-ran-jing-tai-wen-jian-diao-yong-de-pei-zhi"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/02/KoaJS-2.0.0的测试版本-视图渲染、静态文件调用的配置/"
  - "/2025/07/02/KoaJS-2.0.0的测试版本-视图渲染、静态文件调用的配置.html"
  - "/KoaJS-2.0.0的测试版本-视图渲染、静态文件调用的配置/"
  - "/KoaJS-2.0.0的测试版本-视图渲染、静态文件调用的配置.html"
  - "/2025/07/02/KoaJS-2-0-0的测试版本-视图渲染-静态文件调用的配置/"
  - "/2025/07/02/KoaJS-2-0-0的测试版本-视图渲染-静态文件调用的配置.html"
  - "/2025/07/02/koajs-200-de-ce-shi-ban-ben-shi-tu-xuan-ran-jing-tai-wen-jian-diao-yong-de-pei-zhi/"
  - "/2025/07/02/koajs-200-de-ce-shi-ban-ben-shi-tu-xuan-ran-jing-tai-wen-jian-diao-yong-de-pei-zhi.html"
  - "/koajs-200-de-ce-shi-ban-ben-shi-tu-xuan-ran-jing-tai-wen-jian-diao-yong-de-pei-zhi.html"
---
针对koa2.0.0的测试版本，在使用的过程中遇到了很多的问题，这篇文章讲解一下如何进行操作html的调用和静态文件的调用

因为koa2.0.0版本的升级，很多的中间件都没有跟随着一起调整，所以有些中间件就出现了很多问题，这里说的就是针对试图文件的调用渲染和静态文件的调用

视图文件的调用使用的是如下的中间件：koa-swig

安装koa-swig:

```bash
cnpm install koa-swig --save
```

配置如下：

```bash
app.context.render = co.wrap(render({
  root: path.join(__dirname, 'dest'),
  autoescape: true,
  cache: 'memory', // disable, set to false 
  ext: 'html'
}));
```

路由中调用的方式如下：

```bash
router.get('/home', (ctx, next) => {
  return next().then(() => {
    ctx.render('index.html');
  });
});
```

这里到这里就解决了视图调用的问题，访问的时候如果页面中调用的是本地的js或者css的话，会包404的错误，就是找不到对应的路由，OK，下面记录下。

这里调用得了两个中间件:koa-convert,koa-static

```bash
const convert = require('koa-convert');
const serve = require('koa-static');
```

安装这两个中间件：

```bash
cnpm install koa-static koa-convert --save
```

对应的配置如下：

```bash
app.use(convert(serve(__dirname + '/dest')));
```

这里就是很简单了，刚开始的时候是无效的，后来在github上问了一下，就找打了解决办法。可以到这里看下：<https://github.com/koajs/static/issues/59>

好了，到这里两个部分的操作就完成了。


