---
title: "Gulp解决less一条龙服务"
date: "2025-07-01 15:04:04"
slug: "gulp-jie-jue-less-yi-tiao-long-fu-wu"
categories: ["技术"]
tags: ["Gulp"]
aliases:
  - "/2025/07/01/Gulp解决less一条龙服务/"
  - "/2025/07/01/Gulp解决less一条龙服务.html"
  - "/Gulp解决less一条龙服务/"
  - "/Gulp解决less一条龙服务.html"
  - "/2025/07/01/gulp-jie-jue-less-yi-tiao-long-fu-wu/"
  - "/2025/07/01/gulp-jie-jue-less-yi-tiao-long-fu-wu.html"
  - "/gulp-jie-jue-less-yi-tiao-long-fu-wu.html"
---
所谓gulp对less的一条龙服务是指，由less编译为css，再由css编译为min.css，再由min.css编译为min.css.map

大白话就是Less文件转为css文件，然后将css文件压缩，再然后生成css压缩文件的map文件最后就得到了我们的需要使用的

min文件和一些奇葩浏览器要用到的map文件

gulp的配置如下

```js
var gulp = require('gulp');
var gulpLess = require('gulp-less');
var gulpConcat = require('gulp-concat');
var gulpSourcemaps = require('gulp-sourcemaps');
var gulpMinifyCss = require('gulp-minify-css');
var gulpRename = require('gulp-rename');
gulp.task('less',function(){
  return gulp.src(paths.less)
    .pipe(gulpLess())
    .pipe(gulp.dest('./app/css'))//这个是要存放css的目录
    .pipe(gulpConcat('./app.css'))//这个是生成的css文件名
    .pipe(gulpSourcemaps.init())
    .pipe(gulpMinifyCss())
    .pipe(gulpRename({
      'suffix': '.min'
    }))
    .pipe(gulpSourcemaps.write('./'))
    .pipe(gulp.dest('./app/css'))
});
```

然后没有安装gulp的去google下安装一下

运行

`gulp less`

