---
title: "Webpack4代码分割实现按需加载/懒加载"
date: "2025-07-07 15:48:49"
slug: "webpack4-dai-ma-fen-ge-shi-xian-an-xu-jia-zai-lan-jia-zai"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4代码分割实现按需加载/懒加载/"
  - "/2025/07/07/Webpack4代码分割实现按需加载/懒加载.html"
  - "/Webpack4代码分割实现按需加载/懒加载/"
  - "/Webpack4代码分割实现按需加载/懒加载.html"
  - "/2025/07/07/Webpack4代码分割实现按需加载-懒加载/"
  - "/2025/07/07/Webpack4代码分割实现按需加载-懒加载.html"
  - "/2025/07/07/webpack4-dai-ma-fen-ge-shi-xian-an-xu-jia-zai-lan-jia-zai/"
  - "/2025/07/07/webpack4-dai-ma-fen-ge-shi-xian-an-xu-jia-zai-lan-jia-zai.html"
  - "/webpack4-dai-ma-fen-ge-shi-xian-an-xu-jia-zai-lan-jia-zai.html"
---
为什么要实现按需加载或懒加载，引用下官网的话

> 懒加载或者按需加载，是一种很好的优化网页或应用的方式。这种方式实际上是先把你的代码在一些逻辑断点处分离开，然后在一些代码块中完成某些操作后，立即引用或即将引用另外一些新的代码块。这样加快了应用的初始加载速度，减轻了它的总体体积，因为某些代码块可能永远不会被加载。

1、现在clone原始项目如下

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git webpack-react-demo
cd webpack-react-demo
npm install
npm start
```

2、安装代码分割懒加载需要的库

```bash
npm install babel-plugin-syntax-dynamic-import --save-dev
npm install react-loadable
```

3、代码配置  
webpack.config.js

```js
output: {
  filename: '[name].bundle.js',
  path: path.resolve(__dirname, 'dist'),
},
```

添加如下代码

``` Webpack
chunkFilename: '[name].bundle.js',
```

结果如下

```bash
output: {
  filename: '[name].bundle.js',
  chunkFilename: '[name].bundle.js',
  path: path.resolve(__dirname, 'dist'),
},
```

.babelrc

``` js
"plugins": [
  "transform-async-to-generator",
  "transform-strict-mode",
  "transform-object-assign",
  "transform-decorators-legacy",
  "react-hot-loader/babel"
],
```

plugins中添加如下代码

``` js
"syntax-dynamic-import"
```

结果如下

``` js
"plugins": [
  "transform-async-to-generator",
  "transform-strict-mode",
  "transform-object-assign",
  "transform-decorators-legacy",
  "react-hot-loader/babel",
  "syntax-dynamic-import"
],
```

4、修改代码调用  
修改src/routes.jsx  
添加

``` jsx
import Loadable from 'react-loadable';
```

将路由配置中的

```jsx
<Route path="/about" component={AboutComponent} />
```

改为

```jsx
<Route
  path="/about"
  component={Loadable({
    loader: () => import('./components/AboutComponent'),
    loading: LoadingComponent,
  })}
/>
```

从webpack-dev-server控制台可以看出原来的如下图

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528816837/gowhich/WX20180611-141726_1.png)  
更新代码后通过webpack-dev-server控制台可以看出多了一个类似0.bundle.js的文件，如下图  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528816841/gowhich/WX20180611-142156_2.png)

同样的逻辑我们更改 /topics对应的组件和/counter对应的组件  
从webpack-dev-server控制台可以看出,多了几个类似的文件

如果我重新启动webpack-dev-server的话可以从webpack-dev-server控制台日志看出类似下图的输出  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/q_81/v1528816838/gowhich/WX20180611-142759_3.png)

小知识点  
将

```js
chunkFilename: '[name].bundle.js',
```

改为

```js
chunkFilename: '[chunkhash].bundle.js',
```

重新

```bash
npm start
```

看看日志输出，会看到类似如下的输出  
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528816838/gowhich/WX20180611-143747_4.png)  
这个特点有助于项目的版本发布需求

```bash
https://github.com/durban89/webpack4-react16-reactrouter-demo.git
tag: v_1.0.4
```
