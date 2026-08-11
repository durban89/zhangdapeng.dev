---
title: "TypeScript基础入门 - 枚举 - 联合枚举与枚举成员的类型"
date: "2025-07-09 09:59:56"
slug: "typescript-ji-chu-ru-men-mei-ju-lian-he-mei-ju-yu-mei-ju-cheng-yuan-de-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-枚举-联合枚举与枚举成员的类型/"
  - "/2025/07/09/TypeScript基础入门-枚举-联合枚举与枚举成员的类型.html"
  - "/TypeScript基础入门-枚举-联合枚举与枚举成员的类型/"
  - "/TypeScript基础入门-枚举-联合枚举与枚举成员的类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-lian-he-mei-ju-yu-mei-ju-cheng-yuan-de-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-lian-he-mei-ju-yu-mei-ju-cheng-yuan-de-lei-xing.html"
  - "/typescript-ji-chu-ru-men-mei-ju-lian-he-mei-ju-yu-mei-ju-cheng-yuan-de-lei-xing.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.7
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

### 联合枚举与枚举成员的类型

存在一种特殊的非计算的常量枚举成员的子集：字面量枚举成员。 字面量枚举成员是指不带有初始值的常量枚举成员，或者是值被初始化为

* 任何字符串字面量（例如： "foo"， "bar"， "baz"）
* 任何数字字面量（例如： 1, 100）
* 应用了一元 -符号的数字字面量（例如： -1, -100）

当所有枚举成员都拥有字面量枚举值时，它就带有了一种特殊的语义。

首先，枚举成员成为了类型！ 例如，我们可以说某些成员 只能是枚举成员的值：

```ts
enum ShapeKind {
    Circle,
    Square,
}

interface Circle {
    kind: ShapeKind.Circle,
    radius: number,
}

interface Square {
    kind: ShapeKind.Square,
    sideLength: number,
}

let c: Circle = {
    kind: ShapeKind.Square,
    redius: 100,
}
```

运行后会有如下错误提示

```bash
$ npx ts-node src/generics_8.ts
⨯ Unable to compile TypeScript:
src/generics_8.ts(17,5): error TS2322: Type 'ShapeKind.Square' is not assignable to type 'ShapeKind.Circle'.
```

另一个变化是枚举类型本身变成了每个枚举成员的 联合。 虽然我们还没有讨论[联合类型](./Advanced Types.md#union-types)，但你只要知道通过联合枚举，类型系统能够利用这样一个事实，它可以知道枚举里的值的集合。 因此，TypeScript能够捕获在比较值的时候犯的愚蠢的错误。 例如：

```ts
enum E {
    Foo,
    Bar,
}

function f(x: E) {
    if (x !== E.Foo || x !== E.Bar) {

    }
}
```

运行后会有如下错误提示

```bash
$ npx ts-node src/generics_8.ts
⨯ Unable to compile TypeScript:
src/generics_8.ts(27,23): error TS2367: This condition will always return 'true' since the types 'E.Foo' and 'E.Bar' have no overlap.
```

这个例子里，我们先检查 x是否不是 E.Foo。 如果通过了这个检查，然后 ||会发生短路效果， if语句体里的内容会被执行。 然而，这个检查没有通过，那么 x则 只能为 E.Foo，因此没理由再去检查它是否为 E.Bar。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.8
```
