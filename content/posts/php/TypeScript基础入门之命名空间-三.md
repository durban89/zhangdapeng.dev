---
title: "TypeScript基础入门之命名空间(三)"
date: "2025-07-10 10:23:16"
slug: "typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之命名空间(三)/"
  - "/2025/07/10/TypeScript基础入门之命名空间(三).html"
  - "/TypeScript基础入门之命名空间(三)/"
  - "/TypeScript基础入门之命名空间(三).html"
  - "/2025/07/10/TypeScript基础入门之命名空间-三/"
  - "/2025/07/10/TypeScript基础入门之命名空间-三.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-san/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-san.html"
  - "/typescript-ji-chu-ru-men-zhi-ming-ming-kong-jian-san.html"
---
继续上篇文章[[TypeScript基础入门之命名空间(二)](https://www.gowhich.com/blog/941)]

## 别名

另一种可以简化名称空间使用方法的方法是使用import q = x.y.z为常用对象创建较短的名称。  
不要与用于加载模块的import x = require（"name"）语法相混淆，此语法只是为指定的符号创建别名。  
您可以将这些类型的导入（通常称为别名）用于任何类型的标识符，包括从模块导入创建的对象。

```ts
namespace Shapes {
    export namespace Polygons {
        export class Triangle { }
        export class Square { }
    }
}

import polygons = Shapes.Polygons;
let sq = new polygons.Square(); // 类似于 'new Shapes.Polygons.Square()'
```

请注意，我们不使用require关键字;  
相反，我们直接从我们导入的符号的限定名称中分配。  
这类似于使用var，但也适用于导入符号的类型和名称空间含义。  
重要的是，对于值，import是与原始符号的不同引用，因此对别名var的更改不会反映在原始变量中。

## 使用其他JavaScript库

要描述不是用TypeScript编写的库的形状，我们需要声明库公开的API。  
因为大多数JavaScript库只公开一些顶级对象，所以命名空间是表示它们的好方法。

我们称之为未定义实现“环境”的声明。  
通常，这些是在.d.ts文件中定义的。  
如果您熟悉C/C++，可以将它们视为.h文件。  
我们来看几个例子。

### 环境命名空间

流行的库D3在名为d3的全局对象中定义其功能。  
因为此库是通过`<script>`标记（而不是模块加载器）加载的，所以它的声明使用命名空间来定义其形状。  
要让TypeScript编译器看到这个形状，我们使用环境命名空间声明。  
例如，我们可以开始编写如下：D3.d.ts（简化摘录）

```ts
declare namespace D3 {
    export interface Selectors {
        select: {
            (selector: string): Selection;
            (element: EventTarget): Selection;
        };
    }

    export interface Event {
        x: number;
        y: number;
    }

    export interface Base extends Selectors {
        event: Event;
    }
}

declare var d3: D3.Base;
```
