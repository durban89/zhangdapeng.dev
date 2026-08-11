---
title: "PHP中Curl如何使请求的域名被解析到指定IP上"
date: "2025-07-03 17:37:46"
slug: "php-zhong-curl-ru-he-shi-qing-qiu-de-yu-ming-bei-jie-xi-dao-zhi-ding-ip-shang"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP中Curl如何使请求的域名被解析到指定IP上/"
  - "/2025/07/03/PHP中Curl如何使请求的域名被解析到指定IP上.html"
  - "/PHP中Curl如何使请求的域名被解析到指定IP上/"
  - "/PHP中Curl如何使请求的域名被解析到指定IP上.html"
  - "/2025/07/03/php-zhong-curl-ru-he-shi-qing-qiu-de-yu-ming-bei-jie-xi-dao-zhi-ding-ip-shang/"
  - "/2025/07/03/php-zhong-curl-ru-he-shi-qing-qiu-de-yu-ming-bei-jie-xi-dao-zhi-ding-ip-shang.html"
  - "/php-zhong-curl-ru-he-shi-qing-qiu-de-yu-ming-bei-jie-xi-dao-zhi-ding-ip-shang.html"
---
我们在测试的时候会遇到一个情况，就是在做上线前的接口测试的时候，想要模拟真实的环境，那么接口的域名地址是少不了的，这个情况下，我们又不想直接调用线上的数据，想通过域名跟IP的映射，调用另外一台机器上的代码【即将要上线的代码】。可以采用php中curl的参数配置来操作，具体如下：

这里的Curl使用的是ixudra/curl

简单的实例代码如下

```php
$response = Curl::to($host)
->enableDebug('/usr/local/openresty/nginx/html/api.qeeniao.com/qeeniao/storage/logs/laravel-2017-11-03.log')
->withOption('RESOLVE',['xxx.xxxx.com:443:xxx.xxx.xxx.xxx'])
->withData($params)->get();
```

其实熟悉curl的话对这个就不陌生了

```bash
curl --resolve fdh5imgcdn.oz1997.com:443:58.216.109.182
```

如果不用ixudra/curl的话，可以参照下面的代码使用，效果其实是一样的

```php
$resolve = array(sprintf(
    "%s:%d:%s", 
    $hostname,
    $port,
    $host_ip
));

$ch = curl_init($url); 
curl_setopt($ch, CURLOPT_RESOLVE, $resolve);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
$result = curl_exec($ch); 
curl_close($ch);
```
