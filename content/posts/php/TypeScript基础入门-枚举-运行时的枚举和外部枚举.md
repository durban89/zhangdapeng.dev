---
title: "TypeScript基础入门 - 枚举 - 运行时的枚举和外部枚举"
date: "2025-07-09 09:59:58"
slug: "typescript-ji-chu-ru-men-mei-ju-yun-xing-shi-de-mei-ju-he-wai-bu-mei-ju"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-枚举-运行时的枚举和外部枚举/"
  - "/2025/07/09/TypeScript基础入门-枚举-运行时的枚举和外部枚举.html"
  - "/TypeScript基础入门-枚举-运行时的枚举和外部枚举/"
  - "/TypeScript基础入门-枚举-运行时的枚举和外部枚举.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-yun-xing-shi-de-mei-ju-he-wai-bu-mei-ju/"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-yun-xing-shi-de-mei-ju-he-wai-bu-mei-ju.html"
  - "/typescript-ji-chu-ru-men-mei-ju-yun-xing-shi-de-mei-ju-he-wai-bu-mei-ju.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.8
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 枚举

使用枚举我们可以定义一些带名字的常量。 使用枚举可以清晰地表达意图或创建一组有区别的用例。 TypeScript支持数字的和基于字符串的枚举。

### 运行时的枚举

枚举是在运行时真正存在的对象。 例如下面的枚举：

```ts
enum E {
    X, Y, Z
}
```

实际上可以传递给函数

```ts
enum E {
    X,Y,Z
}
function f(obj: { X: number }) {
    return obj.X
}

console.log(f(E));
```

### 反向映射

除了创建一个以属性名做为对象成员的对象之外，数字枚举成员还具有了 反向映射，从枚举值到枚举名字。 例如，在下面的例子中：

```ts
enum Enum {
    A,
}

let a = Enum.A;
let nameOfA = Enum[a];
console.log(nameOfA);
```

TypeScript可能会将这段代码编译为下面的JavaScript：

```ts
var Enum;
(function (Enum) {
    Enum[Enum["A"] = 0] = "A";
})(Enum || (Enum = {}));
var a = Enum.A;
var nameOfA = Enum[a];
console.log(nameOfA);
```

生成的代码中，枚举类型被编译成一个对象，它包含了正向映射（ name -> value）和反向映射（ value -> name）。 引用枚举成员总会生成为对属性访问并且永远也不会内联代码。

要注意的是 不会为字符串枚举成员生成反向映射。

### const枚举

大多数情况下，枚举是十分有效的方案。 然而在某些情况下需求很严格。 为了避免在额外生成的代码上的开销和额外的非直接的对枚举成员的访问，我们可以使用 const枚举。 常量枚举通过在枚举上使用 const修饰符来定义。

```ts
const enum Enum {
    A = 1,
    B = A * 2,
}
```

常量枚举只能使用常量枚举表达式，并且不同于常规的枚举，它们在编译阶段会被删除。 常量枚举成员在使用的地方会被内联进来。 之所以可以这么做是因为，常量枚举不允许包含计算成员。

```ts
const enum Directions {
    Up,
    Down,
    Left,
    Right,
}

let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
```

生成后的代码为：

```ts
var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
```

## 外部枚举

外部枚举用来描述已经存在的枚举类型的形状。

```ts
declare enum Enum {
    A = 1,
    B,
    C = 2
}
```

外部枚举和非外部枚举之间有一个重要的区别，在正常的枚举里，没有初始化方法的成员被当成常数成员。 对于非常数的外部枚举而言，没有初始化方法时被当做需要经过计算的。  
本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.9
```
