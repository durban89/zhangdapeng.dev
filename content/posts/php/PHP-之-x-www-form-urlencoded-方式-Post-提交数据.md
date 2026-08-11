---
title: "PHP 之 x-www-form-urlencoded 方式 Post 提交数据"
date: "2025-07-03 11:59:27"
slug: "php-zhi-x-www-form-urlencoded-fang-shi-post-ti-jiao-shu-ju"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP-之-x-www-form-urlencoded-方式-Post-提交数据/"
  - "/2025/07/03/PHP-之-x-www-form-urlencoded-方式-Post-提交数据.html"
  - "/PHP-之-x-www-form-urlencoded-方式-Post-提交数据/"
  - "/PHP-之-x-www-form-urlencoded-方式-Post-提交数据.html"
  - "/2025/07/03/php-zhi-x-www-form-urlencoded-fang-shi-post-ti-jiao-shu-ju/"
  - "/2025/07/03/php-zhi-x-www-form-urlencoded-fang-shi-post-ti-jiao-shu-ju.html"
  - "/php-zhi-x-www-form-urlencoded-fang-shi-post-ti-jiao-shu-ju.html"
---
php的curl库进行post提交还是蛮方便的。但是提交方式不同，contentType 不同导致你的api是否能接收到数据也是个变数，这里来个简单的实例。

```php
$postUrl = '';
$postData = array(
    'user_name'=>$userName,
    'identity_no'=>$idCardNo
);
$postData = http_build_query($postData);
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $postUrl);
curl_setopt($curl, CURLOPT_USERAGENT,'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // stop verifying certificate
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); 
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded'));
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
$r = curl_exec($curl); 
curl_close($curl);

print_r($r);
```

关键一段代码是

```php
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded'));
```


