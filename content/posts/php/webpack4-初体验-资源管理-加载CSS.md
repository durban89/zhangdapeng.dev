---
title: "webpack4 初体验 - 资源管理 - 加载CSS"
date: "2025-07-04 14:02:26"
slug: "webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-css"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-资源管理-加载CSS/"
  - "/2025/07/04/webpack4-初体验-资源管理-加载CSS.html"
  - "/webpack4-初体验-资源管理-加载CSS/"
  - "/webpack4-初体验-资源管理-加载CSS.html"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-css/"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-css.html"
  - "/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-css.html"
---
继续上一篇博文[[webpack4 初体验](https://www.gowhich.com/blog/816)]

**加载 CSS**  
为了从 JavaScript 模块中 import 一个 CSS 文件，你需要在 module 配置中 安装并添加 style-loader 和 css-loader：

```bash
npm install --save-dev style-loader css-loader
```

webpack 根据正则表达式，来确定应该查找哪些文件，并将其提供给指定的 loader。在这种情况下，以 .css 结尾的全部文件，都将被提供给 style-loader 和 css-loader。

webpack.config.js

```bash
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
        ],
      }
    ],
  }
};
```

这使你可以在依赖于此样式的文件中 import './index.css'。现在，当该模块运行时，含有 CSS 字符串的 `<style>` 标签，将被插入到 html 文件的 `<head>` 中。

我们尝试一下，通过在项目中添加一个新的 index.css 文件，并将其导入到我们的 index.js 中：

项目目录结构

```bash
├── dist
│   ├── bundle.js
│   ├── index.html
│   └── main.js
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── index.css
│   └── index.js
└── webpack.config.js
```

src/style.css

```css
.red-color {
  color: red;
}
```

src/index.js

```js
import _ from 'lodash';
import './index.css';

function component() {
  var element = document.createElement('div');

  // Lodash, now imported by this script
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');
  element.classList.add('red-color');

  return element;
}

document.body.appendChild(component());
```

现在运行构建命令：

```bash
$ npm run build

> xx@xx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: a4ca66fcccee921aa2ec
Version: webpack 4.9.1
Time: 3696ms
Built at: 2018-05-27 12:37:20
    Asset      Size  Chunks             Chunk Names
bundle.js  75.7 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[4] ./node_modules/css-loader!./src/index.css 189 bytes {0} [built]
[5] ./src/index.css 1.05 KiB {0} [built]
[6] (webpack)/buildin/module.js 519 bytes {0} [built]
[7] (webpack)/buildin/global.js 509 bytes {0} [built]
[8] ./src/index.js 315 bytes {0} [built]
    + 4 hidden modules

WARNING in configuration
The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/concepts/mode/
```

再次在浏览器中打开 index.html，你应该看到 Hello webpack 现在的样式是红色。要查看 webpack 做了什么，请检查页面（不要查看页面源代码，因为它不会显示结果），并查看页面的 head 标签。它应该包含我们在 index.js 中导入的 style 块元素。

请注意，在多数情况下，你也可以进行 CSS 分离，以便在生产环境中节省加载时间。最重要的是，现有的 loader 可以支持任何你可以想到的 CSS 处理器风格 - postcss, sass 和 less 等。

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:https://github.com/durban89/webpack4-demo.git**
