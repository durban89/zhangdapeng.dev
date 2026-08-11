---
title: "Yii主题切换设置"
date: "2025-06-25 10:09:31"
slug: "yii-zhu-ti-qie-huan-she-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/25/Yii主题切换设置/"
  - "/2025/06/25/Yii主题切换设置.html"
  - "/Yii主题切换设置/"
  - "/Yii主题切换设置.html"
  - "/2025/06/25/yii-zhu-ti-qie-huan-she-zhi/"
  - "/2025/06/25/yii-zhu-ti-qie-huan-she-zhi.html"
  - "/yii-zhu-ti-qie-huan-she-zhi.html"
---
### [第一步：配置文件](#1)

```php
return [
	'basePath'=>dirname(__FILE__).DIRECTORY_SEPARATOR.'..',
	'name'=>'GoWhich',
	'theme'=>'flatui'
];
```

### [第二步：创建主题文件夹](#2)

在themes目录下面创建主题flatui

在flatui文件夹下，创建views,js,css,images等文件夹，views文件夹里面的文件及文件夹请参考`./protected/views/`下面的内容。

### [第三步：theme路径的替换和修改](#3)


`Yii::app()->theme->baseUrl`的替换

### [第四步：修改相应的layout](#4)

$this->layout的修改

