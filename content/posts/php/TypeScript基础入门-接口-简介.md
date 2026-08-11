---
title: "TypeScript基础入门 - 接口 - 简介"
date: "2025-07-08 15:16:57"
slug: "typescript-ji-chu-ru-men-jie-kou-jian-jie"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-简介/"
  - "/2025/07/08/TypeScript基础入门-接口-简介.html"
  - "/TypeScript基础入门-接口-简介/"
  - "/TypeScript基础入门-接口-简介.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-jian-jie/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-jian-jie.html"
  - "/typescript-ji-chu-ru-men-jie-kou-jian-jie.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.6
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

### **接口初探**

下面通过一个简单示例来观察接口是如何工作的：

```ts
function printLabel(labelledObj: { label: string }) {
    console.log(labelledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```

运行后接到的结果如下

```bash
Size 10 Object
```

类型检查器会查看printLabel的调用。 printLabel有一个参数，并要求这个对象参数有一个名为label类型为string的属性。 需要注意的是，我们传入的对象参数实际上会包含很多属性，但是编译器只会检查那些必需的属性是否存在，并且其类型是否匹配。 然而，有些时候TypeScript却并不会这么宽松，示例演示如下。下面我们重写上面的例子，这次使用接口来描述：必须包含一个label属性且类型为string：

```ts
interface LabelledValue {
  label: string;
}

function printLabel(labelledObj: LabelledValue) {
  console.log(labelledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);
```

运行后接到的结果如下

```bash
Size 10 Object
```

LabelledValue接口就好比一个名字，用来描述上面例子里的要求。 它代表了有一个 label属性且类型为string的对象。 需要注意的是，我们在这里并不能像在其它语言里一样，说传给 printLabel的对象实现了这个接口。我们只会去关注值的外形。 只要传入的对象满足上面提到的必要条件，那么它就是被允许的。

还有一点值得提的是，类型检查器不会去检查属性的顺序，只要相应的属性存在并且类型也是对的就可以。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.7
```
