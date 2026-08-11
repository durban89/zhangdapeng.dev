---
title: "Webpack4 之 编译Typescript"
date: "2025-07-07 16:41:08"
slug: "webpack4-zhi-bian-yi-typescript"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/07/Webpack4-之-编译Typescript/"
  - "/2025/07/07/Webpack4-之-编译Typescript.html"
  - "/Webpack4-之-编译Typescript/"
  - "/Webpack4-之-编译Typescript.html"
  - "/2025/07/07/webpack4-zhi-bian-yi-typescript/"
  - "/2025/07/07/webpack4-zhi-bian-yi-typescript.html"
  - "/webpack4-zhi-bian-yi-typescript.html"
---
TypeScript 是 JavaScript 的超集，为其增加了类型系统，可以编译为普通的 JavaScript 代码。这篇文章里我们将时间 webpack 是如何跟 TypeScript 进行集成。

一如既往的创建项目的流程

```bash
mkdir webpack4-typescript-demo
cd webpack4-typescript-demo
npm init -y
npm install webpack webpack-cli --save-dev
```

构建项目，目录结构如下

```bash
├── package.json
├── src
│   └── index.tsx
└── webpack.config.js
```

## **基础安装**

首先，执行以下命令，安装 TypeScript 编译器和需要的loader：

```bash
npm install --save-dev typescript ts-loader
```

现在，我们将修改目录结构和配置文件：

```bash
├── package.json
├── src
│   └── index.tsx
├── tsconfig.json
└── webpack.config.js
```

设置一个基本的配置，来支持 JSX，并将 TypeScript 编译到 ES5  
tsconfig.json内容如下

```json
{
    "compilerOptions": {
        "outDir": "./dist/",
        "noImplicitAny": true,
        "module": "es6",
        "target": "es5",
        "jsx": "react",
        "allowJs": true
    }
}
```

在 webpack 配置中处理 TypeScript  
webpack.config.js

```js
const path = require('path');

module.exports = {
  entry: './src/index.tsx',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ '.tsx', '.ts', '.js' ]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

这会直接将 webpack 的入口起点指定为 ./index.tsx，然后通过 ts-loader \_加载所有的 .ts 和 .tsx 文件，并且在当前目录输出\_一个 bundle.js 文件。

*ts-loader*  
为什么使用 ts-loader，因为它能够很方便地启用额外的 webpack 功能，例如将其他 web 资源导入到项目中。

*source-map*  
要启用 source map，我们必须配置 TypeScript，以将内联的 source map 输出到编译过的 JavaScript 文件。必须在 TypeScript 配置中添加下面这行：  
tsconfig.json

```json
{
    "compilerOptions": {
        "outDir": "./dist/",
        "noImplicitAny": true,
        "module": "es6",
        "sourceMap": true, // 添加这行
        "target": "es5",
        "jsx": "react",
        "allowJs": true
    }
}
```

然后配置webpack，告诉 webpack 提取这些 source map，并内联到最终的 bundle 中。  
添加如下

```js
devtool: 'inline-source-map',
```

代码  
webpack.config.js

```js
const path = require('path');

module.exports = {
  entry: './src/index.tsx',
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ '.tsx', '.ts', '.js' ]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

## **如何使用第三方库**

当从 npm 安装第三方库时，一定要牢记同时安装这个库的类型声明文件。你可以从 TypeSearch[http://microsoft.github.io/TypeSearch/] 中找到并安装这些第三方库的类型声明文件。  
举个例子，如果想安装 lodash 这个库的类型声明文件，我们可以运行下面的命令：

```bash
npm install --save-dev @types/lodash
```

## **动手写实例**

当前项目目录结构如下

```bash
├── dist
│   └── index.html
├── package.json
├── src
│   └── index.tsx
├── tsconfig.json
└── webpack.config.js
```

添加dist/index.html

```html
<!doctype html>
<html>

<head>
    <title>Webpack - TypeScript</title>
</head>

<body>
    <script src="./bundle.js"></script>
</body>

</html>
```

src/index.tsx内容如下

```tsx
import * as _ from "lodash";

function component() {
    var element = document.createElement('div');
    element.innerHTML = _.padStart("Hello TypeScript!", 20, "-");
    return element;
}

document.body.appendChild(component());
```

运行

```bash
npm run build
```

dist目录会多一个dist文件  
使用浏览器打开dist/index.html  
会看到输出如下内容

```bash
---Hello TypeScript!
```

项目地址

```bash
https://github.com/durban89/webpack4-typescript-demo.git
```
