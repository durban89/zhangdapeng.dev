---
title: "在使用gulp-less的误区"
date: "2025-07-01 15:04:00"
slug: "zai-shi-yong-gulp-less-de-wu-qu"
categories: ["技术"]
tags: ["Gulp"]
aliases:
  - "/2025/07/01/在使用gulp-less的误区/"
  - "/2025/07/01/在使用gulp-less的误区.html"
  - "/在使用gulp-less的误区/"
  - "/在使用gulp-less的误区.html"
  - "/2025/07/01/zai-shi-yong-gulp-less-de-wu-qu/"
  - "/2025/07/01/zai-shi-yong-gulp-less-de-wu-qu.html"
  - "/zai-shi-yong-gulp-less-de-wu-qu.html"
---
在使用gulp-less的时候会出现这样的一个问题

**这个修改之前的代码**

```js
//变量声明
var paths = {
  'less':[
      './app/less/**/*.less',
    ]
};
gulp.task('less',function(){
  return gulp.src(paths.less)
    .pipe(gulpLess())
    .pipe(gulp.dest('./app/css'))
});
```

其实我的意思就是，将我less目录下面的所有文件合并成一个app.css

但是这样执行确实行不通，会爆出来很多的错误。之前还是一头雾水，后来换了方式

**这个修改之后的代码**

```js
//变量声明
var paths = {
  'less':[
      './app/less/app.less',
      './app/less/main.less', 
    ]
};
gulp.task('less',function(){
  return gulp.src(paths.less)
    .pipe(gulpLess())
    .pipe(gulp.dest('./app/css'))
});
```

其实这样执行就没有问题了，其实很明了，问题已经出现了，也知道了原因，因为我们要生成一个文件app.css，那么其实app.less是主要文件

那么在其中的一些变量都是引过来，然后执行。那么我之前的代码问题就是在于我要将所有的less文件都编译成对应的css，我的天，怎么可能，

那要解决的问题就是每个文件都要引入需要的文件，哈哈，糊涂了。


