---
title: "Webpack4缓存相关配置"
date: "2025-07-07 15:54:12"
slug: "webpack4-huan-cun-xiang-guan-pei-zhi"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4缓存相关配置/"
  - "/2025/07/07/Webpack4缓存相关配置.html"
  - "/Webpack4缓存相关配置/"
  - "/Webpack4缓存相关配置.html"
  - "/2025/07/07/webpack4-huan-cun-xiang-guan-pei-zhi/"
  - "/2025/07/07/webpack4-huan-cun-xiang-guan-pei-zhi.html"
  - "/webpack4-huan-cun-xiang-guan-pei-zhi.html"
---
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529507174/gowhich/16080123386116.jpg)

关于webpack的缓存相关配置，我用我之前文章的项目来做下实践

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
```

**提取模板(Extracting Boilerplate)**

```bash
npm install --save-dev webpack-manifest-plugin
```

添加如下代码  
引入

```js
const ManifestPlugin = require('webpack-manifest-plugin');
```

在plugins中加入

```js
new ManifestPlugin(),
```

plugins中结果如下

```js
plugins: [
  new CleanWebpackPlugin(['dist']),
  new HtmlWebpackPlugin({
    title: 'React + ReactRouter Demo',
    filename: './index.html', // 调用的文件
    template: './index.html', // 模板文件
  }),
  new webpack.DefinePlugin({
    'process.env.NODE_ENV': JSON.stringify('development'),
  }),
  new ExtractTextPlugin({
    filename: '[name].[hash].bundle.css',
  }),
  new ManifestPlugin(),
],
```

将

```js
new ExtractTextPlugin({
  filename: '[name].bundle.css',
}),
```

改为

```js
new ExtractTextPlugin({
  filename: '[name].[hash].bundle.css',
}),
```

再将

```js
output: {
  filename: '[name].bundle.js',
  chunkFilename: '[name].bundle.js',
  path: path.resolve(__dirname, 'dist'),
  publicPath: '/',
},
```

改为

```js
output: {
  filename: '[name].[hash].bundle.js',
  chunkFilename: '[name].[hash].bundle.js',
  path: path.resolve(__dirname, 'dist'),
  publicPath: '/',
},
```

这次我们执行

```bash
npx webpack --config webpack.dev.js
```

然后看下打包效果

```bash
Hash: 88fb183afd5b8cdbb10b
Version: webpack 4.12.0
Time: 2748ms
Built at: 2018-06-14 17:43:46
                              Asset       Size  Chunks             Chunk Names
 app.88fb183afd5b8cdbb10b.bundle.js   1.17 MiB     app  [emitted]  app
   0.88fb183afd5b8cdbb10b.bundle.js   10.9 KiB       0  [emitted]
   1.88fb183afd5b8cdbb10b.bundle.js     11 KiB       1  [emitted]
   2.88fb183afd5b8cdbb10b.bundle.js   10.1 KiB       2  [emitted]
app.88fb183afd5b8cdbb10b.bundle.css  233 bytes     app  [emitted]  app
                       ./index.html  439 bytes          [emitted]
                      manifest.json  366 bytes          [emitted]
```

多了一个manifest.json  
在项目目录下面查看下这个文件

```bash
cat ./dist/manifest.json
```

```bash
{
  "app.js": "/app.88fb183afd5b8cdbb10b.bundle.js",
  "app.css": "/app.88fb183afd5b8cdbb10b.bundle.css",
  "0.88fb183afd5b8cdbb10b.bundle.js": "/0.88fb183afd5b8cdbb10b.bundle.js",
  "1.88fb183afd5b8cdbb10b.bundle.js": "/1.88fb183afd5b8cdbb10b.bundle.js",
  "2.88fb183afd5b8cdbb10b.bundle.js": "/2.88fb183afd5b8cdbb10b.bundle.js",
  "./index.html": "/./index.html"
}
```

这个文件干嘛用，后面说

根据官方的说法

> 将第三方库(library)（例如 lodash 或 react）提取到单独的 vendor chunk 文件中，是比较推荐的做法，这是因为，它们很少像本地的源代码那样频繁修改。因此通过实现以上步骤，利用客户端的长效缓存机制，可以通过命中缓存来消除请求，并减少向服务器获取资源，同时还能保证客户端代码和服务器端代码版本一致。

但是目前官网的实例不起作用了，经过我的实践当前webpack的版本已经使用了新的逻辑，具体操作如下  
我们先配置webpack.dev.js  
添加如下配置

```js
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
        test: /react|lodash/, // 正则规则验证，如果符合就提取 chunk
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
},
```

entry中加入

```js
vendor: [
  'react',
  'react-dom',
  'redux',
],
```

然后执行

```bash
npx webpack --config webpack.dev.js
```

得到类似如下输出

```bash
Hash: 29ff4803e0ac98b32c1c
Version: webpack 4.12.0
Time: 2641ms
Built at: 2018-06-14 17:51:36
                                Asset       Size  Chunks             Chunk Names
   app.29ff4803e0ac98b32c1c.bundle.js   1.17 MiB     app  [emitted]  app
