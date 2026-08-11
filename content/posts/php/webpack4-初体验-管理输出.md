---
title: "webpack4 初体验 - 管理输出"
date: "2025-07-04 14:27:05"
slug: "webpack4-chu-ti-yan-guan-li-shu-chu"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-管理输出/"
  - "/2025/07/04/webpack4-初体验-管理输出.html"
  - "/webpack4-初体验-管理输出/"
  - "/webpack4-初体验-管理输出.html"
  - "/2025/07/04/webpack4-chu-ti-yan-guan-li-shu-chu/"
  - "/2025/07/04/webpack4-chu-ti-yan-guan-li-shu-chu.html"
  - "/webpack4-chu-ti-yan-guan-li-shu-chu.html"
---
我们在 index.html 文件中手动引入所有资源，然而随着应用程序增长，并且一旦开始对文件名使用哈希(hash)]并输出多个 bundle，手动地对 index.html 文件进行管理，一切就会变得困难起来。然而，可以通过一些插件，会使这个过程更容易操控。

首先，让我们调整一下我们的项目：

```bash
├── dist
│   ├── 448c34a56d699c29117adc64c43affeb.woff2
│   ├── 84cfb15e659da6455e7ad3a9d702b9c6.png
│   ├── bundle.js
│   ├── fa2772327f55d8198301fdb8bcfc8158.woff
│   ├── index.html
│   └── main.js
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── data.xml
│   ├── demo-image.png
│   ├── font.woff2
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   ├── glyphicons-halflings-regular.woff2
│   ├── index.css
│   ├── index.js
│   └── print.js
└── webpack.config.js
```

我们在 src/print.js 文件中添加一些逻辑：

src/print.js

```js
export default function printMe() {
  console.log('I get called from print.js!');
}
```

并且在 src/index.js 文件中使用这个函数：src/index.js

```js
import _ from 'lodash';
import './index.css';
import DemoImage from './demo-image.png';
import Data from './data.xml';
import printMe from './print.js';

function component() {
  let element = document.createElement('div');
  let btn = document.createElement('button');

  // Lodash, now imported by this script
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');
  element.classList.add('red-color');

  let img = new Image();
  img.src = DemoImage;
  element.appendChild(img);

  console.log(Data);

  btn.innerHTML = '点击我并查看控制台!';
  btn.onclick = printMe;
  element.appendChild(btn);

  return element;
}

document.body.appendChild(component());
```

我们还要更新 dist/index.html 文件，来为 webpack 分离入口做好准备：dist/index.html

```html
<!doctype html>
<html>

<head>
    <title>输出管理</title>
    <script src="./print.bundle.js"></script>
</head>

<body>
    <script src="./app.bundle.js"></script>
</body>

</html>
```

现在调整配置。我们将在 entry 添加 src/print.js 作为新的入口起点（print），然后修改 output，以便根据入口起点名称动态生成 bundle 名称：  
webpack.config.js

```js
const path = require('path');

module.exports = {
  entry: {
    app: './src/index.js',
    print: './src/print.js'
  },
  output: {
    filename: '[name].bundle.js',
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
      },
      {
        test: /\.(csv|tsv)$/,
        use: [
          'csv-loader',
        ]
      },
      {
        test: /\.xml$/,
        use: [
          'xml-loader',
        ]
      }
    ],
  }
};
```

执行 npm run build，然后看到生成如下：

