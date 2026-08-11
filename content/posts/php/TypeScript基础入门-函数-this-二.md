---
title: "TypeScript基础入门 - 函数 - this(二)"
date: "2025-07-08 16:01:49"
slug: "typescript-ji-chu-ru-men-han-shu-this-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-this(二)/"
  - "/2025/07/08/TypeScript基础入门-函数-this(二).html"
  - "/TypeScript基础入门-函数-this(二)/"
  - "/TypeScript基础入门-函数-this(二).html"
  - "/2025/07/08/TypeScript基础入门-函数-this-二/"
  - "/2025/07/08/TypeScript基础入门-函数-this-二.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-er/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-er.html"
  - "/typescript-ji-chu-ru-men-han-shu-this-er.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.3
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

### **this**

学习如何在JavaScript里正确使用this就好比一场成年礼。 由于TypeScript是JavaScript的超集，TypeScript程序员也需要弄清 this工作机制并且当有bug的时候能够找出错误所在。 幸运的是，TypeScript能通知你错误地使用了 this的地方。 如果你想了解JavaScript里的 this是如何工作的，那么首先阅读Yehuda Katz写的[Understanding JavaScript Function Invocation and "this"](http://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)。 Yehuda的文章详细的阐述了 this的内部工作原理，因此这里只做简单介绍。

### **this参数**

继续上篇文章【[TypeScript基础入门 - 函数 - this(一)](https://www.gowhich.com/blog/893)】

this.suits[pickedSuit]的类型依旧为any。 这是因为 this来自对象字面量里的函数表达式。 修改的方法是，提供一个显式的 this参数。 this参数是个假的参数，它出现在参数列表的最前面，如下

```ts
function f(this: void) {
    // 确保`this`在这个独立功能中无法使用
}
```

我们添加一些接口，Card 和 Deck，让类型重用能够变得清晰简单些，代码如下

```ts
interface Card {
    suit: string;
    card: number;
}

interface Deck {
    suits: string[];
    cards: number[];
    createCardPicker(this: Deck): () => Card;
}

let deck: Deck = {
    suits: [
        'hearts',
        'spades',
        'clubs',
        'diamods'
    ],
    cards: Array(52),
    createCardPicker: function (this: Deck) {
        return () => {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {
                suit: this.suits[pickedCard],
                card: pickedCard % 13,
            }
        }
    }

}

let cardPicker = deck.createCardPicker();
let pickedCard = cardPicker();
console.log("card: " + pickedCard.card + " of " + pickedCard.suit);
```

运行后得到的结果类似如下

```bash
$ npx ts-node src/function_5.ts
card: 3 of diamods
```

现在TypeScript知道createCardPicker期望在某个Deck对象上调用。 也就是说 this是Deck类型的，而非any，因此--noImplicitThis不会报错了。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.4
```
