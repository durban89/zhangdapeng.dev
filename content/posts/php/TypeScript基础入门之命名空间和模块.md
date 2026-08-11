---
title: "TypeScript基础入门之命名空间和模块"
date: "2025-07-10 10:23:21"
slug: "typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-he-mo-kuai"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之命名空间和模块/"
  - "/2025/07/10/TypeScript基础入门之命名空间和模块.html"
  - "/TypeScript基础入门之命名空间和模块/"
  - "/TypeScript基础入门之命名空间和模块.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-he-mo-kuai/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-he-mo-kuai.html"
  - "/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-he-mo-kuai.html"
---
## 命名空间和模块

关于术语的说明：值得注意的是，在TypeScript 1.5中，命名法已经改变。  
"内部模块"现在是"命名空间"。  
"外部模块"现在只是"模块"，以便与ECMAScript 2015的术语保持一致（即module X {相当于现在首选的namespace X {）。

### 介绍

本文概述了使用TypeScript中的命名空间和模块组织代码的各种方法。  
我们还将讨论如何使用命名空间和模块的一些高级主题，并解决在TypeScript中使用它们时常见的一些陷阱。

有关模块的更多信息，请参阅模块文档。  
有关命名空间的更多信息，请参阅命名空间文档。

### 使用命名空间

命名空间只是全局命名空间中的JavaScript对象。  
这使命名空间成为一个非常简单的构造。  
它们可以跨多个文件，并且可以使用--outFile连接。  
命名空间可以是在Web应用程序中构建代码的好方法，所有依赖项都包含在HTML页面中的`<script>`标记中。

就像所有全局命名空间污染一样，很难识别组件依赖性，尤其是在大型应用程序中。

### 使用模块

就像命名空间一样，模块可以包含代码和声明。  
主要区别在于模块声明了它们的依赖关系。

模块还依赖于模块加载器（例如CommonJs/Require.js）。  
对于小型JS应用程序而言，这可能不是最佳选择，但对于大型应用程序，成本具有长期模块化和可维护性优势。  
模块为捆绑提供了更好的代码重用，更强的隔离和更好的工具支持。

值得注意的是，对于Node.js应用程序，模块是构造代码的默认方法和推荐方法。

从 ECMAScript `2015`开始，模块是该语言的本机部分，并且应该受到所有兼容引擎实现的支持。  
因此，对于新项目，模块将是推荐的代码组织机制。

### 命名空间和模块的缺陷

下面我们将描述使用命名空间和模块时的各种常见缺陷，以及如何避免它们。

### */// <reference>-ing a module*

一个常见的错误是尝试使用`/// <reference ... />`语法来引用模块文件，而不是使用import语句。  
为了理解这种区别，我们首先需要了解编译器如何根据导入的路径找到模块的类型信息（例如...在,`import x from "...";import x = require("...");`等等。路径。

编译器将尝试使用适当的路径查找.ts，.tsx和.d.ts。  
如果找不到特定文件，则编译器将查找环境模块声明。  
回想一下，这些需要在.d.ts文件中声明。

myModules.d.ts

```ts
// In a .d.ts file or .ts file that is not a module:
declare module "SomeModule" {
    export function fn(): string;
}
```

myOtherModule.ts

```ts
/// <reference path="myModules.d.ts" />
import * as m from "SomeModule";
```

这里的引用标记允许我们找到包含环境模块声明的声明文件。  
这就是使用几个TypeScript示例使用的node.d.ts文件的方式。

### *无需命名空间*

如果您要将程序从命名空间转换为模块，则可以很容易地得到如下所示的文件：

shapes.ts

```ts
export namespace Shapes {
    export class Triangle { /* ... */ }
    export class Square { /* ... */ }
}
```

这里的顶级模块Shapes无缘无故地包装了Triangle和Square。  
这对您的模块的消费者来说是令人困惑和恼人的：

shapeConsumer.ts

```ts
import * as shapes from "./shapes";
let t = new shapes.Shapes.Triangle(); // shapes.Shapes?
```

TypeScript中模块的一个关键特性是两个不同的模块永远不会为同一范围提供名称。  
因为模块的使用者决定分配它的名称，所以不需要主动地将命名空间中的导出符号包装起来。

为了重申您不应该尝试命名模块内容的原因，命名空间的一般概念是提供构造的逻辑分组并防止名称冲突。  
由于模块文件本身已经是逻辑分组，并且其顶级名称由导入它的代码定义，因此不必为导出的对象使用其他模块层。

这是一个修改过的例子：  
shapes.ts

```ts
export class Triangle { /* ... */ }
export class Square { /* ... */ }
```

shapeConsumer.ts

```ts
import * as shapes from "./shapes";
let t = new shapes.Triangle();
```

### 模块的权衡

正如JS文件和模块之间存在一对一的对应关系一样，TypeScript在模块源文件与其发出的JS文件之间具有一对一的对应关系。  
这样做的一个结果是，根据您定位的模块系统，无法连接多个模块源文件。  
例如，在定位commonjs或umd时不能使用outFile选项，但使用TypeScript 1.8及更高版本时，可以在定位amd或system时使用outFile。
