---
title: "Nodejs小知识之event（事件）一"
date: "2025-07-11 11:15:41"
slug: "nodejs-xiao-zhi-shi-zhi-event-shi-jian-yi"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/11/Nodejs小知识之event（事件）一/"
  - "/2025/07/11/Nodejs小知识之event（事件）一.html"
  - "/Nodejs小知识之event（事件）一/"
  - "/Nodejs小知识之event（事件）一.html"
  - "/2025/07/11/Nodejs小知识之event-事件-一/"
  - "/2025/07/11/Nodejs小知识之event-事件-一.html"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-shi-jian-yi/"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-shi-jian-yi.html"
  - "/nodejs-xiao-zhi-shi-zhi-event-shi-jian-yi.html"
---
大多数 Node.js 核心 API 构建于惯用的异步事件驱动架构，其中某些类型的对象（又称触发器，Emitter）会触发命名事件来调用函数（又称监听器，Listener）。

先看下event（事件）如何使用

```javascript
const Emitter = require("events");

const emitter = new Emitter();

emitter.on("event", function () {
  console.log("an event occur");
});

emitter.on("event1", function () {
  console.log("an event1 occur");
});

emitter.emit("event");
emitter.emit("event1");
```

上面我们绑定了两个事件分别为`event`和`event1`，然后通过`emit`分别触发了这两个事件

运行结果如下

```bash
an event occur
an event1 occur
```

事件触发了，那么如何能在触发事件的时候传递参数，看下面的代码

```javascript
const Emitter = require("events");

const emitter = new Emitter();

emitter.on("run", function (name, distance) {
  console.log(`【${name}】跑了${distance}米`);

  console.log(this);
  console.log(this === emitter);
});

emitter.emit("run", "xiaowang", 20);
```

输出结果如下

```bash
【xiaowang】跑了20米
EventEmitter {
  _events: [Object: null prototype] { run: [Function] },
  _eventsCount: 1,
  _maxListeners: undefined }
true
```

在这里不建议使用 ES6 Arrow Functions

```javascript
const Emitter = require("events");

const emitter = new Emitter();

emitter.on("run", (name, distance) => {
  console.log(`【${name}】跑了${distance}米`);

  console.log(this);
  console.log(this === emitter);
});

emitter.emit("run", "xiaowang", 20);
```

运行结果如下

```bash
【xiaowang】跑了20米
{}
false
```
