---
title: "CSS实现图片旋转（原地转圈）"
date: "2025-07-14 14:44:42"
slug: "css-shi-xian-tu-pian-xuan-zhuan-yuan-di-zhuan-quan"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/07/14/CSS实现图片旋转（原地转圈）/"
  - "/2025/07/14/CSS实现图片旋转（原地转圈）.html"
  - "/CSS实现图片旋转（原地转圈）/"
  - "/CSS实现图片旋转（原地转圈）.html"
  - "/2025/07/14/CSS实现图片旋转-原地转圈/"
  - "/2025/07/14/CSS实现图片旋转-原地转圈.html"
  - "/2025/07/14/css-shi-xian-tu-pian-xuan-zhuan-yuan-di-zhuan-quan/"
  - "/2025/07/14/css-shi-xian-tu-pian-xuan-zhuan-yuan-di-zhuan-quan.html"
  - "/css-shi-xian-tu-pian-xuan-zhuan-yuan-di-zhuan-quan.html"
---
css能让图片转动起来，而且很简单，适用的场景包括音频是否在播放

如果视频播放的时候我们就让图片转圈，而且想转的快或者慢都可以加以控制。

代码示例如下

css code

```css
@-webkit-keyframes rotation{
  from {-webkit-transform: rotate(0deg);}
  to {-webkit-transform: rotate(360deg);}
}

.img-rotate{
  -webkit-transform: rotate(360deg);
  animation: rotation 1.4s linear infinite;
  -moz-animation: rotation 1.4s linear infinite;
  -webkit-animation: rotation 1.4s linear infinite;
  -o-animation: rotation 1.4s linear infinite;
}
```

html code

```html
<div style='60px'>
  <img v-if='audioPlayStatus==true' class="img-rotate" src="https://xxxx.com/audio_start_play.png" style="width: 100%" />
</div>
```
