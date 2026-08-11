---
title: "canvas图片压缩"
date: "2025-07-11 10:29:04"
slug: "canvas-tu-pian-ya-suo"
categories: ["技术"]
tags: ["Canvas"]
aliases:
  - "/2025/07/11/canvas图片压缩/"
  - "/2025/07/11/canvas图片压缩.html"
  - "/canvas图片压缩/"
  - "/canvas图片压缩.html"
  - "/2025/07/11/canvas-tu-pian-ya-suo/"
  - "/2025/07/11/canvas-tu-pian-ya-suo.html"
  - "/canvas-tu-pian-ya-suo.html"
---
canvas生成图片的方法，我们通过官方教程都能简单的生成，但是我遇到的情况是，在生成的过程中，图片有点大，其实图片大也没什么问题，但是要知道图片大的话上传是比较消耗时间和流量的，所以对于大尺寸的图片还是要进行下压缩比较好

正常生成图片我们可以配置参数

```js
canvas.toDataURL("image/jpeg", quality);
```

**image/jpeg**

可以替换为 *image/png* 或者 *image/webp*

不过 *image/webp* 格式的话ios好像默认情况下是不支持的

**quality** 是一个*0-1*的值，具体值为多少可以根据情况来设定

有了上面的方法我们就可以根据这个思路进行压缩，方法如下

```js
/**
 * @param base64 为64位编码的图片数据
 * @param w 要压缩的图片的宽度
 * @param calback 回掉函数
 */
function dealImage (base64, w, callback) {
  var newImage = new Image();
  var quality = 1; //压缩系数0-1之间
  newImage.src = base64;
  newImage.setAttribute("crossOrigin", 'Anonymous'); // url为外域时需要
  var imgWidth, imgHeight;
  newImage.onload = function () {
    imgWidth = this.width;
    imgHeight = this.height;
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    if (Math.max(imgWidth, imgHeight) > w) {
      if (imgWidth > imgHeight) {
        canvas.width = w;
        canvas.height = w * imgHeight / imgWidth;
      } else {
        canvas.height = w;
        canvas.width = w * imgWidth / imgHeight;
      }
    } else {
      canvas.width = imgWidth;
      canvas.height = imgHeight;
      quality = 1;
    }
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(this, 0, 0, canvas.width, canvas.height);
    var base64 = canvas.toDataURL("image/jpeg", quality); //压缩语句

    callback(base64);
  }
}
```