```bash
$ npm run build

> xxx@xxx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: 9d8ee08ba9107370fec6
Version: webpack 4.9.1
Time: 3696ms
Built at: 2018-05-27 13:32:23
                                 Asset       Size  Chunks                    Chunk Names
  84cfb15e659da6455e7ad3a9d702b9c6.png   1.55 MiB          [emitted]  [big]
 fa2772327f55d8198301fdb8bcfc8158.woff   22.9 KiB          [emitted]
448c34a56d699c29117adc64c43affeb.woff2   17.6 KiB          [emitted]
                       print.bundle.js  660 bytes       0  [emitted]         print
                         app.bundle.js   76.8 KiB    1, 0  [emitted]         app
Entrypoint app = app.bundle.js
Entrypoint print = print.bundle.js
 [0] ./src/print.js 83 bytes {0} {1} [built]
 [1] ./src/demo-image.png 82 bytes {1} [built]
 [2] ./src/data.xml 110 bytes {1} [built]
 [6] ./src/glyphicons-halflings-regular.woff 83 bytes {1} [built]
 [7] ./src/glyphicons-halflings-regular.woff2 84 bytes {1} [built]
[10] ./node_modules/css-loader!./src/index.css 627 bytes {1} [built]
[11] ./src/index.css 1.05 KiB {1} [built]
[12] (webpack)/buildin/module.js 519 bytes {1} [built]
[13] (webpack)/buildin/global.js 509 bytes {1} [built]
[14] ./src/index.js 654 bytes {1} [built]
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

我们可以看到，webpack 生成 print.bundle.js 和 app.bundle.js 文件，这也和我们在 index.html 文件中指定的文件名称相对应。如果你在浏览器中打开 index.html，就可以看到在点击按钮时会发生什么。

但是，如果我们更改了我们的一个入口起点的名称，甚至添加了一个新的名称，会发生什么？生成的包将被重命名在一个构建中，但是我们的index.html文件仍然会引用旧的名字。我们用 HtmlWebpackPlugin 来解决这个问题。

**配置HtmlWebpackPlugin**  
首先安装插件，并且调整 webpack.config.js 文件：webpack.config.js

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: {
    app: './src/index.js',
    print: './src/print.js'
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: '输出管理'
    }),
  ],
  output: {
    filename: '[name].bundle.js',
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
      },
      {
        test: /\.(csv|tsv)$/,
        use: [
          'csv-loader',
        ]
      },
      {
        test: /\.xml$/,
        use: [
          'xml-loader',
        ]
      }
    ],
  }
};
```

在我们构建之前，你应该了解，虽然在 dist/ 文件夹我们已经有 index.html 这个文件，然而 HtmlWebpackPlugin 还是会默认生成 index.html 文件。这就是说，它会用新生成的 index.html 文件，把我们的原来的替换。让我们看下在执行 npm run build 后会发生什么：

```bash
$ npm run build

> xxx@xxx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: 0f3c73600a9071697137
Version: webpack 4.9.1
Time: 882ms
Built at: 2018-05-27 13:37:08
                                 Asset       Size  Chunks                    Chunk Names
  84cfb15e659da6455e7ad3a9d702b9c6.png   1.55 MiB          [emitted]  [big]
 fa2772327f55d8198301fdb8bcfc8158.woff   22.9 KiB          [emitted]
448c34a56d699c29117adc64c43affeb.woff2   17.6 KiB          [emitted]
                       print.bundle.js  660 bytes       0  [emitted]         print
                         app.bundle.js   76.8 KiB    1, 0  [emitted]         app
                            index.html  241 bytes          [emitted]
Entrypoint app = app.bundle.js
Entrypoint print = print.bundle.js
 [0] ./src/print.js 83 bytes {0} {1} [built]
 [1] ./src/demo-image.png 82 bytes {1} [built]
 [2] ./src/data.xml 110 bytes {1} [built]
 [6] ./src/glyphicons-halflings-regular.woff 83 bytes {1} [built]
 [7] ./src/glyphicons-halflings-regular.woff2 84 bytes {1} [built]
[10] ./node_modules/css-loader!./src/index.css 627 bytes {1} [built]
[11] ./src/index.css 1.05 KiB {1} [built]
[12] (webpack)/buildin/module.js 519 bytes {1} [built]
[13] (webpack)/buildin/global.js 509 bytes {1} [built]
[14] ./src/index.js 654 bytes {1} [built]
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
Child html-webpack-plugin for "index.html":
     1 asset
    Entrypoint undefined = index.html
    [0] (webpack)/buildin/module.js 519 bytes {0} [built]
    [1] (webpack)/buildin/global.js 509 bytes {0} [built]
        + 2 hidden modules
```

