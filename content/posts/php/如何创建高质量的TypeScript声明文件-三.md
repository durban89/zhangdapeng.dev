---
title: "如何创建高质量的TypeScript声明文件(三)"
date: "2025-07-10 10:56:53"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(三)/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(三).html"
  - "/如何创建高质量的TypeScript声明文件(三)/"
  - "/如何创建高质量的TypeScript声明文件(三).html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-三/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-三.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-san/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-san.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-san.html"
---
继续上篇文章[[如何创建高质量的TypeScript声明文件(二)](https://www.gowhich.com/blog/965)]

**模块插件或UMD插件**

模块插件更改另一个模块（UMD或模块）的形状。 例如，在Moment.js中，时刻范围为时刻对象添加了一个新的范围方法。

出于编写声明文件的目的，无论要更改的模块是普通模块还是UMD模块，您都将编写相同的代码。

*模板*

使用module-plugin.d.ts模板。

**全局插件**

全局插件是改变某些全局形状的全局代码。 与全局修改模块一样，这些会增加运行时冲突的可能性。

例如，某些库将新函数添加到Array.prototype或String.prototype。

*识别全局插件*

全局插件通常很容易从他们的文档中识别出来。

您将看到如下所示的示例：

```ts
var x = "hello, world";
// Creates new methods on built-in types
console.log(x.startsWithHello());

var y = [1, 2, 3];
// Creates new methods on built-in types
console.log(y.reverseAndSort());
```

*模板*

使用global-plugin.d.ts模板。

**全局修改模块**

全局修改模块在导入时会更改全局范围中的现有值。 例如，可能存在一个库，在导入时会向String.prototype添加新成员。 由于运行时冲突的可能性，这种模式有点危险，但我们仍然可以为它编写声明文件。

*识别全局修改模块*

全局修改模块通常很容易从其文档中识别。 通常，它们与全局插件类似，但需要一个require调用来激活它们的效果。

你可能会看到这样的文档：

```ts
// 'require' call that doesn't use its return value
var unused = require("magic-string-time");
/* or */
require("magic-string-time");

var x = "hello, world";
// Creates new methods on built-in types
console.log(x.startsWithHello());

var y = [1, 2, 3];
// Creates new methods on built-in types
console.log(y.reverseAndSort());
```

*模板*

使用global-modifying-module.d.ts模板。

### 使用依赖性

您可能拥有多种依赖关系。

**对全局库的依赖**

如果您的库依赖于全局库，请使用`/// <reference types ="..."/>`指令：

```ts
/// <reference types="someLib" />

function getThing(): someLib.thing;
```

**对模块的依赖性**

如果您的库依赖于模块，请使用import语句：

```ts
import * as moment from "moment";

function getThing(): moment;
```

未完待续...
