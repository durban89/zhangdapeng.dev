---
title: "NestJS中的async/await的使用"
date: "2025-07-15 09:52:23"
slug: "nestjs-zhong-de-asyncawait-de-shi-yong"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/15/NestJS中的async/await的使用/"
  - "/2025/07/15/NestJS中的async/await的使用.html"
  - "/NestJS中的async/await的使用/"
  - "/NestJS中的async/await的使用.html"
  - "/2025/07/15/NestJS中的async-await的使用/"
  - "/2025/07/15/NestJS中的async-await的使用.html"
  - "/2025/07/15/nestjs-zhong-de-asyncawait-de-shi-yong/"
  - "/2025/07/15/nestjs-zhong-de-asyncawait-de-shi-yong.html"
  - "/nestjs-zhong-de-asyncawait-de-shi-yong.html"
---
前景

最近在试驾Nestjs，感觉还不错，但是知识点满多的，嗯，暂时还没放弃

在试驾的过程中，遇到一个获取数据逻辑，现在的逻辑这样的，函数如下

```javascript
@Get('/index')
index(@Res() res: Response) {
  var cats: Promise<Cats[]> = this.catsService.findAll();

  cats.then(data => {
    return res.render('cats/index', {
      message: 'Cats',
      data: data
    })
  }).catch(error => {
    console.log(error);
  })
}
```

写完之后，发现then...catch，让我想起来，我用Reactjs开发的时候，曾经把这玩意换成了async/await于是，函数修改成如下

```javascript
@Get('/index')
async index(@Res() res: Response) {
  var cats: Promise<Cats[]> = this.catsService.findAll();

  var data = await cats;

  return res.render('cats/index', {
    message: 'Cats",
    data: data,
  })
}
```

该写完之后，又让我想起来，我在用Nodejs写接口的时候，需要对await cats的执行做下异常捕获，不然访问的时候直接崩溃，对终端不太友好，于是该写如下

```javascript
@Get('/index')
async index(@Res() res: Response) {
  var cats: Promise<Cats[]> = this.catsService.findAll();

  try {
    const data = await cats;

    return res.render('cats/index', {
      message: 'Cats",
      data: data,
    })
  } catch (err) {
    // 处理异常逻辑
    console.log(err);
  }
}
```

建议：使用async/await的情况下，如果遇到异常会导致接口异常，为了能够正常处理逻辑，可以使用try...catch
