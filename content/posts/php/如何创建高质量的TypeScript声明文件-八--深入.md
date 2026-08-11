---
title: "如何创建高质量的TypeScript声明文件(八) - 深入"
date: "2025-07-10 10:57:13"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-ba-shen-ru"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(八)-深入/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(八)-深入.html"
  - "/如何创建高质量的TypeScript声明文件(八)-深入/"
  - "/如何创建高质量的TypeScript声明文件(八)-深入.html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-八-深入/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-八-深入.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-ba-shen-ru/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-ba-shen-ru.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-ba-shen-ru.html"
---
### 深入

定义文件原理：深入

构建模块以提供您想要的精确API形状可能会非常棘手。例如，我们可能想要一个可以使用或不使用new调用的模块来生成不同的类型，在层次结构中公开各种命名类型，并且在模块对象上也有一些属性。

通过深入理解定义文件原理，您将拥有编写复杂定义文件的工具，这些文件可以显示友好的API表面。本指南重点介绍模块（或UMD）库，因为此处的选项更加多样化。

**关键概念**

通过了解TypeScript如何工作的一些关键概念，您可以完全理解如何进行任何形式的定义。

*类型*

为了更明确，引入了一种类型：

* 类型别名声明（type sn = number | string;）
* 接口声明（interface I { x: number[]; }）
* 类声明（class C { }）
* 枚举声明（enum E { A, B, C }）
* 引用类型的import声明

每个声明表单都会创建一个新的类型名称。

*值*

与类型一样，您可能已经了解了什么是值。值是我们可以在表达式中引用的运行时名称。例如，让x = 5;创建一个名为x的值。

同样，明确地，以下事物创造价值：

* let，const和var声明
* 包含值的命名空间或模块声明
* 枚举声明
* 一个类声明
* 引用值的导入声明
* 功能声明

*命令空间*

类型可以存在于名称空间中。例如，如果我们有声明let x: A.B.C，我们说类型C来自A.B命名空间。

这种区别是微妙而重要的 - 在这里，A.B不一定是一种类型或价值。

**简单组合：一个名称，多个含义**

给定名称A，我们可能会为A找到最多三种不同的含义：类型，值或命名空间。如何解释名称取决于使用它的上下文。例如，在声明中，让m：A.A = A;，A首先用作命名空间，然后用作类型名称，然后用作值。这些含义最终可能指的是完全不同的声明！

这可能看起来令人困惑，但只要我们不过度超载事物，它实际上非常方便。让我们看看这种组合行为的一些有用方面。

*内置组合*

精明的读者会注意到，例如，类出现在类型和值列表中。声明类C {}创建两件事：一个C类引用类的实例形状，一个值C引用类的构造函数。枚举声明的行为类似。

*用户组合*

假设我们写了一个模块文件foo.d.ts：

```ts
export var SomeVar: { a: SomeType };
export interface SomeType {
  count: number;
}
```

然后调用它：

```ts
import * as foo from './foo';
let x: foo.SomeType = foo.SomeVar.a;
console.log(x.count);
```

这种方法效果很好，但我们可以想象SomeType和SomeVar非常密切相关，因此您希望它们具有相同的名称。我们可以使用组合来在同一个名称Bar下呈现这两个不同的对象（值和类型）：

```ts
export var Bar: { a: Bar };
export interface Bar {
  count: number;
}
```

这为使用代码中的解构提供了一个非常好的机会：

```ts
import { Bar } from './foo';  
let x: Bar = Bar.a;  
console.log(x.count);  
````

同样，我们在这里使用Bar作为类型和值。请注意，我们不必将Bar值声明为Bar类型 - 它们是独立的。

**高级组合**

某些类型的声明可以跨多个声明组合。例如，类C {}和接口C {}可以共存，并且都为C类型提供属性。

只要它不会产生冲突，这是合法的。一般的经验法则是值总是与同名的其他值冲突，除非它们被声明为名称空间，如果使用类型别名声明（type s = string）声明类型，则类型将发生冲突，并且名称空间永远不会发生冲突。

让我们看看如何使用它。

*使用interface添加*

我们可以使用另一个接口声明向接口添加其他成员：

```ts
interface Foo {
  x: number;
}
// ... elsewhere ...
interface Foo {
  y: number;
}
let a: Foo = ...;
console.log(a.x + a.y); // OK
```

这也适用于类：

```ts
class Foo {
  x: number;
}
// ... elsewhere ...
interface Foo {
  y: number;
}
let a: Foo = ...;
console.log(a.x + a.y); // OK
```

请注意，我们无法使用接口添加类型别名（type s = string;）。

*使用namespace添加*

命名空间声明可用于以任何不会产生冲突的方式添加新类型，值和命名空间。

例如，我们可以向类添加静态成员：

```ts
class C {
}
// ... elsewhere ...
namespace C {
  export let x: number;
}
let y = C.x; // OK
```

请注意，在此示例中，我们向C的静态端（其构造函数）添加了一个值。这是因为我们添加了一个值，所有值的容器都是另一个值（类型由名称空间包含，名称空间包含在其他名称空间中）。

我们还可以为类添加命名空间类型：

```ts
class C {
}
// ... elsewhere ...
namespace C {
  export interface D { }
}
let y: C.D; // OK
```

在这个例子中，在我们为它编写名称空间声明之前，没有名称空间C.C作为命名空间的含义与类创建的C的值或类型含义不冲突。

最后，我们可以使用命名空间声明执行许多不同的合并。这不是一个特别现实的例子，但显示了各种有趣的行为：

```ts
namespace X {
  export interface Y { }
  export class Z { }
}

// ... elsewhere ...
namespace X {
  export var Y: number;
  export namespace Z {
    export class C { }
  }
}
type X = string;
```

在此示例中，第一个块创建以下名称含义：

* 值X（因为名称空间声明包含值Z）
* 命名空间X（因为命名空间声明包含一个类型，Y）
* X命名空间中的类型Y.
* X命名空间中的类型Z（类的实例形状）
* 值Z，它是X值的属性（类的构造函数）

第二个块创建以下名称含义：

* 值Y（类型编号），它是X值的属性
* 命名空间Z.
* 值Z，它是X值的属性
* X.Z命名空间中的类型C.
* 值C，它是X.Z值的属性
* X型

使用export =或import

一个重要的规则是export和import声明export或import其目标的所有含义。
