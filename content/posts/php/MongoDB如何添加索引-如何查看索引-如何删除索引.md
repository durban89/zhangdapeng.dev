---
title: "MongoDB如何添加索引、如何查看索引、如何删除索引"
date: "2025-07-14 16:21:25"
slug: "mongodb-ru-he-tian-jia-suo-yin-ru-he-cha-kan-suo-yin-ru-he-shan-chu-suo-yin"
categories: ["技术"]
tags: ["MongoDB"]
aliases:
  - "/2025/07/14/MongoDB如何添加索引、如何查看索引、如何删除索引/"
  - "/2025/07/14/MongoDB如何添加索引、如何查看索引、如何删除索引.html"
  - "/MongoDB如何添加索引、如何查看索引、如何删除索引/"
  - "/MongoDB如何添加索引、如何查看索引、如何删除索引.html"
  - "/2025/07/14/MongoDB如何添加索引-如何查看索引-如何删除索引/"
  - "/2025/07/14/MongoDB如何添加索引-如何查看索引-如何删除索引.html"
  - "/2025/07/14/mongodb-ru-he-tian-jia-suo-yin-ru-he-cha-kan-suo-yin-ru-he-shan-chu-suo-yin/"
  - "/2025/07/14/mongodb-ru-he-tian-jia-suo-yin-ru-he-cha-kan-suo-yin-ru-he-shan-chu-suo-yin.html"
  - "/mongodb-ru-he-tian-jia-suo-yin-ru-he-cha-kan-suo-yin-ru-he-shan-chu-suo-yin.html"
---
开始记录前的说明

表名：users

表中字段名：id,name,age,ctime

#### 创建索引

创建语句语法

`db.COLLECTION_NAME.ensureIndex(keys[,options])` 用于3.0及以下版本

`db.COLLECTION_NAME.createIndex(keys[,options])`用于3.0及以上版本

keys:要建立索引的参数列表。

如：{KEY:1}，其中key表示字段名，1表示升序排序，也可使用使用数字-1降序。  
options:可选参数，表示建立索引的设置。

可选值如下：  
background: Boolean - 在后台建立索引，以便建立索引时不阻止其他数据库活动。默认值为false。  
unique: Boolean - 创建唯一索引。默认值 false。  
name: String - 指定索引的名称。如果未指定，MongoDB会生成一个索引字段的名称和排序顺序串联。  
partialFilterExpression: document - 如果指定,MongoDB只会给满足过滤表达式的记录建立索引.  
sparse: Boolean - 对文档中不存在的字段数据不启用索引。默认值是 false。  
expireAfterSeconds: integer - 指定索引的过期时间  
storageEngine: document - 允许用户配置索引的存储引擎

第一个情况，创建单字段索引

```bash
db.users.createIndex({"name":1})
```

第二个情况，创建多字段索引

```bash
db.users.createIndex({"name":1,"age":1})
```

第三种情况，创建索引加可选项，这个情况建议多使用

```bash
db.users.createIndex({"name":1,"age":1}, {background: 1})
```

#### 查看索引

记录几种常用的方法

1. getIndexes()方法可以用来查看集合的所有索引，
2. getIndexKeys()方法查看索引键。
3. totalIndexSize()查看集合索引的总大小，
4. getIndexSpecs()方法查看集合各索引的详细信息

#### 删除索引

记录下常用方法

1. dropIndex()方法用于删除指定的索引
2. dropIndexes()方法用于删除全部的索引
