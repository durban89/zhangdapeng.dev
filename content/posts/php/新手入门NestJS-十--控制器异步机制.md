---
title: "新手入门NestJS（十）- 控制器异步机制"
date: "2025-07-14 16:21:31"
slug: "xin-shou-ru-men-nestjs-shi-kong-zhi-qi-yi-bu-ji-zhi"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（十）-控制器异步机制/"
  - "/2025/07/14/新手入门NestJS（十）-控制器异步机制.html"
  - "/新手入门NestJS（十）-控制器异步机制/"
  - "/新手入门NestJS（十）-控制器异步机制.html"
  - "/2025/07/14/新手入门NestJS-十-控制器异步机制/"
  - "/2025/07/14/新手入门NestJS-十-控制器异步机制.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-kong-zhi-qi-yi-bu-ji-zhi/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-kong-zhi-qi-yi-bu-ji-zhi.html"
  - "/xin-shou-ru-men-nestjs-shi-kong-zhi-qi-yi-bu-ji-zhi.html"
  - "/2025/07/14/新手入门NestJS-十--控制器异步机制.html"
---
#### 异步机制

Nest.js也是支持现在javascript的异步机制的，`async/await`

同时每个`async`函数必须返回一个`Promise`

看个简单的例子

```javascript
import { Controller, Get, HostParam } from '@nestjs/common';

@Controller('account')
export class AccountController {
  @Get()
  getInfo(@HostParam('account') account) {
    return account;
  }
  @Get('all')
  async findAll(): Promise<any[]> {
    return [];
  }
}
```

同时Nest.js还可以处理[observable streams](http://reactivex.io/rxjs/class/es6/Observable.js~Observable.html).

例子如下

```javascript
import { Controller, Get, HostParam } from '@nestjs/common';
import { Observable, of } from 'rxjs';

@Controller('account')
export class AccountController {
  @Get()
  getInfo(@HostParam('account') account) {
    return account;
  }

  @Get('all')
  findAll(): Observable<any[]> {
    return of([]);
  }
}
```

上面两个例子在访问的时候都会直接返回一个空数组
