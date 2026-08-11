---
title: "webpack4 初体验"
date: "2025-07-04 14:02:19"
slug: "webpack4-chu-ti-yan"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4-初体验/"
  - "/2025/07/04/webpack4-初体验.html"
  - "/webpack4-初体验/"
  - "/webpack4-初体验.html"
  - "/2025/07/04/webpack4-chu-ti-yan/"
  - "/2025/07/04/webpack4-chu-ti-yan.html"
  - "/webpack4-chu-ti-yan.html"
---
**1、创建项目并安装webpack**

```bash
mkdir webpack4-demo && cd webpack4-demo
npm init -y
npm install webpack webpack-cli --save-dev
```

```bash
webpack4-demo
  |- package.json
  |- index.html
  |- /src
    |- index.js
```

src/index.js

```js
function component() {
  var element = document.createElement('div');

  // Lodash
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  return element;
}

document.body.appendChild(component());
```

index.html

```html
<!doctype html>
<html>
  <head>
    <title>起步</title>
    <script src="https://unpkg.com/xx@xx"></script>
  </head>
  <body>
    <script src="./src/index.js"></script>
  </body>
</html>
```

我们还需要调整 package.json 文件，以便确保我们安装包是私有的(private)，并且移除 main 入口。这可以防止意外发布你的代码。  
package.json

```json
{
    "name": "webpack-demo",
    "version": "1.0.0",
    "description": "",
    "private": true,
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "devDependencies": {
        "webpack": "^4.0.1",
        "webpack-cli": "^2.0.9"
    },
    "dependencies": {}
}
```

**2、创建一个打包文件**

首先，我们稍微调整下目录结构，将“源”代码(/src)从我们的“分发”代码(/dist)中分离出来。“源”代码是用于书写和编辑的代码。“分发”代码是构建过程产生的代码最小化和优化后的“输出”目录，最终将在浏览器中加载：

```bash
webpack4-demo
  |- package.json
  |- /dist
    |- index.html
  |- /src
    |- index.js
```

要在 index.js 中打包 lodash 依赖，我们需要在本地安装 library：

```bash
npm install --save lodash
```

现在，在我们的脚本中 import lodash：  
src/index.js

```js
import _ from 'lodash';

function component() {
  var element = document.createElement('div');

  // Lodash, now imported by this script
  element.innerHTML = _.join(['Hello', 'webpack'], ' ');

  return element;
}

document.body.appendChild(component());
```

现在，由于通过打包来合成脚本，我们必须更新 index.html 文件。因为现在是通过 import 引入 lodash，所以将 lodash `<script>` 删除，然后修改另一个 `<script>` 标签来加载 bundle，而不是原始的 /src 文件：

```html
<!doctype html>
<html>

<head>
    <title>起步</title>
</head>

<body>
    <script src="main.js"></script>
</body>

</html>
```

```bash
$ npx webpack
Hash: 7262ef43d0038d60faef
Version: webpack 4.9.1
Time: 3375ms
Built at: 2018-05-27 12:07:49
  Asset    Size  Chunks             Chunk Names
main.js  70 KiB       0  [emitted]  main
Entrypoint main = main.js
[1] (webpack)/buildin/module.js 519 bytes {0} [built]
[2] (webpack)/buildin/global.js 509 bytes {0} [built]
[3] ./src/index.js 255 bytes {0} [built]
    + 1 hidden module
```

在浏览器中打开 index.html，如果一切访问都正常，你应该能看到以下文本：'Hello webpack'。

ES2015 中的 import 和 export 语句已经被标准化。虽然大多数浏览器还无法支持它们，但是 webpack 却能够提供开箱即用般的支持。

事实上，webpack 在幕后会将代码“转译”，以便旧版本浏览器可以执行。如果你检查 dist/main.js，你可以看到 webpack 具体如何实现，这是独创精巧的设计！除了 import 和 export，webpack 还能够很好地支持多种其他模块语法，更多信息请查看模块 API。

注意，webpack 不会更改代码中除 import 和 export 语句以外的部分。如果你在使用其它 ES2015 特性，请确保你在 webpack 的 loader 系统中使用了一个像是 Babel 或 Bublé 的转译器

**3、创建webpack配置文件**

在 webpack 4 中，可以无须任何配置使用，然而大多数项目会需要很复杂的设置，这就是为什么 webpack 仍然要支持 配置文件。这比在终端(terminal)中手动输入大量命令要高效的多，所以让我们创建一个取代以上使用 CLI 选项方式的配置文件

```bash
webpack4-demo
  |- package.json
  |- webpack.config.js
  |- /dist
    |- index.html
  |- /src
    |- index.js
```

webpack.config.js

```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

编译下看看

```bash
$ npx webpack --config webpack.config.js
Hash: b983ef9ac0012695b0e5
Version: webpack 4.9.1
Time: 3369ms
Built at: 2018-05-27 12:09:40
    Asset    Size  Chunks             Chunk Names
bundle.js  70 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[1] (webpack)/buildin/module.js 519 bytes {0} [built]
[2] (webpack)/buildin/global.js 509 bytes {0} [built]
[3] ./src/index.js 255 bytes {0} [built]
    + 1 hidden module

WARNING in configuration
The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/concepts/mode/
```

**4、NPM 脚本配置**  
考虑到用 CLI 这种方式来运行本地的 webpack 不是特别方便，我们可以设置一个快捷方式。在 package.json 添加一个 npm 脚本(npm script)：  
package.json

```json
{
  "name": "webpack4-demo",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "css-loader": "^0.28.11",
    "style-loader": "^0.21.0",
    "webpack": "^4.9.1",
    "webpack-cli": "^2.1.4"
  },
  "dependencies": {
    "lodash": "^4.17.10"
  }
}
```

现在，可以使用 npm run build 命令，来替代我们之前使用的 npx 命令。注意，使用 npm 的 scripts，我们可以像使用 npx 那样通过模块名引用本地安装的 npm 包。这是大多数基于 npm 的项目遵循的标准，因为它允许所有贡献者使用同一组通用脚本（如果必要，每个 flag 都带有 --config 标志）。

```bash
$ npm run build

> xx@xx build /Users/durban/nodejs/webpack4-demo
> webpack

Hash: b983ef9ac0012695b0e5
Version: webpack 4.9.1
Time: 350ms
Built at: 2018-05-27 12:10:14
    Asset    Size  Chunks             Chunk Names
bundle.js  70 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[1] (webpack)/buildin/module.js 519 bytes {0} [built]
[2] (webpack)/buildin/global.js 509 bytes {0} [built]
[3] ./src/index.js 255 bytes {0} [built]
    + 1 hidden module

WARNING in configuration
The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/concepts/mode/
```

// 重点  
通过向 npm run build 命令和你的参数之间添加两个中横线，可以将自定义参数传递给 webpack，例如：npm run build -- --colors。

整个体验下来还可以，后面继续体验，最后的目录结果如下

```bash
├── dist
│   ├── bundle.js
│   ├── index.html
│   └── main.js
├── index.html
├── package-lock.json
├── package.json
├── src
│   └── index.js
├── webpack-demo
└── webpack.config.js
```

> 体验环境  
> mac os  
> npm - 6.0.1  
> node - v8.9.4

**项目地址:https://github.com/durban89/webpack4-demo.git**
