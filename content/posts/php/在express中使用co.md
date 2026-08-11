---
title: "在express中使用co"
date: "2025-07-02 15:40:47"
slug: "zai-express-zhong-shi-yong-co"
categories: ["技术"]
tags: ["ExpressJS", "NodeJS"]
aliases:
  - "/2025/07/02/在express中使用co/"
  - "/2025/07/02/在express中使用co.html"
  - "/在express中使用co/"
  - "/在express中使用co.html"
  - "/2025/07/02/zai-express-zhong-shi-yong-co/"
  - "/2025/07/02/zai-express-zhong-shi-yong-co.html"
  - "/zai-express-zhong-shi-yong-co.html"
---
以下支持的Nodejs版本是 >=4.2.1

在express中我们都知道，我们可以在文件中定义一个方法，如下，然后可以在router中调用这个方法进行相应的处理。但是我们不想一直去写一些回调的方法，

希望对于异步的处理能像写顺序编程那样一直按照逻辑顺序去执行，co就帮了我们一个大忙，试试如下这种方式吧。【前提是要安装下co】

```js
module.exports.addBackground = function (req, res, next) {
  let title = req.body.title || '';
  let theme = req.body.theme || '';
  let theorder = req.body.theorder || 0;
  let big_url = req.body.big_url || '';
  let thumb_url = req.body.thumb_url || '';
  let mtime = parseInt(new Date().valueOf() / 1000);
  if (!title || !theme || !big_url || !thumb_url) {
    throw new Error('Arguments is Error.');
  }
  co(function *() {
    let _isAdmin = yield User.isAdmin(req.user.id);
    if (!_isAdmin) {
      throw new Error('Admin only.');
    }
    let e_sql = 'SELECT * FROM xxxxx.app_dft_background where title = ' + mysql.escape(title);
    let e_res = yield mysql.thunkQuery(e_sql);
    if (e_res.length > 0) {
      return false;
    }
    let sql = sqlBuilder.makeInsertSql('xxxxx.app_dft_background', {
      title: title,
      theme: theme,
      theorder: theorder,
      big_url: big_url,
      thumb_url: thumb_url,
      mtime: mtime
    });
    let res = yield mysql.thunkQuery(sql);
    return res;
  }).then((data) => {
    if (!data) {
      res.json({'success': false, 'message': '名称已存在'});
    } else {
      res.json({'success': true, 'data': data});
    }
  }).catch((err) => {
    next(err);
  });
};
```

如果还是没有理解清楚可以去看下co和Promise。很容易理解的


