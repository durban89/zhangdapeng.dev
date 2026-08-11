---
title: "移动端H5 iOS开发中 Fetch Api使用的注意事项"
date: "2025-07-10 10:58:01"
slug: "yi-dong-duan-h5-ios-kai-fa-zhong-fetch-api-shi-yong-de-zhu-yi-shi-xiang"
categories: ["技术"]
tags: ["iOS", "H5"]
aliases:
  - "/2025/07/10/移动端H5-iOS开发中-Fetch-Api使用的注意事项/"
  - "/2025/07/10/移动端H5-iOS开发中-Fetch-Api使用的注意事项.html"
  - "/移动端H5-iOS开发中-Fetch-Api使用的注意事项/"
  - "/移动端H5-iOS开发中-Fetch-Api使用的注意事项.html"
  - "/2025/07/10/yi-dong-duan-h5-ios-kai-fa-zhong-fetch-api-shi-yong-de-zhu-yi-shi-xiang/"
  - "/2025/07/10/yi-dong-duan-h5-ios-kai-fa-zhong-fetch-api-shi-yong-de-zhu-yi-shi-xiang.html"
  - "/yi-dong-duan-h5-ios-kai-fa-zhong-fetch-api-shi-yong-de-zhu-yi-shi-xiang.html"
---
1、为什么在发送请求的时候会收不到cookie

一般情况下我们会这样使用

```js
const data = await fetch('/mall/point/exchangecheck', {
  body: JSON.stringify(dataObj),
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
}).catch(e => {
  console.log(e);
  toast({
    'message': '网络异常'
  });
});

```

针对这个情况我们要这样使用

```js
const data = await fetch('/mall/point/exchangecheck', {
  body: JSON.stringify(dataObj),
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  credentials: "same-origin",
}).catch(e => {
  console.log(e);
  toast({
    'message': '网络异常'
  });
});
```

要加一下"credentials: "same-origin"

官方说明

> credentials (String) - Authentication credentials mode. Default: "omit"
>
> "omit" - don't include authentication credentials (e.g. cookies) in the request
>
> "same-origin" - include credentials in requests to the same site
>
> "include" - include credentials in requests to all sites

2、iPhone4、iPhone5机型支持async/await

iPhone4、iPhone5机型支持async/await，即使我使用babel 7，我是在浏览器中直接引用，当然我也是使用了，自定义plugins的方式进行了调试，然后会出现另外其他的问题，针对具体如何使用的方式我会在另外一篇文章做分享。现针对这个问题说下我的解决方案。

```js
const checkExchangeHandle = (id) => {
  return fetch('/xxx/xxx/xxx', {
    body: JSON.stringify({
      'goods_id': id
    }),
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: "same-origin",
  });
}

const exchangeHandle = (id) => {
  checkExchangeHandle(id).then(data => {
    data.json().then(o => {
      console.log(o);

      if (!o.success) {
        throw new Error(o.message);
      }

      window.location.href='/xxx/xxx/xxxsuccess';
    }).catch(e => {
      console.log(e);
      toast({
        'message': e.message
      });
    });
  }).catch(e => {
    console.log(e);
    toast({
      'message': '网络异常'
    });
  });
}
```

其实调用方式类似于Promise的使用，这里使用的fetch方法是<https://github.com/github/fetch>提供的。兼容性还可以的。
