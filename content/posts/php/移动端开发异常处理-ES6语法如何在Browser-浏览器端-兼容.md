---
title: "移动端开发异常处理-ES6语法如何在Browser（浏览器端）兼容"
date: "2025-07-11 11:16:22"
slug: "yi-dong-duan-kai-fa-yi-chang-chu-li-es6-yu-fa-ru-he-zai-browser-liu-lan-qi-duan-jian-rong"
categories: ["技术"]
tags: ["移动端", "ES6"]
aliases:
  - "/2025/07/11/移动端开发异常处理-ES6语法如何在Browser（浏览器端）兼容/"
  - "/2025/07/11/移动端开发异常处理-ES6语法如何在Browser（浏览器端）兼容.html"
  - "/移动端开发异常处理-ES6语法如何在Browser（浏览器端）兼容/"
  - "/移动端开发异常处理-ES6语法如何在Browser（浏览器端）兼容.html"
  - "/2025/07/11/移动端开发异常处理-ES6语法如何在Browser-浏览器端-兼容/"
  - "/2025/07/11/移动端开发异常处理-ES6语法如何在Browser-浏览器端-兼容.html"
  - "/2025/07/11/yi-dong-duan-kai-fa-yi-chang-chu-li-es6-yu-fa-ru-he-zai-browser-liu-lan-qi-duan-jian-ro/"
  - "/2025/07/11/yi-dong-duan-kai-fa-yi-chang-chu-li-es6-yu-fa-ru-he-zai-browser-liu-lan-qi-duan-jia.html"
  - "/yi-dong-duan-kai-fa-yi-chang-chu-li-es6-yu-fa-ru-he-zai-browser-liu-lan-qi-duan-jian-rong.html"
---
移动端开发或者是浏览器都会遇到这个问题，尤其是最近几年ES6语法比较流行，很多浏览器也都支持了，但是很多用户并没有将浏览器更新到最新版本，这样就会遇到一个显示的问题，不支持ES6语法的不支持，如果是在开发中使用的打包工具的话，如webpack等，也许这个问题还要解决，在打包过程中使用babel工具，便可以自动的将需要的es6语法转译为es5语法，从而完美的解决兼容性，但是往往我们在开发的过程中，总是避免不了需要进行简单的页面开发，那么就没必要进行复杂的工具配置，比如webpack等的配置，因为开发前期还是比较费时间的。当然也有很多的工具都是现成的，只需要npm install一下，然后执行对应的命令就可以，连webpack都不需要进行配置，那么这个时候是不是还要进行安装，如果网络好的话，或许能立刻开工进行开发，但是网络不好估计半天的时间就没有了。所以我们看下如何在浏览器下进行兼容呢

有了这个库，也许会解决这个问题，至少我是这么干的，也许适合你，能够帮你解决es6中promise的问题

下面是ES6的项目地址 <https://github.com/stefanpenner/es6-promise>

### Downloads

[es6-promise 27.86 KB (7.33 KB gzipped)](https://cdn.jsdelivr.net/npm/es6-promise/dist/es6-promise.js) [es6-promise-auto 27.78 KB (7.3 KB gzipped)](https://cdn.jsdelivr.net/npm/es6-promise/dist/es6-promise.auto.js) - Automatically provides/replaces Promise if missing or broken. [es6-promise-min 6.17 KB (2.4 KB gzipped)](https://cdn.jsdelivr.net/npm/es6-promise/dist/es6-promise.min.js) [es6-promise-auto-min 6.19 KB (2.4 KB gzipped)](https://cdn.jsdelivr.net/npm/es6-promise/dist/es6-promise.auto.min.js) - Minified version of es6-promise-auto above.

### CDN

```html
<!-- Automatically provides/replaces `Promise` if missing or broken. -->
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.js"></script>
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.auto.js"></script> 

<!-- Minified version of `es6-promise-auto` below. -->
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.auto.min.js"></script>
```

说下实际情况下如何使用

将下面的代码放在所有js引入入口的最前面（或者按需来操作也行）

```html
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.auto.min.js"></script>
```

然后下面这种带有then语法的就能解决了

```javascript
axios.post('/api/activity/qrj/buy', {
  id: gift.img_id || gift.id || 0,
  user_star_autokid: autokid,
}).then(function (response) {
  // ...
}).catch(function (error) {
  // ...
});
html2canvas(document.querySelector("#canvas-container"), {
  dpi: window.devicePixelRatio,
  useCORS: true,
  width: window.document.body.offsetWidth,   //获取当前网页的宽度
  height: offsetHeight, //获取当前网页的高度
  windowWidth: document.body.scrollWidth,     //获取X方向滚动条内容
  windowHeight: windowHeight, //获取Y方向滚动条内容
  x: 0,
  y: offset,
}).then(function(canvas){
  // var urlBase64Data = canvas.toDataURL('image/webp', 0.8);
  // ...
}).catch(function(e){
  // ...
});
```

html2canvas兼容ES6的使用说明详见：<https://www.javascripting.com/view/html2canvas>

### Polyfill(也许你需要)

我是没有找到具体的项目下载地址

唯一我找到能在浏览器中直接使用的源文件是在[这里](https://registry.npm.taobao.org/@babel/polyfill/download/@babel/polyfill-7.8.3.tgz)，版本可能会过期

你可以通过下面的安装命令获取到

```bash
npm install --save @babel/polyfill
```

然后在node\_modules目录下面[babel/polyfill](https://github.com/babel/polyfill "GitHub Repository: babel/polyfill")/dist目录下面，即`node_modules/@babel/polyfill/dist`，一般会有两个文件

```bash
polyfill.js
polyfill.min.js
```

选择自己需要的就可以了。
