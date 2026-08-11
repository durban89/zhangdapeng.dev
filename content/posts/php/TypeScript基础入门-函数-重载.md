---
title: "TypeScript基础入门 - 函数 - 重载"
date: "2025-07-08 16:01:56"
slug: "typescript-ji-chu-ru-men-han-shu-zhong-zai"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-重载/"
  - "/2025/07/08/TypeScript基础入门-函数-重载.html"
  - "/TypeScript基础入门-函数-重载/"
  - "/TypeScript基础入门-函数-重载.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-zhong-zai/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-zhong-zai.html"
  - "/typescript-ji-chu-ru-men-han-shu-zhong-zai.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.5
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## **函数**

### **重载**

JavaScript本身是个动态语言。 JavaScript里函数根据传入不同的参数而返回不同类型的数据是很常见的。如下实例

```ts
let suits = ["hearts", "spades", "clubs", "diamonds"];

function pickCard(x: any): any {
    if (typeof x == "object") {
        let pickCard = Math.floor(Math.random() * x.length);
        return pickCard;
    } else if (typeof x == 'number') {
        let pickedSuit = Math.floor(x / 13);
        return {
            suit: suits[pickedSuit],
            card: x % 13,
        }
    }
}

let myDeck = [
    {
        suit: "diamands",
        card: 2,
    },
    {
        suit: 'spades',
        card: 10,
    },
    {
        suit: 'hearts',
        card: 4
    }
]

let pickedCard1 = myDeck[pickCard(myDeck)];
let pickedCard2 = pickCard(15);

console.log('card: ' + pickedCard1.card + ' of ' + pickedCard1.suit);
console.log('card: ' + pickedCard2.card + ' of ' + pickedCard2.suit);
```

运行后得到类型如下结果

```ts
$ npx ts-node src/function_7.ts
card: 2 of diamands
card: 2 of spades
```

pickCard方法根据传入参数的不同会返回两种不同的类型。 如果传入的是代表纸牌的对象，函数作用是从中抓一张牌。 如果用户想抓牌，我们告诉他抓到了什么牌。 但是这怎么在类型系统里表示呢。方法是为同一个函数提供多个函数类型定义来进行函数重载。 编译器会根据这个列表去处理函数的调用。 下面我们来重载 pickCard函数。

```ts
let suits = ["hearts", "spades", "clubs", "diamonds"];

function pickCard(x: {suit: string, card: number}[]): number;
function pickCard(x: number): {suit: string, card: number};
function pickCard(x: any): any {
    if (typeof x == "object") {
        let pickedCard = Math.floor(Math.random() * x.length);
        return pickedCard;
    } else if (typeof x == 'number') {
        let pickedSuit = Math.floor(x / 13);
        return {
            suit: suits[pickedSuit],
            card: x % 13,
        }
    }
}

let myDeck = [
    {
        suit: "diamands",
        card: 2,
    },
    {
        suit: 'spades',
        card: 10,
    },
    {
        suit: 'hearts',
        card: 4
    }
]

let pickedCard1 = myDeck[pickCard(myDeck)];
let pickedCard2 = pickCard(15);

console.log('card: ' + pickedCard1.card + ' of ' + pickedCard1.suit);
console.log('card: ' + pickedCard2.card + ' of ' + pickedCard2.suit);
```

得到的结果类似如下

```bash
$ npx ts-node src/function_7.ts
card: 10 of spades
card: 2 of spades
```

这样改变后，重载的pickCard函数在调用的时候会进行正确的类型检查。

为了让编译器能够选择正确的检查类型，它与JavaScript里的处理流程相似。 它查找重载列表，尝试使用第一个重载定义。 如果匹配的话就使用这个。 因此，在定义重载的时候，一定要把最精确的定义放在最前面。

注意，function pickCard(x: any): any并不是重载列表的一部分，因此这里只有两个重载：一个是接收对象另一个接收数字。 以其它参数调用 pickCard会产生错误。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.6
```
