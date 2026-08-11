---
title: "Yii扩展类可以放在extensions目录下面"
date: "2025-05-29 15:25:04"
slug: "yii-kuo-zhan-lei-ke-yi-fang-zai-extensions-mu-lu-xia-mian"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/05/29/Yii扩展类可以放在extensions目录下面/"
  - "/2025/05/29/Yii扩展类可以放在extensions目录下面.html"
  - "/Yii扩展类可以放在extensions目录下面/"
  - "/Yii扩展类可以放在extensions目录下面.html"
  - "/2025/05/29/yii-kuo-zhan-lei-ke-yi-fang-zai-extensions-mu-lu-xia-mian/"
  - "/2025/05/29/yii-kuo-zhan-lei-ke-yi-fang-zai-extensions-mu-lu-xia-mian.html"
  - "/yii-kuo-zhan-lei-ke-yi-fang-zai-extensions-mu-lu-xia-mian.html"
---
下面举个例子：

如果我想写个截取字符串长度的函数功能，可以在extensions目录下面新建一个文件，命名为Helper.php

代码如下：

```php
<?php
class Helper extends CController{
    public static function truncate_utf8_string($string, $length, $etc = '...') {
        $result = '';
        $string = html_entity_decode(trim(strip_tags($string)), ENT_QUOTES, 'UTF-8');
        $strlen = strlen($string);
        for ($i = 0; (($i < $strlen) && ($length > 0)); $i++){
            if ($number = strpos(str_pad(decbin(ord(substr($string, $i, 1))), 8, '0', STR_PAD_LEFT), '0')){
                if ($length < 1.0){
                    break;
                }
                $result .= substr($string, $i, $number);
                $length -= 1.0;
                $i += $number - 1;
            }else{
                $result .= substr($string, $i, 1);
                $length -= 0.5;
            }
        }
        $result = htmlspecialchars($result, ENT_QUOTES, 'UTF-8');
        if ($i < $strlen){
            $result .= $etc;
        }
        return $result;
    }
}

```

然后就可以在自己的代码中引用了`Helper::truncate_utf8_string('XXXXXXXXXXX',10,'.......');`

如果出现问题可以在`config/main.php`中加入在import引入要加载扩展的目录

类似：

```php
'import'=> array(
    'application.models.*',
    'application.components.*',
    'application.extensions.*', // 新加
    'application.extensions.yii-mail.*',
),
```
