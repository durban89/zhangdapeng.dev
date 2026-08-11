---
title: "TypeScript基础入门 - 类型兼容性 - 泛型"
date: "2025-07-09 10:00:13"
slug: "typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-fan-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-类型兼容性-泛型/"
  - "/2025/07/09/TypeScript基础入门-类型兼容性-泛型.html"
  - "/TypeScript基础入门-类型兼容性-泛型/"
  - "/TypeScript基础入门-类型兼容性-泛型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-fan-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-fan-xing.html"
  - "/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-fan-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.1
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 泛型

因为TypeScript是结构性的类型系统，类型参数只影响使用其做为类型一部分的结果类型。比如，

```ts
interface Generics<T> {}

let g1: Generics<number> = <Generics<number>>{};
let g2: Generics<string> = <Generics<string>>{};

g1 = g2;
```

上面代码里，g1和g2是兼容的，因为它们的结构使用类型参数时并没有什么不同。 把这个例子改变一下，增加一个成员，就能看出是如何工作的了：

```ts
interface Generics<T> {
    data: T;
}

let g1: Generics<number> = <Generics<number>>{};
let g2: Generics<string> = <Generics<string>>{};

g1 = g2;
```

运行后会看到类似如下的输出

```bash
$ npx ts-node src/type_compatibility_3.ts
⨯ Unable to compile TypeScript:
src/type_compatibility_3.ts(8,1): error TS2322: Type 'Generics<string>' is not assignable to type 'Generics<number>'.
  Type 'string' is not assignable to type 'number'.
```

在这里，泛型类型在使用时就好比不是一个泛型类型。对于没指定泛型类型的泛型参数时，会把所有泛型参数当成any比较。 然后用结果类型进行比较，如下例子。比如：

```ts
let t1 = function<T>(x: T): T {
    // other ...
}

let t2 = function<U>(y: U): U {
    // other ...
}

t1 = t2
```

如果有个类似如上的代码实例，是能否执行成功的，因为这里`(x: any): any == (y: any): any`

## 高级主题

### 子类型与赋值

目前为止，我们使用了兼容性，它在语言规范里没有定义。 在TypeScript里，有两种类型的兼容性：子类型与赋值。 它们的不同点在于，赋值扩展了子类型兼容，允许给 any赋值或从any取值和允许数字赋值给枚举类型或枚举类型赋值给数字。

语言里的不同地方分别使用了它们之中的机制。 实际上，类型兼容性是由赋值兼容性来控制的，即使在implements和extends语句也不例外。 更多信息，请参阅 [[TypeScript语言规范](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md)]

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.2
```
