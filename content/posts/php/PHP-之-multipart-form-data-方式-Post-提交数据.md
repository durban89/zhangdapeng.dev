---
title: "PHP 之 multipart/form-data 方式 Post 提交数据"
date: "2025-07-03 11:59:30"
slug: "php-zhi-multipartform-data-fang-shi-post-ti-jiao-shu-ju"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP-之-multipart/form-data-方式-Post-提交数据/"
  - "/2025/07/03/PHP-之-multipart/form-data-方式-Post-提交数据.html"
  - "/PHP-之-multipart/form-data-方式-Post-提交数据/"
  - "/PHP-之-multipart/form-data-方式-Post-提交数据.html"
  - "/2025/07/03/PHP-之-multipart-form-data-方式-Post-提交数据/"
  - "/2025/07/03/PHP-之-multipart-form-data-方式-Post-提交数据.html"
  - "/2025/07/03/php-zhi-multipartform-data-fang-shi-post-ti-jiao-shu-ju/"
  - "/2025/07/03/php-zhi-multipartform-data-fang-shi-post-ti-jiao-shu-ju.html"
  - "/php-zhi-multipartform-data-fang-shi-post-ti-jiao-shu-ju.html"
---
post的curl库，模拟post提交的时候，默认的方式 multipart/form-data ，这个算是post提交的几个基础的实现方式。

```php
$postUrl = '';
$postData = array(
    'user_name'=>$userName,
    'identity_no'=>$idCardNo
);

$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $postUrl);
curl_setopt($curl, CURLOPT_USERAGENT,'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // stop verifying certificate
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true); 
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);
$r = curl_exec($curl); 
curl_close($curl);

print_r($r);
```


