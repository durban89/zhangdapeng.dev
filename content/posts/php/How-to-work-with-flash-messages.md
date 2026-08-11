---
title: "How to work with flash messages"
date: "2025-06-20 14:33:46"
slug: "how-to-work-with-flash-messages"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/How-to-work-with-flash-messages/"
  - "/2025/06/20/How-to-work-with-flash-messages.html"
  - "/How-to-work-with-flash-messages/"
  - "/How-to-work-with-flash-messages.html"
  - "/2025/06/20/how-to-work-with-flash-messages/"
  - "/2025/06/20/how-to-work-with-flash-messages.html"
  - "/how-to-work-with-flash-messages.html"
---
1，Setting flash messages（设置）

A flash message is used in order to keep a message in session through one or several requests of the same user.

```php
Yii::app()->user->setFlash('success', "数据设置成功");
```

2，Displaying flash messages（显示）

To check for flash messages we use the hasFlash() Method and to obtain the flash message we use the getFlash() Method. Since Yii v1.1.3, there is also a method getFlashes() to fetch all the messages.

1），静态显示

```php
<?php if(Yii::app()->user->hasFlash('success')):?>
    <div class="info">
        <?php echo Yii::app()->user->getFlash('success'); ?>
    </div>
<?php endif; ?>
```

全部显示

```php
$flashMessages = Yii::app()->user->getFlashes();
if ($flashMessages) {
    echo '<ul class="flashes">';
    foreach($flashMessages as $key => $message) {
        echo '<li><div class="flash-' . $key . '">' . $message . "</div></li>\n";
    }
    echo '</ul>';
}
```

2），动态显示

```php
Yii::app()->clientScript->registerScript(
   'myHideEffect',
   '$(".info").animate({opacity: 1.0}, 3000).fadeOut("slow");',
   CClientScript::POS_READY
);
```

With these lines of code we register a piece of jQuery (already included with YII) javascript code, using 'myHideEffect' as ID. It will be inserted in the jQuery's ready function (CClientScript::POS\_READY).

