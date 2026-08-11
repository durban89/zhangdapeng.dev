---
title: "CURL模拟登录新浪微博"
date: "2025-06-10 10:44:49"
slug: "curl-mo-ni-deng-lu-xin-lang-wei-bo"
categories: ["技术"]
tags: ["CURL"]
aliases:
  - "/2025/06/10/CURL模拟登录新浪微博/"
  - "/2025/06/10/CURL模拟登录新浪微博.html"
  - "/CURL模拟登录新浪微博/"
  - "/CURL模拟登录新浪微博.html"
  - "/2025/06/10/curl-mo-ni-deng-lu-xin-lang-wei-bo/"
  - "/2025/06/10/curl-mo-ni-deng-lu-xin-lang-wei-bo.html"
  - "/curl-mo-ni-deng-lu-xin-lang-wei-bo.html"
---
使用curl登录很简单，关键是破解它的加密方式

这个加密方式是如何破解的，我才用的是nodejs的方式，直接执行里面的js的函数，让他自己进行加密解密，除掉了自己浪费时间去解密的方法

搭建nodejs，然后自己调用接口去传递参数解密，这个过程我写在了我的一篇文章里面 [nodejs搭建web服务器](https://www.gowhich.com/blog/49) ,其实就是我的一个解密的接口，可以按照此方法进行搭建。

下面给出，最简单的部分，就是使用curl获取新浪微博的cookie

这里给出我的代码：

```php
<?php
class Control
{

    /**
     * 获取新浪微博的登录的加密数据
     * */
    public static function getEntryData($servertime, $nonce, $password)
    {
        return self::curlRequest('http://xxx.xxx.xxx.xxx:8006/weibo?servertime=' . $servertime . '&nonce=' . $nonce . '&password=' . $password, '', '');
        // return self::curlRequest('http://10.211.55.5:8006/weibo?servertime='.$servertime.'&nonce='.$nonce.'&password='.$password,'','');
    }

    /**
     * CURL请求 辅助登录的
     * @param String $url 请求地址
     * @param Array $data 请求数据
     */
    public static function curlRequest($url, $data = '', $cookieFile = '')
    {
        $ch = curl_init();
        $option = [
            CURLOPT_URL => $url,
            CURLOPT_HEADER => 0,
            CURLOPT_RETURNTRANSFER => 1,
            CURLOPT_HTTPHEADER => ['Expect:'],
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_USERAGENT => 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
        ];
        if ($cookieFile) {
            $option[CURLOPT_COOKIEJAR] = $cookieFile;
            $option[CURLOPT_COOKIEFILE] = $cookieFile;
        }
        if ($data) {
            $option[CURLOPT_POST] = 1;
            $option[CURLOPT_POSTFIELDS] = $data;
        }

        curl_setopt_array($ch, $option);
        $response = curl_exec($ch);
        if (curl_errno($ch) > 0) {
            //echo "CURL ERROR:$url ".curl_error($ch);
        }
        curl_close($ch);
        return $response;
    }

    /**
     *
     * 微博登录
     * @param string $username
     * @param string $password
     * @param string $cookie_file
     */
    public static function loginWeibo($username, $password, $cookie_file)
    {

        if (!empty($username) && !empty($password)) {
            $preLoginData = self::curlRequest('http://login.sina.com.cn/sso/prelogin.php?entry=account&callback=sinaSSOController.preloginCallBack&su=' . base64_encode($username) . '&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.5)', '', $cookie_file);

            preg_match('/sinaSSOController.preloginCallBack\((.*)\)/', $preLoginData, $preArr);
            $jsonArr = json_decode($preArr[1], true);

            if (is_array($jsonArr)) {
                $postArr = [
                    'entry' => 'weibo',
                    'gateway' => 1,
                    'from' => '',
                    'savestate' => 7,
                    'useticket' => 1,
                    'pagerefer' => '',
                    'vsnf' => 1,
                    'su' => base64_encode(urlencode($username)),
                    'service' => 'sso',
                    'servertime' => $jsonArr['servertime'],
                    'nonce' => $jsonArr['nonce'],
                    'pwencode' => 'rsa2',
                    'rsakv' => $jsonArr['rsakv'],
                    'prelt' => 0,
                    'sp' => self::getEntryData($jsonArr['servertime'], $jsonArr['nonce'], $password),
                    'encoding' => 'UTF-8',
                    'url' => 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    'returntype' => 'META',
                ];

                $loginData = self::curlRequest('http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)', $postArr, $cookie_file);

                if ($loginData) {
                    $matchs = [];
                    preg_match('/replace\([\'|\"](.*?)[\'|\"]\)/', $loginData, $matchs);

                    $loginResult = self::curlRequest($matchs[1], '', $cookie_file);

                    $loginResultArr = [];
                    preg_match('/feedBackUrlCallBack\((.*?)\)/', $loginResult, $loginResultArr);

                    if (!empty($loginResultArr[1])) {
                        $userInfo = json_decode($loginResultArr[1]);

                        if ($userInfo->result) {
                            // echo "Login Success \n";
                            //throw new Exception('Login Success');
                        }
                    } else {
                        // echo "Login Failure \n";
                        //throw new Exception('Login Failure');
                    }
                } else {
                    //echo "Login SinaWeibo Failure \n";
                    //throw new Exception('Login SinaWeibo Failure');
                }
            } else {
                //echo "preLoginData \n";
                //throw new Exception("$preLoginData");
            }
        } else {
            //echo "Param Error. \n";
            //throw new Exception('Param Error.');
        }
    }
}
```

获取加密的部分，其实我已经在我的上篇博文写过了，可以参考一下 [nodejs搭建web服务器](https://www.gowhich.com/blog/49)
