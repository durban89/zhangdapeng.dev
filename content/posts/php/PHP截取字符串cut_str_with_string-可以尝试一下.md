---
title: "PHP截取字符串cut_str_with_string 可以尝试一下"
date: "2025-06-27 14:14:37"
slug: "php-jie-qu-zi-fu-chuan-cut-str-with-string-ke-yi-chang-shi-yi-xia"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/PHP截取字符串cut-str-with-string-可以尝试一下/"
  - "/2025/06/27/PHP截取字符串cut-str-with-string-可以尝试一下.html"
  - "/PHP截取字符串cut-str-with-string-可以尝试一下/"
  - "/PHP截取字符串cut-str-with-string-可以尝试一下.html"
  - "/2025/06/27/php-jie-qu-zi-fu-chuan-cut-str-with-string-ke-yi-chang-shi-yi-xia/"
  - "/2025/06/27/php-jie-qu-zi-fu-chuan-cut-str-with-string-ke-yi-chang-shi-yi-xia.html"
  - "/php-jie-qu-zi-fu-chuan-cut-str-with-string-ke-yi-chang-shi-yi-xia.html"
---
cut_str_with_string 截取字符串，可以指定要截取的字符串的长度，指定超过指定字符截取。

```php
/**
 * 截取中文英文字符串
 * @param $str
 * @param int $length                   如果长度超过这个值，进行截取
 * @param int $start
 * @param int $end                      如果不为零，设置为指定截取字符串的长度
 * @param string $dot
 * @return mixed|string
 */
function cut_str_with_string($str, $length=200, $start=0, $special_length=0, $dot='...')
{
    $str = htmlspecialchars_decode($str);
    $str = strip_tags($str);
    $str = trim($str);
    $str = preg_replace("/\s(?=\s)/","",$str);
    $str = preg_replace("/[\n\r\t]/","",$str);
    $str = preg_replace("/\s/","",$str);
    $str = preg_replace("/&nbsp;/","",$str);

    $str = trim($str);

    $strlen = mb_strlen($str);
    $content = '';
    $sing = 0;
    $count = 0;

    if($length > $strlen) {
        return $str;
    }
    if($start >= $strlen) {
        return '';
    }

    if($special_length){
        if($length < $strlen && ($length > $special_length)){
            while($special_length != ($count-$start)){
                if(ord($str[$sing]) > 0xa0) {
                    if(!$start || $start <= $count) {
                        $content .= $str[$sing].$str[$sing+1].$str[$sing+2];
                    }
                    $sing += 3;
                    $count++;
                }else{
                    if(!$start || $start <= $count) {
                        $content .= $str[$sing];
                    }
                    $sing++;
                    $count++;
                }
            }
        }else{
            return $str;
        }
    }else{
        while($length != ($count-$start)){
            if(ord($str[$sing]) > 0xa0) {
                if(!$start || $start <= $count) {
                    $content .= $str[$sing].$str[$sing+1].$str[$sing+2];
                }
                $sing += 3;
                $count++;
            }else{
                if(!$start || $start <= $count) {
                    $content .= $str[$sing];
                }
                $sing++;
                $count++;
            }
        }
    }
    return $content.$dot;
}
```

