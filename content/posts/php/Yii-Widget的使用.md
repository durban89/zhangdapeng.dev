---
title: "Yii Widget的使用"
date: "2025-06-03 15:18:28"
slug: "yii-widget-de-shi-yong"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii-Widget的使用/"
  - "/2025/06/03/Yii-Widget的使用.html"
  - "/Yii-Widget的使用/"
  - "/Yii-Widget的使用.html"
  - "/2025/06/03/yii-widget-de-shi-yong/"
  - "/2025/06/03/yii-widget-de-shi-yong.html"
  - "/yii-widget-de-shi-yong.html"
---
小插件解决大问题，做网站，最喜欢使用这种东西，不需要重写代码，直接调用，传递参数，就得到想要的模块，yii也有次功能，看代码：

```php
$this->beginWidget('CBootStrapPortlet', [
    'title' => '博文分类', //导航标题
    'htmlOptions' => ['class' => 'nav nav-pills nav-stacked'], //样式定义
    'tagName' => 'ul', //
    'decorationCssClass' => 'active',
    'titleCssClass' => '',
    'contentCssClass' => '',

]);

$this->widget('CBootStrapMenu', [
    'items' => $this->blogType,
    'htmlOptions' => ['class' => ''],
]);

$this->endWidget();
```

上面的代码是我的列表的小插件，样式我已经定义好了，只要给变量，传递参数就好了s
