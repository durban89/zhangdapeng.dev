---
title: "如何创建高质量的TypeScript声明文件(十) - 发布"
date: "2025-07-10 10:57:23"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-fa-bu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(十)-发布/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(十)-发布.html"
  - "/如何创建高质量的TypeScript声明文件(十)-发布/"
  - "/如何创建高质量的TypeScript声明文件(十)-发布.html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-十-发布/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-十-发布.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-fa-bu/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-fa-bu.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-fa-bu.html"
---
### 发布

经过前面的文章介绍声明文件的使用，现在您应该可以创作一个声明文件了，并且可以将创作的文件发布到npm了。发布的话可以通过两种主要方式将声明文件发布到npm：

1. 打包你的npm包
2. 在npm上发布到[@types组织](https://www.npmjs.com/~types)。

如果你的包是用TypeScript编写的，那么第一种方法是受欢迎的。 使用--declaration标志生成声明文件。 这样，您的声明和JavaScript始终保持同步。

如果您的包不是用TypeScript编写的，那么第二种方法是首选方法。

**在你的npm包中包含声明**

如果你的包有一个main.js文件，你还需要在package.json文件中指明主声明文件。 将types属性设置为指向打包的声明文件。 例如：

```json
{
    "name": "awesome",
    "author": "Vandelay Industries",
    "version": "1.0.0",
    "main": "./lib/main.js",
    "types": "./lib/main.d.ts"
}
```

请注意，“typings”字段与“types”同义，也可以使用。

另请注意，如果主声明文件名为index.d.ts并且位于包的根目录（index.js旁边），则不需要标记“types”属性，但建议这样做。

**依赖**

所有依赖项都由npm管理。 确保您所依赖的所有声明包都在package.json的“dependencies”部分中进行了适当标记。 例如，假设我们编写了一个使用Browserify和TypeScript的包。

```json
{
    "name": "browserify-typescript-extension",
    "author": "Vandelay Industries",
    "version": "1.0.0",
    "main": "./lib/main.js",
    "types": "./lib/main.d.ts",
    "dependencies": {
        "browserify": "latest",
        "@types/browserify": "latest",
        "typescript": "next"
    }
}
```

在这里，我们的包依赖于browserify和typescript包。 browserify不会将其声明文件与其npm包捆绑在一起，因此我们需要依赖@types/browserify来声明它的声明。 另一方面，typescript打包其声明文件，因此不需要任何其他依赖项。

我们的包公开了每个声明的声明，因此我们的browserify-typescript-extension包的任何用户也需要具有这些依赖关系。 出于这个原因，我们使用“依赖”而不是“devDependencies”，因为否则我们的消费者需要手动安装这些包。 如果我们刚刚编写了一个命令行应用程序并且不希望我们的包被用作库，那么我们可能已经使用了devDependencies。

**警告**

*`/// <reference path="..." />`*

不要在声明文件中使用`/// <reference path =“...”/>`。

```javascript
/// <reference path="../typescript/lib/typescriptServices.d.ts" />
....
```

使用`/// <reference types="..." />`替换

```javascript
/// <reference types="typescript" />
....
```

*包装依赖声明*

如果您的类型定义依赖于另一个包：

* 不要将它与你的相结合，将每个文件保存在自己的文件中。
* 不要复制包中的声明。
* 如果它没有打包其声明文件，请依赖于npm类型声明包。

### 发布到[@types](https://www.npmjs.com/~types)

@types组织下的软件包将使用types-publisher工具从DefinitelyTyped自动发布。要将您的声明作为@types包发布，请向 <https://github.com/DefinitelyTyped/DefinitelyTyped> 提交拉取请求。您可以在贡献指南页面中找到更多详细信息。
