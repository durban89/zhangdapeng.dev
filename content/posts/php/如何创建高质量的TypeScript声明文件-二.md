---
title: "如何创建高质量的TypeScript声明文件(二)"
date: "2025-07-10 10:56:49"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(二)/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(二).html"
  - "/如何创建高质量的TypeScript声明文件(二)/"
  - "/如何创建高质量的TypeScript声明文件(二).html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-二/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-二.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-er/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-er.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-er.html"
---
继续上篇文章[[如何创建高质量的TypeScript声明文件(一)](https://www.gowhich.com/blog/964)]

**模块化库**

有些库只能在模块加载器环境中工作。 例如，因为express仅适用于Node.js，必须使用CommonJS require函数加载。

ECMAScript 2015（也称为ES2015，ECMAScript 6和ES6），CommonJS和RequireJS具有类似的导入模块的概念。 例如，在JavaScript CommonJS（Node.js）中，您可以编写

```ts
var fs = require("fs");
```

在TypeScript或ES6中，import关键字用于相同的目的：

```ts
import fs = require("fs");
```

您通常会看到模块化库在其文档中包含以下行之一：

```ts
var someLib = require('someLib');
```

或

```ts
define(..., ['someLib'], function(someLib) {

});
```

与全局模块一样，您可能会在UMD模块的文档中看到这些示例，因此请务必查看代码或文档。

*从代码中识别模块库*

模块化库通常至少具有以下某些功能：

* 无条件调用require或define
* import \* as a from 'b'的声明，或export c;
* 对exports或module.exports的赋值

他们很少会：

* 分配window或global的属性

*模块化库的示例*

许多流行的Node.js库都在模块系列中，例如express，gulp和request。

### UMD

UMD模块可以用作模块（通过导入），也可以用作全局模块（在没有模块加载器的环境中运行）。 许多流行的库，如Moment.js，都是以这种方式编写的。 例如，在Node.js中或使用RequireJS，您可以编写：

```ts
import moment = require("moment");
console.log(moment.format());
```

而在vanilla浏览器环境中，你会写：

```ts
console.log(moment.format());
```

**识别UMD库**

UMD模块检查是否存在模块加载器环境。 这是一个易于查看的模式，看起来像这样：

```ts
(function (root, factory) {
    if (typeof define === "function" && define.amd) {
        define(["libName"], factory);
    } else if (typeof module === "object" && module.exports) {
        module.exports = factory(require("libName"));
    } else {
        root.returnExports = factory(root.libName);
    }
}(this, function (b) {
```

如果您在库的代码中看到typeof define，typeof window或typeof module的测试，特别是在文件的顶部，它几乎总是一个UMD库。

UMD库的文档通常还会演示一个"Using in Node.js"示例，其中显示了require，以及一个"Using in the browser"示例，该示例显示了使用`<script>`标记加载脚本。

**UMD库的示例**

大多数流行的库现在都可以作为UMD包使用。 示例包括jQuery，Moment.js，lodash等等。

*模板*

模块有三个模板，module.d.ts，module-class.d.ts和module-function.d.ts。

如果您的模块可以像函数一样被调用，请使用module-function.d.ts：

```ts
var x = require("foo");
// Note: calling 'x' as a function
var y = x(42);
```

请务必阅读脚注"[ES6对模块调用签名的影响](http://www.typescriptlang.org/docs/handbook/declaration-files/library-structures.html#the-impact-of-es6-on-module-plugins)"

如果您的模块可以使用new构建，请使用module-class.d.ts：

```ts
var x = require("bar");
// Note: using 'new' operator on the imported variable
var y = new x("hello");
```

同样的脚注适用于这些模块。

如果您的模块不可调用或可构造，请使用module.d.ts文件。

未完待续...