vendor.29ff4803e0ac98b32c1c.bundle.js    735 KiB  vendor  [emitted]  vendor
     0.29ff4803e0ac98b32c1c.bundle.js   10.9 KiB       0  [emitted]
     1.29ff4803e0ac98b32c1c.bundle.js     11 KiB       1  [emitted]
     2.29ff4803e0ac98b32c1c.bundle.js   10.1 KiB       2  [emitted]
  app.29ff4803e0ac98b32c1c.bundle.css  233 bytes     app  [emitted]  app
                         ./index.html  524 bytes          [emitted]
                        manifest.json  423 bytes          [emitted]
```

多了一个vendor.29ff4803e0ac98b32c1c.bundle.js这个文件 同时app.29ff4803e0ac98b32c1c.bundle.js的大小也减小了

**模块标识符(Module Identifiers)**

> 从上面的实践中我们发现我们其实是没有更改代码的但是文件中hash的值却变化了  
> 根据官网的描述  
>   
> 这是因为每个 module.id 会基于默认的解析顺序(resolve order)进行增量。也就是说，当解析顺序发生变化，ID 也会随之改变。因此，简要概括：
>
> main bundle 会随着自身的新增内容的修改，而发生变化。  
> vendor bundle 会随着自身的 module.id 的修改，而发生变化。  
> manifest bundle 会因为当前包含一个新模块的引用，而发生变化。  
> 第一个和最后一个都是符合预期的行为 -- 而 vendor 的 hash 发生变化是我们要修复的。幸运的是，可以使用两个插件来解决这个问题。第一个插件是 NamedModulesPlugin，将使用模块的路径，而不是数字标识符。虽然此插件有助于在开发过程中输出结果的可读性，然而执行时间会长一些。第二个选择是使用 HashedModuleIdsPlugin，推荐用于生产环境构建：

由于我们现在改的是webpack.dev.js，我们用来实践下  
在plugins中添加如下代码

```js
new webpack.NamedModulesPlugin(),
```

然后

```bash
npx webpack --config webpack.dev.js
```

看下打包效果

```bash
Hash: 29ff4803e0ac98b32c1c
Version: webpack 4.12.0
Time: 2813ms
Built at: 2018-06-14 17:57:59
                                Asset       Size  Chunks             Chunk Names
   app.29ff4803e0ac98b32c1c.bundle.js   1.17 MiB     app  [emitted]  app
vendor.29ff4803e0ac98b32c1c.bundle.js    735 KiB  vendor  [emitted]  vendor
     0.29ff4803e0ac98b32c1c.bundle.js   10.9 KiB       0  [emitted]
     1.29ff4803e0ac98b32c1c.bundle.js     11 KiB       1  [emitted]
     2.29ff4803e0ac98b32c1c.bundle.js   10.1 KiB       2  [emitted]
  app.29ff4803e0ac98b32c1c.bundle.css  233 bytes     app  [emitted]  app
                         ./index.html  524 bytes          [emitted]
                        manifest.json  423 bytes          [emitted]
```

可以修改下CounterComponet.jsx后在执行

```bash
npx webpack --config webpack.dev.js
```

再看下打包效果

```bash
Hash: 3cf568e90b38c1c3c339
Version: webpack 4.12.0
Time: 2709ms
Built at: 2018-06-14 17:59:00
                                Asset       Size  Chunks             Chunk Names
   app.3cf568e90b38c1c3c339.bundle.js   1.17 MiB     app  [emitted]  app
