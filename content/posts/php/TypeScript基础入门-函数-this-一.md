---
title: "TypeScript基础入门 - 函数 - this(一)"
date: "2025-07-08 16:01:46"
slug: "typescript-ji-chu-ru-men-han-shu-this-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-this(一)/"
  - "/2025/07/08/TypeScript基础入门-函数-this(一).html"
  - "/TypeScript基础入门-函数-this(一)/"
  - "/TypeScript基础入门-函数-this(一).html"
  - "/2025/07/08/TypeScript基础入门-函数-this-一/"
  - "/2025/07/08/TypeScript基础入门-函数-this-一.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-yi/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-yi.html"
  - "/typescript-ji-chu-ru-men-han-shu-this-yi.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.2
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

### **this和箭头函数**

JavaScript里，this的值在函数被调用的时候才会指定。 这是个既强大又灵活的特点，但是你需要花点时间弄清楚函数调用的上下文是什么。 但众所周知，这不是一件很简单的事，尤其是在返回一个函数或将函数当做参数传递的时候。

下面看一个例子：

```ts
let deck = {
    suits: [
        'hearts',
        'spades',
        'clubs',
        'diamods'
    ],
    cards: Array(52),
    createCardPicker: function () {
        return function () {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {
                suit: this.suits[pickedSuit], card: pickedCard % 13,
            }
        }
    }
}

let cardPicker = deck.createCardPicker();
let pickedCard = cardPicker();
console.log("card: " + pickedCard.card + " of " + pickedCard.suit);
```

可以看到createCardPicker是个函数，并且它又返回了一个函数。 如果我们尝试运行这个程序，会得到如下类似错误提示

```bash
$ npx ts-node src/function_4.ts
Cannot read property '2' of undefined
```

因为 createCardPicker返回的函数里的this被设置成了window而不是deck对象。 因为我们只是独立的调用了 cardPicker()。 顶级的非方法式调用会将 this视为window。 （注意：在严格模式下， this为undefined而不是window）。为了解决这个问题，我们可以在函数被返回时就绑好正确的this。 这样的话，无论之后怎么使用它，都会引用绑定的'deck'对象。 我们需要改变函数表达式来使用ECMAScript 6箭头语法。 箭头函数能保存函数创建时的 this值，而不是调用时的值：

```ts
let deck = {
    suits: [
        'hearts',
        'spades',
        'clubs',
        'diamods'
    ],
    cards: Array(52),
    createCardPicker: function() {
        return () => {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);

            return {
                suit: this.suits[pickedSuit],
                card: pickedCard % 13,
            }
        }
    }
}

let cardPicker = deck.createCardPicker();
let pickedCard = cardPicker();
console.log("card: " + pickedCard.card + " of " + pickedCard.suit);
```

运行后得到的结果如下

```bash
$ npx ts-node src/function_4.ts
card: 10 of hearts
```

TypeScript会警告你犯了一个错误，如果你给编译器设置了--noImplicitThis标记。 它会指出 this.suits[pickedSuit]里的this的类型为any。

***这个是官方说的，但是实际上运行的时候，并没有什么警告的信息***

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.3
```
