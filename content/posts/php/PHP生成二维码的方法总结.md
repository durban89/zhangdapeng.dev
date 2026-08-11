---
title: "PHP生成二维码的方法总结"
date: "2025-06-20 11:07:48"
slug: "php-sheng-cheng-er-wei-ma-de-fang-fa-zong-jie"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/PHP生成二维码的方法总结/"
  - "/2025/06/20/PHP生成二维码的方法总结.html"
  - "/PHP生成二维码的方法总结/"
  - "/PHP生成二维码的方法总结.html"
  - "/2025/06/20/php-sheng-cheng-er-wei-ma-de-fang-fa-zong-jie/"
  - "/2025/06/20/php-sheng-cheng-er-wei-ma-de-fang-fa-zong-jie.html"
  - "/php-sheng-cheng-er-wei-ma-de-fang-fa-zong-jie.html"
---
### [利用google生成二维码的开放接口](#1)

代码如下：

```php
/**
 * google api 二维码生成【QRcode可以存储最多4296个字母数字类型的任意文本，具体可以查看二维码数据格式】
 * @param string $data 二维码包含的信息，可以是数字、字符、二进制信息、汉字。不能混合数据类型，数据必须经过UTF-8 URL-encoded.如果需要传递的信息超过2K个字节，请使用POST方式
 * @param int $widhtHeight 生成二维码的尺寸设置
 * @param string $EC_level 可选纠错级别，QR码支持四个等级纠错，用来恢复丢失的、读错的、模糊的、数据。
 *                         L-默认：可以识别已损失的7%的数据
 *                         M-可以识别已损失15%的数据
 *                         Q-可以识别已损失25%的数据
 *                         H-可以识别已损失30%的数据
 * @param int $margin 生成的二维码离图片边框的距离
 */
function generateQRfromGoogle($data,$widhtHeight='150',$EC_level='L',$margin='0'){
	$url=urlencode($data);
	echo '<img src="http://chart.apis.google.com/chart?chs='.$widhtHeight.'x'.$widhtHeight.'&cht=qr&chld='.$EC_level.'|'.$margin.'&chl='.$data.'" widhtHeight="'.$widhtHeight.'" widhtHeight="'.$widhtHeight.'"/>';
}
```

使用方法：

```php
$data='版权所有：http://www.gowhich.com/';
generateQRfromGoogle($data);
```

生成的二维码图片如下：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1589245057/gowhich/chart_1.png)

同时，post方法实现请求google api 生成二维码的方式如下：

```php
function generateQRfromGoogle($width,$height,$string){
	$postData=array();
	$postData['cht']='qr';
	$postData['chs']=$width."x".$height;
	$postData['chl']=$string;
	$postData['choe']="UTF-8";
	$url="http://chart.apis.google.com/chart";
	$dataArray=array();
	foreach($postData as $key=>$value){
		$dataArray[]=$key.'='.$value;
	}
	$data=implode("&",$dataArray);
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_URL, $url);    
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$result=curl_exec($ch);
	return $result;
}
```

调用的方法如下

```php
header("Content-type:image/png");
$width=300;
$height=300;
$data='版权所有：https://www.gowhich.com/';
echo generateQRfromGoogle($width,$height,$data);
```

### [使用php QR Code类库生成二维码](#2)

注意使用该类库必须首先下载类库包，下载地址：  
  
地址：http://phpqrcode.sourceforge.net/  
下载：http://sourceforge.net/projects/phpqrcode/  
  
下载下来的压缩包里面有很多示例，可以自行研究，下面给出一个简单的使用案例（具体参数的意思和上面大同小异）：

```php
<?php 
include "./phpqrcode.php";
$data='版权所有：http://www.gowhich.com/';
$errorCorrectionLevel="L";
$matrixPointSize="4";
QRcode::png($data,false,$errorCorrectionLevel,$matrixPointSize);
```
