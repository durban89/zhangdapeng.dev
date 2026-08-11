---
title: "TypeScript基础入门 - 枚举 - 数字枚举和字符串枚举"
date: "2025-07-09 09:59:43"
slug: "typescript-ji-chu-ru-men-mei-ju-shu-zi-mei-ju-he-zi-fu-chuan-mei-ju"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-枚举-数字枚举和字符串枚举/"
  - "/2025/07/09/TypeScript基础入门-枚举-数字枚举和字符串枚举.html"
  - "/TypeScript基础入门-枚举-数字枚举和字符串枚举/"
  - "/TypeScript基础入门-枚举-数字枚举和字符串枚举.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-shu-zi-mei-ju-he-zi-fu-chuan-mei-ju/"
  - "/2025/07/09/typescript-ji-chu-ru-men-mei-ju-shu-zi-mei-ju-he-zi-fu-chuan-mei-ju.html"
  - "/typescript-ji-chu-ru-men-mei-ju-shu-zi-mei-ju-he-zi-fu-chuan-mei-ju.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.5
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

### 数字枚举

首先我们看看数字枚举，如果你使用过其它编程语言应该会很熟悉。

```ts
enum Derection {
    Up = 1,
    Down,
    Left,
    Right
}
```

如上，我们定义了一个数字枚举， Up使用初始化为 1。 其余的成员会从 1开始自动增长。 换句话说， Direction.Up的值为 1， Down为 2， Left为 3， Right为 4。

我们还可以完全不使用初始化器，如下

```ts
enum Derection {
    Up,
    Down,
    Left,
    Right
}
```

现在， Up的值为 0， Down的值为 1等等。 当我们不在乎成员的值的时候，这种自增长的行为是很有用处的，但是要注意每个枚举成员的值都是不同的。  
使用枚举很简单：通过枚举的属性来访问枚举成员，和枚举的名字来访问枚举类型，如下示例

```ts
enum ResponseOther {
    No = 0,
    Yes = 1,
}

function respond(re: string, me: ResponseOther) {
    // other doing
}

respond("message", ResponseOther.No)
```

数字枚举可以被混入到 计算过的和常量成员（如下所示）。 简短地说，不带初始化器的枚举或者被放在第一的位置，或者被放在使用了数字常量或其它常量初始化了的枚举后面。 换句话说，下面的情况是不被允许的：

```ts
enum E {
    A = getSomeValue(),
    B, // error! 'A' is not constant-initialized, so 'B' needs an initializer
}
```

### 字符串枚举

字符串枚举的概念很简单，但是有细微的 运行时的差别。 在一个字符串枚举里，每个成员都必须用字符串字面量，或另外一个字符串枚举成员进行初始化。

```ts
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT",
}
```

由于字符串枚举没有自增长的行为，字符串枚举可以很好的序列化。 换句话说，如果你正在调试并且必须要读一个数字枚举的运行时的值，这个值通常是很难读的 - 它并不能表达有用的信息（尽管 反向映射会有所帮助），字符串枚举允许你提供一个运行时有意义的并且可读的值，独立于枚举成员的名字。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.6
```
