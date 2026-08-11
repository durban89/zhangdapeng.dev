---
title: "csv文件中文乱码处理方式"
date: "2025-07-10 10:58:14"
slug: "csv-wen-jian-zhong-wen-luan-ma-chu-li-fang-shi"
categories: ["技术"]
tags: ["乱码"]
aliases:
  - "/2025/07/10/csv文件中文乱码处理方式/"
  - "/2025/07/10/csv文件中文乱码处理方式.html"
  - "/csv文件中文乱码处理方式/"
  - "/csv文件中文乱码处理方式.html"
  - "/2025/07/10/csv-wen-jian-zhong-wen-luan-ma-chu-li-fang-shi/"
  - "/2025/07/10/csv-wen-jian-zhong-wen-luan-ma-chu-li-fang-shi.html"
  - "/csv-wen-jian-zhong-wen-luan-ma-chu-li-fang-shi.html"
---
日常开发中总会遇到一些下载文件，然后通过程序处理文件内容的功能，因此也会遇到，读取后的内容不能达到我们的要求，比如从csv文件中读取到的中文是乱码，处理方式如下

```php
function getFileContent($file) {

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

  return $content;
}
```

输入文件的路径，获取文件正确的中文内容，此函数适合于csv文件，其他文件雷同。

```php
$file = '/dd/ddd/ddd/ddd.csv';
getFileContent($file);
```
