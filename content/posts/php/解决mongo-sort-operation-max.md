---
title: "解决mongo sort operation max"
date: "2025-07-14 16:27:53"
slug: "jie-jue-mongo-sort-operation-max"
categories: ["技术"]
tags: ["MongoDB"]
aliases:
  - "/2025/07/14/解决mongo-sort-operation-max/"
  - "/2025/07/14/解决mongo-sort-operation-max.html"
  - "/解决mongo-sort-operation-max/"
  - "/解决mongo-sort-operation-max.html"
  - "/2025/07/14/jie-jue-mongo-sort-operation-max/"
  - "/2025/07/14/jie-jue-mongo-sort-operation-max.html"
  - "/jie-jue-mongo-sort-operation-max.html"
---
最近使用mongodb进行统计查询，遇到了下面的错误提示

> mongo 错误提示:OperationFailed: Sort operation used more than the maximum 33554432 bytes of RAM. Add an index, or specify a smaller limit

也许你遇到了跟我一样的问题，不知道如何解决

其原因是

> Mongodb的sort操作是把数据拿到内存中再进行排序的，为了节约内存，默认给sort操作限制了最大内存为32Mb，当数据量越来越大直到超过32Mb的时候就自然抛出异常了.值得注意是,如果你使用 skip 和 limit 联合使用实际也会产生排序.

下面是两种方式，仅供参考

方法1:增加缓存

```bash
//查询值
db.runCommand({ "getParameter" : 1, "internalQueryExecMaxBlockingSortBytes" : 1 } )
//设置新值
db.adminCommand({"setParameter":1, "internalQueryExecMaxBlockingSortBytes":335544320})
```

方法2:增加索引

根据业务对排序的key进行建立索引

我采用的方式是第二种方法

参考文章，[点击这里](https://gclinux.github.io/2018/03/01/mongo-sort-ram-limit-error/)
