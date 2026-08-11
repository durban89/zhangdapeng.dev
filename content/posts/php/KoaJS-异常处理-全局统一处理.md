---
title: "KoaJS 异常处理 全局统一处理"
date: "2025-07-01 11:36:12"
slug: "koajs-yi-chang-chu-li-quan-ju-tong-yi-chu-li"
categories: ["技术"]
tags: ["KoaJS"]
aliases:
  - "/2025/07/01/KoaJS-异常处理-全局统一处理/"
  - "/2025/07/01/KoaJS-异常处理-全局统一处理.html"
  - "/KoaJS-异常处理-全局统一处理/"
  - "/KoaJS-异常处理-全局统一处理.html"
  - "/2025/07/01/koajs-yi-chang-chu-li-quan-ju-tong-yi-chu-li/"
  - "/2025/07/01/koajs-yi-chang-chu-li-quan-ju-tong-yi-chu-li.html"
  - "/koajs-yi-chang-chu-li-quan-ju-tong-yi-chu-li.html"
---
记录下koajs的异常使用:

下面介绍一下 几个文件

test.js启动文件

router.js 路由文件

api/Admin.js 逻辑处理文件

koajs的异常处理逻辑代码如下[放在test.js 启动文件中]

```js
/**
 * 统一处理默认Error
 */
app.use(function *(next) {
  try {
    yield next;
  } catch (err) {
    this.status = err.status;
    this.body = {
      name: "GowhichApiServerError",
      code: err.status || 600,
      message: err.message || "Server internal error.",
      success: false
    }
  }
});
```

600 :我自己定义的,为了区别系统的错误

接下来简单的看下路由:

```js
router.post('/xxx/xxxxx', Admin.mailxxxxImport);
router.post('/xxxx/xxxx', Admin.mailxxxxBill);
```

这个router 我使用的是koa-router

好了, 到这里应该说一切都没问题了.下面就看我们如何出发这个错误了

那么在Admin.js里面我们写段代码:

```js
module.exports.mailxxxxBill = function *(next){
  var uid = _uid(this.request);
  var taskid = this.request.body.taskid;

  if (!uid || !taskid) {
    return this.throw('任务参数不能为空');
  }
  
  //测试使用
  return this.throw('任务参数不能为空');
}
```

没错就是这句代码:

```js
this.throw('任务参数不能为空');
```

当触发的时候,就会调用test.js的错误处理逻辑,可以了,动起来吧.


