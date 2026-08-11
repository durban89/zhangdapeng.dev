---
title: "新手入门NestJS（十四）- Modules"
date: "2025-07-14 16:28:02"
slug: "xin-shou-ru-men-nestjs-shi-si-modules"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（十四）-Modules/"
  - "/2025/07/14/新手入门NestJS（十四）-Modules.html"
  - "/新手入门NestJS（十四）-Modules/"
  - "/新手入门NestJS（十四）-Modules.html"
  - "/2025/07/14/新手入门NestJS-十四-Modules/"
  - "/2025/07/14/新手入门NestJS-十四-Modules.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-si-modules/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-shi-si-modules.html"
  - "/xin-shou-ru-men-nestjs-shi-si-modules.html"
---
新手入门，了解Nest.js的Modules

在Nest.js中，一个带有@Module()装饰器的类，即是一个Module

每个Application都至少有一个Module，root module

同时Nest.js强烈建议使用一个Module作为一个有效的方式来管理你的组件

下面看下如何创建一个Module

#### 创建一个module

创建module的命令如下

```bash
nest g module cats
```

运行后结果如下

```bash
$ nest g module cats
CREATE src/cats/cats.module.ts (81 bytes)
UPDATE src/app.module.ts (603 bytes)
```

创建后默认的代码如下

```javascript
import { Module } from '@nestjs/common';

@Module({})
export class CatsModule {}
```

使用module

下面修改下cats.module.ts，修改后的结果如下

```javascript
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

同时需要修改下app.module.ts

```javascript
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AccountController } from './account/account.controller';
import { DogsController } from './dogs/dogs.controller';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
  controllers: [AppController, AccountController, DogsController],
  providers: [AppService],
})
export class AppModule {}
```

跟没有使用cats.module.ts的时候对比下

```javascript
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsController } from './cats/cats.controller';
import { AccountController } from './account/account.controller';
import { DogsController } from './dogs/dogs.controller';
import { CatsService } from './cats/cats.service';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
  controllers: [AppController, CatsController, AccountController, DogsController],
  providers: [AppService, CatsService],
})
export class AppModule {}
```

可以发现少了对应的CatsController，CatsService

从这个方面可以看出 Nest.js的代码体现了SOLID原则，对代码的维护是很有帮助的。
