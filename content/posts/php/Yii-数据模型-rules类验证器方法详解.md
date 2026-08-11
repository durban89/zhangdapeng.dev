---
title: "Yii 数据模型 rules类验证器方法详解"
date: "2025-06-17 18:57:05"
slug: "yii-shu-ju-mo-xing-rules-lei-yan-zheng-qi-fang-fa-xiang-jie"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/17/Yii-数据模型-rules类验证器方法详解/"
  - "/2025/06/17/Yii-数据模型-rules类验证器方法详解.html"
  - "/Yii-数据模型-rules类验证器方法详解/"
  - "/Yii-数据模型-rules类验证器方法详解.html"
  - "/2025/06/17/yii-shu-ju-mo-xing-rules-lei-yan-zheng-qi-fang-fa-xiang-jie/"
  - "/2025/06/17/yii-shu-ju-mo-xing-rules-lei-yan-zheng-qi-fang-fa-xiang-jie.html"
  - "/yii-shu-ju-mo-xing-rules-lei-yan-zheng-qi-fang-fa-xiang-jie.html"
---
rules类验证器方法，这个感觉蛮重要的，自己找资料的时候无意间发现了，感觉挺全的，记录一下好了。

解说代码如下：

```php
public function rules()
{
    return [
        ['project_id, type_id, status_id, owner_id, requester_id,', 'numerical', 'integerOnly' => true],
        ['name', 'length', 'max' => 256],
        ['description', 'length', 'max' => 2000],
        ['create_time,create_user_id,update_user_id, update_time', 'safe'],
        ['id, name, description, project_id, type_id, status_id, owner_id', 'on' => 'search'],
    ];
}
```

```php
//required: 必填
['title,content', 'required'],

//match: 正则表达式验证
['birthday', 'match', 'pattern' => '%^\d{4}(\-|\/|\.)\d{1,2}\1\d{1,2}$%', 'allowEmpty' => true, 'message' => '生日必须是年-月-日格式']，

//email:邮箱格式验证
['user_mail', 'email'],

//url:URL格式验证
['user', 'url'],

//unique:唯一性验证
['username', 'unique', 'caseSensitive' => false, 'className' => 'user', 'message' => '用户名"{value}"已经被注册，请更换']，
//caseSensitive 定义大小写是否敏感

//compare:一致性验证
['repassword', 'compare', 'compareAttribute' => 'password', 'message' => '两处输入的密码并不一致'],

//length:长度验证

//in: 验证此属性值在列表之中（通过range指定）。

//numerical: 验证此属性的值是一个数字

//captcha: 验证属性值和验证码中显示的一致
['verifyCode', 'captcha'],

//type: 验证属性的类型是否为type所指定的类型.

//file: 验证一个属性是否接收到一个有效的上传文件

//default: 属性指定默认值

//exist: 验证属性值在数据库中是否存在

//boolean: 验证布尔属性值

//date: 检验此属性是否描述了一个日期、时间或日期时间

//safe: 属性标志为在批量赋值时是安全的。

//unsafe: 标志为不安全，所以他们不能被批量赋值。
```
