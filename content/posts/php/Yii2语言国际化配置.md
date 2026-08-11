---
title: "Yii2语言国际化配置"
date: "2025-07-08 16:02:00"
slug: "yii2-yu-yan-guo-ji-hua-pei-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/07/08/Yii2语言国际化配置/"
  - "/2025/07/08/Yii2语言国际化配置.html"
  - "/Yii2语言国际化配置/"
  - "/Yii2语言国际化配置.html"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-pei-zhi/"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-pei-zhi.html"
  - "/yii2-yu-yan-guo-ji-hua-pei-zhi.html"
---
最近想将博客做成支持多语言的，还好Yii2支持这个功能，于是查看了下官方的文档，哎，看了半天不知道干嘛用的，于是各种百度，Google的搜索，最终才明白原来很简单，只是官方写的太复杂

下面介绍下具体的使用步骤，具体介绍我就不写了，官方写比我清楚，我就写怎么使用

## 第一步 创建i18n配置文件

```bash
./yii message/config @app/config/i18.php // yii 在项目目录下 Yii2创建的时候自动生成的
```

执行完命令之后会在项目根目录config下创建一个i18n.php文件

为什么要创建这个文件，因为我们为了多语言处理，需要生成一个对应的映射文件，只要生成就好了，稍后的配置程序会自动调用处理

## 第二步 修改配置规则

打开config/i18n.php，看下生成的配置文件的代码，如下：

```php
return [
    'color' => null,
    'interactive' => true,
    'help' => null,
    'sourcePath' => '@yii',
    'messagePath' => '@yii/messages',
    'languages' => [],
    'translator' => 'Yii::t',
    'sort' => false,
    'overwrite' => true,
    'removeUnused' => false,
    'markUnused' => true,
    'except' => [
        '.svn',
        '.git',
        '.gitignore',
        '.gitkeep',
        '.hgignore',
        '.hgkeep',
        '/messages',
        '/BaseYii.php',
    ],
    'only' => [
        '*.php',
    ],
    'format' => 'php',
    'db' => 'db',
    'sourceMessageTable' => '{&#8203;{%source_message}}',
    'messageTable' => '{&#8203;{%message}}',
    'catalog' => 'messages',
    'ignoreCategories' => [],
    'phpFileHeader' => '',
    'phpDocBlock' => null,
];
```

修改后的代码，如下：

```php
return [
    'color' => null,
    'interactive' => true,
    'help' => null,
    'sourcePath' => '@app',
    'messagePath' => '@app/messages',
    'languages' => ['zh-CN', 'ru-RU'],
    'translator' => 'Yii::t',
    'sort' => false,
    'overwrite' => true,
    'removeUnused' => false,
    'markUnused' => true,
    'except' => [
        '.svn',
        '.git',
        '.gitignore',
        '.gitkeep',
        '.hgignore',
        '.hgkeep',
        '/messages',
        '/BaseYii.php',
        'vendor',
    ],
    'only' => [
        '*.php',
    ],
    'format' => 'php',
    'db' => 'db',
    'sourceMessageTable' => '{&#8203;{%source_message}}',
    'messageTable' => '{&#8203;{%message}}',
    'catalog' => 'messages',
    'ignoreCategories' => [],
    'phpFileHeader' => '',
    'phpDocBlock' => null,
];
```

我这里只改了两个地方

```php
'sourcePath' => '@app', // 将@yii改为@app 只处理我们自己应用中的代码
'messagePath' => '@app/messages', // 将@yii/messages改为@app/messages 将需要翻译的字段提取出来要放的目录
'languages' => ['zh-CN', 'ru-RU'], // 要翻译成目标的语言，我这里定义了一个"中文"和"俄语"
```

和

```php
'except' => [
    '.svn',
    '.git',
    '.gitignore',
    '.gitkeep',
    '.hgignore',
    '.hgkeep',
    '/messages',
    '/BaseYii.php',
    'vendor', // 将vendor目录下的过滤掉，不然可能太多了
],
```

## 第三步 生成翻译配置文件

执行下面的命令

```bash
./yii message/extract @app/config/i18n.php
```

执行完之后会在messages目录下（如果没有messages目录的话需要手动创建下）得到如下的目录结构

```bash
├── ru-RU
│   └── app.php
└── zh-CN
    └── app.php
```

提示下再做这个操作之前，需要在自己的项目中有类似Yii:t()的调用，比如我这里在components/HeaderWidget.php这个文件中

```php
Yii::t('app', 'Home')
```

这里的app的作用是用来进行文件分类的，我这里暂时没有计划生成的时候会将所有需要翻译的字段放在app开头命名的php文件app.php文件中  
如果像下面这样调用的话

```php
Yii::t('appp', 'Home')
```

会生成一个appp.php的文件

## 第四步 翻译配置文件

看下中文的翻译文件messages/zh-CN/app.php，我的是下面这个

```php
return [
    'Archive' => '',
    'Autokid' => '',
    'Blog' => '',
    'Ctime' => '',
    'IP地址' => '',
    'UserAgent' => '',
    '主题' => '',
    '内容' => '',
    '姓名' => '',
    '日期' => '',
    '邮箱地址' => '',
    '页面路径' => '',
    'Home' => '首页', // 右边的键值对应 Yii::t('app', 'Home')中的Home，只需要在value中写入需要的汉字就可以了。
];
```

## 第五步 修改目标国际化语言

修改配置文件

```php
'language' => 'zh-CN', // 指定为要翻译的语言
```

再打开网页，就可以看到已经翻译成了对应需要的语言，当然这样的配置很不灵活，如果是部署多态机器并通过域名或者其他方式来实现的话，也是可以的，这里的话我建议如下方式

创建自己的Controller，然后将语言配置放在Session中,通过获取Session中的语言来更换全站的语言。具体见后面分享

提示，网站很多地方提到要加个配置，官方也是

```php
'i18n' => [
    'translations' => [
        'app*' => [
            'class' => 'yii\i18n\PhpMessageSource',
            'basePath' => '@app/messages',
            'sourceLanguage' => 'en-US',
            'fileMap' => [
                'app' => 'app.php',
            ],
        ],
    ],
],
```

我这边在配置的时候没有加，运行也都是正常的，如有遇到问题，可以一起沟通交流下。
