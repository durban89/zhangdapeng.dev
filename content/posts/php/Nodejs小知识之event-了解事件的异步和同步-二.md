---
title: "Nodejs小知识之event（了解事件的异步和同步）二"
date: "2025-07-11 11:15:45"
slug: "nodejs-xiao-zhi-shi-zhi-event-liao-jie-shi-jian-de-yi-bu-he-tong-bu-er"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/11/Nodejs小知识之event（了解事件的异步和同步）二/"
  - "/2025/07/11/Nodejs小知识之event（了解事件的异步和同步）二.html"
  - "/Nodejs小知识之event（了解事件的异步和同步）二/"
  - "/Nodejs小知识之event（了解事件的异步和同步）二.html"
  - "/2025/07/11/Nodejs小知识之event-了解事件的异步和同步-二/"
  - "/2025/07/11/Nodejs小知识之event-了解事件的异步和同步-二.html"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-liao-jie-shi-jian-de-yi-bu-he-tong-bu-er/"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-liao-jie-shi-jian-de-yi-bu-he-tong-bu-er.html"
  - "/nodejs-xiao-zhi-shi-zhi-event-liao-jie-shi-jian-de-yi-bu-he-tong-bu-er.html"
---
现看个简单的关于事件使用的代码

```javascript
const Emitter = require("events");

const emitter = new Emitter();

emitter.on("event_1", function (name, age) {
  setImmediate(function () {
    console.log("event_1 immediate");
  });

  console.log(`event_1 ${name} age is ${age}`);
});

emitter.on("event_2", function (name, age) {
  setImmediate(function () {
    console.log("event_2 immediate");
  });
  console.log(`event_2 ${name} age is ${age}`);
});

emitter.on("event_3", function (name, age) {
  process.nextTick(function () {
    console.log("event_3 nextTick");
  });

  console.log(`event_3 ${name} age is ${age}`);
});

emitter.emit("event_1", "xiaowang", 20);
emitter.emit("event_2", "xiaoli", 30);
emitter.emit("event_1", "xiaowang2", 20);
emitter.emit("event_2", "xiaoli2", 30);
emitter.emit("event_3", "xiaowei", 29);
emitter.emit("event_3", "xiaowei2", 29);
```

输出的结果如下

```bash
event_1 xiaowang age is 20
event_2 xiaoli age is 30
event_1 xiaowang2 age is 20
event_2 xiaoli2 age is 30
event_3 xiaowei age is 29
event_3 xiaowei2 age is 29
event_3 nextTick
event_3 nextTick
event_1 immediate
event_2 immediate
event_1 immediate
event_2 immediate
```

从上面的输出结果可以看出，emit触发事件的时候，事件的执行顺序是按照顺序从上到下依次执行（应该可以看作是事件的同步）

```bash
event_1 xiaowang age is 20
event_2 xiaoli age is 30
event_1 xiaowang2 age is 20
event_2 xiaoli2 age is 30
event_3 xiaowei age is 29
event_3 xiaowei2 age is 29
```

再看下这里的输出结果，会发现，无论执行多少次这个顺序是不会变的（应该可以看作是事件的异步）

```bash
event_3 nextTick
event_3 nextTick
event_1 immediate
event_2 immediate
event_1 immediate
event_2 immediate
```

process.nextTick和setImmediate，作为异步处理的函数，居然process.nextTick会比setImmediate的调用更先一步执行

具体的原因可以参考官方的文章[《Node.js 事件循环，定时器和 process.nextTick()》](https://nodejs.org/zh-cn/docs/guides/event-loop-timers-and-nexttick/)

从官方的文章中也得出结果，setImmediate应该多用，process.nextTick应该少用，虽然这需要一个漫长的过程
