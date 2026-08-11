---
title: "Webpack4缓存相关配置 - Manifest"
date: "2025-07-07 15:54:15"
slug: "webpack4-huan-cun-xiang-guan-pei-zhi-manifest"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4缓存相关配置-Manifest/"
  - "/2025/07/07/Webpack4缓存相关配置-Manifest.html"
  - "/Webpack4缓存相关配置-Manifest/"
  - "/Webpack4缓存相关配置-Manifest.html"
  - "/2025/07/07/webpack4-huan-cun-xiang-guan-pei-zhi-manifest/"
  - "/2025/07/07/webpack4-huan-cun-xiang-guan-pei-zhi-manifest.html"
  - "/webpack4-huan-cun-xiang-guan-pei-zhi-manifest.html"
---
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529593673/gowhich/16080123387372.jpg)

Manifest干嘛用，我摘抄了下官网的一些内容如下，先来了解下

> 一旦你的应用程序中，如 index.html 文件、一些 bundle 和各种资源加载到浏览器中，会发生什么？你精心安排的 /src 目录的文件结构现在已经不存在，所以 webpack 如何管理所有模块之间的交互呢？这就是 manifest 数据用途的由来……

> 当编译器(compiler)开始执行、解析和映射应用程序时，它会保留所有模块的详细要点。这个数据集合称为 "Manifest"，当完成打包并发送到浏览器时，会在运行时通过 Manifest 来解析和加载模块。无论你选择哪种模块语法，那些 import 或 require 语句现在都已经转换为 __webpack_require__ 方法，此方法指向模块标识符(module identifier)。通过使用 manifest 中的数据，runtime 将能够查询模块标识符，检索出背后对应的模块。
>
> 所以，现在你应该对 webpack 在幕后工作有一点了解。“但是，这对我有什么影响呢？”，你可能会问。答案是大多数情况下没有。runtime 做自己该做的，使用 manifest 来执行其操作，然后，一旦你的应用程序加载到浏览器中，所有内容将展现出魔幻般运行。然而，如果你决定通过使用浏览器缓存来改善项目的性能，理解这一过程将突然变得尤为重要。
>
> 通过使用 bundle 计算出内容散列(content hash)作为文件名称，这样在内容或文件修改时，浏览器中将通过新的内容散列指向新的文件，从而使缓存无效。一旦你开始这样做，你会立即注意到一些有趣的行为。即使表面上某些内容没有修改，计算出的哈希还是会改变。这是因为，runtime 和 manifest 的注入在每次构建都会发生变化。

**什么是Runtime**

> runtime，以及伴随的 manifest 数据，主要是指：在浏览器运行时，webpack 用来连接模块化的应用程序的所有代码。runtime 包含：在模块交互时，连接模块所需的加载和解析逻辑。包括浏览器中的已加载模块的连接，以及懒加载模块的执行逻辑。

