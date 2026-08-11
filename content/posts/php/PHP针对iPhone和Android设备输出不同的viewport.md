---
title: "PHP针对iPhone和Android设备输出不同的viewport"
date: "2025-06-13 10:13:12"
slug: "php-zhen-dui-iphone-he-android-she-bei-shu-chu-bu-tong-de-viewport"
categories: ["技术"]
tags: ["PHP", "iOS", "Android"]
aliases:
  - "/2025/06/13/PHP针对iPhone和Android设备输出不同的viewport/"
  - "/2025/06/13/PHP针对iPhone和Android设备输出不同的viewport.html"
  - "/PHP针对iPhone和Android设备输出不同的viewport/"
  - "/PHP针对iPhone和Android设备输出不同的viewport.html"
  - "/2025/06/13/php-zhen-dui-iphone-he-android-she-bei-shu-chu-bu-tong-de-viewport/"
  - "/2025/06/13/php-zhen-dui-iphone-he-android-she-bei-shu-chu-bu-tong-de-viewport.html"
  - "/php-zhen-dui-iphone-he-android-she-bei-shu-chu-bu-tong-de-viewport.html"
---
PHP针对iPhone和Android设备输出不同的viewport

```php
<?php
//if iphone
$browser = strpos($_SERVER['HTTP_USER_AGENT'], "iPhone");
if (true == $browser) {
    $browser = 'iphone';
}

//if android
$android = strpos($_SERVER['HTTP_USER_AGENT'], "Android");
if (true == $android) {
    $brower = 'android';
}
```

html模版

```php
<?php if ($browser == 'iphone') { ?>
  <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
<?php } elseif ($brower == 'android') { ?>
  <meta name="HandheldFriendly" content="true" />
  <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no" />
<?php } ?>
```
