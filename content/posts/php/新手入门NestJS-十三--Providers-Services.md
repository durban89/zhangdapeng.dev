---
title: "新手入门NestJS（十三）- Providers - Services"
date: "2025-07-14 16:22:10"
slug: "xin-shou-ru-men-nestjs-shi-san-providers-services"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（十三）-Providers-Services/"
  - "/2025/07/14/新手入门NestJS（十三）-Providers-Services.html"
  - "/新手入门NestJS（十三）-Providers-Services/"
  - "/新手入门NestJS（十三）-Providers-Services.html"
  - "/2025/07/14/新手入门NestJS-十三-Providers-Services/"
  - "/2025/07/14/新手入门NestJS-十三-Providers-Services.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-san-providers-services/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-san-providers-services.html"
  - "/xin-shou-ru-men-nestjs-shi-san-providers-services.html"
---
Providers是什么，看下官网的解释

> Providers are a fundamental concept in Nest. Many of the basic Nest classes may be treated as a provider – services, repositories, factories, helpers, and so on. The main idea of a provider is that it can **inject** dependencies; this means objects can create various relationships with each other, and the function of "wiring up" instances of objects can largely be delegated to the Nest runtime system. A provider is simply a class annotated with an `@Injectable()` decorator.

Services

通过命令行创建 Services

```bash
nest g service cats
```

执行后结果类似如下

```bash
$ nest g service cats
CREATE src/cats/cats.service.spec.ts (446 bytes)
CREATE src/cats/cats.service.ts (88 bytes)
UPDATE src/app.module.ts (544 bytes)
```

创建完`src/cats/cats.service.ts`代码如下

```javascript
import { Injectable } from '@nestjs/common';

@Injectable()
export class CatsService {}
```

修改下，修改前提我们添加一个`interface`

如果创建`interface`，命令行命令如下

```bash
$ nest g interface cat
CREATE src/cat.interface.ts (24 bytes)
```

创建完`src/cat.interface.ts`代码如下

```javascript
export interface Cat {}
```

修改后`src/cats/cats.service.ts`的代码如下

```javascript
import { Injectable } from '@nestjs/common';
import { Cat } from 'src/cat.interface';

@Injectable()
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll() {
    return this.cats;
  }
}
```

顺便修改src/cat.interface.ts，代码如下

```javascript
export interface Cat {
  name: string;
  age: number;
  bread: string;
}
```

下面看下如何在Controller中应用

```javascript
constructor(private catsService: CatsService) {}

@Get()
async findAll(@Req() request: Request): Promise<Cat[]> {
  return this.catsService.findAll();
}

@Post()
async create(@Body() createCatDto: CreateCatDto) {
  this.catsService.create(createCatDto);
  console.log(createCatDto);
  return 'This action will create a new cat';
}
```

上面代码是主要关注的地方

另外需要导入对应的包

```javascript
import { Cat } from 'src/cat.interface';
import { CatsService } from './cats.service';
```

然后访问`http://127.0.0.1:3000/cats`会得到一个空数组

执行下面的命令

```bash
$ curl -d 'name=durban1&age=12&bread=1' http://127.0.0.1:3000/cats
```

然后在访问`http://127.0.0.1:3000/cats`类似如下的数据

```json
[{"name":"durban1","age":"12","bread":"1"},{"name":"durban1","age":"12","bread":"1"}]
```
