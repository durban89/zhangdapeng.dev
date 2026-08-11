---
title: "Yii redirect 和createUrl的路由设置"
date: "2025-06-10 12:05:23"
slug: "yii-redirect-he-createurl-de-lu-you-she-zhi"
categories: ["技术"]
tags: ["Yii", "PHP"]
aliases:
  - "/2025/06/10/Yii-redirect-和createUrl的路由设置/"
  - "/2025/06/10/Yii-redirect-和createUrl的路由设置.html"
  - "/Yii-redirect-和createUrl的路由设置/"
  - "/Yii-redirect-和createUrl的路由设置.html"
  - "/2025/06/10/yii-redirect-he-createurl-de-lu-you-she-zhi/"
  - "/2025/06/10/yii-redirect-he-createurl-de-lu-you-she-zhi.html"
  - "/yii-redirect-he-createurl-de-lu-you-she-zhi.html"
---
### [$this->redirect这里的$this是当前的controller](#1)。

可能是应用程序的也可能是模块下的  
这里仅解一下第一个参url，当url是一个字符串时，它会自己动跳转，如`$this->redirect('/')`; 会跳转到站点根，如果你的当前主机为localhost,那么他就会跳到http://localhost/ 再者`$this->redirect('/books');`，则会跳到http://localhost/books  在应用程序的controller中，也可以使用`$this->redirect('books');`也会跳到http://localhost/books 但是当你在module中这样使用，则会出现另一种情况，当你打开urlManager，并设置了隐藏脚本文件，如果你当前的访问地址为 http://localhost/admin/default/index  当使用`$this->redirect('books');` 跳转， 跳转后地址则是  http://localhost/admin/default/books 这里只是说一下，redirect的简单跳转，我个人建议，如果不是跳到其他项目，或外站`$this->redirect('http://yiibook.com');`，建议都使用下面的方法  url使用数组  
当url为数组时，会调用urlManager来根据路由组织跳转的路径，这种情况比较理想，而且会根据路由的修改而改变  
如果有一条路由为

```php
'book'=>'admin/default/index'
```

格式为：'路由'=>'真实地址',  
即指定了访问book，就相当于方问admin模型下的default控制器的index操作方法。  
既然使用了路由，主要是为了让url更友好，并隐藏真实地址  
那么，当想使用$this->redirect跳转到这个路由时，需要指定真实地址，如

```php
$this->redirect(array('admin/default/index'));
```

这样就会跳到这个地址了，而且url显示的确是book，而当你修路由名称时,如  
'books'=>'admin/default/index'，或干脆去掉这个路径，都不用修改你的程序  
在模块中的情况，如果你当前在admin模块的controller中，使用跳转，则可以不用写moduleId  
直接使用$this->redirect(array('default/index')); 也是ok的，这样你的module也不会  
依赖于moduleId了  
再有如果你当前也在admin模块下的default控制器中，也可以使用  
$this->redirect(array('index'));进行跳转，不依赖于控制器的名字  
我们再看一下带参数的路由

```php
'book<id:\d+>'=>'admin/default/index'
```

那么，url需要为这个路径传递一个参数id，如

```php
$this->redirect(array('admin/default/index', 'id'=>1));
```

url格式为array('真实路径', '参数名'=>'参数值’，'参数名2'=>'参数值2', ....);  
Yii中许多组件或方法都有支持这种url的格式，如CMenu等等。

### [createUrl，有$this->createUrl和Yii::app()->createUrl](#2)，

createUrl它会根据真实地址，组织成路由格式的地址  
根据上面的路由，创建url

```php
$this->createUrl('admin/default/index')
```

带参数情况

```php
$this->createUrl('admin/default/index', array('id'=>1));
```

admin模块中，使用

```php
$this->createUrl('default/index');
```

或

```php
$this->create('index');
```

不要使用Yii::app()->createUrl，避免依赖于具体的路由

注意一下redirect与createUrl的参数区别。

