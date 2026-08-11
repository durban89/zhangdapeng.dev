---
title: "TypeScript基础入门 - 接口 - 只读属性"
date: "2025-07-08 15:17:05"
slug: "typescript-ji-chu-ru-men-jie-kou-zhi-du-shu-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-只读属性/"
  - "/2025/07/08/TypeScript基础入门-接口-只读属性.html"
  - "/TypeScript基础入门-接口-只读属性/"
  - "/TypeScript基础入门-接口-只读属性.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-zhi-du-shu-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-zhi-du-shu-xing.html"
  - "/typescript-ji-chu-ru-men-jie-kou-zhi-du-shu-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.8
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

### **只读属性**

一些对象属性只能在对象刚刚创建的时候修改其值。 你可以在属性名前用 readonly来指定只读属性:

```ts
interface Point {
    readonly x: number;
    readonly y: number;
}
```

你可以通过赋值一个对象字面量来构造一个Point。 赋值后， x和y再也不能被改变了。

```ts
let p1: Point = { x: 10, y: 20 };
p1.x = 5; // error!
```

运行后得到如下结果

```bash
⨯ Unable to compile TypeScript:
src/interface_3.ts(7,4): error TS2540: Cannot assign to 'x' because it is a constant or a read-only property.
```

TypeScript具有ReadonlyArray<T>类型，它与Array<T>相似，只是把所有可变方法去掉了，因此可以确保数组创建后再也不能被修改：

```ts
let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
ro[0] = 12; // error!
ro.push(5); // error!
ro.length = 100; // error!
a = ro; // error!
```

运行后得到的结果如下

```bash
⨯ Unable to compile TypeScript:
src/interface_3.ts(11,1): error TS2542: Index signature in type 'ReadonlyArray<number>' only permits reading.
src/interface_3.ts(12,4): error TS2339: Property 'push' does not exist on type 'ReadonlyArray<number>'.
src/interface_3.ts(13,4): error TS2540: Cannot assign to 'length' because it is a constant or a read-only property.
src/interface_3.ts(14,1): error TS2322: Type 'ReadonlyArray<number>' is not assignable to type 'number[]'.
  Property 'push' is missing in type 'ReadonlyArray<number>'.
```

上面代码的最后一行，可以看到就算把整个ReadonlyArray赋值到一个普通数组也是不可以的。 但是你可以用类型断言重写：

```ts
let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
a = ro as number[];
console.log(a);
```

运行后得到的结果如下

```bash
[ 1, 2, 3, 4 ]
```

### **readonly vs const**

最简单判断该用readonly还是const的方法是看要把它做为变量使用还是做为一个属性。 做为变量使用的话用 const，若做为属性则使用readonly。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.9
```
