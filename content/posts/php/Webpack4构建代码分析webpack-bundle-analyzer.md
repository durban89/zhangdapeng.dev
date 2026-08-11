---
title: "Webpack4构建代码分析webpack-bundle-analyzer"
date: "2025-07-07 15:59:08"
slug: "webpack4-gou-jian-dai-ma-fen-xi-webpack-bundle-analyzer"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4构建代码分析webpack-bundle-analyzer/"
  - "/2025/07/07/Webpack4构建代码分析webpack-bundle-analyzer.html"
  - "/Webpack4构建代码分析webpack-bundle-analyzer/"
  - "/Webpack4构建代码分析webpack-bundle-analyzer.html"
  - "/2025/07/07/webpack4-gou-jian-dai-ma-fen-xi-webpack-bundle-analyzer/"
  - "/2025/07/07/webpack4-gou-jian-dai-ma-fen-xi-webpack-bundle-analyzer.html"
  - "/webpack4-gou-jian-dai-ma-fen-xi-webpack-bundle-analyzer.html"
---
用交互式可缩放树形图显示webpack输出文件的大小。感觉用了之后又高大上了。

实践的上面我还是使用前面文章的项目，没有的可以按照如下的部署进行安装

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
```

下面开始配置并使用webpack-bundle-analyzer

**安装**

```bash
npm install --save-dev webpack-bundle-analyzer
```

配置[这里只配置webpack.prod.js]  
分别添加如下代码到文件中

```js
const WebpackBundleAnalyzer = require('webpack-bundle-analyzer');

const {
  BundleAnalyzerPlugin,
} = WebpackBundleAnalyzer;

new BundleAnalyzerPlugin()
```

添加后结果如下

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
const WebpackBundleAnalyzer = require('webpack-bundle-analyzer');
const common = require('./webpack.common');

const {
  BundleAnalyzerPlugin,
} = WebpackBundleAnalyzer;

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
    new BundleAnalyzerPlugin(),
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

结果类似如下图  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529666473/gowhich/webpack-bundle-analyzer_1_WX20180621-155507.png)

会自动打开一个浏览器，如下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529666481/gowhich/webpack-bundle-analyzer_2_WX20180621-155507.png)  
是不是很赞，以后我们就可以根据这个来分析打包的情况

我们也可以命令行的方式，操作如下[注意，需要将配置中的new BundleAnalyzerPlugin()注释掉，不然会在下面的操作执行产生冲突而卡住]

```bash
npx webpack --config=webpack.prod.js --profile --json > stats.json
```

然后执行

```bash
npx webpack-bundle-analyzer ./stats.json
```

输出如下

```bash
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/0.d12185fd8e6117c063c6.bundle.js": no such file
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/2.682c3024cf3095674f24.bundle.js": no such file
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/manifest.e6adb1315c7823bc535e.bundle.js": no such file
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/vendor.7aaf509786ae83a5de3c.bundle.js": no such file
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/app.bb3713d2c6aeb09ceeb9.bundle.js": no such file
Error parsing bundle asset "/Users/durban/nodejs/webpack-react-demo/1.8539b93fe0620243ce58.bundle.js": no such file

No bundles were parsed. Analyzer will show only original module sizes from stats file.

Webpack Bundle Analyzer is started at http://127.0.0.1:8888
Use Ctrl+C to close it
```

发现有错误，找不到要分析的文件，更换下执行命令

```bash
npx webpack-bundle-analyzer ./stats.json dist
```

类似如下输出

```bash
Webpack Bundle Analyzer is started at http://127.0.0.1:8888
Use Ctrl+C to close it
```

跟上面的类似

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.12
```
