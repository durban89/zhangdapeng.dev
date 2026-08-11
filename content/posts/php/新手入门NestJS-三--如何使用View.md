---
title: "新手入门NestJS（三）- 如何使用View"
date: "2025-07-14 14:54:40"
slug: "xin-shou-ru-men-nestjs-san-ru-he-shi-yong-view"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（三）-如何使用View/"
  - "/2025/07/14/新手入门NestJS（三）-如何使用View.html"
  - "/新手入门NestJS（三）-如何使用View/"
  - "/新手入门NestJS（三）-如何使用View.html"
  - "/2025/07/14/新手入门NestJS-三-如何使用View/"
  - "/2025/07/14/新手入门NestJS-三-如何使用View.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-san-ru-he-shi-yong-view/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-san-ru-he-shi-yong-view.html"
  - "/xin-shou-ru-men-nestjs-san-ru-he-shi-yong-view.html"
---
前面记录了如何安装Nest.js以及如何创建项目

都是很简单，没有太多可以介绍的，但是作为web开发，最关系的是如何调用视图（View）

官方也有文档，[点击这里](https://docs.nestjs.com/techniques/mvc)

### 1、如何展示一个页面

方式也很简单，主要原理是整合了express框架，然后通过express设置模版引擎，这里使用的模板引擎是[hbs](https://github.com/pillarjs/hbs#readme)

我们看下如何配置

先安装hbs

```bash
npm install --save hbs
```

然后打开项目根目录下面的main.ts

将里面的bootstrap()方法修改如下

```javascript
async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);

  app.setBaseViewsDir(join(__dirname, '..', 'views'));
  app.setViewEngine('hbs');

  await app.listen(3000);
}
```

上面的代码就是配置模版引擎

main.ts最后代码如下

```ts
import { Controller, Get, Render } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('/index')
  @Render('index')
  getIndex() {
    return {};
  }
}
```

如何调用视图

1、在根目录（不是src目录）下创建public和views文件夹

2、在views目录中创建index.hbs

添加代码如下

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>App</title>
</head>

<body>
    Message
</body>

</html>
```

3、controller中调用视图（View）

代码如下

```ts
import { Controller, Get, Render, Res } from '@nestjs/common';
import { AppService } from './app.service';
import { Response } from 'express';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('/index')
  @Render('index')
  getIndex() {
    return {};
  }

  @Get('/dynamic')
  getDynamic(@Res() res: Response) {
    return res.render('index');
  }
}
```

其中官网也介绍了两种调用视图的方式

第一种，静态视图

```javascript
@Get('/index')
@Render('index')
getIndex() {
  return {};
}
```

将视图文件的名称index，添加到Render修饰器里面，然后函数返回对应的变量值就可以了

第二种，动态视图，访问的路由一样的情况，需要根据逻辑来展示不同的视图

```javascript
@Get('/dynamic')
getDynamic(@Res() res: Response) {
  return res.render('index');
}
```

方法中传入res参数并在参数前面加上@Res修饰器，然后调用res.render就可以了，这样配置后就可以正常写View了，后面记录下静态文件相关的使用

### 2、如何添加静态文件

修改main.ts

```javascript
async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);

  // 添加静态文件目录配置
  app.useStaticAssets(join(__dirname, '..', 'public'));
  // 添加视图文件目录配置
  app.setBaseViewsDir(join(__dirname, '..', 'views'));
  app.setViewEngine('hbs');

  await app.listen(3000);
}
```

修改index.hbs

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>App</title>
  <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
</head>

<body>
  <header>
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
      </div>
    </nav>
  </header>
  <div class='container'>
    Message
  </div>
  <script src="/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>
```

同时在项目根目录下面建立public目录，添加自己的静态文件，我这里添加的是bootstrap的静态文件

### 3、如何动态的展示一个页面（页面参数传递）

修改app.controller.ts

```ts
import { Controller, Get, Render } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('/index')
  @Render('index')
  getIndex() {
    return { message: 'Index Page' };
  }
}
```

修改index.hbs

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>App</title>
  <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
</head>

<body>
  <header>
    <nav class="navbar navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
      </div>
    </nav>
  </header>

  <div class="container">
    {{ message }}
  </div>

  <script src="/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>
```
