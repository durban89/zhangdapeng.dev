---
title: "新手入门NestJS（四）- 控制器路由"
date: "2025-07-14 14:54:49"
slug: "xin-shou-ru-men-nestjs-si-kong-zhi-qi-lu-you"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（四）-控制器路由/"
  - "/2025/07/14/新手入门NestJS（四）-控制器路由.html"
  - "/新手入门NestJS（四）-控制器路由/"
  - "/新手入门NestJS（四）-控制器路由.html"
  - "/2025/07/14/新手入门NestJS-四-控制器路由/"
  - "/2025/07/14/新手入门NestJS-四-控制器路由.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-si-kong-zhi-qi-lu-you/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-si-kong-zhi-qi-lu-you.html"
  - "/xin-shou-ru-men-nestjs-si-kong-zhi-qi-lu-you.html"
---
一个控制器的目的是接收来自应用的一个请求

路由机制控制了控制器接收哪个请求

通常每个控制器都有多于一个的路由，而且不同的路由能够执行不同的操作

为了创建一个基本的控制器，Nest.js使用了一个类和装饰器。

装饰器关联类然后允许Nest.js创建一个路由Map

#### 路由

下面看个简单的例子，如下代码

```javascript
import { Controller, Get, Render, Res } from '@nestjs/common';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(): string {
    return 'This action will returns all cats';
  }
}
```

这里提示一点

Nest提供了一个非常方便的创建控制的命令

```bash
nest g controller cats
```

执行后得到下面的结果

```bash
$ nest g controller cats
CREATE src/cats/cats.controller.spec.ts (478 bytes)
CREATE src/cats/cats.controller.ts (97 bytes)
UPDATE src/app.module.ts (322 bytes)
```

我们看下`src/app.module.ts`文件

```bash
diff --git a/src/app.module.ts b/src/app.module.ts
index 8662803..7bc3188 100644
--- a/src/app.module.ts
+++ b/src/app.module.ts
@@ -1,10 +1,11 @@
 import { Module } from '@nestjs/common';
 import { AppController } from './app.controller';
 import { AppService } from './app.service';
+import { CatsController } from './cats/cats.controller';

 @Module({
   imports: [],
-  controllers: [AppController],
+  controllers: [AppController, CatsController],
   providers: [AppService],
 })
 export class AppModule {}
```

其实自动帮我们更新module中的代码，然后创建了对应的控制器，非常方便，大大提高了开发效率

然后运行

```bash
npm run start:dev
```

得到如下输出

```bash
[Nest] 9167   - 2020-09-26 11:41:33 PM   [NestFactory] Starting Nest application...
[Nest] 9167   - 2020-09-26 11:41:33 PM   [InstanceLoader] AppModule dependencies initialized +21ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RoutesResolver] AppController {}: +9ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RouterExplorer] Mapped {, GET} route +13ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RouterExplorer] Mapped {/index, GET} route +4ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RouterExplorer] Mapped {/dynamic, GET} route +5ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RoutesResolver] CatsController {/cats}: +4ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [RouterExplorer] Mapped {/cats, GET} route +4ms
[Nest] 9167   - 2020-09-26 11:41:33 PM   [NestApplication] Nest application successfully started +4ms
```

从输出中可以看出，`/cats`路由已经添加，当访问`/cats`的时候，会执行`findAll()`的方法，同时还是一个`Get`请求
