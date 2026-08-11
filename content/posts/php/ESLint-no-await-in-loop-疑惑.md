---
title: "ESLint - no-await-in-loop 疑惑"
date: "2025-07-03 17:11:47"
slug: "eslint-no-await-in-loop-yi-huo"
categories: ["技术"]
tags: ["ESLint", "JavaScript"]
aliases:
  - "/2025/07/03/ESLint-no-await-in-loop-疑惑/"
  - "/2025/07/03/ESLint-no-await-in-loop-疑惑.html"
  - "/ESLint-no-await-in-loop-疑惑/"
  - "/ESLint-no-await-in-loop-疑惑.html"
  - "/2025/07/03/eslint-no-await-in-loop-yi-huo/"
  - "/2025/07/03/eslint-no-await-in-loop-yi-huo.html"
  - "/eslint-no-await-in-loop-yi-huo.html"
---
在使用eslint的时候，遇到async/await语法 会报错，总是提示 no-await-in-loop。举个例子看下面的代码的逻辑

```js
for (let i = 0; i < userRedpacketItem.length; i += 1) {
  userRedpacketItem[i].product_id = await productModel.redpacketMapPrdIdToRefId(ctx, userRedpacketItem[i].product_id);
  // 是否过期
  userRedpacketItem[i] = userHasRedpacketModel.markExpire(userRedpacketItem[i]);
}
```

注意点是在for循环中使用了await

有点懵了，不能await，那我怎么取值进行更新值呢，根本就没有办法处理了，难我要先进行取值然后在进行循环赋值？嗯，这样肯定不行的，看来自己还是有点菜，不知其中的规范用法，好了，进行不断学习找到了解决办法，看下面的代码

```js
await Promise.all(userRedpacketItem.map(async (item) => {
  let newItem = item;
  newItem.product_id = await productModel.redpacketMapPrdIdToRefId(ctx, item.product_id);
  // 是否过期
  newItem = userHasRedpacketModel.markExpire(item);
  return newItem;
}));
```

嗯这样就不报错了，而且这个方法觉得也很node。
