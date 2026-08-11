---
title: "如何创建高质量的TypeScript声明文件(十一) - 使用"
date: "2025-07-10 10:57:26"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-yi-shi-yong"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(十一)-使用/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(十一)-使用.html"
  - "/如何创建高质量的TypeScript声明文件(十一)-使用/"
  - "/如何创建高质量的TypeScript声明文件(十一)-使用.html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-十一-使用/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-十一-使用.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-yi-shi-yong/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-yi-shi-yong.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-shi-yi-shi-yong.html"
---
### 使用

在TypeScript 2.0中，在获取，使用和查找声明文件时，它变得非常容易。 下面说下如何做到这三点。

**下载**

在TypeScript 2.0及更高版本中获取类型声明不需要除npm之外的任何工具。

例如，获取像lodash这样的库的声明只需要以下命令

```bash
npm install --save @types/lodash
```

值得注意的是，如果npm包已经包含了发布中描述的声明文件，则不需要下载相应的@types包。

**使用**

从那里你可以在你的TypeScript代码中使用lodash而不用大惊小怪。这适用于模块和全局代码。

例如，一旦你安装了你的类型声明，就可以使用import和write

```ts
import * as _ from "lodash";
_.padStart("Hello TypeScript!", 20, " ");
```

或者如果您不使用模块，则可以使用全局变量\_。

```ts
_.padStart("Hello TypeScript!", 20, " ");
```

**搜索**

在大多数情况下，类型声明包应始终与npm上的包名称相同，但前缀为@types/，但如果需要，可以查看[https://aka.ms/types](https://aka.ms/types%E4%BB%A5%E6%9F%A5%E6%89%BE%E4%BD%A0%E6%9C%80%E5%96%9C%E6%AC%A2%E7%9A%84%E5%BA%93%E7%9A%84%E5%8C%85%E3%80%82) 以查找你最喜欢的库的包。

注意：如果您要搜索的声明文件不存在，您可以随时贡献一份，并帮助下一位寻找它的开发人员。 有关详细信息，请参阅[DefinitelyTyped贡献](http://definitelytyped.org/guides/contributing.html)指南页面。
