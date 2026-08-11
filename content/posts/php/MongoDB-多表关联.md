---
title: "MongoDB - 多表关联"
date: "2025-07-14 14:53:34"
slug: "mongodb-duo-biao-guan-lian"
categories: ["技术"]
tags: ["MongoDB"]
aliases:
  - "/2025/07/14/MongoDB-多表关联/"
  - "/2025/07/14/MongoDB-多表关联.html"
  - "/MongoDB-多表关联/"
  - "/MongoDB-多表关联.html"
  - "/2025/07/14/mongodb-duo-biao-guan-lian/"
  - "/2025/07/14/mongodb-duo-biao-guan-lian.html"
  - "/mongodb-duo-biao-guan-lian.html"
---
之前一直使用MySQL，后面因为其他原因，需要使用mongodb，但是自己对mongodb又不是很熟悉

今天经历了一个算是我任务超级复杂的案例了

下面看下这个聚合的查询语句

```sql
db.table_name.aggregate([
    {
        '$match': {
            'dtime': 0
        }
    },
    {
        '$lookup': {
            'as': 'content',
            'localField': 'rule_id',
            'foreignField': 'rule_id',
            'from': 'table2'
        }
    },
    {
        '$addFields': {
              starIDs: '$star_ids'
        }
    },

    {
        '$unwind': "$starIDs"
    },

    {
        '$addFields': {
              starIDStr: {$concat: [ "star_id::", {$toString: "$starIDs"}]}
        }
    },

    {
        '$unwind': "$content"
    },

    {
        '$match': {
            'content.dtime': 0
        }
    },
    {
        '$lookup': {
            'as': 'audit',
            'localField': 'starIDStr',
            'foreignField': 'person_id',
            'from': 'table3'
        }
    },

    {
        '$group': {
            '_id': '$_id',
            'doc': {"$first":"$$ROOT"}，

        }
    },

    {
        "$replaceRoot":{"newRoot":"$doc"}
    },

    {
        '$sort': {
            'content.contents.0.ctime': -1,
            'content.group_id': -1
        }
    },

    {
        '$skip': 0
    },

    {
        '$limit': 15
    },
]);
```

需求是这样的

首先用table\_name表去关联table1，别名为content，通过rule\_id去关联，之后需要关联另外一个表table3，但是table3这个表的字段跟table2表字段类型不一致

table2表字段是一个数组`star_ids: [123,456]`

table3表需要关联的字段是一个字符串，字段值举例子（`person_id: 'star_id::123'`）

这个时候需要进行字段的类型转换，于是我们用到了`addFields`管道工具，从上面的执行语句中可以看到，我们执行了一个`unmind`操作，主要是为了将数组值转为字符串，

具体效果如下，从如下

```bash
a----1
|----2
```

变成了

```bash
a----1
a----2
```

也就是将

```bash
star_ids: [123,456]
```

变成了

```bash
star_ids: 123
star_ids: 456
```

这里注意下，转换后的结果是两条记录

但是我们有个要求就是不能更改原有字段类型，也就是

```bash
star_ids: [123,456]
```

这个是不能修改的

于是我们重命名之后在进行字符串的拼接

最后 `star_ids: [123,456]`（这个依然存在不会更改） 分身出来一个 `starIDs: [123,456]，同时因为unwind了starIDs，最后starIDS变成了`

```bash
starIDs: 123
starIDs： 456
```

`然后就可以进行字符串的拼接了`

```bash
'$addFields': {
        starIDStr: {$concat: [ "star_id::", {$toString: "$starIDs"}]}
}
```

最后starIDs变成了

```bash
starIDs: 'star_id::123'
starIDs：'star_id::456'
```

最后整理成了与person\_id字段值规则一致的了，这样就可以就行查询了

也就有了

```bash
{
    '$lookup': {
        'as': 'audit',
        'localField': 'starIDStr',
        'foreignField': 'person_id',
        'from': 'table3'
    }
},
```

最后由于由

star\_ids: [123, 456]

变成

star\_ids: 123

star\_ids: 456

的时候

记录条数由一条变成了两条，需要进行去重处理

于是用到了

```bash
{
    '$group': {
        '_id': '$_id',
    }
},
```

之后由于用到了group，是的记录不能返回所有的字段

于是由了下面这个管道

```bash
{
    '$group': {
        '_id': '$_id',
        'doc': {"$first":"$$ROOT"}，

    }
},

{
    "$replaceRoot":{"newRoot":"$doc"}
},
```

最终解决了一个复杂的查询，可以说mongodb的管道工具还是很强大的，但是用起来也是超级复杂