如果你在代码编辑器中将 index.html 打开，你就会看到 HtmlWebpackPlugin 创建了一个全新的文件，所有的 bundle 会自动添加到 html 中。

如果你想要了解更多 HtmlWebpackPlugin 插件提供的全部功能和选项，那么你就应该多多熟悉 HtmlWebpackPlugin[https://github.com/jantimon/html-webpack-plugin] 仓库。

你还可以看一下 html-webpack-template，除了默认模板之外，还提供了一些额外的功能。

**清理 /dist 文件夹**

在之前的几篇关于webpack的文章中，会发现/dist 文件夹相当杂乱。webpack 会生成文件，然后将这些文件放置在 /dist 文件夹中，但是 webpack 无法追踪到哪些文件是实际在项目中用到的。

通常，在每次构建前清理 /dist 文件夹，是比较推荐的做法，因此只会生成用到的文件。让我们完成这个需求。

clean-webpack-plugin 是一个比较普及的管理插件，让我们安装和配置下。

配置CleanWebpackPlugin

```bash
npm install clean-webpack-plugin --save-dev
```

webpack.config.js

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  entry: {
    app: './src/index.js',
    print: './src/print.js'
  },
  plugins: [
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: 'Webpack-输出管理'
    }),
  ],
  output: {
    filename: '[name].bundle.js',
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
      },
      {
        test: /\.(csv|tsv)$/,
        use: [
          'csv-loader',
        ]
      },
      {
        test: /\.xml$/,
        use: [
          'xml-loader',
        ]
      }
    ],
  }
};
```

现在执行 npm run build，再检查 /dist 文件夹。如果一切顺利，你现在应该不会再看到旧的文件，只有构建后生成的文件！

```bash
$ npm run build

> xxx@xxx build /Users/durban/nodejs/webpack4-demo
> webpack

clean-webpack-plugin: /Users/durban/nodejs/webpack4-demo/dist has been removed.
Hash: 0f3c73600a9071697137
Version: webpack 4.9.1
Time: 887ms
Built at: 2018-05-27 13:44:59
                                 Asset       Size  Chunks                    Chunk Names
  84cfb15e659da6455e7ad3a9d702b9c6.png   1.55 MiB          [emitted]  [big]
 fa2772327f55d8198301fdb8bcfc8158.woff   22.9 KiB          [emitted]
448c34a56d699c29117adc64c43affeb.woff2   17.6 KiB          [emitted]
                       print.bundle.js  660 bytes       0  [emitted]         print
                         app.bundle.js   76.8 KiB    1, 0  [emitted]         app
                            index.html  249 bytes          [emitted]
Entrypoint app = app.bundle.js
Entrypoint print = print.bundle.js
 [0] ./src/print.js 83 bytes {0} {1} [built]
 [1] ./src/demo-image.png 82 bytes {1} [built]
 [2] ./src/data.xml 110 bytes {1} [built]
 [6] ./src/glyphicons-halflings-regular.woff 83 bytes {1} [built]
 [7] ./src/glyphicons-halflings-regular.woff2 84 bytes {1} [built]
[10] ./node_modules/css-loader!./src/index.css 627 bytes {1} [built]
[11] ./src/index.css 1.05 KiB {1} [built]
[12] (webpack)/buildin/module.js 519 bytes {1} [built]
[13] (webpack)/buildin/global.js 509 bytes {1} [built]
[14] ./src/index.js 654 bytes {1} [built]
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
Child html-webpack-plugin for "index.html":
     1 asset
    Entrypoint undefined = index.html
    [0] (webpack)/buildin/module.js 519 bytes {0} [built]
    [1] (webpack)/buildin/global.js 509 bytes {0} [built]
        + 2 hidden modules
```

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:<https://github.com/durban89/webpack4-demo.git>**
