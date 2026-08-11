---
title: "PHP中Curl的Post请求"
date: "2025-07-04 11:48:10"
slug: "php-zhong-curl-de-post-qing-qiu"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/04/PHP中Curl的Post请求/"
  - "/2025/07/04/PHP中Curl的Post请求.html"
  - "/PHP中Curl的Post请求/"
  - "/PHP中Curl的Post请求.html"
  - "/2025/07/04/php-zhong-curl-de-post-qing-qiu/"
  - "/2025/07/04/php-zhong-curl-de-post-qing-qiu.html"
  - "/php-zhong-curl-de-post-qing-qiu.html"
---
看代码，仔细看

```php
$postDomain = 'http://127.0.0.1:3333';
$postData = array(
    'user_name' => 'lala',
    'identity_no' => 'lala',
);
```

第一个示例

```php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $postDomain . '/api/test');
curl_setopt($curl, CURLOPT_USERAGENT, 'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); // stop verifying certificate
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLINFO_HEADER_OUT, 1);
curl_setopt($curl, CURLOPT_POST, 1); // enable posting
curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($postData)); // post images
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1); // if any redirection after upload
$r = curl_exec($curl);
curl_close($curl);
$r = json_decode($r);
var_dump($r);
```

第二个示例

```php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $postDomain . '/api/test');
curl_setopt($curl, CURLOPT_USERAGENT, 'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); // stop verifying certificate
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLINFO_HEADER_OUT, 1);
curl_setopt($curl, CURLOPT_POST, 1); // enable posting
curl_setopt($curl, CURLOPT_POSTFIELDS, $postData); // post images
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1); // if any redirection after upload
$r = curl_exec($curl);
curl_close($curl);
$r = json_decode($r);
var_dump($r);
```

好了，我们来说下区别

第一个示例请求参数默认是按照“multipart/form-data”格式进行编码的。

第二个示例请求参数默认是按照“application/x-www-form-urlencoded”进行编码的。

**特别注意:**

php的curl进行post请求的时候，只能传递一维数组作为传递的参数，那么如果想要传递多维数组需要怎么处理？有两种方式可以来处理，分别是下面的方式。

1、将多维数组进行http_build_query()进行处理

这种方式也是通过application/x-www-form-urlencoded进行编码的

2、将多维数组转换为json格式的字符串，对字符串进行application/json格式编码，在接收方通过file_get_contents("php://input")或者$GLOBALS['HTTP_RAW_POST_DATA']的方式获取传递过来的json格式的字符串，然后将json格式的字符串转换为数组进行处理。

```php
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $postDomain . '/api/test');
curl_setopt($curl, CURLOPT_USERAGENT, 'Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0); // stop verifying certificate
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLINFO_HEADER_OUT, 1);
curl_setopt($curl, CURLOPT_POST, 1); // enable posting
curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($postData)); 
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json', 'Content-Length: ' . strlen(json_encode($postData))));
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1); // if any redirection after upload
$r = curl_exec($curl);
curl_close($curl);
$r = json_decode($r);
var_dump($r);
```
