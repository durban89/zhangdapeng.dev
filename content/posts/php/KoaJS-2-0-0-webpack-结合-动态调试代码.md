---
title: "KoaJS 2.0.0 webpack 结合 动态调试代码"
date: "2025-07-02 15:39:52"
slug: "koajs-200-webpack-jie-he-dong-tai-tiao-shi-dai-ma"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/02/KoaJS-2.0.0-webpack-结合-动态调试代码/"
  - "/2025/07/02/KoaJS-2.0.0-webpack-结合-动态调试代码.html"
  - "/KoaJS-2.0.0-webpack-结合-动态调试代码/"
  - "/KoaJS-2.0.0-webpack-结合-动态调试代码.html"
  - "/2025/07/02/KoaJS-2-0-0-webpack-结合-动态调试代码/"
  - "/2025/07/02/KoaJS-2-0-0-webpack-结合-动态调试代码.html"
  - "/2025/07/02/koajs-200-webpack-jie-he-dong-tai-tiao-shi-dai-ma/"
  - "/2025/07/02/koajs-200-webpack-jie-he-dong-tai-tiao-shi-dai-ma.html"
  - "/koajs-200-webpack-jie-he-dong-tai-tiao-shi-dai-ma.html"
---
koa2.0.0 的路由和视图渲染完之后的一个问题就是，如何高效的开发前端代码。

因为我之前的前端代码是用webpack进行打包，然后打包过程中，使用babel实现了，ES6语法的转换，这行我就不能太干脆的丢弃webpack，然后里面使用了react+react-router+reflux,整个开发体系还是比较可以的。为了整合之前的代码，需要将之前的connect框架改为koa2.0.0，毕竟koa的实现方式还有与express，connect等这样的框架，实现方式不太一样，所以，稍微还有有点小困难，不过我这里记录下，也就不困难了。

从webpack-dev-server说起，我们使用webpack-dev-server是为了能够时时监控我们的代码改变，然后用它自己的socket-io去刷新我们的页面，实现了代码修改即页面重载，当然只是在开发环境。

webpack-dev-server并没有多大的改变，只是将原来的一个proxy的操作去掉了，然后整合到koa的启动文件里面了。

```javascript
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config.development');
const debug = require('debug');
new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  noInfo: false,
  historyApiFallback: true,
  stats: { colors: true },
  headers: { 'Access-Control-Allow-Origin': '*' }
}).listen(8080, '127.0.0.1', function(err,result) {
  if (err) {
    console.log(err);
  }
  console.log('Webpack Listening at 127.0.0.1:8080');
});
```

关于webpack的config文件的代码是不需要改变的，继续使用。

下面就是在koa的启动文件里面加入启动需要的proxy处理。

```javascript
//解析 开发环境 development
app.use(convert(proxy({
  host:'http://127.0.0.1:8080/js',
  match: /^\/js\//
})));
```

就这么简单，这里使用了两个中间件：

koa-proxy，koa-convert。

解释一下好了，就是将访问的path中有带/js/部分的路径，进行重新proxy一下就好，这样就将文件转向到了webpack-dev-server这边的对应的文件了。相关的其他的问题可以参考我之前的几篇文章.


