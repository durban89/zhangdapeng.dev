---
title: "Webpack4生产环境构建相关配置 - 指定环境"
date: "2025-07-07 15:54:04"
slug: "webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-zhi-ding-huan-jing"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4生产环境构建相关配置-指定环境/"
  - "/2025/07/07/Webpack4生产环境构建相关配置-指定环境.html"
  - "/Webpack4生产环境构建相关配置-指定环境/"
  - "/Webpack4生产环境构建相关配置-指定环境.html"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-zhi-ding-huan-jing/"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-zhi-ding-huan-jing.html"
  - "/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-zhi-ding-huan-jing.html"
---
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529324253/gowhich/16080123385115.jpg)

继续之前的分享【[Webpack4生产环境构建相关配置 - 代码压缩](https://www.gowhich.com/blog/833)】

下面让我们用我们之前文章的项目来做下实践

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
```

> 许多 library 将通过与 process.env.NODE_ENV 环境变量关联，以决定 library 中应该引用哪些内容。例如，当不处于生产环境中时，某些 library 为了使调试变得容易，可能会添加额外的日志记录(log)和测试(test)。其实，当使用 process.env.NODE_ENV === 'production' 时，一些 library 可能针对具体用户的环境进行代码优化，从而删除或添加一些重要代码。我们可以使用 webpack 内置的 DefinePlugin 为所有的依赖定义这个变量：

大概设置配置如下  
修改webpack.prod.js,在plugins里面加入如下

```js
new webpack.DefinePlugin({
  'process.env.NODE_ENV': JSON.stringify('production'),
}),
```

最终plugins如下

```js
plugins: [
  new CleanWebpackPlugin(['dist']),
  new HtmlWebpackPlugin({
    title: 'React + ReactRouter',
    filename: './index.html', // 调用的文件
    template: './index.html', // 模板文件
  }),
  new UglifyJsPlugin({
    sourceMap: true,
  }),
  new webpack.DefinePlugin({
    'process.env.NODE_ENV': JSON.stringify('production'),
  }),
],
```

官方还有一个说明

> 技术上讲，NODE_ENV 是一个由 Node.js 暴露给执行脚本的系统环境变量。通常用于决定在开发环境与生产环境(dev-vs-prod)下，服务器工具、构建脚本和客户端 library 的行为。然而，与预期不同的是，无法在构建脚本 webpack.config.js 中，将 process.env.NODE_ENV 设置为 "production"，请查看 #2537[https://github.com/webpack/webpack/issues/2537]。因此，例如 process.env.NODE_ENV === 'production' ? '[name].[hash].bundle.js' : '[name].bundle.js' 这样的条件语句，在 webpack 配置文件中，无法按照预期运行。

我记得以前是可以按照预期执行的，但是现在说不行，我们就认为不行吧，以防做了其他的改动，也为了跟官方一致，我们按照官方的说明来配置

如果有印象的话，之前文章有一个环节是配置redux-logger的，在src/index.jsx里面有个

```js
if (typeof __DEV__ !== 'undefined') {
  middleware.push(createLogger());
}
```

虽然这种方式也能实现，但是感觉不专业，毕竟像react库自己或者其他大型的库都是通过使用process.env.NODE_ENV这样的方式来判断的，为了保持自己库也能跟国际挂钩，咱也按照标准来，修改如下

```js
if (process.env.NODE_ENV !== 'production') {
  middleware.push(createLogger());
}
```

```bash
npm run build
```

打包完之后我们打开index.html，这里会个问题，就是需要一个真实的server去运行咱们的项目根目录就设置在dist下面，  
推荐一个http-server  
如果没有的话按照我的步骤安装下，安装如下

```bash
npm install http-server -g
```

安装为之后通过终端进入到本项目的dist目录下，然后执行

```bash
http-server ./ -p 8084
```

如果有如下输出表示已经启动成功

```bash
Starting up http-server, serving ./
Available on:
  http://127.0.0.1:8084
  http://172.18.0.70:8084
Hit CTRL-C to stop the server
```

用Chrome浏览器打开http://127.0.0.1:8084，然后调出DevTools，然后进入到计数器，点击加减号，右侧的console中是没有任何输出，如下图，表示我们的webpack.pord.js的配置是起作用的。

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529323878/gowhich/%E6%8C%87%E5%AE%9A%E7%8E%AF%E5%A2%83_1_WX20180613-133903.png)

我们运行下

```bash
npm run start
```

效果如下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529323894/gowhich/%E6%8C%87%E5%AE%9A%E7%8E%AF%E5%A2%83_2_WX20180613-134154.png)  
console中会有对应的输出，这是因为我们没有在webpack.dev.js做任何配置

以后在生产环境和开发环境有任何的需要根据环境变量来做判断处理，这个就是一个很好的例子

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.8
```
