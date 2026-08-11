---
title: "新手入门NestJS（六）- 控制器Resources、路由通配符"
date: "2025-07-14 14:54:56"
slug: "xin-shou-ru-men-nestjs-liu-kong-zhi-qi-resources-lu-you-tong-pei-fu"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（六）-控制器Resources、路由通配符/"
  - "/2025/07/14/新手入门NestJS（六）-控制器Resources、路由通配符.html"
  - "/新手入门NestJS（六）-控制器Resources、路由通配符/"
  - "/新手入门NestJS（六）-控制器Resources、路由通配符.html"
  - "/2025/07/14/新手入门NestJS-六-控制器Resources-路由通配符/"
  - "/2025/07/14/新手入门NestJS-六-控制器Resources-路由通配符.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-liu-kong-zhi-qi-resources-lu-you-tong-pei-fu/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-liu-kong-zhi-qi-resources-lu-you-tong-pei-fu.html"
  - "/xin-shou-ru-men-nestjs-liu-kong-zhi-qi-resources-lu-you-tong-pei-fu.html"
---
#### Nest.js控制中的Resources

前面介绍了路由中如何通过GET方式访问路由，Nest.js还支持Post、Delete、Patch、Options、Head和All等

下面看下如何使用Post

```javascript
import { Controller, Get, Post, Req, Request } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Req() request: Request): string {
    return 'This action will returns all cats';
  }

  @Post()
  create(): string {
    return 'This action will create a new cat';
  }
}
```

项目运行起来后，做个简单的测试

```bash
$ curl -d '' http://127.0.0.1:3000/cats
This action will create a new cat
```

可以看到，post请求的时候访问到了create()方法

#### Route通配符

看个简单的例子

```javascript
@Get('x*z')
find() {
  return 'This action uses a wildcard';
}
```

然后启动项目做下面几个测试

```bash
$ curl http://127.0.0.1:3000/cats/xyz
This action uses a wildcard
```

```bash
$ curl http://127.0.0.1:3000/cats/xyyz
This action uses a wildcard
```

```bash
$ curl http://127.0.0.1:3000/cats/xyyzz
This action uses a wildcard
```

从上面的输出可以观察到，输出的内容都是一致的，说明访问的路由其实调用了同一个方法

`'x*z'`路由将会匹配`xyz`,`xyyz`,`xyyzz`等，`?`,`+`,`*`,`()`都可以被用在路由的路径中
