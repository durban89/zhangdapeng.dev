---
title: "TypeScript基础入门 - 接口 - 可选属性"
date: "2025-07-08 15:17:01"
slug: "typescript-ji-chu-ru-men-jie-kou-ke-xuan-shu-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-可选属性/"
  - "/2025/07/08/TypeScript基础入门-接口-可选属性.html"
  - "/TypeScript基础入门-接口-可选属性/"
  - "/TypeScript基础入门-接口-可选属性.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ke-xuan-shu-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ke-xuan-shu-xing.html"
  - "/typescript-ji-chu-ru-men-jie-kou-ke-xuan-shu-xing.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.7
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

### **可选属性**

接口里的属性不全都是必需的。 有些是只在某些条件下存在，或者根本不存在。 可选属性在应用“option bags”模式时很常用，即给函数传入的参数对象中只有部分属性赋值了。下面是应用了“option bags”的例子：

```ts
interface SquareConfig {
    color?: string;
    width?: number;
}

function createSquare(config: SquareConfig): { color: string; area: number } {
    let newSquare = { color: "white", area: 100 };
    if (config.color) {
        newSquare.color = config.color;
    }
    if (config.width) {
        newSquare.area = config.width * config.width;
    }
    return newSquare;
}

let mySquare = createSquare({ color: "black" });
console.log(mySquare);
```

运行后结果如下

```bash
{ color: 'black', area: 100 }
```

带有可选属性的接口与普通的接口定义差不多，只是在可选属性名字定义的后面加一个?符号。可选属性的好处之一是可以对可能存在的属性进行预定义，好处之二是可以捕获引用了不存在的属性时的错误。 比如，我们故意将 createSquare里的color属性名拼错，就会得到一个错误提示：

```ts
interface SquareConfig {
    color?: string;
    width?: number;
}

function createSquare(config: SquareConfig): { color: string; area: number } {
    let newSquare = {color: "white", area: 100};
    if (config.clor) {
        // Error: Property 'clor' does not exist on type 'SquareConfig'
        newSquare.color = config.clor;
    }
    if (config.width) {
        newSquare.area = config.width * config.width;
    }
    return newSquare;
}

let mySquare = createSquare({color: "black"});
console.log(mySquare);
```

运行后结果如下

```bash
⨯ Unable to compile TypeScript:
src/interface_2.ts(27,16): error TS2551: Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?
src/interface_2.ts(29,34): error TS2551: Property 'clor' does not exist on type 'SquareConfig'. Did you mean 'color'?
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.8
```
