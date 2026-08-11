---
title: "新手入门NestJS（五）- 控制器Request"
date: "2025-07-14 14:54:52"
slug: "xin-shou-ru-men-nestjs-wu-kong-zhi-qi-request"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（五）-控制器Request/"
  - "/2025/07/14/新手入门NestJS（五）-控制器Request.html"
  - "/新手入门NestJS（五）-控制器Request/"
  - "/新手入门NestJS（五）-控制器Request.html"
  - "/2025/07/14/新手入门NestJS-五-控制器Request/"
  - "/2025/07/14/新手入门NestJS-五-控制器Request.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-wu-kong-zhi-qi-request/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-wu-kong-zhi-qi-request.html"
  - "/xin-shou-ru-men-nestjs-wu-kong-zhi-qi-request.html"
---
一个控制器的目的是接收来自应用的一个请求

那么如何来处理这个请求，以及如何接收一个请求

Nest.js提供了一个Request Object

先看下之前写的一个例子

```tsx
import { Controller, Get, Render, Res } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(): string {
    return 'This action will returns all cats';
  }
}
```

我们想知道如何在这个例子中获取request中的参数

修改代码如下

```tsx
import { Controller, Get, Render, Req, Request } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Req() request: Request): string {
    return 'This action will returns all cats';
  }
}
```

http obejct包括了所有http的属性，比如http query 参数、http header、body、parameters等

但是在Nest.js中已经提供了专用的装饰器比如`@Body`、`@Query`等

其他的罗列在下面了

|  |  |
| --- | --- |
| `@Request()` | `req` |
| `@Response(), @Res()`\* | `res` |
| `@Next()` | `next` |
| `@Session()` | `req.session` |
| `@Param(key?: string)` | `req.params` / `req.params[key]` |
| `@Body(key?: string)` | `req.body` / `req.body[key]` |
| `@Query(key?: string)` | `req.query` / `req.query[key]` |
| `@Headers(name?: string)` | `req.headers` / `req.headers[name]` |
| `@Ip()` | `req.ip` |
