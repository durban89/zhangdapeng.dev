---
title: "Gulp 实现 js、CSS,img 合并和压缩"
date: "2025-06-30 14:08:55"
slug: "gulp-shi-xian-js-cssimg-he-bing-he-ya-suo"
categories: ["技术"]
tags: ["Gulp", "JavaScript"]
aliases:
  - "/2025/06/30/Gulp-实现-js、CSS,img-合并和压缩/"
  - "/2025/06/30/Gulp-实现-js、CSS,img-合并和压缩.html"
  - "/Gulp-实现-js、CSS,img-合并和压缩/"
  - "/Gulp-实现-js、CSS,img-合并和压缩.html"
  - "/2025/06/30/Gulp-实现-js-CSS-img-合并和压缩/"
  - "/2025/06/30/Gulp-实现-js-CSS-img-合并和压缩.html"
  - "/2025/06/30/gulp-shi-xian-js-cssimg-he-bing-he-ya-suo/"
  - "/2025/06/30/gulp-shi-xian-js-cssimg-he-bing-he-ya-suo.html"
  - "/gulp-shi-xian-js-cssimg-he-bing-he-ya-suo.html"
---
前提条件，知道如何安装nodejs、gulp，这里不做介绍，可以自行google

实现此功能需要安装的gulp工具有如下

```bash
npm install gulp-htmlmin gulp-imagemin imagemin-pngcrush gulp-minify-css gulp-jshint gulp-uglify gulp-concat gulp-rename gulp-notify --save-dev
```

gulp配置文件如下

```js
//在你的项目根目录下创建gulpfile.js，代码如下：
 
// 引入 gulp
var gulp = require('gulp');
 
// 引入组件
var htmlmin = require('gulp-htmlmin'), //html压缩
    imagemin = require('gulp-imagemin'),//图片压缩
    pngcrush = require('imagemin-pngcrush'),
    minifycss = require('gulp-minify-css'),//css压缩
    jshint = require('gulp-jshint'),//js检测
    uglify = require('gulp-uglify'),//js压缩
    concat = require('gulp-concat'),//文件合并
    rename = require('gulp-rename'),//文件更名
    notify = require('gulp-notify');//提示信息
 
// 压缩html
gulp.task('html', function() {
  return gulp.src('src/*.html')
    .pipe(htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest('./dest'))
    .pipe(notify({ message: 'html task ok' }));
 
});
 
// 压缩图片
gulp.task('img', function() {
  return gulp.src('src/images/*')
    .pipe(imagemin({
        progressive: true,
        svgoPlugins: [{removeViewBox: false}],
        use: [pngcrush()]
    }))
    .pipe(gulp.dest('./dest/images/'))
    .pipe(notify({ message: 'img task ok' }));
});
 
// 合并、压缩、重命名css
gulp.task('css', function() {
  return gulp.src('src/css/*.css')
    .pipe(concat('main.css'))
    .pipe(gulp.dest('dest/css'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(minifycss())
    .pipe(gulp.dest('dest/css'))
    .pipe(notify({ message: 'css task ok' }));
});
 
// 检查js
gulp.task('lint', function() {
  return gulp.src('src/js/*.js')
    .pipe(jshint())
    .pipe(jshint.reporter('default'))
    .pipe(notify({ message: 'lint task ok' }));
});
 
// 合并、压缩js文件
gulp.task('js', function() {
  return gulp.src('src/js/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('dest/js'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify())
    .pipe(gulp.dest('dest/js'))
    .pipe(notify({ message: 'js task ok' }));
});
 
// 默认任务
gulp.task('default', function(){
  gulp.run('img', 'css', 'lint', 'js', 'html');
 
  // 监听html文件变化
  gulp.watch('src/*.html', function(){
    gulp.run('html');
  });
 
  // Watch .css files
  gulp.watch('src/css/*.css', ['css']);
 
  // Watch .js files
  gulp.watch('src/js/*.js', ['lint', 'js']);
 
  // Watch image files
  gulp.watch('src/images/*', ['img']);
});
```

执行下看看效果吧


