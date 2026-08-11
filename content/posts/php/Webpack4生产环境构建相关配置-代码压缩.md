---
title: "Webpack4生产环境构建相关配置 - 代码压缩"
date: "2025-07-07 15:52:12"
slug: "webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-dai-ma-ya-suo"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4生产环境构建相关配置-代码压缩/"
  - "/2025/07/07/Webpack4生产环境构建相关配置-代码压缩.html"
  - "/Webpack4生产环境构建相关配置-代码压缩/"
  - "/Webpack4生产环境构建相关配置-代码压缩.html"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-dai-ma-ya-suo/"
  - "/2025/07/07/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-dai-ma-ya-suo.html"
  - "/webpack4-sheng-chan-huan-jing-gou-jian-xiang-guan-pei-zhi-dai-ma-ya-suo.html"
---
继续之前的分享【[Webpack4生产环境构建相关配置 - 基础配置](https://www.gowhich.com/blog/832)】

下面让我们用我们之前文章的项目来做下实践

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-webpack-demo && cd react-webpack-demo
npm install
```

1、安装代码压缩需要的插件uglifyjs-webpack-plugin

```bash
npm i -D uglifyjs-webpack-plugin
```

2、修改webpack配置  
修改webpack.prod.js

> 为什么改webpack.prod.js而不是webpack.dev.js，因为在生产环境为了减少文件的大小以加快文件的加载速度，以此来提高用户的体验度

在plugins加入如下代码

```js
new UglifyJsPlugin()
```

结果如下

```js
plugins: [
  new CleanWebpackPlugin(['dist']),
  new HtmlWebpackPlugin({
    title: 'React + ReactRouter',
    filename: './index.html', // 调用的文件
    template: './index.html', // 模板文件
  }),
  new UglifyJsPlugin(),
],
```

我们做下对比，使用压缩工具，跟不使用压缩工具的区别  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528988589/gowhich/%E4%BB%A3%E7%A0%81%E5%8E%8B%E7%BC%A9_1_WX20180612-170055.png)  
上图是使用压缩扩展的  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528988589/gowhich/%E4%BB%A3%E7%A0%81%E5%8E%8B%E7%BC%A9_2_WX20180612-170337.png)  
上图是未使用压缩扩展的  
奇怪好像没有什么区别，也许webpack在生产环境下应该默认调用了压缩扩展

**source map**  
这里引用下官方的话

“  
我们鼓励你在生产环境中启用 source map，因为它们对调试源码(debug)和运行基准测试(benchmark tests)很有帮助。虽然有如此强大的功能，然而还是应该针对生成环境用途，选择一个构建快速的推荐配置（具体细节请查看 devtool）。对于本指南，我们将在生产环境中使用 source-map 选项，而不是我们在开发环境中用到的 inline-source-map  
”  
因人而异吧，我们来看下这个如果我们加了会有什么变化

修改配置webpack.prod.js  
添加

```js
devtool: 'source-map',
```

并修改

```js
new UglifyJSPlugin()
```

为下面的代码

```js
new UglifyJSPlugin({
  sourceMap: true
})
```

webpack.prod.js结果如下

```js
module.exports = merge(common, {
  mode: 'production',
  devtool: 'source-map',
  entry: {
    app: [
      './src/index.jsx',
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
    new UglifyJsPlugin({
      sourceMap: true,
    }),
  ],
});
```

运行下

```bash
npm run build
```

如下图  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528988588/gowhich/%E4%BB%A3%E7%A0%81%E5%8E%8B%E7%BC%A9_3_WX20180612-183151.png)  
可以看出文件稍微变大了。

开发环境不建议使用代码压缩，这样不方便调试，生产环境可加可不加，因人而异，因需求而异。

项目地址

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag：v_1.0.7
```
