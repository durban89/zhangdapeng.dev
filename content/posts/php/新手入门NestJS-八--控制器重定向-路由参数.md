---
title: "新手入门NestJS（八）- 控制器重定向、路由参数"
date: "2025-07-14 16:21:21"
slug: "xin-shou-ru-men-nestjs-ba-kong-zhi-qi-zhong-ding-xiang-lu-you-can-shu"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（八）-控制器重定向、路由参数/"
  - "/2025/07/14/新手入门NestJS（八）-控制器重定向、路由参数.html"
  - "/新手入门NestJS（八）-控制器重定向、路由参数/"
  - "/新手入门NestJS（八）-控制器重定向、路由参数.html"
  - "/2025/07/14/新手入门NestJS-八-控制器重定向-路由参数/"
  - "/2025/07/14/新手入门NestJS-八-控制器重定向-路由参数.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-ba-kong-zhi-qi-zhong-ding-xiang-lu-you-can-shu/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-ba-kong-zhi-qi-zhong-ding-xiang-lu-you-can-shu.html"
  - "/xin-shou-ru-men-nestjs-ba-kong-zhi-qi-zhong-ding-xiang-lu-you-can-shu.html"
---
#### 重定向

Nest.js提供了一种方式可以重定向路由

方式可以通过使用装饰器@Redirect和res.redirect

这里记录下如何使用装饰器来重定向

```javascript
@Get('items')
@Redirect('https://www.gowhich.com', 302)
getItems(@Query('version') version) {
  if (version && version == 5) {
    return {
      url: 'https://www.gowhich.com/cats/items/v5',
    };
  }
}
```

#### 当访问http://127.0.0.1:3000/cats/items，URI会被重定向到https://www.gowhich.com

当访问http://127.0.0.1:3000/cats/items?version=5，URI会被重定向到https://www.gowhich.com/cats/items/v5

#### 获取路由参数

这里说的路由参数值的是，当访问cats/1这样的路由的时候，能否获取到1这个参数值

当然Nest.js也提供了一个非常好用的装饰器@Param

这个装饰器，我们可以使用两种方式来获取到参数

第一种

```javascript
@Get(':id')
getOne(@Param() param): string {
  return `This action return id #${param.id}`;
}
```

第二种

```javascript
@Get(':name')
getName(@Param('name') name): string {
  return `This action return name #${name}`;
}
```
