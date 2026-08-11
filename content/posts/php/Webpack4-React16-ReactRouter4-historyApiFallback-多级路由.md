---
title: "Webpack4+React16+ReactRouter4 - historyApiFallback 多级路由"
date: "2025-07-07 15:48:44"
slug: "webpack4react16reactrouter4-historyapifallback-duo-ji-lu-you"
categories: ["技术"]
tags: ["Webpack", "React-Router", "ReactJS"]
aliases:
  - "/2025/07/07/Webpack4+React16+ReactRouter4-historyApiFallback-多级路由/"
  - "/2025/07/07/Webpack4+React16+ReactRouter4-historyApiFallback-多级路由.html"
  - "/Webpack4+React16+ReactRouter4-historyApiFallback-多级路由/"
  - "/Webpack4+React16+ReactRouter4-historyApiFallback-多级路由.html"
  - "/2025/07/07/Webpack4-React16-ReactRouter4-historyApiFallback-多级路由/"
  - "/2025/07/07/Webpack4-React16-ReactRouter4-historyApiFallback-多级路由.html"
  - "/2025/07/07/webpack4react16reactrouter4-historyapifallback-duo-ji-lu-you/"
  - "/2025/07/07/webpack4react16reactrouter4-historyapifallback-duo-ji-lu-you.html"
  - "/webpack4react16reactrouter4-historyapifallback-duo-ji-lu-you.html"
---
之前的几篇文章写的很多，里面在开发环境下都用到了

```js
historyApiFallback: {
  rewrites: [{
    from: /^\/$/,
    to: './index.html',
  },
  ],
},
```

但是在我们开发也许会遇到一个很奇怪的问题就是，当我们访问到二级以上的路由的情况下，在刷新页面会发现页面加载不出需要的js,此时会显示一个404，说文件不存在，但是仔细看的话发现加载的js路径不对呀，正常来说js的加载是在/下面的,如、xxx.js，但是当我们访问到比如/topics/1的时候，js请求的路径就变成了/topics/xxx.js，这个问题根据经验来说应该是html-webpack-plugin的原因，因为它在帮我们加入js文件的时候应该给我们一个base的参数，但是我也没有找到类似这样的参数，或者其他配置可以解决这个问题，最终让我追溯到了webpack的配置中output的选项中，其中有个publicPath这个选项

文档中的意思是

该选项的值是以 runtime(运行时) 或 loader(载入时) 所创建的每个 URL 为前缀。因此，在多数情况下，此选项的值都会以/结束。

那么我们就来设置下

```js
output: {
  filename: '[name].bundle.js',
  chunkFilename: '[chunkhash].bundle.js',
  path: path.resolve(__dirname, 'dist'),
},
```

中加入

```js
publicPath: '/',
```

结果如下

```bash
output: {
  filename: '[name].bundle.js',
  chunkFilename: '[chunkhash].bundle.js',
  path: path.resolve(__dirname, 'dist'),
  publicPath: '/',
},
```

保存后重启webpack-dev-server

```bash
npm start
```

然后再去刷新，发现问题得到了解决。在任何页面进行刷新就能保证正常的加载到js文件。

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag: v_1.0.5
```
