---
title: "使用TypeScript开发React应用(一)"
date: "2025-07-10 10:57:30"
slug: "shi-yong-typescript-kai-fa-react-ying-yong-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/使用TypeScript开发React应用(一)/"
  - "/2025/07/10/使用TypeScript开发React应用(一).html"
  - "/使用TypeScript开发React应用(一)/"
  - "/使用TypeScript开发React应用(一).html"
  - "/2025/07/10/使用TypeScript开发React应用-一/"
  - "/2025/07/10/使用TypeScript开发React应用-一.html"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-yi/"
  - "/2025/07/10/shi-yong-typescript-kai-fa-react-ying-yong-yi.html"
  - "/shi-yong-typescript-kai-fa-react-ying-yong-yi.html"
---
本次分享如何使用[React](http://facebook.github.io/react/)连接TypeScript开发应用。 到最后，我们会得到一个如下的知识掌握

* 一个使用React和TypeScript的项目
* 使用[TSLint](https://github.com/palantir/tslint)进行linting
* 用[Jest](https://facebook.github.io/jest/)和[Enzyme](http://airbnb.io/enzyme/)测试
* 使用[Redux](https://github.com/reactjs/react-redux)进行状态管理

我们将使用create-react-app工具快速初始化一个React项目。

我们假设您已经在使用npm的Node.js。 您可能还想了解React的基础知识。这里就暂不做介绍了，前面的文章有对应的介绍，可以翻一番我前面的分享

### 安装create-react-app

我们将使用create-react-app，因为它为React项目设置了一些有用的工具和规范默认值。 这只是一个命令行实用程序来构建新的React项目。

```bash
npm install -g create-react-app
```

### 初始化创建项目

我们将创建一个名为ts-react-app的新项目：

```bash
create-react-app ts-react-app --scripts-version=react-scripts-ts
```

react-scripts-ts是一组调整，用于采用标准的create-react-app项目管道并将TypeScript引入混合。

此时，您的项目布局应如下所示：

```bash
├── README.md
├── images.d.ts
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
├── src
│   ├── App.css
│   ├── App.test.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── index.tsx
│   ├── logo.svg
│   └── registerServiceWorker.ts
├── tsconfig.json
├── tsconfig.prod.json
├── tsconfig.test.json
└── tslint.json
```

*注意点*

* tsconfig.json包含我们项目的特定于TypeScript的选项。

  + 我们还有一个tsconfig.prod.json和一个tsconfig.test.json，以防我们想要对我们的生产版本或我们的测试版本进行任何调整。
* tslint.json存储我们的linter，TSLint将使用的设置。
* package.json包含我们的依赖项，以及我们想要运行的命令的一些快捷方式，用于测试，预览和部署我们的应用程序。
* public包含静态资产，例如我们计划部署到的HTML页面或图像。 除index.html之外，您可以删除此文件夹中的任何文件。
* src包含我们的TypeScript和CSS代码。 index.tsx是我们文件的入口点，是必需的。
* images.d.ts将告诉TypeScript可以导入某些类型的图像文件，create-react-app支持这些文件。

### 设置源代码管理

我们的测试工具Jest期望存在某种形式的源代码控制（例如Git或Mercurial）。 为了正确运行，我们需要初始化一个git存储库。

```bash
cd ts-react-app
git init
git add .
git commit -m "Initial commit."
```

### 重写默认值

react-scripts-ts设置的TSLint配置有点过于热心。 让我们解决这个问题。

```bash
{
-  "extends": ["tslint:recommended", "tslint-react", "tslint-config-prettier"],
+  "extends": [],
+  "defaultSeverity": "warning",
   "linterOptions": {
     "exclude": [
       "config/**/*.js",
       "node_modules/**/*.ts"
     ]
   }
 }
```

[配置TSLint](https://palantir.github.io/tslint/usage/configuration/)超出了此篇文章要分享的范围，但您可以随意尝试适合您的操作。

### 运行项目

运行项目就像运行一样简单

```bash
npm run start
```

这将运行我们的package.json中指定的启动脚本，并将在我们保存文件时生成重新加载页面的服务器。 通常，服务器在[http://localhost:3000运行，但应自动为您打开。](http://localhost:3000%E8%BF%90%E8%A1%8C%EF%BC%8C%E4%BD%86%E5%BA%94%E8%87%AA%E5%8A%A8%E4%B8%BA%E6%82%A8%E6%89%93%E5%BC%80%E3%80%82) 这允许我们快速预览更改，从而收紧迭代循环。

### 测试项目

测试也只是一个命令：

```bash
npm run test
```

此命令针对扩展名以.test.ts或.spec.ts结尾的所有文件运行Jest，这是一个非常有用的测试实用程序。 与npm run start命令一样，Jest会在检测到更改后立即自动运行。 如果您愿意，可以并排运行npm run start和npm run test，以便您可以预览更改并同时测试它们。

### 创建生产构建

使用npm run start运行项目时，我们最终没有使用优化的构建。 通常，我们希望我们发送给用户的代码尽可能快速和小巧、缩小等某些优化可以实现这一目标，但通常需要更多时间。 我们称之为"production"构建的构建（与开发构建相对）。

要运行生产构建，只需运行即可

```bash
npm run build
```

这将分别在./build/static/js和./build/static/css中创建优化的JS和CSS构建。

您不需要在大多数时间运行生产构建，但如果您需要测量应用程序的最终大小等内容，则非常有用。

未完待续...
