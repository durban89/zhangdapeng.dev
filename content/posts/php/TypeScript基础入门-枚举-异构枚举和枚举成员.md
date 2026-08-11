---
title: "TypeScript基础入门 - 枚举 - 异构枚举和枚举成员"
date: "2025-07-09 09:59:46"
slug: "typescript-ji-chu-ru-men-mei-ju-yi-gou-mei-ju-he-mei-ju-cheng-yuan"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/09/TypeScript基础入门-枚举-异构枚举和枚举成员/"
  - "/2025/07/09/TypeScript基础入门-枚举-异构枚举和枚举成员.html"
  - "/TypeScript基础入门-枚举-异构枚举和枚举成员/"
  - "/TypeScript基础入门-枚举-异构枚举和枚举成员.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-yi-gou-mei-ju-he-mei-ju-cheng-yuan/"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-yi-gou-mei-ju-he-mei-ju-cheng-yuan.html"
  - "/typescript-ji-chu-ru-men-mei-ju-yi-gou-mei-ju-he-mei-ju-cheng-yuan.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.6
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

### 枚举

使用枚举我们可以定义一些带名字的常量。 使用枚举可以清晰地表达意图或创建一组有区别的用例。 TypeScript支持数字的和基于字符串的枚举。

### 异构枚举（Heterogeneous enums）

从技术的角度来说，枚举可以混合字符串和数字成员，但是似乎你并不会这么做：

```ts
enum BooleanLikeHeterogeneousEnum {
    No = 0,
    Yes = "YES",
}
```

除非你真的想要利用JavaScript运行时的行为，否则我们不建议这样做。

### 计算的和常量成员

每个枚举成员都带有一个值，它可以是 常量或 计算出来的。 当满足如下条件时，枚举成员被当作是常量：

> 它是枚举的第一个成员且没有初始化器，这种情况下它被赋予值 0：

```ts
// E.X is constant:
enum E { X }
```

> 它不带有初始化器且它之前的枚举成员是一个 数字常量。 这种情况下，当前枚举成员的值为它上一个枚举成员的值加1。

```ts
enum E1 { X, Y, Z }

enum E2 {
    A = 1, B, C
}
```

> 枚举成员使用 常量枚举表达式初始化。 常数枚举表达式是TypeScript表达式的子集，它可以在编译阶段求值。 当一个表达式满足下面条件之一时，它就是一个常量枚举表达式：

* 一个枚举表达式字面量（主要是字符串字面量或数字字面量）
* 一个对之前定义的常量枚举成员的引用（可以是在不同的枚举类型中定义的）
* 带括号的常量枚举表达式
* 一元运算符 +, -, ~其中之一应用在了常量枚举表达式
* 常量枚举表达式做为二元运算符 +, -, \*, /, %, <<, >>, >>>, &, |, ^的操作对象。 若常数枚举表达式求值后为 NaN或 Infinity，则会在编译阶段报错。

所有其它情况的枚举成员被当作是需要计算得出的值。

```ts
enum FileAccess {
    // 常量
    None,
    Read= 1 << 1,
    Write = 1 << 2,
    ReadWrite = Read | Write,
    // 计算出来的
    G = "123".length,
}
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.7
```
