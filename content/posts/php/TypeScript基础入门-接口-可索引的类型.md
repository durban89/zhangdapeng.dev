---
title: "TypeScript基础入门 - 接口 - 可索引的类型"
date: "2025-07-08 16:00:29"
slug: "typescript-ji-chu-ru-men-jie-kou-ke-suo-yin-de-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-可索引的类型/"
  - "/2025/07/08/TypeScript基础入门-接口-可索引的类型.html"
  - "/TypeScript基础入门-接口-可索引的类型/"
  - "/TypeScript基础入门-接口-可索引的类型.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ke-suo-yin-de-lei-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ke-suo-yin-de-lei-xing.html"
  - "/typescript-ji-chu-ru-men-jie-kou-ke-suo-yin-de-lei-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.11
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node src/learn_basic_types.ts
```

```bash
npx ts-node 脚本路径
```

## **接口**

TypeScript的核心原则之一是对值所具有的结构进行类型检查。 它有时被称做“鸭式辨型法”或“结构性子类型化”。 在TypeScript里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。

### **可索引的类型**

与使用接口描述函数类型差不多，我们也可以描述那些能够“通过索引得到”的类型，比如a[10]或ageMap["daniel"]。 可索引类型具有一个 索引签名，它描述了对象索引的类型，还有相应的索引返回值类型。 让我们看一个例子：

```ts
interface SomeArray {
    [index: number]: string;
}

let someArray: SomeArray;
someArray = ["string1", "string2"];

let str: string = someArray[0];
console.log(str);
```

运行后结果如下

```bash
string1
```

上面例子里，我们定义了SomeArray接口，它具有索引签名。 这个索引签名表示了当用 number去索引SomeArray时会得到string类型的返回值。共有支持两种索引签名：字符串和数字。 可以同时使用两种类型的索引，但是数字索引的返回值必须是字符串索引返回值类型的子类型。 这是因为当使用 number来索引时，JavaScript会将它转换成string然后再去索引对象。 也就是说用 100（一个number）去索引等同于使用"100"（一个string）去索引，因此两者需要保持一致。

```ts
class Person {
    name: string;
}
class Student extends Person {
    className: string;
}

// 错误：使用数值型的字符串索引，有时会得到完全不同的Person!
interface NotOkay {
    // [x: number]: Person; // 数字索引类型“Person”不能赋给字符串索引类型“Student”
    [x: string]: Student;
}
```

字符串索引签名能够很好的描述dictionary模式，并且它们也会确保所有属性与其返回值类型相匹配。 因为字符串索引声明了 obj.property和obj["property"]两种形式都可以。 下面的例子里， name的类型与字符串索引类型不匹配，所以类型检查器给出一个错误提示：

```ts
interface SomeInterface {
    [index: string]: string
    // length: number    // 错误，`length`的类型与索引类型返回值的类型不匹配
    name: string       // 可以，name是string类型
}
```

最后，你可以将索引签名设置为只读，这样就防止了给索引赋值：

```ts
interface SomeInterface {
    [index: string]: string
    // length: number    // 错误，`length`的类型与索引类型返回值的类型不匹配
    name: string       // 可以，name是string类型
}

interface ReadonlySomeArray {
    readonly [index: number]: string;
}
let readonlyArray: ReadonlySomeArray = ["string1", "string2"];
readonlyArray[2] = "string3"; // error!
```

运行后会得到如下错误提示

```bash
src/interface_6.ts(36,1): error TS2542: Index signature in type 'ReadonlySomeArray' only permits reading.
```

你不能设置readonlyArray[2]，因为索引签名是只读的。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.12
```
