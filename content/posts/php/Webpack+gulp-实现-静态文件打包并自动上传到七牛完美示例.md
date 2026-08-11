---
title: "Webpack+Gulp 实现 静态文件打包并自动上传到七牛完美示例"
date: "2025-07-02 15:40:19"
slug: "webpackgulp-shi-xian-jing-tai-wen-jian-da-bao-bing-zi-dong-shang-chuan-dao-qi-niu-wan-mei-shi-li"
categories: ["技术"]
tags: ["Gulp", "Webpack"]
aliases:
  - "/2025/07/02/Webpack+Gulp-实现-静态文件打包并自动上传到七牛完美示例/"
  - "/2025/07/02/Webpack+Gulp-实现-静态文件打包并自动上传到七牛完美示例.html"
  - "/Webpack+Gulp-实现-静态文件打包并自动上传到七牛完美示例/"
  - "/Webpack+Gulp-实现-静态文件打包并自动上传到七牛完美示例.html"
  - "/2025/07/02/Webpack+gulp-实现-静态文件打包并自动上传到七牛完美示例/"
  - "/2025/07/02/Webpack+gulp-实现-静态文件打包并自动上传到七牛完美示例.html"
  - "/2025/07/02/webpackgulp-shi-xian-jing-tai-wen-jian-da-bao-bing-zi-dong-shang-chuan-dao-qi-niu-wan-m/"
  - "/2025/07/02/webpackgulp-shi-xian-jing-tai-wen-jian-da-bao-bing-zi-dong-shang-chuan-dao-qi-niu-w.html"
  - "/webpackgulp-shi-xian-jing-tai-wen-jian-da-bao-bing-zi-dong-shang-chuan-dao-qi-niu-wan-mei-shi-.html"
---
经过几天的努力终于实现了一个完美的作品，webpack可以与gulp完美结合的进行打包静态文件，并将静态文件上传到七牛云存储，当然也可以传到你想传的云存储了，这里只分享一个七牛的云存储方案。

关于如何使用webpack打包静态代码，这个可以参考我之前的一些文章和方案，不行的话可以进群交流。

这里只分享一下gulp这边的操作，然后给一个例子实现如何一条命令打包静态文件并更新cdn文件的方法。

先展示一下gulpfile.js文件

```javascript
const gulp = require('gulp');
const uglify = require('gulp-uglify');
const concat = require('gulp-concat');
const shrink = require('gulp-cssshrink');
const webpack = require('gulp-webpack');
const qn = require('gulp-qn');
// MD5戳
const rev = require('gulp-rev-qn');
const revCollector = require('gulp-rev-collector');
const runSequence = require('run-sequence');
const config = require('./webpack.config');
const qiniu_options = {
  accessKey: 'xxx',
  secretKey: 'xxx',
  bucket: 'xxx',
  domain: 'http://xxx.com'
};
gulp.task('publish-js', function () {
  return gulp.src(['./build/js/*.js'])
    .pipe(uglify())
    .pipe(rev())
    .pipe(gulp.dest('./build/js'))
    .pipe(qn({
      qiniu: qiniu_options,
      prefix: 'js'
    }))
    .pipe(rev.manifest())
    .pipe(gulp.dest('./build/rev/js'));
});
gulp.task('publish-font-img', function () {
  return gulp.src(['./build/js/*.svg','./build/js/*.gif','./build/js/*.woff2','./build/js/*.ttf','./build/js/*.eot','./build/js/*.woff'])
    .pipe(qn({
      qiniu: qiniu_options,
      prefix: 'js'
    }));
});
gulp.task('publish-css', function () {
  return gulp.src(['./build/js/*.css'])
    .pipe(rev())
    .pipe(gulp.dest('./build/js'))
    .pipe(qn({
      qiniu: qiniu_options,
      prefix: 'css'
    }))
    .pipe(rev.manifest())
    .pipe(gulp.dest('./build/rev/css'));
});
gulp.task('publish-html', function () {
  return gulp.src(['./build/rev/**/*.json', './build/views/*.html'])
    .pipe(revCollector({
      dirReplacements: {
        '/js/': ''
      }
    }))
    .pipe(gulp.dest('./build/views'));
});
gulp.task('default',function(callback){
  runSequence(
    ['publish-css','publish-js','publish-font-img'],
    'publish-html',
    callback);
});
```

publish-js部分是将我的js文件进行版本更新并上传到七牛。

publish-font-img部分是将我的字体文件、图片文件上传到七牛

publish-css部分是将我的css文件进行版本更新并上传到七牛

publish-html将我html文件中对应的js路径进行替换，好了，可以直接发布这个build文件夹下的文件了。

