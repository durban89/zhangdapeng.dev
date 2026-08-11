---
title: "新手入门Nest.js（七）- 控制器HttpCode、Header信息设置"
date: "2025-07-14 14:55:04"
slug: "xin-shou-ru-men-nestjs-qi-kong-zhi-qi-httpcode-header-xin-xi-she-zhi"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门Nest.js（七）-控制器HttpCode、Header信息设置/"
  - "/2025/07/14/新手入门Nest.js（七）-控制器HttpCode、Header信息设置.html"
  - "/新手入门Nest.js（七）-控制器HttpCode、Header信息设置/"
  - "/新手入门Nest.js（七）-控制器HttpCode、Header信息设置.html"
  - "/2025/07/14/新手入门NestJS-七-控制器HttpCode-Header信息设置/"
  - "/2025/07/14/新手入门NestJS-七-控制器HttpCode-Header信息设置.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-qi-kong-zhi-qi-httpcode-header-xin-xi-she-zhi/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-qi-kong-zhi-qi-httpcode-header-xin-xi-she-zhi.html"
  - "/xin-shou-ru-men-nestjs-qi-kong-zhi-qi-httpcode-header-xin-xi-she-zhi.html"
---
#### 如何设置状态码

Nest.js通过装饰器`@HttpCode`来设置状态码，状态码默认200

```javascript
@Get()
@HttpCode(204)
itemError(): string {
  return 'This action return 204 error';
}
```

`HttpCode`从`@nestjs/common`包中导入

#### 如何设置Header信息

Header信息是可以自定义的，Nest.js也提供了一个`@Header`装饰器来帮助我们添加Header信息

```javascript
@Get()
@Header('Cache-Control', 'none')
itemCustomHeader(): string {
  return 'This action custom header';
}
```

`Header`从`@nestjs/common`包中导入
