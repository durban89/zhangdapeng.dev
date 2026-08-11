---
title: "Webpack4渐进式网络应用程序"
date: "2025-07-07 15:59:13"
slug: "webpack4-jian-jin-shi-wang-luo-ying-yong-cheng-xu"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4渐进式网络应用程序/"
  - "/2025/07/07/Webpack4渐进式网络应用程序.html"
  - "/Webpack4渐进式网络应用程序/"
  - "/Webpack4渐进式网络应用程序.html"
  - "/2025/07/07/webpack4-jian-jin-shi-wang-luo-ying-yong-cheng-xu/"
  - "/2025/07/07/webpack4-jian-jin-shi-wang-luo-ying-yong-cheng-xu.html"
  - "/webpack4-jian-jin-shi-wang-luo-ying-yong-cheng-xu.html"
---
什么是渐进式网络应用程序

> 渐进式网络应用程序(Progressive Web Application - PWA)，是一种可以提供类似于原生应用程序(native app)体验的网络应用程序(web app)。PWA 可以用来做很多事。其中最重要的是，在离线(offline)时应用程序能够继续运行功能。这是通过使用名为 Service Workers[https://developers.google.com/web/fundamentals/primers/service-workers/] 的网络技术来实现的。

到目前为止，我们一直是直接查看本地文件系统的输出结果。通常情况下，真正的用户是通过网络访问网络应用程序；用户的浏览器会与一个提供所需资源（例如，.html, .js 和 .css 文件）的服务器通讯。

那么让我们来使用一个简易服务器，搭建出我们所需的离线体验。我们将使用 http-server package 包：

```bash
npm install http-server --save-dev
```

还要修改 package.json 的 scripts 部分，来添加一个 server:run 脚本：

操作之前如果本地没有实践项目的话，可以使用之前分享的项目来实践，具体操作如下

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
```

操作完后继续如下操作  
在package.json中添加如下

```json
"server:run": "npx http-server dist"
```

添加完后类似如下

```json
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "build": "npx webpack --config webpack.prod.js",
  "build:package": "NODE_ENV=production npx webpack --config webpack.prod.js",
  "start": "npx webpack-dev-server --open --hot --config webpack.dev.js",
  "server:run": "npx http-server dist"
},
```

我们先打包并运行下，操作如下

```bash
npm run build // 为了顺畅，可以先将webpack-bundle-analyzer关掉
npm run server:run
```

会有类似如下输出

```bash
> xx@xx server:run /Users/durban/nodejs/webpack-react-demo
> npx http-server dist

Starting up http-server, serving dist
Available on:
  http://127.0.0.1:8081
  http://172.18.0.70:8081
Hit CTRL-C to stop the server
```

如果你打开浏览器访问 http://127.0.0.1:8081，应该会看到在 dist 目录创建出服务，并可以访问 webpack 应用程序。如果停止服务器然后刷新，则 webpack 应用程序不再可访问。

这就是我们最终要改变的现状。“停止服务器然后刷新，仍然可以查看应用程序正常运行”

**添加 Workbox**  
添加 workbox-webpack-plugin 插件，并调整 webpack.prod.js 文件

```bash
npm install workbox-webpack-plugin --save-dev
```

webpack.prod.js修改的地方如下  
引入

```js
const WorkboxWebpackPlugin = require('workbox-webpack-plugin');
```

plugins中添加

```js
new WorkboxWebpackPlugin.GenerateSW({
  clientsClaim: true,
  skipWaiting: true,
  exclude: [/\.map$/],
}),
```

有了 Workbox，再执行 npm run build 时会发生什么，如下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529763153/gowhich/Webpack4%E6%B8%90%E8%BF%9B%E5%BC%8F%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F_1_WX20180621-183124.png)  
可以看到，生成了 2 个额外的文件

* service-worker.js
* precache-manifest.2f20a332d5e297960a8442509af3aa18.js

**注册 Service Worker**  
修改src/index.jsx，修改添加如下代码

```jsx
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js').then((registration) => {
      console.log('SW registered: ', registration);
    }).catch((registrationError) => {
      console.log('SW registration failed: ', registrationError);
    });
  });
}
```

再次运行 npm build build 来构建包含注册代码版本的应用程序。然后用

```bash
npm run server:run
```

启动服务。访问 http://127.0.0.1:8081 并查看 console 控制台。在那里你应该看到，如下图  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529763152/gowhich/Webpack4%E6%B8%90%E8%BF%9B%E5%BC%8F%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F_2_WX20180621-184517.png)

现在来进行测试。停止服务器并刷新页面。如果浏览器能够支持 Service Worker，你应该可以看到你的应用程序还在正常运行。然而，服务器已经停止了服务，此刻是 Service Worker 在提供服务。

激动的不要不要的，此等功力果然深厚

注意：  
在实践过程中，遇到几个问题  
1、如何清空precache  
2、如何更新precache

比如我忘记加了某个文件我要做清空怎么办？  
比如我加错了某个文件想要更新怎么办？

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.13
```
