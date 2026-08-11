---
title: "如何创建高质量的TypeScript声明文件(四)"
date: "2025-07-10 10:56:57"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-si"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(四)/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(四).html"
  - "/如何创建高质量的TypeScript声明文件(四)/"
  - "/如何创建高质量的TypeScript声明文件(四).html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-四/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-四.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-si/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-si.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-si.html"
---
继续上篇文章[[如何创建高质量的TypeScript声明文件(三)](https://www.gowhich.com/blog/966)]

### 对UMD库的依赖性

*来自全局库*

如果您的全局库依赖于UMD模块，请使用`/// <reference types指令`：

```ts
/// <reference types="moment" />

function getThing(): moment;
```

*来自模块或UMD库*

如果您的模块或UMD库依赖于UMD库，请使用import语句：

```ts
import * as someLib from 'someLib';
```

不要使用`/// <reference指令`声明对UMD库的依赖！

### 补充说明

**防止名称冲突**

请注意，在编写全局声明文件时，可以在全局范围中定义许多类型。 我们强烈反对这一点，因为当许多声明文件在项目中时，它会导致可能无法解析的名称冲突。

一个简单的规则是仅通过库定义的任何全局变量声明命名空间类型。 例如，如果库定义全局值'cats'，您应该写

```ts
declare namespace cats {
    interface KittySettings { }
}
```

而不是

```ts
// at top-level
interface CatsKittySettings { }
```

还可以确保在不破坏声明文件用户的情况下将库转换为UMD。

**ES6对模块插件的影响**

某些插件在现有模块上添加或修改顶级导出。 虽然这在CommonJS和其他加载器中是合法的，但ES6模块被认为是不可变的，并且这种模式是不可能的。 因为TypeScript与加载程序无关，所以没有编译时强制执行此策略，但是打算转换到ES6模块加载程序的开发人员应该知道这一点。

**ES6对模块呼叫签名的影响**

许多流行的库（如Express）在导入时将自身暴露为可调用函数。 例如，典型的Express用法如下所示：

```ts
import exp = require("express");
var app = exp();
```

在ES6模块加载器中，顶级对象（此处导入为exp）只能具有属性; 顶级模块对象永远不可调用。 这里最常见的解决方案是为可调用/可构造对象定义默认导出; 某些模块加载程序填充程序将自动检测此情况并使用默认导出替换顶级对象。
