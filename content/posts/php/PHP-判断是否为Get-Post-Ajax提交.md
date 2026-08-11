---
title: "PHP 判断是否为Get/Post/Ajax提交"
date: "2025-06-27 10:59:43"
slug: "php-pan-duan-shi-fou-wei-getpostajax-ti-jiao"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/PHP-判断是否为Get/Post/Ajax提交/"
  - "/2025/06/27/PHP-判断是否为Get/Post/Ajax提交.html"
  - "/PHP-判断是否为Get/Post/Ajax提交/"
  - "/PHP-判断是否为Get/Post/Ajax提交.html"
  - "/2025/06/27/PHP-判断是否为Get-Post-Ajax提交/"
  - "/2025/06/27/PHP-判断是否为Get-Post-Ajax提交.html"
  - "/2025/06/27/php-pan-duan-shi-fou-wei-getpostajax-ti-jiao/"
  - "/2025/06/27/php-pan-duan-shi-fou-wei-getpostajax-ti-jiao.html"
  - "/php-pan-duan-shi-fou-wei-getpostajax-ti-jiao.html"
---
PHP 判断是否为Get/Post/Ajax提交

```php
/**
 * 是否是AJAx提交的
 * @return bool
 */
function isAjax(){
    if(isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest'){
        return true;
    }else{
        return false;
    }
}

/**
 * 是否是GET提交的
 */
function isGet(){
    return $_SERVER['REQUEST_METHOD'] == 'GET' ? true : false;
}

/**
 * 是否是POST提交
 * @return int
 */
function isPost() {
    return ($_SERVER['REQUEST_METHOD'] == 'POST' && checkurlHash($GLOBALS['verify']) && (empty($_SERVER['HTTP_REFERER']) || preg_replace("~https?:\/\/([^\:\/]+).*~i", "\\1", $_SERVER['HTTP_REFERER']) == preg_replace("~([^\:]+).*~", "\\1", $_SERVER['HTTP_HOST']))) ? 1 : 0;
}
```
