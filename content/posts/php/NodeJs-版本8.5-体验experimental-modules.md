---
title: "NodeJs 版本8.5 体验experimental-modules"
date: "2025-07-03 17:37:10"
slug: "nodejs-ban-ben-85-ti-yan-experimental-modules"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/NodeJs-版本8.5-体验experimental-modules/"
  - "/2025/07/03/NodeJs-版本8.5-体验experimental-modules.html"
  - "/NodeJs-版本8.5-体验experimental-modules/"
  - "/NodeJs-版本8.5-体验experimental-modules.html"
  - "/2025/07/03/nodejs-ban-ben-85-ti-yan-experimental-modules/"
  - "/2025/07/03/nodejs-ban-ben-85-ti-yan-experimental-modules.html"
  - "/nodejs-ban-ben-85-ti-yan-experimental-modules.html"
---
最近NodeJs 版本 8.5 已经支持了 ESM module，感觉之前的babel编译可以放弃不用了，不过这个只是一个实验性的，具体稳定与否，是否可以上生产环境，还是需要测试一段时间的。

体验环境搭建：

NodeJs: v8.5.0

依赖包：

```js
"dependencies": {
  "axios": "^0.16.2",
  "koa": "^2.3.0",
  "koa-router": "^7.2.1",
  "koa-views": "^6.1.0",
  "twig": "^1.10.5"
}
```

这里使用的是koajs，大家可以使用下express

模块引入不在需要require了，哈哈，感觉不一样的体验

```js
import koa from 'koa';
import koaRouter from 'koa-router';
import axios from 'axios';
import views from 'koa-views';
import path from 'path';
```

像这样是不是感觉，瓦萨，还不错

继续看下面的配置

```js
app.use(views(path.resolve() + '/views', {
  map: {
    html: 'twig',
  },
  extension: 'twig',
}));
```

对于web开发，推荐koa-views,可以支持很多模板，想用哪个就用哪个

```js
const viewsTest = async (ctx, next) => {
  ctx.state = {
    title: 'viewsTest',
  };

  await ctx.render('views_test', {
    title: 'viewsTest',
  });
  return next();
};

router.get('/views', viewsTest);

app
  .use(router.routes())
  .use(router.allowedMethods());

app.listen(8888);
```

好了，我的index.mjs创建完成，注意这里的index文件是以mjs结尾的 ，不然稍后运行的话是不会执行的。

view_test.twig模板其实很简单，为了测试简单加下就好了。

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
</head>

<body>
{{ title }}
</body>

</html>
```

目录结果也给大家演示下

|-index.mjs

|-node\_modules

|-package.json

|-package-lock.json

|-views

  |-views\_test.twig

运行我们的程序

```bash
node --experimental-modules index.mjs
```

出现下面的提示就是运行起来了

```bash
$ node --experimental-modules index.mjs
(node:6999) ExperimentalWarning: The ESM module loader is experimental.
```

感觉开发代码又便捷了很多呀。
