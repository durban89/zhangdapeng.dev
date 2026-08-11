---
title: "TypeScript 3 + Koajs + Node.js"
date: "2025-07-09 10:42:24"
slug: "typescript-3-koajs-nodejs"
categories: ["技术"]
tags: ["TypeScript", "NodeJS", "KoaJS"]
aliases:
  - "/2025/07/09/TypeScript-3-+-Koajs-+-Node.js/"
  - "/2025/07/09/TypeScript-3-+-Koajs-+-Node.js.html"
  - "/TypeScript-3-+-Koajs-+-Node.js/"
  - "/TypeScript-3-+-Koajs-+-Node.js.html"
  - "/2025/07/09/TypeScript-3-KoaJS-NodeJS/"
  - "/2025/07/09/TypeScript-3-KoaJS-NodeJS.html"
  - "/2025/07/09/typescript-3-koajs-nodejs/"
  - "/2025/07/09/typescript-3-koajs-nodejs.html"
  - "/typescript-3-koajs-nodejs.html"
---
自NodeJS早期以来，Express一直是NodeJS开发人员事实上的标准Web框架。  
但是，JavaScript在过去几年中已经走过了漫长的道路，像promises和async函数这样的功能使得构建更小，更强大的Web框架成为可能。

Koa就是这样一个框架。  
它由Express背后的团队构建，以利用最新的JavaScript和NodeJS功能，特别是异步功能。

与Express和其他node框架（如Hapi）不同，Koa不需要使用回调。  
这消除了难以跟踪的错误的巨大潜在来源，并使框架非常容易为新开发人员选择。

在本文中，我将向您介绍如何使用Koa和TypeScript来开发新的Web应用程序项目

## 第一步、安装和配置

Koa需要一个具有异步功能支持的Node版本，因此在开始之前确保安装了Node 8.x（或更高版本）。  
Node 8将于2017年10月成为新的长期支持版本，因此它是启动新项目的绝佳选择。

我们现在将创建一个安装了以下内容的新node项目：

1. Koa  
2. Koa Router  
3. TypeScript  
4. TS-Node 和 Nodemon(用于在开发期间自动构建和重启)

为项目创建一个新文件夹，然后执行以下命令：

```bash
npm init   # and follow the resulting prompts to set up the project
npm i koa koa-router
npm i --save-dev typescript ts-node nodemon
npm i --save-dev @types/koa @types/koa-router
```

现在，在项目的根目录中，创建一个新的tsconfig.json文件并添加以下内容：

```json
{
    "compilerOptions": {
        "module": "commonjs",
        "target": "es2017",
        "noImplicitAny": true,
        "outDir": "./dist",
        "sourceMap": true
    },
    "include": [
        "./src/***/*",
    ]
}
```

请注意，我们将TypeScript配置为转换为ES2017 - 这可确保我们利用Node的本机async/await功能。

## 第二步、创建服务器

由于Koa的核心是微框架，因此启动和运行它非常简单。在项目目录中，创建一个src文件夹，在其中创建一个新文件：server.ts，其中包含以下内容：

```ts
import * as Koa from 'koa';
import * as Router from "koa-router";

const app = new Koa();
const router = new Router();

router.get('/*', async (ctx) => {
  ctx.body = "Hi TS";
})

app.use(router.routes());

app.listen(8080);

console.log("Server running on port 8080");
```

## 第三步、使用Nodemon和TS-Node运行服务器

在开发过程中，每次进行更改时都要记住重新启动服务器会很麻烦，所以我想设置我的服务器端项目以自动重新启动代码更改。

为此，我们将向我们的项目添加watch-server npm脚本。  
为此，请将以下内容添加到package.json的"scripts"部分：

```json
"watch-server": "nodemon --watch 'src/***/*' -e ts,tsx --exec 'ts-node' ./src/server.ts"
```

现在开始新的TypeScript Koa项目，只需执行以下操作即可

```bash
npm run watch-server
```

您应该看到以下输出：

```bash
> xx@xx watch-server /Users/durban/nodejs/ts_node_koa_blog
> nodemon --watch 'src/***/*' -e ts,tsx --exec 'ts-node' ./src/server.ts

[nodemon] 1.18.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching: src/***/*
[nodemon] starting `ts-node ./src/server.ts`
Server running on port 8080
```

现在您应该能够在浏览器中访问http//localhost:8080/ :)

## 第四步、构建应用程序 - 添加中间件

主要的Koa库只包含基本的HTTP功能。  
要构建完整的Web应用程序，我们需要添加适当的中间件，例如Logging, Error Handling, CSRF Protection等。在Koa中，中间件本质上是一堆函数，通过app.use()创建。  
收到Web请求后，它将传递给堆栈中的第一个函数。  
该函数可以处理请求，然后可选地将其传递给下一个中间件函数。  
让我们将上面的示例扩展为包含一个中间件函数，该函数将每个Web请求的URL记录到控制台：

```ts
import * as Koa from 'koa';
import * as Router from "koa-router";

const app = new Koa();

app.use(async (ctx, next) => {
  // Log the request to the console
  console.log("Url: ", ctx.url);

  // Pass the request to the next middleware function
  await next();
})

const router = new Router();

router.get('/*', async (ctx) => {
  ctx.body = "Hi TS";
})

app.use(router.routes());

app.listen(8080);

console.log("Server running on port 8080");
```

在上面的示例中，我们现在定义两个中间件函数：

1. 第一个中间件函数从请求上下文(ctx.url)获取Url，并使用console.log()将其输出到控制台  
2. 然后该函数await next()，告诉Koa将请求传递给堆栈中的下一个中间件函数  
3. 第二个中间件函数来自koa-router - 它使用请求的url来匹配我们通过router.get()配置的路由现在，当您在浏览器中访问http://localhost:8080/时，您应该看到类似于以下内容的输出：

```bash
> xx@xx watch-server /Users/durban/nodejs/ts_node_koa_blog
> nodemon --watch 'src/***/*' -e ts,tsx --exec 'ts-node' ./src/server.ts

[nodemon] 1.18.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching: src/***/*
[nodemon] starting `ts-node ./src/server.ts`
Server running on port 8080
Url:  /
Url:  /
Url:  /blog
Url:  /blog
```

## 第五步、标准中间件

显然，你真的不想为你的网络应用重新发明轮子。  
根据您要创建的应用程序类型，以下中间件可能很有用：

> Koa路由器  
> https://github.com/alexmingoia/koa-router
>
> Koa Body Parser（用于JSON和Form Data支持）  
> https://github.com/dlau/koa-body
>
> Koa Cross-Site-Request-Forgery（CSRF）预防  
> https://github.com/koajs/csrf
>
> Koa Examples（许多有用的东西，包括错误处理）  
> https://github.com/koajs/examples

我已经创建了一个基本的TypeScript和Koa项目。可以进行后面自己感兴趣的开发了。
