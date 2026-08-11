---
title: "uglify error log 处理"
date: "2025-07-03 11:07:30"
slug: "uglify-error-log-chu-li"
categories: ["技术"]
tags: ["UglifyJS"]
aliases:
  - "/2025/07/03/uglify-error-log-处理/"
  - "/2025/07/03/uglify-error-log-处理.html"
  - "/uglify-error-log-处理/"
  - "/uglify-error-log-处理.html"
  - "/2025/07/03/uglify-error-log-chu-li/"
  - "/2025/07/03/uglify-error-log-chu-li.html"
  - "/uglify-error-log-chu-li.html"
---
使用uglify在做js的处理过程中，会遇到js的各种问题，而导致uglify自己报错，但是往往我们不知道具体是哪个文件的js报错了。

这样情况下

```js
uglify().on('error', gutil.log)
```

gulp-util就能很好的解决我们的问题。

