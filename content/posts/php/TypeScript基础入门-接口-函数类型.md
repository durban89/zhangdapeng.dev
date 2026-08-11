---
title: "TypeScript基础入门 - 接口 - 函数类型"
date: "2025-07-08 15:17:12"
slug: "typescript-ji-chu-ru-men-jie-kou-han-shu-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-函数类型/"
  - "/2025/07/08/TypeScript基础入门-接口-函数类型.html"
  - "/TypeScript基础入门-接口-函数类型/"
  - "/TypeScript基础入门-接口-函数类型.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-han-shu-lei-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-han-shu-lei-xing.html"
  - "/typescript-ji-chu-ru-men-jie-kou-han-shu-lei-xing.html"
---
项目实践仓库

```javascript
https://github.com/durban89/typescript_demo.git
tag: 1.0.10
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

### **函数类型**

接口能够描述JavaScript中对象拥有的各种各样的外形。 除了描述带有属性的普通对象外，接口也可以描述函数类型。

为了使用接口表示函数类型，我们需要给接口定义一个调用签名。 它就像是一个只有参数列表和返回值类型的函数定义。参数列表里的每个参数都需要名字和类型。如下示例

```ts
interface SomeInterface {
  (arg1: string, arg2: string): boolean;
}
```

这样定义后，我们可以像使用其它接口一样使用这个函数类型的接口。 下例展示了如何创建一个函数类型的变量，并将一个同类型的函数赋值给这个变量。

```ts
let someFunc: SomeInterface
someFunc = function (arg1: string, arg2: string) {
    const res = arg1.search(arg2)
    return res > -1;
}
console.log(someFunc('weast','east'));
```

运行后得到的结果如下

```bash
true
```

对于函数类型的类型检查来说，函数的参数名不需要与接口里定义的名字相匹配。 比如，我们使用下面的代码重写上面的例子：

```ts
let someFunc2: SomeInterface;
someFunc2 = function (x: string, y: string): boolean {
    const res = x.search(y);
    return res > -1;
}
console.log(someFunc2('weast', 'east'));
```

运行后得到的结果如下

```bash
true
```

函数的参数会逐个进行检查，要求对应位置上的参数类型是兼容的。 如果你不想指定类型，TypeScript的类型系统会推断出参数类型，因为函数直接赋值给了 someInterface类型变量。 函数的返回值类型是通过其返回值推断出来的（此例是 false和true）。 如果让这个函数返回数字或字符串，类型检查器会警告我们函数的返回值类型与someInterface接口中的定义不匹配。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.11
```
