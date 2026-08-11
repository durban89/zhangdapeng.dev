---
title: "webpack4 初体验 - 资源管理 - 加载数据"
date: "2025-07-04 14:26:58"
slug: "webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-shu-ju"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验-资源管理-加载数据/"
  - "/2025/07/04/webpack4-初体验-资源管理-加载数据.html"
  - "/webpack4-初体验-资源管理-加载数据/"
  - "/webpack4-初体验-资源管理-加载数据.html"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-shu-ju/"
  - "/2025/07/04/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-shu-ju.html"
  - "/webpack4-chu-ti-yan-zi-yuan-guan-li-jia-zai-shu-ju.html"
---
继续上一篇博文[[webpack4 初体验 - 资源管理 - 加载字体](https://www.gowhich.com/blog/819)]

可以加载的有用资源还有数据，如 JSON 文件，CSV、TSV 和 XML。类似于 NodeJS，JSON 支持实际上是内置的，也就是说 import Data from './data.json' 默认将正常运行。要导入 CSV、TSV 和 XML，你可以使用 csv-loader 和 xml-loader。让我们处理这三类文件：

```bash
npm install --save-dev csv-loader xml-loader
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

给你的项目添加一些数据文件

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
│   └── index.js
└── webpack.config.js
```

src/data.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
    <to>BJ</to>
    <from>SH</from>
    <heading>Reminder</heading>
    <body>Call Durban on Tuesday</body>
</note>
```

现在，你可以 import 这四种类型的数据(JSON, CSV, TSV, XML)中的任何一种，所导入的 Data 变量将包含可直接使用的已解析 JSON：src/index.js

```js
import _ from 'lodash';
import './index.css';
import DemoImage from './demo-image.png';
import Data from './data.xml';

function component() {
  let element = document.createElement('div');

  // Lodash, now imported by this script
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');
  element.classList.add('red-color');

  let img = new Image();
  img.src = DemoImage;
  element.appendChild(img);

  console.log(Data);

  return element;
}

document.body.appendChild(component());
```

再次重新构建

```bash
$ npm run build

> xxx@xxx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: 0325e1f96ed155017d91
Version: webpack 4.9.1
Time: 3802ms
Built at: 2018-05-27 13:16:12
                                 Asset      Size  Chunks                    Chunk Names
  84cfb15e659da6455e7ad3a9d702b9c6.png  1.55 MiB          [emitted]  [big]
 fa2772327f55d8198301fdb8bcfc8158.woff  22.9 KiB          [emitted]
448c34a56d699c29117adc64c43affeb.woff2  17.6 KiB          [emitted]
                             bundle.js  76.6 KiB       0  [emitted]         main
Entrypoint main = bundle.js
 [0] ./src/demo-image.png 82 bytes {0} [built]
 [1] ./src/data.xml 110 bytes {0} [built]
 [5] ./src/glyphicons-halflings-regular.woff 83 bytes {0} [built]
 [6] ./src/glyphicons-halflings-regular.woff2 84 bytes {0} [built]
 [9] ./node_modules/css-loader!./src/index.css 627 bytes {0} [built]
[10] ./src/index.css 1.05 KiB {0} [built]
[11] (webpack)/buildin/module.js 519 bytes {0} [built]
[12] (webpack)/buildin/global.js 509 bytes {0} [built]
[13] ./src/index.js 488 bytes {0} [built]
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

当你打开 index.html 并查看开发者工具中的控制台，你应该能够看到你导入的数据被打印在了上面！

在使用 d3 等工具来实现某些数据可视化时，预加载数据会非常有用。我们可以不用再发送 ajax 请求，然后于运行时解析数据，而是在构建过程中将其提前载入并打包到模块中，以便浏览器加载模块后，可以立即从模块中解析数据。

总结

之前几篇webpack资源管理的内容中最出色之处是，以对应的各种方式加载资源，你可以以更直观的方式将模块和资源组合在一起。无需依赖于含有全部资源的 /assets 目录，而是将资源与代码组合在一起。例如，类似这样的结构会非常有用：

```bash
|– /components
|  |– /my-component
|  |  |– index.jsx
|  |  |– index.css
|  |  |– icon.svg
|  |  |– img.png
-
```

这种配置方式会使你的代码更具备可移植性，因为现有的统一放置的方式会造成所有资源紧密耦合在一起。假如你想在另一个项目中使用 /my-component，只需将其复制或移动到 /components 目录下。只要你已经安装了任何扩展依赖(external dependencies)，并且你已经在配置中定义过相同的 loader，那么项目应该能够良好运行。

但是，假如你无法使用新的开发方式，只能被固定于旧有开发方式，或者你有一些在多个组件（视图、模板、模块等）之间共享的资源。你仍然可以将这些资源存储在公共目录(base directory)中，甚至配合使用 alias 来使它们更方便 import 导入。

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:<https://github.com/durban89/webpack4-demo.git>**
