---
title: "Yii中使用session和cookie"
date: "2025-06-20 14:33:36"
slug: "yii-zhong-shi-yong-session-he-cookie"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii中使用session和cookie/"
  - "/2025/06/20/Yii中使用session和cookie.html"
  - "/Yii中使用session和cookie/"
  - "/Yii中使用session和cookie.html"
  - "/2025/06/20/yii-zhong-shi-yong-session-he-cookie/"
  - "/2025/06/20/yii-zhong-shi-yong-session-he-cookie.html"
  - "/yii-zhong-shi-yong-session-he-cookie.html"
---
### [在Yii中使用session](#1)

1，CHttpSession  
与原生态php5的session使用差别是，php5使用session\_start();$\_session['key'] = $value;  
在yii中，session已经被封装。  
To start the session, call open(); To complete and send out session data, call close(); To destroy the session, call destroy().  
  
If autoStart is set true, the session will be started automatically when the application component is initialized by the application.

/\*\*\*\*\* 方式一、实例添加 \*\*\*\*\*/

```php
$session=new CHttpSession;  
$session->open();  
$value1=$session['name1'];  
```

/\*\*\*\*\* 方式二、直接调用应用添加 \*\*\*\*\*/

```php
Yii::app()->session->add('name','foobar');  
Yii::app()->session->add('name2','foobar');  
Yii::app()->session->add('name3','foobar');  
```

或者

```php
$session = Yii::app()->session;  
$session['key'] = 'value';  
var_dump($session['key']);  
```

遍历

```php
foreach($session as $name=>$value)
```

一个实例，

```php
$session = new CHttpSession;  
$session->open();  
          
$user_id = $this->user->id;  
$sessionKey = $user_id.'_is_sending';  
          
if(isset($session[$sessionKey])){  
    $first_submit_time = $session[$sessionKey];  
    $current_time      = time();  
    if($current_time - $first_submit_time < 10){  
        $session[$sessionKey] = $current_time;  
        $this->response(array('status'=>1, 'msg'=>'不能在10秒钟内连续发送两次。'));  
    }else{  
        unset($session[$sessionKey]);//超过限制时间，释放session";  
    }  
}  
  
//第一次点击确认按钮时执行  
if(!isset($session[$sessionKey])){  
    $session[$sessionKey] = time();  
}  
          
var_dump($sessionKey);
var_dump($session[$sessionKey]);
exit();
```

在index.php  
在$app->run();前

```php
$session = Yii::app()->session;  
session_set_save_handler(  
    array($session,'openSession'),  
    array($session,'closeSession'),  
    array($session,'readSession'),  
    array($session,'writeSession'),  
    array($session,'destroySession'),  
    array($session,'gcSession')  
);
```

2，CDbHttpSession  
CDbHttpSession继承自 CHttpSession ，把session数据存储在数据库中（表名是YiiSession），  
The table name can be changed by setting sessionTableName. If the table does not exist, it will be automatically created if autoCreateSessionTable is set true.

```sql
#The following is the table structure:
CREATE TABLE YiiSession
(
    id CHAR(32) PRIMARY KEY,
    expire INTEGER,
    data TEXT
)
```

CDbHttpSession relies on PDO to access database.  
  
By default, it will use an SQLite3 database named 'session-YiiVersion.db' under the application runtime directory. You can also specify connectionID so that it makes use of a DB application component to access database.  
  
When using CDbHttpSession in a production server, we recommend you pre-create the session DB table and set autoCreateSessionTable to be false. This will greatly improve the performance. You may also create a DB index for the 'expire' column in the session table to further improve the performance.

```sql
CREATE TABLE `YiiSession` (  
  `id` char(32) NOT NULL,  
  `expire` int(11) default NULL,  
  `data` text,  
  PRIMARY KEY  (`id`),  
  KEY `expire` (`expire`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

例，在../config/main.php中配置

```php
'session'=>array(  
    'class' => 'CDbHttpSession',  
    'autoStart' => true,  
    'sessionTableName'=>'YiiSession',  
    'autoCreateSessionTable'=> false,  
    'connectionID'=>'db',  
),
```

### [在Yii中使用cookie](#2)

Yii实现了一个cookie验证机制，可以防止cookie被修改。启用之后可以对cookie的值进行HMAC检查。  
Cookie验证在默认情况下是禁用的。如果你要启用它，可以编辑应用配置 中的组件中的CHttpRequest部分。  
一定要使用经过Yii验证过的cookie数据。使用Yii内置的cookies组件来进行cookie操作，不要使用$\_COOKIES。  
实例：

```php
// 检索一个名为$name的cookie值  
$cookie=Yii::app()->request->cookies[$name];  
$value=$cookie->value;  
......  
// 设置一个cookie  
$cookie=new CHttpCookie($name,$value);  
Yii::app()->request->cookies[$name]=$cookie;
```

