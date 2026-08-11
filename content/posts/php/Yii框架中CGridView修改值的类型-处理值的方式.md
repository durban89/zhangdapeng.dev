---
title: "Yii框架中CGridView修改值的类型，处理值的方式"
date: "2025-06-09 17:41:16"
slug: "yii-kuang-jia-zhong-cgridview-xiu-gai-zhi-de-lei-xing-chu-li-zhi-de-fang-shi"
categories: ["技术"]
tags: ["Yii"]
aliases:
  - "/2025/06/09/Yii框架中CGridView修改值的类型，处理值的方式/"
  - "/2025/06/09/Yii框架中CGridView修改值的类型，处理值的方式.html"
  - "/Yii框架中CGridView修改值的类型，处理值的方式/"
  - "/Yii框架中CGridView修改值的类型，处理值的方式.html"
  - "/2025/06/09/Yii框架中CGridView修改值的类型-处理值的方式/"
  - "/2025/06/09/Yii框架中CGridView修改值的类型-处理值的方式.html"
  - "/2025/06/09/yii-kuang-jia-zhong-cgridview-xiu-gai-zhi-de-lei-xing-chu-li-zhi-de-fang-shi/"
  - "/2025/06/09/yii-kuang-jia-zhong-cgridview-xiu-gai-zhi-de-lei-xing-chu-li-zhi-de-fang-shi.html"
  - "/yii-kuang-jia-zhong-cgridview-xiu-gai-zhi-de-lei-xing-chu-li-zhi-de-fang-shi.html"
---
表中的每一行代表一个数据项的数据,和一个列通常代表一个属性的物品(一些列可能对应于复杂的表达式的属性或静态文本)。　　CGridView既支持排 序和分页的数据项。排序和分页可以在AJAX模式或正常的页面请求。使用CGridView的一个好处是,当用户浏览器禁用JavaScript,排序和 分页自动退化普通页面请求和仍然正常运行。

代码如下：

```php
<?php
$this->widget('zii.widgets.grid.CGridView', [
    'id' => 'chapter-grid',
    'dataProvider' => $model->search(), //数据结果集
    'filter' => $model,
    'columns' => [
        'id',
        //锚点<a href="http://www.gulianqiang.com/"></a>
        [
            'name' => 'name',
            'type' => 'raw',
            'value' => 'CHtml::link($data->name,"/book/$data->id")',
        ],
        //图片
        [
            'name' => 'image',
            'type' => 'image',
            'value' => 'LImages::getPath("book").$data->image', //图片相对路径
        ],
        //下拉列表
        [
            'name' => 'type',
            'value' => 'Lookup::item("chapterType",$data->type)',
            'filter' => Lookup::items('chapterType'),
        ],
        //内容截取
        [
            'name' => 'content',
            'type' => 'html',
            'value' => 'mb_substr(htmlspecialchars_decode($data->content),0,100,"utf-8")',
        ],
        //时间
        [
            'name' => 'create_time',
            'type' => 'datetime',
        ],
        // 根据相关信息读数据库
        [
            'name' => 'user_id',
            'value' => 'User::model()->findbyPk($data->user_id)->username',
            'filter' => false,
        ],
        [
            'class' => 'CButtonColumn',
        ],
    ],
]);
```

我的使用代码：

其实也是可以加入自己的方法的

```php
<?php
$this->widget('zii.widgets.grid.CGridView', [
    'id' => 'link-grid',
    'dataProvider' => $model->search(),
    'summaryCssClass' => 'hide',
    'itemsCssClass' => 'table table-bordered',
    'emptyText' => '搜索结果为空',
    'pagerCssClass' => 'pagination',
    'filterCssClass' => '',
    'pager' => [
        'class' => 'CLinkPager',
        'nextPageLabel' => '下一页',
        'prevPageLabel' => '上一页',
        'firstPageLabel' => '最前',
        'lastPageLabel' => '最后',
        'htmlOptions' => ['class' => ''],
        'header' => '',
        'hiddenPageCssClass' => '',
        'selectedPageCssClass' => 'active',
        'previousPageCssClass' => '',
        'nextPageCssClass' => '',
    ],
    'filter' => $model,
    'columns' => [
        'title' => [
            'name' => 'title',
            'type' => 'raw',
            'value' => 'Helper::truncate_utf8_string($data->title, 20,\'......\')',
        ],
        'url' => [
            'name' => 'url',
            'type' => 'raw',
            'value' => 'Helper::truncate_utf8_string($data->url, 20,\'......\')',
        ],
        'create_date',
        [
            'class' => 'CButtonColumn',
        ],
    ],
]);
```

以上已经提供常用的数据显示类型。基本可以将使用Yii框架开发web应用使用CGridView的情况都列出。

参考资料：http://www.gulianqiang.com/yii/158.html
