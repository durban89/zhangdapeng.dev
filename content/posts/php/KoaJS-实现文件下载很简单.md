---
title: "KoaJS 实现文件下载很简单"
date: "2025-07-03 11:58:13"
slug: "koajs-shi-xian-wen-jian-xia-zai-hen-jian-dan"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/03/KoaJS-实现文件下载很简单/"
  - "/2025/07/03/KoaJS-实现文件下载很简单.html"
  - "/KoaJS-实现文件下载很简单/"
  - "/KoaJS-实现文件下载很简单.html"
  - "/2025/07/03/koajs-shi-xian-wen-jian-xia-zai-hen-jian-dan/"
  - "/2025/07/03/koajs-shi-xian-wen-jian-xia-zai-hen-jian-dan.html"
  - "/koajs-shi-xian-wen-jian-xia-zai-hen-jian-dan.html"
---
Express框架下载文件的方法，我想已经有人已经知道了。

这里说下Koajs的方法。

首先设置Content-disposition

```js
let filename = 'xxxx';
ctx.set('Content-disposition', 'attachment; filename=' + filename + '.pdf');//attachment
```

或者

```js
ctx.set('Content-disposition', 'inline; filename=' + filename + '.pdf');//inline
```

以上两种的区别是一个是attachment，意思就是附件，还有一种是inline，意思就是内附。区别就是attachment打开的时候可以下载文件，inline有时候可以下载，有时候可以直接浏览，好像跟浏览器有关。

然后设置下文件类型

```js
ctx.set('Content-type', 'application/pdf');
```

给body赋值，这里是一个Buffer。

然后把文件内容读出来

`let gReadData = new Buffer();`//这里自己根据自己的具体情况去实现就好了。

在函数最后

```js
return ctx.body = gReadData;
```

整体代码大概如下：

```js
module.exports.downloadPdf = async (ctx,next) => {
  let filename = 'xxxx';
  ctx.set('Content-disposition', 'attachment; filename=' + filename + '.pdf');
  ctx.set('Content-type', 'application/pdf');
  return ctx.body = gReadData;
}
```


