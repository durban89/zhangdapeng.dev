---
title: "Yii CDbCriteria常用方法"
date: "2025-06-03 15:01:08"
slug: "yii-cdbcriteria-chang-yong-fang-fa"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii-CDbCriteria常用方法/"
  - "/2025/06/03/Yii-CDbCriteria常用方法.html"
  - "/Yii-CDbCriteria常用方法/"
  - "/Yii-CDbCriteria常用方法.html"
  - "/2025/06/03/yii-cdbcriteria-chang-yong-fang-fa/"
  - "/2025/06/03/yii-cdbcriteria-chang-yong-fang-fa.html"
  - "/yii-cdbcriteria-chang-yong-fang-fa.html"
---
Yii的Active Recorder包装了很多。

特别是把SQL中 把where,order,limit,IN/not IN,like等常用短句都包含进CDbCriteria这个类中去，这样整个代码会比较规范，一目了然。

```php
$criteria = newCDbCriteria;
$criteria->addCondition("id=1"); //查询条件，即where id =1
$criteria->addInCondition('id', [1, 2, 3, 4, 5]); //代表where id IN (1,23,,4,5,);
$criteria->addNotInCondition('id', [1, 2, 3, 4, 5]); //与上面正好相法，是NOT IN
$criteria->addCondition('id=1', 'OR'); //这是OR条件，多个条件的时候，该条件是OR而非AND
$criteria->addSearchCondition('name', '分类'); //搜索条件，其实代表了。。where name like ‘%分类%’
$criteria->addBetweenCondition('id', 1, 4); //between1 and 4

$criteria->compare('id', 1); //这个方法比较特殊，他会根据你的参数自动处理成addCondition或者addInCondition，
//即如果第二个参数是数组就会调用addInCondition

$criteria->addCondition("id = :id");
$criteria->params[':id'] = 1;

$criteria->select = 'id,parentid,name'; //代表了要查询的字段，默认select=’*';
$criteria->join = 'xxx'; //连接表
$criteria->with = 'xxx'; //调用relations
$criteria->limit = 10; //取1条数据，如果小于0，则不作处理
$criteria->offset = 1; //两条合并起来，则表示 limit 10 offset1,或者代表了。limit 1,10
$criteria->order = 'xxx DESC,XXX ASC'; //排序条件
$criteria->group = 'group 条件';
$criteria->having = 'having 条件 ';
$criteria->distinct = false; //是否唯一查询
```
