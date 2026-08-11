---
title: "Yii CDbCriteria 条件查询 常用用法"
date: "2025-06-20 14:13:31"
slug: "yii-cdbcriteria-tiao-jian-cha-xun-chang-yong-yong-fa"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii-CDbCriteria-条件查询-常用用法/"
  - "/2025/06/20/Yii-CDbCriteria-条件查询-常用用法.html"
  - "/Yii-CDbCriteria-条件查询-常用用法/"
  - "/Yii-CDbCriteria-条件查询-常用用法.html"
  - "/2025/06/20/yii-cdbcriteria-tiao-jian-cha-xun-chang-yong-yong-fa/"
  - "/2025/06/20/yii-cdbcriteria-tiao-jian-cha-xun-chang-yong-yong-fa.html"
  - "/yii-cdbcriteria-tiao-jian-cha-xun-chang-yong-yong-fa.html"
---
$criteria = new CDbCriteria;

### [addCondition() 方法](#1)

```php
public CDbCriteria addCondition(mixed $condition, string $operator='AND')
```

```php
$criteria->addCondition("id = :id");
$criteria->addCondition('id=1','OR');
$criteria->params[':id']=1;
```

### [addInCondition() 方法](#2)

```php
public CDbCriteria addInCondition(string $column, array $values, string $operator='AND')
```

```php
$criteria->addInCondition('id', array(1, 2, 3));
```

### [addNotInCondition() 方法](#3)

```php
public CDbCriteria addNotInCondition(string $column, array $values, string $operator='AND')
```

```php
$criteria->addNotInCondition(‘id’, array(1, 2, 3));
```

### [addSearchCondition() 方法](#4)

```php
public CDbCriteria addSearchCondition(string $column, string $keyword, boolean $escape=true, string $operator='AND', string $like='LIKE')
```

```php
$criteria->addSearchCondition('name','分类');
```

### [compare() 方法](#5)

```php
public CDbCriteria compare(string $column, mixed $value, boolean $partialMatch=false, string $operator='AND', boolean $escape=true)
```

```php
$criteria->compare('id,1);
```

### [addBetweenCondition()](#6)

```php
public CDbCriteria addBetweenCondition(string $column, string $valueStart, string $valueEnd, string $operator='AND')
```

```php
$criteria->addBetweenCondition('id', 1, 4);

$criteria->select = 'id,parentid,name';//field default='*';

$criteria->join = 'xxx'; //连接表

$criteria->with = 'xxx';//调用relations

$criteria->limit =10; //取1条数据，如果小于0，则不作处理

$criteria->offset =1; //两条合并起来，则表示 limit 10 offset1,或者代表了。limit 1,10

$criteria->order = 'xxx DESC,XXX ASC' ;//排序条件

$criteria->group = 'group 条件';

$criteria->having = 'having 条件 ';

$criteria->distinct = FALSE;//是否唯一查询
```

