---
title: "利用php soap实现web service"
date: "2025-06-23 15:27:47"
slug: "li-yong-php-soap-shi-xian-web-service"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/23/利用php-soap实现web-service/"
  - "/2025/06/23/利用php-soap实现web-service.html"
  - "/利用php-soap实现web-service/"
  - "/利用php-soap实现web-service.html"
  - "/2025/06/23/li-yong-php-soap-shi-xian-web-service/"
  - "/2025/06/23/li-yong-php-soap-shi-xian-web-service.html"
  - "/li-yong-php-soap-shi-xian-web-service.html"
---
php有两个扩展可以实现web service，一个是NuSoap,一个是php 官方的soap扩展，由于soap是官方的，所以我们这里以soap来实现web service.由于默认是没有打开soap扩展的，所以自己先看一下soap扩展有没有打开。

在soap编写web service的过程中主要用到了SoapClient,SoapServer,SoapFault三个类。

### [SoapClient类](#1)

这个类用来使用Web services。SoapClient类可以作为给定Web services的客户端。  
它有两种操作形式：  
  
- \* WSDL 模式

- \* Non-WSDL 模式

在WSDL模式中，构造器可以使用WSDL文件名作为参数，并从WSDL中提取服务所使用的信息。

non-WSDL模式中使用参数来传递要使用的信息。

### [SoapServer类](#2)

这个类可以用来提供Web services。与SoapClient类似，SoapServer也有两种操作模式：WSDL模式和non-WSDL模式。这两种模式的意义跟 SoapClient的两种模式一样。在WSDL模式中，服务实现了WSDL提供的接口；在non-WSDL模式中，参数被用来管理服务的行为。  
  
在SoapServer类的众多方法中，有三个方法比较重要。它们是`SoapServer::setClass()`，`SoapServer::addFunction()`和`SoapServer::handle()`。

下面给出实例：  
定义一个提供服务的php类,这个类所提供的函数就是web service对外提供的服务

```php
<?php
class PersonInfo{
    public function getName(){
        return "My name is David";
    }
}
?>
```

服务器端的代码：

```php
<?php
require_once 'PersonInfo.php';
//wsdl方式提供web service,如果生成了wsdl文件则可直接传递到//SoapServer的构造函数中
//$s = new SoapServer('PersonInfo.wsdl');
 
//doesn't work 只有location不能提供web service
//output:looks like we got no XML document
//$s = new SoapServer(null,array("location"=>"http://localhost/Test/MyService/Server.php"));
 
//下面两种方式均可以工作，只要指定了相应的uri
//$s = new SoapServer(null,array("uri"=>"Server.php"));
$s = new SoapServer(null,array("location"=>"http://local.ubuntu.test.com/soapserver/server.php","uri"=>"server.php"));
$s->setClass("PersonInfo");
$s->handle();
?>
```

客户端代码：

```php
<?php
try{
    //wsdl方式调用web service
    //wsdl方式中由于wsdl文件写定了，如果发生添加删除函数等操作改动，不会反应到wsdl，相对non-wsdl方式
    //来说不够灵活
    //$soap = new SoapClient("http://localhost/Test/MyService/PersonInfo.wsdl");

    //non-wsdl方式调用web service    
    //在non-wsdl方式中option location是必须提供的,而服务端的location是选择性的，可以不提供
    $soap = new SoapClient(null,array('location'=>"http://local.ubuntu.test.com/soapserver/server.php",'uri'=>'server.php'));

    //两种调用方式，直接调用方法，和用__soapCall简接调用
    $result1 = $soap->getName();
    $result2 = $soap->__soapCall("getName",array());
    echo $result1."<br/>";
    echo $result2;
     
}catch(SoapFault $e){
    echo $e->getMessage();
}catch(Exception $e){
    echo $e->getMessage();
}
?>
```

输出的结果为：

```php
My name is David
My name is David
```

