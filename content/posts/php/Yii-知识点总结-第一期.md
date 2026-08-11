---
title: "Yii 知识点总结 第一期"
date: "2025-06-18 11:28:22"
slug: "yii-zhi-shi-dian-zong-jie-di-yi-qi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/18/Yii-知识点总结-第一期/"
  - "/2025/06/18/Yii-知识点总结-第一期.html"
  - "/Yii-知识点总结-第一期/"
  - "/Yii-知识点总结-第一期.html"
  - "/2025/06/18/yii-zhi-shi-dian-zong-jie-di-yi-qi/"
  - "/2025/06/18/yii-zhi-shi-dian-zong-jie-di-yi-qi.html"
  - "/yii-zhi-shi-dian-zong-jie-di-yi-qi.html"
---
- 使用updateCounters()来更新计数器字段。

```php
Book::model()->updateCounters(['download_count' => 1], ':id=id', [':id' => $id]);
```

- 使用sendFile()来下载文件。

```php
$type = LFilter::checkString($_GET['t']);
$dataProvider = Book::model()->findByPk($id);
$content = $this->renderPartial('book', [
    'dataProvider' => $dataProvider,
    'type' => $type,
], true, false);
Yii::app()->request->sendFile($dataProvider->name . '.' . $type, $content),
```

- 设计数据库时候如果`create_time`, `update_time`字段为int(10).在模型中使用行为插件。

```php
public function behaviors()
{
    return [
        'CTimestampBehavior' => [
            'class' => 'zii.behaviors.CTimestampBehavior',
            'createAttribute' => 'create_time',
            'updateAttribute' => 'update_time',
        ],
    ];
}
```

- 如果有些字段使用1，2，3之类的数字存储，在程序中使用时候含义不明确。可以model中加入如下函数.

```php
private static $_items = [];
public function loadItems($type, $code = null)
{
    self::$_items = [
        'status' => [
            '1' => Yii::t('dh', '开启'),
            '2' => Yii::t('dh', '关闭'),
        ],
        'type' => [
            '1' => Yii::t('dh', '产品'),
            '2' => Yii::t('dh', '文章'),
        ],
    ];
    return $code ? self::$_items[$type][$code] : self::$_items[$type];
}
```

- 多语言使用`Yii::t()`函数。

```php
public function attributeLabels()
{
    return [
        'verifyCode' => Yii::t('default', '验证码'),
        'name' => Yii::t('default', '名字'),
        'email' => Yii::t('default', '邮箱'),
        'subject' => Yii::t('default', '标题'),
        'body' => Yii::t('default', '内容'),
        'required' => Yii::t('default', '变量"{var}"没有定义'，array('{var}' => $var));,
    ];
}
```

- 数据库表使用了前缀，则使用`{{$tableName}}`。

```php
public function tableName()
{
    return '{{product}}';
}
```

- Cookie的使用

```php
//设置Cookie
$cookie=new CHttpCookie($name,$value);
$cookie=time()+60*60*24;
Yii::app()->request->cookies[$name]=$cookie;
//获取Cookie
$cookie=Yii::app()->request->cookies[$name];
$value=$cookie->value;
//删除Cookie
$cookie = Yii::app()->request->getCookies();
unset($cookie[$name]);
```

- zii.widgets.jui.CJuiTabs的使用

```php
<?php
    $this->widget('zii.widgets.jui.CJuiTabs', array(
        'tabs'=>array(
            Yii::t('book','基本信息') => $this->renderPartial('_basic',array(
                    'model' => $model,
                    'form' => $form,
            ),true),
            Yii::t('book','作品标签') => array('ajax'=> $this->createUrl('tag/boxList',array('tag'=>$model->tag))),
            Yii::t('book','作品封面') => $this->renderPartial('_image',array(
                    'model'=>$model,
                    'form'=>$form,
            ),true),
            Yii::t('book','作品公告') => $this->renderPartial('_notice',array(
                    'model'=>$model,
                    'form'=>$form,
            ),true),
        ),
        // additional javascript options for the tabs plugin
        'options'=>array(
            'collapsible'=>false,
        ),
    ));
?>
```

对于tabs而言，对于复杂内容的渲染结合使用renderPartial();

- zii.widgets.grid.CGridView的使用

```php
<?php
$this->widget('zii.widgets.grid.CGridView', array(
    'id'=>'chapter-grid',
    'dataProvider'=>$model->search(),
    'filter'=>$model,
    'columns'=>array(
        'id',
        //锚点<a href="http://blog.163.com/huv520@126/blog/"></a>
        array(
            'name'=>'name',
            'type'=>'raw',
            'value'=>'CHtml::link($data->name,"/book/$data->id")',
        ),
        //图片
        array(
            'name'=>'image',
            'type'=>'image',
            'value'=>'LImages::getPath("book").$data->image',//图片相对路径
         ),
        //下拉列表
        array(
            'name'=>'type',
            'value'=>'Lookup::item("chapterType",$data->type)',
            'filter'=>Lookup::items('chapterType'),
        ),
        //内容截取
        array(
            'name'=>'content',
            'type'=>'html',
            'value'=>'mb_substr(htmlspecialchars_decode($data->content),0,100,"utf-8")',
        ),
        //时间
        array(
            'name'=>'create_time',
            'type'=>'datetime',
        ),
        // 根据相关信息读数据库
        array(
            'name'=>'user_id',
            'value'=>'User::model()->findbyPk($data->user_id)->username',
            'filter'=>false,
        ),
        array(
            'class'=>'CButtonColumn',
        ),
    ),
)); ?>
```

- findAll()的使用;

```php
$params = [
    'select' => 'id,name,image',
    'order' => 'total_point DESC',
    'limit' => 5,
];
```
