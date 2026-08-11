---
title: "TypeScript基础入门 - 类型兼容性 - 枚举和类"
date: "2025-07-09 10:00:10"
slug: "typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-mei-ju-he-lei"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-类型兼容性-枚举和类/"
  - "/2025/07/09/TypeScript基础入门-类型兼容性-枚举和类.html"
  - "/TypeScript基础入门-类型兼容性-枚举和类/"
  - "/TypeScript基础入门-类型兼容性-枚举和类.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-mei-ju-he-lei/"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-mei-ju-he-lei.html"
  - "/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-mei-ju-he-lei.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.0
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

枚举类型与数字类型兼容，并且数字类型与枚举类型兼容。不同枚举类型之间是不兼容的。比如，

```ts
enum Status {
    Ready,
    Waiting,
};

enum Color {
    Color1,
    Color2,
    Color3,
};

let s = Status.Ready;
s = Color.Color1;
```

运行后会有类似如下的错误提示

```bash
⨯ Unable to compile TypeScript:
src/type_compatibility_2.ts(13,1): error TS2322: Type 'Color.Color1' is not assignable to type 'Status'.
```

## 类

类与对象字面量和接口差不多，但有一点不同：类有静态部分和实例部分的类型。 比较两个类类型的对象时，只有实例的成员会被比较。 静态成员和构造函数不在比较的范围内。如下实例演示

```ts
class PersonType {
    name: string;
    constructor(name: string, age: number) {}
}

class AnimalType {
    name: string;
    constructor (name: string) {}
}

let PT: PersonType = new PersonType('a', 1);
let AT: AnimalType = new AnimalType('a');

AT = PT
PT = AT
```

当我们运行这段代码的时候，会发现没有报任何错误

### 类的私有成员

类中的私有成员和受保护成员会影响其兼容性。检查类的实例是否兼容时，如果目标类型包含私有成员，则源类型还必须包含源自同一类的私有成员。同样，这同样适用于具有受保护成员的实例。这允许类与其超类兼容，但不允许使用来自不同继承层次结构的类，否则这些类具有相同的形状。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.1
```
