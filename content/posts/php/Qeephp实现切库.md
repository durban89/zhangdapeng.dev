---
title: "Qeephp实现切库"
date: "2025-06-12 17:45:10"
slug: "qeephp-shi-xian-qie-ku"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/12/Qeephp实现切库/"
  - "/2025/06/12/Qeephp实现切库.html"
  - "/Qeephp实现切库/"
  - "/Qeephp实现切库.html"
  - "/2025/06/12/qeephp-shi-xian-qie-ku/"
  - "/2025/06/12/qeephp-shi-xian-qie-ku.html"
  - "/qeephp-shi-xian-qie-ku.html"
---
基于要实现切库，而且又要使用Qeephp这个框架，之前一直没有用过，这里最近师兄在搞这一块，他的实现过程是这样的。详见以下代码：

```php
<?php
Q::register(QDB::getConn('xxxxx'), 'dbo_default');
$select = XXXXX::find($sql)->order('id DESC')->all()->asArray()->limit(0, 10);
$this->_view['pager'] = $select->getPagination();
$this->_view['rowset'] = $select->getAll();

$model = Q::ini('app_config/RUN_MODE');
Q::register(QDB::getConn($model, 'dbo_default'));
```