具体如何提取manifest前面的文章【[Webpack4缓存相关配置](https://www.gowhich.com/blog/836)】已经说过了。

下面我们来配置下  
修改webpack.prod.js，另外如果需要webpack.dev.js的话可以另外在处理  
安装

```bash
npm i inline-manifest-webpack-plugin -D
```

分别添加如下

```js
const InlineManifestWebpackPlugin = require('inline-manifest-webpack-plugin');

new InlineManifestWebpackPlugin(),

runtimeChunk: {
  name: 'manifest',
},
```

到配置文件中  
最终结果如下

```js
const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');
const InlineManifestWebpackPlugin = require('inline-manifest-webpack-plugin');
const common = require('./webpack.common');

module.exports = merge(common, {
  mode: 'production',
  devtool: 'source-map',
  entry: {
    app: [
      './src/index.jsx',
    ],
    vendor: [
      'react',
      'react-dom',
      'redux',
    ],
  },
  output: {
    filename: '[name].[chunkhash].bundle.js',
    chunkFilename: '[name].[chunkhash].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/',
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'React + ReactRouter',
      filename: './index.html', // 调用的文件
      template: './index.html', // 模板文件
    }),
    new InlineManifestWebpackPlugin(),
    new UglifyJsPlugin({
      sourceMap: true,
    }),
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
    }),
    new ExtractTextPlugin({
      filename: 'main.[chunkhash].css',
    }),
    new ManifestPlugin(),
    new webpack.NamedModulesPlugin(),
  ],
  optimization: {
    splitChunks: {
      chunks: 'initial', // 必须三选一： "initial" | "all"(默认就是all) | "async"
      minSize: 0, // 最小尺寸，默认0
      minChunks: 1, // 最小 chunk ，默认1
      maxAsyncRequests: 1, // 最大异步请求数， 默认1
      maxInitialRequests: 1, // 最大初始化请求书，默认1
      name: () => {}, // 名称，此选项可接收 function
      cacheGroups: { // 这里开始设置缓存的 chunks
        priority: '0', // 缓存组优先级 false | object |
        vendor: { // key 为entry中定义的 入口名称
          chunks: 'initial', // 必须三选一： "initial" | "all" | "async"(默认就是异步)
          test: /react|lodash|react-dom|redux/, // 正则规则验证，如果符合就提取 chunk
          name: 'vendor', // 要缓存的 分隔出来的 chunk 名称
          minSize: 0,
          minChunks: 1,
          enforce: true,
          maxAsyncRequests: 1, // 最大异步请求数， 默认1
          maxInitialRequests: 1, // 最大初始化请求书，默认1
          reuseExistingChunk: true, // 可设置是否重用该chunk（查看源码没有发现默认值）
        },
      },
    },
    runtimeChunk: {
      name: 'manifest',
    },
  },
});
```

运行

```bash
npm run build
```

执行后输出大概如下

```bash
Hash: b26027576f67c9b4a2ed
Version: webpack 4.12.0
Time: 11329ms
Built at: 2018-06-21 15:44:30
                                      Asset       Size  Chunks             Chunk Names
       1.8539b93fe0620243ce58.bundle.js.map   5.01 KiB       1  [emitted]
           0.d12185fd8e6117c063c6.bundle.js   5.93 KiB       0  [emitted]
           2.682c3024cf3095674f24.bundle.js   6.75 KiB       2  [emitted]
    manifest.e6adb1315c7823bc535e.bundle.js    2.3 KiB       3  [emitted]  manifest
      vendor.7aaf509786ae83a5de3c.bundle.js    107 KiB       4  [emitted]  vendor
         app.bb3713d2c6aeb09ceeb9.bundle.js    224 KiB       5  [emitted]  app
              main.bb3713d2c6aeb09ceeb9.css  290 bytes       5  [emitted]  app
              main.e6adb1315c7823bc535e.css   57 bytes       3  [emitted]  manifest
       0.d12185fd8e6117c063c6.bundle.js.map   4.13 KiB       0  [emitted]
           1.8539b93fe0620243ce58.bundle.js   6.86 KiB       1  [emitted]
       2.682c3024cf3095674f24.bundle.js.map   5.09 KiB       2  [emitted]
manifest.e6adb1315c7823bc535e.bundle.js.map   11.8 KiB       3  [emitted]  manifest
          main.e6adb1315c7823bc535e.css.map  106 bytes       3  [emitted]  manifest
  vendor.7aaf509786ae83a5de3c.bundle.js.map    266 KiB       4  [emitted]  vendor
     app.bb3713d2c6aeb09ceeb9.bundle.js.map    633 KiB       5  [emitted]  app
          main.bb3713d2c6aeb09ceeb9.css.map  106 bytes       5  [emitted]  app
                               ./index.html  666 bytes          [emitted]
                              manifest.json   1.06 KiB          [emitted]
```

我们看下dist/index.html这个文件

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>React + ReactRouter Demo</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="/main.e6adb1315c7823bc535e.css" rel="stylesheet"><link href="/main.bb3713d2c6aeb09ceeb9.css" rel="stylesheet"></head>
<body>
    <div id="root"></div>
<script type="text/javascript" src="/manifest.e6adb1315c7823bc535e.bundle.js"></script><script type="text/javascript" src="/app.bb3713d2c6aeb09ceeb9.bundle.js"></script><script type="text/javascript" src="/vendor.7aaf509786ae83a5de3c.bundle.js"></script></body>
</html>
```

可以看到

```bash
/manifest.e6adb1315c7823bc535e.bundle.js
```

已经被加入了

这样当模块被打包并运输到浏览器上时，runtime就会根据manifest文件来处理和加载模块。利用manifest就知道从哪里去获取模块代码。

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.11
```
