---
title: "Yii relations 写法"
date: "2025-06-20 14:34:14"
slug: "yii-relations-xie-fa"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii-relations-写法/"
  - "/2025/06/20/Yii-relations-写法.html"
  - "/Yii-relations-写法/"
  - "/Yii-relations-写法.html"
  - "/2025/06/20/yii-relations-xie-fa/"
  - "/2025/06/20/yii-relations-xie-fa.html"
  - "/yii-relations-xie-fa.html"
---
yii的relations里`self::BELONGS_TO`默认是用当前指定的键跟关联表的主键进行join，例如：

Post

```php
return array(
	'reply' => array(self::BELONGS_TO, 'BlogPostReply', 'postid'),
);
```

默认生成的sql类似 on id = postid，id是本表的主键，postid是表BookPostReply的一个字段(主键)

但是需要生成 on BookPostReply.postid = t.postid

关联非主键字段

方法一,改成如下：

```php
return array(
	'reply' => array(self::BELONGS_TO, 'BookPostReply', '', 'on' => 't.postid=reply.postid'),
);
```

方法二：

array(self::BELONGS_TO,'对应的模型',array('本模型的外键'=>'对应模型的主键'))

这样也可以定义的，只要明确指定主键和对应表的外键就可以了。

官方开发指南里是这样写的：

```php
array('fkc1'=>'pkc1','fkc2'=>'pkc2')
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### [执行关系查询](#1)

懒惰导入查询方法

最简单的方法就是为AR对象添加一个关联属性，

例:

// 获取PK为10的POST对象 $post=Post::model()->findByPk(10);

// 获取这个POST的作者 $author=$post->author;

如果没有关联的对象，那么将返回NULL或者一个空数组；BELONGS_TO和HAS_ONE结果为NULL，而HAS_MANY和MANY_MANY返回一个空数组。

上面的这种“懒惰导入”方法使用起来非常方便，但是在一些场景下不是非常的效率，比如，如果我们想访问N个POST的作者的信息，使用这种懒惰导入的方法将会执行N个join查询；

### [急切导入查询方法](#2)

下面介绍是一种“急切导入”方法：在使用find和findAll时，使用with()方法，例：

```php
$posts=Post::model()->with('author')->findAll()
```

这样就可以在一次查询时连同查询其他信息了；with方法可以接受多个关系：

```php
$posts=Post::model()->with('author','categories')->findAll();
```

这样就可以将作者和类别的信息一并进行查询；同样，with还支持多重急切导入

```php
$posts=Post::model()->with( 'author.profile', 'author.posts', 'categories')->findAll();
```

上面的代码不仅会返回autho和categories信息，还会返回作者的profile和posts信息

这种“急切导入”方法也支持CDbCriteria::with，下面这两种实现方式效果一样：

```php
$criteria=new CDbCriteria; 
$criteria->with=array( 'author.profile', 'author.posts', 'categories', ); 
$posts=Post::model()->findAll($criteria); 
//or $posts=Post::model()->findAll(array( 'with'=>array( 'author.profile', 'author.posts', 'categories',);
```

### [关系查询选项](#3)

前面提过，在申明关系时可以添加额外的选项，这些选项都是一些key-value对，是用来定制关系查询的，总结如下：

select

定义从AR类中被select的列集合，如果定义为\*，则表示查询所有列

condition

定义where语句，默认为空。

params

生成SQL语句的参数，这个需要用一个key-value对的数组来表示；

on

ON语句，这个条件用来通过AND添加一个joining condintion语句

order

ORDER语句

with

和当前对象一起导出的相关对象列表，要注意如果使用不正确，有可能导致无限死循环；

joinType

定义join的类别，默认为LEFT OUTER JOIN

alias

定义别名，当多个表中有相同的column name时，需要为表格定义alias，然后使用tablename.columnname来指定不同的column

together

这个只在HAS_MANY, MANY_MANY时有用，在实现跨表查询时，可以用这个参数来控制性能。正常用不到，不详细讲述；

join

JOIN语句

group

GROUP语句

having

HAVING语句

index

这个值用来设定返回的结果数组以哪个column做为index值，如果不设定这个值的话，将从0开始组织结果数组。

除此之外还包含下面几个选项，在“懒惰导出”的特定关系时可用limit,返回结果数量的限制，不适用于BELONG_TO关系

offset

offset结果数量的值，不适用于BELONG_TO关系

下面代码，显示上面选项的一些使用：

```php
class User extends CActiveRecord { 
	public function relations() { 
		return array( 
			'posts'=>array(self::HAS_MANY, 'Post', 'author_id', 'order'=>'posts.create_time DESC', 'with'=>'categories'), 
			'profile'=>array(self::HAS_ONE, 'Profile', 'owner_id'), 
		); 
	} 
}
```

此时，我们使用`$author->posts`时，会返回固定ORDER的POST信息

