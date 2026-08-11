---
title: "让Bootstrap的Refresh Icon也spin起来"
date: "2025-07-03 11:08:13"
slug: "rang-bootstrap-de-refresh-icon-ye-spin-qi-lai"
categories: ["技术"]
tags: ["Bootstrap"]
aliases:
  - "/2025/07/03/让Bootstrap的Refresh-Icon也spin起来/"
  - "/2025/07/03/让Bootstrap的Refresh-Icon也spin起来.html"
  - "/让Bootstrap的Refresh-Icon也spin起来/"
  - "/让Bootstrap的Refresh-Icon也spin起来.html"
  - "/2025/07/03/rang-bootstrap-de-refresh-icon-ye-spin-qi-lai/"
  - "/2025/07/03/rang-bootstrap-de-refresh-icon-ye-spin-qi-lai.html"
  - "/rang-bootstrap-de-refresh-icon-ye-spin-qi-lai.html"
---
bootstrap下面有个glyphicon-refresh，但是不会自定动态spin[旋转]，下面提供下我的实例

```css
.spin{
    -webkit-transform-origin: 50% 50%;
    transform-origin:50% 50%;
    -ms-transform-origin:50% 50%; /* IE 9 */
    -webkit-animation: spin .8s infinite linear;
    -moz-animation: spin .8s infinite linear;
    -o-animation: spin .8s infinite linear;
    animation: spin .8s infinite linear;
  }

  @-webkit-keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
  @keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(359deg);
      transform: rotate(359deg);
    }
  }
```

调用方式如下

```html
<span class="glyphicon glyphicon-refresh loading spin"> </span>
```


