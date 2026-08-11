---
title: "webpack4 初体验 - 资源管理 - 加载图片"
date: "2025-07-04 14:02:30"
slug: "webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-tu-pian"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-资源管理-加载图片/"
  - "/2025/07/04/webpack4-初体验-资源管理-加载图片.html"
  - "/webpack4-初体验-资源管理-加载图片/"
  - "/webpack4-初体验-资源管理-加载图片.html"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-tu-pian/"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-tu-pian.html"
  - "/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-tu-pian.html"
---
继续上一篇博文[[webpack4 初体验 - 资源管理 - 加载CSS](https://www.gowhich.com/blog/817)]

如果现在我们正在下载 CSS，但是我们的背景和图标这些图片，要如何处理呢？使用 file-loader，我们可以轻松地将这些内容混合到 CSS 中：

```bash
npm install --save-dev file-loader
```

webpack.config.js

```js
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
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          'file-loader',
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader',
        ]
      }
    ],
  }
};
```

现在，当你 import DemoImage from './demo-image.png'，该图像将被处理并添加到 output 目录，\_并且\_ DemoImage 变量将包含该图像在处理后的最终 url。当使用 css-loader 时，如上篇文章所示，你的 CSS 中的 url('./demo-image.png') 会使用类似的过程去处理。loader 会识别这是一个本地文件，并将 './demo-image.png' 路径，替换为输出目录中图像的最终路径。html-loader 以相同的方式处理 <img src="./demo-image.png" />。

我们向项目添加一个图像，然后看它是如何工作的，你可以使用任何你喜欢的图像：

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
│   ├── demo-image.png
│   ├── index.css
│   └── index.js
└── webpack.config.js
```

src/index.js

```js
import _ from 'lodash';
import './index.css';
import DemoImage from './demo-image.png'

function component() {
  let element = document.createElement('div');

  // Lodash, now imported by this script
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');
  element.classList.add('red-color');

  let img = new Image();
  img.src = DemoImage;
  element.appendChild(img);

  return element;
}

document.body.appendChild(component());
```

重新构建，并再次打开 index.html 文件

```bash
$ npm run build

> xx@xx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: 39cd25fedf5aaf1e45d6
Version: webpack 4.9.1
Time: 3710ms
Built at: 2018-05-27 12:50:13
                               Asset      Size  Chunks                    Chunk Names
84cfb15e659da6455e7ad3a9d702b9c6.png  1.55 MiB          [emitted]  [big]
                           bundle.js  76.1 KiB       0  [emitted]         main
Entrypoint main = bundle.js
 [0] ./src/demo-image.png 82 bytes {0} [built]
 [6] ./node_modules/css-loader!./src/index.css 324 bytes {0} [built]
 [7] ./src/index.css 1.05 KiB {0} [built]
 [8] (webpack)/buildin/module.js 519 bytes {0} [built]
 [9] (webpack)/buildin/global.js 509 bytes {0} [built]
[10] ./src/index.js 433 bytes {0} [built]
    + 5 hidden modules

WARNING in configuration
The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/concepts/mode/

WARNING in asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).
This can impact web performance.
Assets:
  84cfb15e659da6455e7ad3a9d702b9c6.png (1.55 MiB)

WARNING in webpack performance recommendations:
You can limit the size of your bundles by using import() or require.ensure to lazy load some parts of your application.
For more info visit https://webpack.js.org/guides/code-splitting/
```

如果一切顺利，和 Hello webpack 文本旁边的 img 元素一样，现在看到的图标是重复的背景图片。如果你检查此元素，你将看到实际的文件名已更改为像 84cfb15e659da6455e7ad3a9d702b9c6.png 一样。这意味着 webpack 在 src 文件夹中找到我们的文件，并成功处理过它！

下一步是，压缩和优化你的图像。可以通过 image-webpack-loader 和 url-loader 实现，具体的下次在继续。

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:<https://github.com/durban89/webpack4-demo.git>**
