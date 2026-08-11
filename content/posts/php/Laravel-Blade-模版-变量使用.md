---
title: "Laravel Blade 模版 变量使用"
date: "2025-07-03 11:07:56"
slug: "laravel-blade-mo-ban-bian-liang-shi-yong"
categories: ["技术"]
tags: ["Laravel", "Blade"]
aliases:
  - "/2025/07/03/Laravel-Blade-模版-变量使用/"
  - "/2025/07/03/Laravel-Blade-模版-变量使用.html"
  - "/Laravel-Blade-模版-变量使用/"
  - "/Laravel-Blade-模版-变量使用.html"
  - "/2025/07/03/laravel-blade-mo-ban-bian-liang-shi-yong/"
  - "/2025/07/03/laravel-blade-mo-ban-bian-liang-shi-yong.html"
  - "/laravel-blade-mo-ban-bian-liang-shi-yong.html"
---
Laravel Blade模版对于我这样的初玩者来说，确实有点挑战。

习惯了，django的直接定义函数就能直接使用的方法，在Blade中还是没有找到如何使用，这里简单介绍下我自己查到的使用方法。

起始Laravel的Blade是支持php的原生写法的，比如我有个输出的变量，是需要进行逻辑判断在输出的。

```php
<?php $heading = '/images/default.png'; ?>
@if($user->headimg)
  @if(strncmp($user->headimg,'http://',strlen('http://')) == 0)
  <?php $heading = $user->headimg; ?>
  @else
  <?php $headimg = "http://7u2r0u.com1.z0.glb.clouddn.com/" . $user->headimg; ?>
  @endif
@endif
```

就这样我就可以实现了定义变量，在使用变量的方便

```php
<a href={{ $headimg }} class="fancybox" data-fancybox-type="image">
  <img class="img-circle" src={{ $headimg }}
       style='width:32px;height:32px'}}/>
</a>
```


