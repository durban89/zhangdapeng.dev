---
title: "Yii开启错误日志"
date: "2025-06-03 14:56:27"
slug: "yii-kai-qi-cuo-wu-ri-zhi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/03/Yii开启错误日志/"
  - "/2025/06/03/Yii开启错误日志.html"
  - "/Yii开启错误日志/"
  - "/Yii开启错误日志.html"
  - "/2025/06/03/yii-kai-qi-cuo-wu-ri-zhi/"
  - "/2025/06/03/yii-kai-qi-cuo-wu-ri-zhi.html"
  - "/yii-kai-qi-cuo-wu-ri-zhi.html"
---
生产环境中的 Web 应用常需要具有完善的事件日志功能。在我们的博客应用中，我们想记录它在使用时发生的错误。这些错误可能是程序错误或者是用户对系统的不当使用导致的错误。记录这些错误可以帮助我们完善此博客应用。

为启用错误日志功能，我们修改 应用配置 如下,

```php
return [
    'preload' => ['log'],

    // ......

    'components' => [
        'log' => [
            'class' => 'CLogRouter',
            'routes' => [
                [
                    'class' => 'CFileLogRoute',
                    'levels' => 'error, warning',
                ],
                [
                    'class' => 'CProfileLogRoute', //显示页面加载的整个流程，包括mysql语句
                    'levels' => 'profile',
                ],
                [
                    'class' => 'CWebLogRoute',
                    'levels' => 'profile,trace',
                ],
            ],
        ],
        //......
    ],
];
```
通过上述配置，如果有错误（error）或警告（warning）发生，其详细信息将被记录并保存到位于/wwwroot/blog/protected/runtime目录的文件中。

log组件还提供了更多的高级功能，例如将日志信息发送到一个 Email 列表，在 JavaScript 控制台窗口中显示日志信息等。更多详情，请参考~~[指南](http://www.yiiframework.com/doc/guide/topics.logging)~~。
