---
title: "TypeScript基础入门之装饰器(一)"
date: "2025-07-10 10:24:03"
slug: "typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之装饰器(一)/"
  - "/2025/07/10/TypeScript基础入门之装饰器(一).html"
  - "/TypeScript基础入门之装饰器(一)/"
  - "/TypeScript基础入门之装饰器(一).html"
  - "/2025/07/10/TypeScript基础入门之装饰器-一/"
  - "/2025/07/10/TypeScript基础入门之装饰器-一.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-yi/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-yi.html"
  - "/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-yi.html"
---
### 介绍

随着TypeScript和ES6中Classes的引入，现在存在某些场景需要额外的功能来支持注释或修改类和类成员。  
装饰器提供了一种为类声明和成员添加注释和元编程语法的方法。  
装饰器是JavaScript的第2阶段提案，可作为TypeScript的实验性功能使用。

> 注意: 装饰器是一种实验性功能，可能在将来的版本中发生变化。

要为装饰器启用实验支持，必须在命令行或tsconfig.json中启用experimentalDecorators编译器选项：

命令行：

```bash
tsc --target ES5 --experimentalDecorators
```

tsconfig.json:

```json
{
    "compilerOptions": {
        "target": "ES5",
        "experimentalDecorators": true
    }
}
```

### 装饰器

装饰器是一种特殊的声明，可以附加到类声明，方法，访问器，属性或参数。  
装饰器使用@expression形式，其中expression必须求值为一个函数，该函数将在运行时调用有关装饰声明的信息。

例如，给定装饰器@sealed，我们可以编写```sealed```函数，如下所示：

```ts
function sealed(target) {
    // do something with 'target' ...
}
```

> 注意: 您可以在下面的类装饰器中看到更详细的装饰器示例。

### 装饰器工厂

如果我们想自定义装饰器如何应用于声明，我们可以编写一个装饰器工厂。  
装饰器工厂只是一个函数，它返回装饰器在运行时调用的表达式。

我们可以用以下方式编写装饰工厂：

```ts
function color(value: string) { // this is the decorator factory
    return function (target) { // this is the decorator
        // do something with 'target' and 'value'...
    }
}
```

> 注意: 您可以在下面的方法装饰器中看到装饰器工厂的更详细示例。

### 装饰器组成

可以将多个装饰器应用于声明，如以下示例所示：

1. 单行：

```ts
@f @g x
```

2. 多行：

```ts
@f
@g
x
```

当多个装饰器应用于单个声明时，它们的评估类似于数学中的函数组合。  
在该模型中，当组成函数f和g时，得到的复合(f ∘ g)(x)等于f(g(x))。

因此，在TypeScript中评估单个声明上的多个装饰器时，将执行以下步骤：

1. 每个装饰器的表达式都是从上到下进行评估的。  
2. 然后将结果从底部到顶部称为函数。

如果我们要使用装饰器工厂，我们可以通过以下示例观察此评估顺序：

```ts
function f() {
    console.log("f(): evaluated");
    return function (target, propertyKey: string, descriptor: PropertyDescriptor) {
        console.log("f(): called");
    }
}

function g() {
    console.log("g(): evaluated");
    return function (target, propertyKey: string, descriptor: PropertyDescriptor) {
        console.log("g(): called");
    }
}

class C {
    @f()
    @g()
    method() {}
}
```

运行后输出到控制台如下：

```bash
f(): evaluated
g(): evaluated
g(): called
f(): called
```

未完待续...
