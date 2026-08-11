---
title: "Nodejs 之 __dirname 的使用"
date: "2025-07-03 16:49:55"
slug: "nodejs-zhi-dirname-de-shi-yong"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-之-dirname-的使用/"
  - "/2025/07/03/Nodejs-之-dirname-的使用.html"
  - "/Nodejs-之-dirname-的使用/"
  - "/Nodejs-之-dirname-的使用.html"
  - "/2025/07/03/nodejs-zhi-dirname-de-shi-yong/"
  - "/2025/07/03/nodejs-zhi-dirname-de-shi-yong.html"
  - "/nodejs-zhi-dirname-de-shi-yong.html"
---
新建个文件

app.js

里面的内容如下：

```js
console.log(__dirname + '/example.db');
console.log('example.db');
```

如果将app.js放在一个根目录下面

执行node app.js

分别输出如下内容：

```bash
/Users/durban/nodejs/koa-mysql-orm-model/example.db
example.db
```

我们建立一个文件夹app,app下建立一个app.js

里面的内容如下：

```bash
console.log(__dirname + '/example.db');
console.log('example.db');
```

执行node app.js

分别输出如下内容：

```bash
/Users/durban/nodejs/koa-mysql-orm-model/app/example.db
example.db
```

可见，`__dirname`追加了自身的目录路径，一般这样做的好处是，可以避免文件的混乱调用。
