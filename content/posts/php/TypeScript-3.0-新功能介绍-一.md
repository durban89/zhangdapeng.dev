---
title: "TypeScript 3.0 新功能介绍（一）"
date: "2025-07-09 09:59:37"
slug: "typescript-30-xin-gong-neng-jie-shao-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript-3.0-新功能介绍（一）/"
  - "/2025/07/09/TypeScript-3.0-新功能介绍（一）.html"
  - "/TypeScript-3.0-新功能介绍（一）/"
  - "/TypeScript-3.0-新功能介绍（一）.html"
  - "/2025/07/09/TypeScript-3.0-新功能介绍-一/"
  - "/2025/07/09/TypeScript-3.0-新功能介绍-一.html"
  - "/2025/07/09/typescript-30-xin-gong-neng-jie-shao-yi/"
  - "/2025/07/09/typescript-30-xin-gong-neng-jie-shao-yi.html"
  - "/typescript-30-xin-gong-neng-jie-shao-yi.html"
---
TypeScript 3.0 新功能介绍（一）

## 项目引用

TypeScript 3.0引入了项目引用(project references)的新概念。  
项目引用允许TypeScript项目依赖于其他TypeScript项目 - 特别是允许tsconfig.json文件引用其他tsconfig.json文件。  
指定这些依赖项可以更容易地将代码拆分为更小的项目，因为它为TypeScript（及其周围的工具）提供了一种理解构建顺序和输出结构的方法。  
TypeScript 3.0还引入了一种新的tsc模式，即--build标志，它与项目引用一起工作，以实现更快的TypeScript构建。  
有关更多文档，请参阅项目参考手册页面。我这里只简单介绍下官方介绍的一小部分新功能

## 剩余参数和传播表达式中的元组

TypeScript 3.0增加了对多个新功能的支持，以与函数参数列表作为元组类型进行交互。  
TypeScript 3.0增加了如下支持：

* [Expansion of rest parameters with tuple types into discrete parameters](http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#rest-parameters-with-tuple-types).
* [Expansion of spread expressions with tuple types into discrete arguments](http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#spread-expressions-with-tuple-types).
* [Generic rest parameters and corresponding inference of tuple types](http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#generic-rest-parameters).
* [Optional elements in tuple types](http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#optional-elements-in-tuple-types).
* [Rest elements in tuple types](http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#rest-elements-in-tuple-types).

通过这些功能，可以强大地键入一些转换函数及其参数列表的高阶函数。

### 使用元组类型的剩余参数

当剩余参数具有元组类型时，元组类型将扩展为一系列离散参数。  
例如，以下两个声明是等效的：

```ts
declare function foo(...args: [number, boolean, string]): void;
declare function foo(args_0: number, args_1: boolean, args_2: string): void;
```

### 使用元组类型传播表达式

当函数调用包括元组类型的扩展表达式作为最后一个参数时，扩展表达式对应于元组元素类型的离散参数序列。  
因此，以下调用是等效的：

```ts
const args: [number, boolean, string] = [42, true, "hello"];
foo(42, true, "hello");
foo(args[0], args[1], args[2])
foo(...args)
```

### 通用剩余参数

允许剩余参数具有约束为数组类型的泛型类型，并且类型推断可以推断这些通用剩余参数的元组类型。  
这使得部分参数列表的高阶捕获和传播成为可能，如下实例

```ts
declare function bind<T, U extends any[], V>(
    f: (x: T, ...args: U) => V, x: T): (...args: U) => V;

declare function f3(x: number, y: string, z: boolean): void;

const f2 = bind(f3, 42); // (y: string, z: boolean) => void
const f1 = bind(f2, "hello"); // (z: boolean) => void
const f0 = bind(f1, true); // () => void

f3(42, "hello", true);
f2("hello", true);
f1(true);
f0();
```

在上面的f2声明中，类型推断分别为T，U和V推断类型数，[string，boolean]和void。  
请注意，当从一系列参数推断出元组类型并随后扩展为参数列表时（如U的情况），原始参数名称将用于扩展（但是，名称没有语义含义，否则不会  
观察到的）。

### 元组类型中的可选元素

元组类型现在允许`?后缀`  
元素类型的后缀表示该元素是可选的，如下实例

```ts
let t: [number, string?, boolean?];
t = [42, "hello", true];
t = [42, "hello"];
t = [42];
```

在`--strictNullChecks`模式下，一个`?`修饰符在元素类型中自动包含undefined，类似于可选参数。  
如果元素具有`?`后缀，则元组类型允许省略元素，它的类型上的修饰符和它右边的所有元素也有```?```修饰符。  
当为元组类型数据被推断为剩余参数时，源中的可选参数将成为推断类型中的可选元组元素。

带有可选元素的元组类型的length属性表示可能长度的字面类型的并集。  
例如，元组类型[number,string?,boolean?]中的length属性的类型是1|2|3。

### 在元组类型中剩余元素

元组类型的最后一个元素可以是形式为...X的剩余元素，其中X是数组类型。  
剩余元素表示元组类型是开放式的，并且可能具有零个或多个数组元素类型的附加元素。  
例如，[number, ...string[]]表示带有数字元素后跟任意数量的字符串元素的元组。如下实例

```ts
function tuple<T extends any[]>(...args: T): T {
    return args;
}

const numbers: number[] = getArrayOfNumbers();
const t1 = tuple("foo", 1, true);  // [string, number, boolean]
const t2 = tuple("bar", ...numbers);  // [string, ...number[]]
```

具有剩余元素的元组类型的length属性的类型是number。

其余特性请留意后续分享。
