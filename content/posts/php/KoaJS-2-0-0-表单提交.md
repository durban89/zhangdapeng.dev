---
title: "KoaJS 2.0.0 表单提交"
date: "2025-07-02 11:31:55"
slug: "koajs-200-biao-dan-ti-jiao"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/02/KoaJS-2.0.0-表单提交/"
  - "/2025/07/02/KoaJS-2.0.0-表单提交.html"
  - "/KoaJS-2.0.0-表单提交/"
  - "/KoaJS-2.0.0-表单提交.html"
  - "/2025/07/02/KoaJS-2-0-0-表单提交/"
  - "/2025/07/02/KoaJS-2-0-0-表单提交.html"
  - "/2025/07/02/koajs-200-biao-dan-ti-jiao/"
  - "/2025/07/02/koajs-200-biao-dan-ti-jiao.html"
  - "/koajs-200-biao-dan-ti-jiao.html"
---
对于koa2.0.0的表单提交如何处理，也是费了我很久的时间，在多次尝试与研究之下，可以这样来处理：

```bash
proxy.post('/admin/:path', (ctx, next) => {
  const url = ctx.config.hostDomain + '/admin/' +ctx.params.path;
  const options = {
    timeout: ctx.config.httpTimeout,
    method: ctx.request.method,
    headers: ctx.request.headers,
    data: ctx.request.body
  };
  return next().then(() => {
    const request = urllib.request(url, options);
    return request.then( (data) => {
      ctx.body = data.data.toString()
    });
  }).catch((err) => {
    console.log(err);
  });
});
```

我这里只是做了一个接口的调用，其实最重要的是在获得request后如何去进行对应的promise的操作和获取结果，这里其实很简单的：

```javascript
return next().then(() => {
  const request = urllib.request(url, options);
  return request.then( (data) => {
    ctx.body = data.data.toString()
  });
}).catch((err) => {
  console.log(err);
});
```

注意这里的两个return操作，做完request的操作后，直接在开头进行一个return操作就可以了，这样body的值也回调过去了。


