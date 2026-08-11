---
title: "JavaScript使用console.log输出当前的行号"
date: "2025-06-12 17:19:01"
slug: "javascript-shi-yong-consolelog-shu-chu-dang-qian-de-hang-hao"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/12/JavaScript使用console.log输出当前的行号/"
  - "/2025/06/12/JavaScript使用console.log输出当前的行号.html"
  - "/JavaScript使用console.log输出当前的行号/"
  - "/JavaScript使用console.log输出当前的行号.html"
  - "/2025/06/12/javascript-shi-yong-consolelog-shu-chu-dang-qian-de-hang-hao/"
  - "/2025/06/12/javascript-shi-yong-consolelog-shu-chu-dang-qian-de-hang-hao.html"
  - "/javascript-shi-yong-consolelog-shu-chu-dang-qian-de-hang-hao.html"
---
看到一篇帖子，感觉写的很牛，摘抄在这里了：（代码如下）

```js
(function () {
    if (Error.captureStackTrace && Object.defineProperty) {

        var global = window;

        Object.defineProperty(global, '__STACK__', {
            get: function () {
                var old = Error.prepareStackTrace;
                Error.prepareStackTrace = function (error, stack) {
                    return stack;
                };

                var err = new Error();
                Error.captureStackTrace(err, arguments.callee);
                Error.prepareStackTrace = old;

                return err.stack;
            }
        });

        Object.defineProperty(global, '__LINE__', {
            get: function () {
                return __STACK__[1].getLineNumber();
            }
        });

        Object.defineProperty(global, '__FILE__', {
            get: function () {
                return __STACK__[1].getFileName();
            }
        });
    }
})();

var test = function () {
    console.log(__LINE__,__FILE__);
};

test();
```