vendor.3cf568e90b38c1c3c339.bundle.js    735 KiB  vendor  [emitted]  vendor
     0.3cf568e90b38c1c3c339.bundle.js   10.9 KiB       0  [emitted]
     1.3cf568e90b38c1c3c339.bundle.js     11 KiB       1  [emitted]
     2.3cf568e90b38c1c3c339.bundle.js   10.1 KiB       2  [emitted]
  app.3cf568e90b38c1c3c339.bundle.css  233 bytes     app  [emitted]  app
                         ./index.html  524 bytes          [emitted]
                        manifest.json  423 bytes          [emitted]
```

结果还是都变化了，奇怪，我们试下生产环境的方式  
将webpack.dev.js的相关的改动我们在webpack.prod.js中也做下修改，然后再试下【注意生产环境我们用new webpack.HashedModuleIdsPlugin()】  
分别执行

```bash
npm run build
```

第一次输出类似如下

```bash
Hash: e0b25a1605f0da8569c1
Version: webpack 4.12.0
Time: 9622ms
Built at: 2018-06-14 18:14:57
                                    Asset       Size  Chunks             Chunk Names
     1.62c80f16d58866af39d9.bundle.js.map      5 KiB       1  [emitted]
         0.a81f2d5fe8a554f19db1.bundle.js   5.32 KiB       0  [emitted]
         2.4bb6ea90727a9917c466.bundle.js   6.23 KiB       2  [emitted]
    vendor.153d0cc454d09104782f.bundle.js    106 KiB       3  [emitted]  vendor
       app.e7d2f7719c957e5c378e.bundle.js    217 KiB       4  [emitted]  app
            main.e7d2f7719c957e5c378e.css  290 bytes       4  [emitted]  app
     0.a81f2d5fe8a554f19db1.bundle.js.map   4.13 KiB       0  [emitted]
         1.62c80f16d58866af39d9.bundle.js   6.34 KiB       1  [emitted]
     2.4bb6ea90727a9917c466.bundle.js.map   5.08 KiB       2  [emitted]
vendor.153d0cc454d09104782f.bundle.js.map    271 KiB       3  [emitted]  vendor
   app.e7d2f7719c957e5c378e.bundle.js.map    644 KiB       4  [emitted]  app
        main.e7d2f7719c957e5c378e.css.map  106 bytes       4  [emitted]  app
                             ./index.html  518 bytes          [emitted]
                            manifest.json  845 bytes          [emitted]
```

第二次我们修改CounterComponent.jsx,然后再试下结果输出类似如下

```bash
Hash: 3102790f92604ffd6406
Version: webpack 4.12.0
Time: 13758ms
Built at: 2018-06-14 18:17:58
                                    Asset       Size  Chunks             Chunk Names
     1.62c80f16d58866af39d9.bundle.js.map      5 KiB       1  [emitted]
         0.44264f48cf81d76c34f3.bundle.js   5.32 KiB       0  [emitted]
         2.4bb6ea90727a9917c466.bundle.js   6.23 KiB       2  [emitted]
    vendor.153d0cc454d09104782f.bundle.js    106 KiB       3  [emitted]  vendor
       app.2d7ccb1930e41d2c5c9b.bundle.js    217 KiB       4  [emitted]  app
            main.2d7ccb1930e41d2c5c9b.css  290 bytes       4  [emitted]  app
     0.44264f48cf81d76c34f3.bundle.js.map   4.13 KiB       0  [emitted]
         1.62c80f16d58866af39d9.bundle.js   6.34 KiB       1  [emitted]
     2.4bb6ea90727a9917c466.bundle.js.map   5.08 KiB       2  [emitted]
vendor.153d0cc454d09104782f.bundle.js.map    271 KiB       3  [emitted]  vendor
   app.2d7ccb1930e41d2c5c9b.bundle.js.map    644 KiB       4  [emitted]  app
        main.2d7ccb1930e41d2c5c9b.css.map  106 bytes       4  [emitted]  app
                             ./index.html  518 bytes          [emitted]
                            manifest.json  845 bytes          [emitted]
```

可以看出来变动的之后  
0.xxxx.bundle.js这个文件  
看来这个hash的变化针对的只是生产环境，不过这个也可以了，频繁改动只对生产环境的影响比较大

我们将生产环境的构建配置中的

```js
new webpack.HashedModuleIdsPlugin()
```

替换为

```js
new webpack.NamedModulesPlugin()
```

可以再试下，效果跟HashedModuleIdsPlugin是一样的只不过文件大小会有些差别

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.10
```
