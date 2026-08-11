---
title: "webapp iOS拍照90度旋转问题"
date: "2025-07-11 10:29:20"
slug: "webapp-ios-pai-zhao-90-du-xuan-zhuan-wen-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/07/11/webapp-iOS拍照90度旋转问题/"
  - "/2025/07/11/webapp-iOS拍照90度旋转问题.html"
  - "/webapp-iOS拍照90度旋转问题/"
  - "/webapp-iOS拍照90度旋转问题.html"
  - "/2025/07/11/webapp-ios-pai-zhao-90-du-xuan-zhuan-wen-ti/"
  - "/2025/07/11/webapp-ios-pai-zhao-90-du-xuan-zhuan-wen-ti.html"
  - "/webapp-ios-pai-zhao-90-du-xuan-zhuan-wen-ti.html"
---
通过下面这个库可以获取到在iOS下图片旋转的方向值 <http://code.ciaoca.com/javascript/exif-js/>

```js
EXIF.getData(file, function(){
  EXIF.getAllTags(this);
  var orientation = EXIF.getTag(this, 'Orientation');
  console.log(orientation);
});
```

file值的获取方式如下

```js
file = document.getElementById('imgElement');
```

或者

```js
file = event.target.files[0]
```

orientation值的说明，可参考文章 <https://blog.csdn.net/happy08god/article/details/11528479>

部分实现代码如下

```js
function handleFiles(file) {
  var orientation = null;
  EXIF.getData(file, function () {
    EXIF.getAllTags(this);
    orientation = EXIF.getTag(this, 'Orientation');
  });
  var t = this;
  var reader = new FileReader();
  reader.readAsDataURL(file);

  reader.onload = function () {
    var result = this.result;
    var img = new Image();
    img.src = result;

    img.onload = function () {
      var canvas = document.createElement("canvas");
      var ctx = canvas.getContext("2d");
      canvas.width = t.getImage.width;
      canvas.height = t.getImage.height;
      ctx.drawImage(this, 0, 0, t.getImage.width, t.getImage.height);

      switch (orientation) {
        case 6:
          //需要顺时针（向左）90度旋转
          console.log('需要顺时针（向左）90度旋转');
          t.rotateImg(this, 'left', canvas);
          result = canvas.toDataURL();
          break;

        case 8:
          //需要逆时针（向右）90度旋转
          console.log('需要逆时针（向右）90度旋转');
          t.rotateImg(this, 'right', canvas);
          result = canvas.toDataURL();
          break;

        case 3:
          //需要180度旋转
          console.log('需要180度旋转');
          t.rotateImg(this, 'right', canvas); //转两次

          t.rotateImg(this, 'right', canvas);
          result = canvas.toDataURL();
          break;
      }

      t.imgUrl = result;
      t.paintImg(result, orientation);
    };
  };
}

function rotateImg(img, direction, canvas) {
  //最小与最大旋转方向，图片旋转4次后回到原方向
  var min_step = 0;
  var max_step = 3; //var img = document.getElementById(pid);

  if (img == null) return; //img的高度和宽度不能在img元素隐藏后获取，否则会出错

  var height = img.height;
  var width = img.width; //var step = img.getAttribute('step');

  var step = 2;

  if (step == null) {
    step = min_step;
  }

  if (direction == 'right') {
    step++; //旋转到原位置，即超过最大值

    step > max_step && (step = min_step);
  } else {
    step--;
    step < min_step && (step = max_step);
  } //旋转角度以弧度值为参数

  var degree = step * 90 * Math.PI / 180;
  var ctx = canvas.getContext('2d');

  switch (step) {
    case 0:
      canvas.width = width;
      canvas.height = height;
      ctx.drawImage(img, 0, 0);
      break;

    case 1:
      canvas.width = height;
      canvas.height = width;
      ctx.rotate(degree);
      ctx.drawImage(img, 0, -height);
      break;

    case 2:
      canvas.width = width;
      canvas.height = height;
      ctx.rotate(degree);
      ctx.drawImage(img, -width, -height);
      break;

    case 3:
      canvas.width = height;
      canvas.height = width;
      ctx.rotate(degree);
      ctx.drawImage(img, -width, 0);
      break;
  }
}
```
