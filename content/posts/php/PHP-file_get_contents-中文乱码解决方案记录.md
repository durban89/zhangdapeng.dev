---
title: "PHP file_get_contents 中文乱码解决方案记录"
date: "2025-07-10 10:57:58"
slug: "php-file-get-contents-zhong-wen-luan-ma-jie-jue-fang-an-ji-lu"
categories: ["技术"]
tags: ["PHP", "乱码"]
aliases:
  - "/2025/07/10/PHP-file-get-contents-中文乱码解决方案记录/"
  - "/2025/07/10/PHP-file-get-contents-中文乱码解决方案记录.html"
  - "/PHP-file-get-contents-中文乱码解决方案记录/"
  - "/PHP-file-get-contents-中文乱码解决方案记录.html"
  - "/2025/07/10/php-file-get-contents-zhong-wen-luan-ma-jie-jue-fang-an-ji-lu/"
  - "/2025/07/10/php-file-get-contents-zhong-wen-luan-ma-jie-jue-fang-an-ji-lu.html"
  - "/php-file-get-contents-zhong-wen-luan-ma-jie-jue-fang-an-ji-lu.html"
---
最近拉取了京东结算订单csv文件，结果发现在用file\_get\_contents获取内容的时候，中文出现了乱码，感觉京东这么大，这个技术问题他们帮忙解决才好吧，想想还是算了，自己动动手的问题。

大概我也能猜到，京东的系统默认应该都不是utf-8的编码，大多数还是gbk或者是gb2312，因为之前使用过类似的国内产品，可能是由于历史原因，这个不深究了，

解决代码逻辑如下

```php
$content = '';
$text = file_get_contents($file);

//$encodType = mb_detect_encoding($text);
define('UTF32_BIG_ENDIAN_BOM', chr(0x00) . chr(0x00) . chr(0xFE) . chr(0xFF));
define('UTF32_LITTLE_ENDIAN_BOM', chr(0xFF) . chr(0xFE) . chr(0x00) . chr(0x00));
define('UTF16_BIG_ENDIAN_BOM', chr(0xFE) . chr(0xFF));
define('UTF16_LITTLE_ENDIAN_BOM', chr(0xFF) . chr(0xFE));
define('UTF8_BOM', chr(0xEF) . chr(0xBB) . chr(0xBF));
$first2 = substr($text, 0, 2);
$first3 = substr($text, 0, 3);
$first4 = substr($text, 0, 3);
$encodType = "";
if (UTF8_BOM == $first3) {
    $encodType = 'UTF-8 BOM';
} else if (UTF32_BIG_ENDIAN_BOM == $first4) {
    $encodType = 'UTF-32BE';
} else if (UTF32_LITTLE_ENDIAN_BOM == $first4) {
    $encodType = 'UTF-32LE';
} else if (UTF16_BIG_ENDIAN_BOM == $first2) {
    $encodType = 'UTF-16BE';
} else if (UTF16_LITTLE_ENDIAN_BOM == $first2) {
    $encodType = 'UTF-16LE';
}

//下面的判断主要还是判断ANSI编码的·
if ('' == $encodType) {
    //即默认创建的txt文本-ANSI编码的
    $content = iconv("GBK", "UTF-8", $text);
} else if ('UTF-8 BOM' == $encodType) {
    //本来就是UTF-8不用转换
    $content = $text;
} else {
    //其他的格式都转化为UTF-8就可以了
    $content = iconv($encodType, "UTF-8", $text);
}
```
