---
title: "webpack4 初体验 - 资源管理 - 加载字体"
date: "2025-07-04 14:02:37"
slug: "webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-zi-ti"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-资源管理-加载字体/"
  - "/2025/07/04/webpack4-初体验-资源管理-加载字体.html"
  - "/webpack4-初体验-资源管理-加载字体/"
  - "/webpack4-初体验-资源管理-加载字体.html"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-zi-ti/"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-zi-ti.html"
  - "/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-zi-ti.html"
---
继续上一篇博文[[webpack4 初体验 - 资源管理 - 加载图片](https://www.gowhich.com/blog/818)]

像字体这样的其他资源如何处理呢？file-loader 和 url-loader 可以接收并加载任何文件，然后将其输出到构建目录。这就是说，我们可以将它们用于任何类型的文件，包括字体。让我们更新 webpack.config.js 来处理字体文件：

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

在项目中添加一些字体文件：

项目目录结构

```bash
├── dist
│   ├── 84cfb15e659da6455e7ad3a9d702b9c6.png
│   ├── bundle.js
│   ├── index.html
│   └── main.js
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── demo-image.png
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   ├── glyphicons-halflings-regular.woff2
│   ├── index.css
│   └── index.js
└── webpack.config.js
```

通过配置好 loader 并将字体文件放在合适的地方，你可以通过一个 @font-face 声明引入。本地的 url(...) 指令会被 webpack 获取处理，就像它处理图片资源一样：

src/index.css

```css
@font-face {
  font-family: 'index-font';
  src: url('./glyphicons-halflings-regular.woff2') format('woff2'), url('./glyphicons-halflings-regular.woff') format('woff');
  font-weight: '600';
  font-style: normal;
}

.red-color {
  color: red;
  font-family: 'index-font';
  background: url('./demo-image.png');
}
```

现在让我们重新构建来看看 webpack 是否处理了我们的字体：

```bash
$ npm run build

> xx@xx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: 1172ab68582d197a2b60
Version: webpack 4.9.1
Time: 3729ms
Built at: 2018-05-27 13:08:28
                                 Asset      Size  Chunks                    Chunk Names
  84cfb15e659da6455e7ad3a9d702b9c6.png  1.55 MiB          [emitted]  [big]
 fa2772327f55d8198301fdb8bcfc8158.woff  22.9 KiB          [emitted]
448c34a56d699c29117adc64c43affeb.woff2  17.6 KiB          [emitted]
                             bundle.js  76.4 KiB       0  [emitted]         main
Entrypoint main = bundle.js
 [0] ./src/demo-image.png 82 bytes {0} [built]
 [4] ./src/glyphicons-halflings-regular.woff 83 bytes {0} [built]
 [5] ./src/glyphicons-halflings-regular.woff2 84 bytes {0} [built]
 [8] ./node_modules/css-loader!./src/index.css 627 bytes {0} [built]
 [9] ./src/index.css 1.05 KiB {0} [built]
[10] (webpack)/buildin/module.js 519 bytes {0} [built]
[11] (webpack)/buildin/global.js 509 bytes {0} [built]
[12] ./src/index.js 433 bytes {0} [built]
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

重新打开 index.html 看看我们的 Hello webpack 文本显示是否换上了新的字体。如果一切顺利，你应该能看到变化。

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:<https://github.com/durban89/webpack4-demo.git>**
