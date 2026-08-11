---
title: "Yii分页设置"
date: "2025-06-03 15:03:26"
slug: "yii-fen-ye-she-zhi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii分页设置/"
  - "/2025/06/03/Yii分页设置.html"
  - "/Yii分页设置/"
  - "/Yii分页设置.html"
  - "/2025/06/03/yii-fen-ye-she-zhi/"
  - "/2025/06/03/yii-fen-ye-she-zhi.html"
  - "/yii-fen-ye-she-zhi.html"
---
yii自己是带有自动分页功能的。只要在对应的controller里面，类似下面这样鞋代码，就会实现的
```php
$dataProvider = new CActiveDataProvider(
    'Blog',
    [
        'pagination' => ['pageSize' => 10],
        'criteria' => ['order' => 'create_date DESC'],
    ]
);
```

但是样式还是yii中已经写好的，那么对于我，我要改掉这个样式，使用我提供的样式，可以像我下面这样写

```php
<?php
$this->widget('zii.widgets.CListView', [
    'dataProvider' => $dataProvider,
    'itemView' => '_view',
    'summaryCssClass' => 'hide',
    'pagerCssClass' => 'pagination',
    'pager' => [
        'class' => 'CLinkPager',
        'nextPageLabel' => '&raquo;',
        'prevPageLabel' => '&laquo;',
        'firstPageLabel' => '最前',
        'lastPageLabel' => '最后',
        'htmlOptions' => ['class' => ''],
        'header' => '',
        'hiddenPageCssClass' => 'disabled',
        'selectedPageCssClass' => 'active',
        'previousPageCssClass' => '',
        'nextPageCssClass' => '',
    ],
]);
```
其实只要添加自己对应的class属性就可以了，因为yii有自己默认的class属性，这个是比较简单。

下次我们可以看看，如何修改侧边下拉框，改为自己的喜欢的样式。
