---
title: "TypeScript基础入门之声明合并(一)"
date: "2025-07-10 10:23:42"
slug: "typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之声明合并(一)/"
  - "/2025/07/10/TypeScript基础入门之声明合并(一).html"
  - "/TypeScript基础入门之声明合并(一)/"
  - "/TypeScript基础入门之声明合并(一).html"
  - "/2025/07/10/TypeScript基础入门之声明合并-一/"
  - "/2025/07/10/TypeScript基础入门之声明合并-一.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-yi/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-yi.html"
  - "/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-yi.html"
---
## 声明合并

### 介绍

TypeScript中的一些独特概念描述了类型级别的JavaScript对象的形状。  
TypeScript特别独特的一个例子是"声明合并"的概念。  
在使用现有JavaScript时，理解此概念将为您提供优势。  
它还为更高级的抽象概念打开了大门。

出于本文的目的，"声明合并"意味着编译器将使用相同名称声明的两个单独声明合并到单个定义中。  
此合并定义具有两个原始声明的功能。  
可以合并任意数量的声明;  
它不仅限于两个声明。

### 基本概念

在TypeScript中，声明在三个组中的至少一个中创建实体：名称空间，类型或值。  
命名空间创建声明创建一个命名空间，其中包含使用点符号表示法访问的名称。  
类型创建声明就是这样做的：它们创建一个可以使用声明的形状显示并绑定到给定名称的类型。  
最后，创建值的声明会创建在输出JavaScript中可见的值。

|  |  |  |  |
| --- | --- | --- | --- |
| Declaration Type | Namespace | Type | Value |
| Namespace | X |  | X |
| Class |  | X | X |
| Enum |  | X | X |
| Interface |  | X |  |
| Type Alias |  | X |  |
| Function |  |  | X |
| Variable |  |  | X |

了解每个声明创建的内容将帮助您了解执行声明合并时合并的内容。

### 合并接口

最简单，也许是最常见的声明合并类型是接口合并。  
在最基本的层面上，合并机械地将两个声明的成员连接到具有相同名称的单个接口。

```ts
interface Box {
    height: number;
    width: number;
}

interface Box {
    scale: number;
}

let box: Box = {height: 5, width: 6, scale: 10};
```

接口的非功能成员应该是唯一的。  
如果它们不是唯一的，则它们必须属于同一类型。  
如果接口都声明了具有相同名称但具有不同类型的非函数成员，则编译器将发出错误。

对于函数成员，同名的每个函数成员都被视为描述同一函数的重载。  
值得注意的是，在接口A与后面的接口A合并的情况下，第二接口将具有比第一接口更高的优先级。

也就是说，在示例中：

```ts
interface Cloner {
    clone(animal: Animal): Animal;
}

interface Cloner {
    clone(animal: Sheep): Sheep;
}

interface Cloner {
    clone(animal: Dog): Dog;
    clone(animal: Cat): Cat;
}
```

三个接口将合并以创建单个声明，如下所示：

```ts
interface Cloner {
    clone(animal: Dog): Dog;
    clone(animal: Cat): Cat;
    clone(animal: Sheep): Sheep;
    clone(animal: Animal): Animal;
}
```

请注意，每个组的元素保持相同的顺序，但组本身与稍后排序的后续重载集合在一起。

此规则的一个例外是专门签名。  
如果签名的参数类型是单个字符串文字类型（例如，不是字符串文字的并集），那么它将被冒泡到其合并的重载列表的顶部。

例如，以下接口将合并在一起：

```ts
interface Document {
    createElement(tagName: any): Element;
}
interface Document {
    createElement(tagName: "div"): HTMLDivElement;
    createElement(tagName: "span"): HTMLSpanElement;
}
interface Document {
    createElement(tagName: string): HTMLElement;
    createElement(tagName: "canvas"): HTMLCanvasElement;
}
```

由此产生的合并声明文件将如下:

```ts
interface Document {
    createElement(tagName: "canvas"): HTMLCanvasElement;
    createElement(tagName: "div"): HTMLDivElement;
    createElement(tagName: "span"): HTMLSpanElement;
    createElement(tagName: string): HTMLElement;
    createElement(tagName: any): Element;
}
```

未完待续...
