---
title: "TypeScript基础入门 - 函数 - this(三)"
date: "2025-07-08 16:01:52"
slug: "typescript-ji-chu-ru-men-han-shu-this-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-this(三)/"
  - "/2025/07/08/TypeScript基础入门-函数-this(三).html"
  - "/TypeScript基础入门-函数-this(三)/"
  - "/TypeScript基础入门-函数-this(三).html"
  - "/2025/07/08/TypeScript基础入门-函数-this-三/"
  - "/2025/07/08/TypeScript基础入门-函数-this-三.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-san/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-this-san.html"
  - "/typescript-ji-chu-ru-men-han-shu-this-san.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.4
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 函数

## this

学习如何在JavaScript里正确使用this就好比一场成年礼。 由于TypeScript是JavaScript的超集，TypeScript程序员也需要弄清 this工作机制并且当有bug的时候能够找出错误所在。 幸运的是，TypeScript能通知你错误地使用了 this的地方。 如果你想了解JavaScript里的 this是如何工作的，那么首先阅读Yehuda Katz写的[Understanding JavaScript Function Invocation and "this"](http://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)。 Yehuda的文章详细的阐述了 this的内部工作原理，因此这里只做简单介绍。

### this参数在回调函数里

继续上篇文章【[TypeScript基础入门 - 函数 - this(二)](https://www.gowhich.com/blog/894)】

我们也看到过在回调函数里this报错的情况，当你将一个函数传递到某个库函数里稍后会被调用时。 因为当回调被调用的时候，它们会被当成一个普通函数调用， this将为undefined。 稍做改动，你就可以通过 this参数来避免错误。 首先，库函数的作者要指定 this的类型，如下实例

```ts
interface UIElement {
    addClickListener(onclick: (this: void, e: Event) => void): void;
}
```

this: void表示addClickListener期望onclick是一个不需要此类型的函数。  
其次，用这个注释你的调用代码，如下所示

```ts
interface UIElement {
    addClickListener(onclick: (this: void, e: Error) => void): void;
}

class Handler {
    info: string;
    onClickBad(this: Handler, e: Error) {
        // oops, used this here. using this callback would crash at runtime
        this.info = e.message;
    }
}
let h = new Handler();
let uiElement: UIElement = {
    addClickListener(onclick: (this: void, e: Error) => void) {
        // do something
    }
};

uiElement.addClickListener(h.onClickBad); // 这里会报错
```

指定了this类型后，显式声明onClickBad必须在Handler的实例上调用。 然后TypeScript会检测到 addClickListener要求函数带有this: void。 我们添加另外一个函数做下对比，如下

```ts
interface UIElement {
    addClickListener(onclick: (this: void, e: Error) => void): void;
}

class Handler {
    info: string;
    onClickBad(this: Handler, e: Error) {
        this.info = e.message;
    }
    onClickGood(this: void, e: Error) {
        console.log('点击了！');
    }
}
let h = new Handler();
let uiElement: UIElement = {
    addClickListener(onclick: (this: void, e: Error) => void) {
        // do something
    }
};

uiElement.addClickListener(h.onClickGood);
```

通过将h.onClickBad更换为h.onClickGood，就能正常调用。  
因为onClickGood指定了this类型为void，因此传递addClickListener是合法的。 当然了，这也意味着不能使用 this.info. 如果你两者都想要，你不得不使用箭头函数了，如下

```ts
interface UIElement {
    addClickListener(onclick: (this: void, e: Error) => void): void;
}

class Handler {
    info: string;
    onClickGood = (e: Error) => { this.info = e.message }
}

let h = new Handler();
let uiElement: UIElement = {
    addClickListener(onclick: (this: void, e: Error) => void) {
        // do something
    }
};

uiElement.addClickListener(h.onClickGood);
```

这是可行的因为箭头函数不会捕获this，所以你总是可以把它们传给期望this: void的函数。 缺点是每个 Handler对象都会创建一个箭头函数。 另一方面，方法只会被创建一次，添加到 Handler的原型链上。 它们在不同 Handler对象间是共享的。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.5
```
