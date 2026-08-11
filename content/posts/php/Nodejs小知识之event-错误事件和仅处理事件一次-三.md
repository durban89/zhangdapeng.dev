---
title: "Nodejs小知识之event（错误事件和仅处理事件一次）三"
date: "2025-07-11 11:16:00"
slug: "nodejs-xiao-zhi-shi-zhi-event-cuo-wu-shi-jian-he-jin-chu-li-shi-jian-yi-ci-san"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/11/Nodejs小知识之event（错误事件和仅处理事件一次）三/"
  - "/2025/07/11/Nodejs小知识之event（错误事件和仅处理事件一次）三.html"
  - "/Nodejs小知识之event（错误事件和仅处理事件一次）三/"
  - "/Nodejs小知识之event（错误事件和仅处理事件一次）三.html"
  - "/2025/07/11/Nodejs小知识之event-错误事件和仅处理事件一次-三/"
  - "/2025/07/11/Nodejs小知识之event-错误事件和仅处理事件一次-三.html"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-cuo-wu-shi-jian-he-jin-chu-li-shi-jian-yi-ci-san/"
  - "/2025/07/11/nodejs-xiao-zhi-shi-zhi-event-cuo-wu-shi-jian-he-jin-chu-li-shi-jian-yi-ci-san.html"
  - "/nodejs-xiao-zhi-shi-zhi-event-cuo-wu-shi-jian-he-jin-chu-li-shi-jian-yi-ci-san.html"
---
event - 错误事件和仅处理事件一次

当使用 eventEmitter.on() 注册监听器时，监听器会在每次触发命名事件时被调用。

```javascript
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("event", function () {
  console.log("event emitter");
});

emitter.emit("event");
emitter.emit("event");
```

运行后得到的结果如下

```javascript
$ node main.js
event emitter
event emitter
```

使用 eventEmitter.once() 可以注册最多可调用一次的监听器。 当事件被触发时，监听器会被注销，然后再调用。

```javascript
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.once("event", function () {
  console.log("event emitter");
});

emitter.emit("event");
emitter.emit("event");
```

运行后得到的结果如下

```bash
$ node main.js
event emitter
```

（错误事件）Error events

```javascript
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.emit("error", new Error("i am a error"));
```

运行结果如下

```bash
$ node main.js
events.js:174
      throw er; // Unhandled 'error' event
      ^

Error: i am a error
    at Object.<anonymous> (/Users/durban/nodejs/main.js:45:23)
    at Module._compile (internal/modules/cjs/loader.js:778:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:789:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:831:12)
    at startup (internal/bootstrap/node.js:283:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:623:3)
Emitted 'error' event at:
    at Object.<anonymous> (/Users/durban/nodejs/main.js:45:9)
    at Module._compile (internal/modules/cjs/loader.js:778:30)
    [... lines matching original stack trace ...]
    at bootstrapNodeJSCore (internal/bootstrap/node.js:623:3)
```

再看下面实例

```javascript
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("error", function (error) {
  console.log("i am catch a error");
  console.log(error);
});

emitter.emit("error", new Error("i am a error"));
```

运行后结果如下

```bash
$ node main.js
i am catch a error
Error: i am a error
    at Object.<anonymous> (/Users/durban/nodejs/main.js:77:23)
    at Module._compile (internal/modules/cjs/loader.js:778:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:789:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:831:12)
    at startup (internal/bootstrap/node.js:283:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:623:3)
```

event（事件）的简单使用记录再次
