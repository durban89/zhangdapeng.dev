---
title: "Yii 隐藏index.php的方法"
date: "2025-06-20 14:13:36"
slug: "yii-yin-cang-indexphp-de-fang-fa"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii-隐藏index.php的方法/"
  - "/2025/06/20/Yii-隐藏index.php的方法.html"
  - "/Yii-隐藏index.php的方法/"
  - "/Yii-隐藏index.php的方法.html"
  - "/2025/06/20/Yii-隐藏index-php的方法/"
  - "/2025/06/20/Yii-隐藏index-php的方法.html"
  - "/2025/06/20/yii-yin-cang-indexphp-de-fang-fa/"
  - "/2025/06/20/yii-yin-cang-indexphp-de-fang-fa.html"
  - "/yii-yin-cang-indexphp-de-fang-fa.html"
---
关于Yii 隐藏index.php的方法

配置环境是nginx+ubuntu+php

ubuntu的配置和php的配置这里不再讨论，讨论一下nginx的配置和yii的配置

nginx的配置


```ini
server {
        listen   80; ## listen for ipv4; this line is default and implied
        root /home/davidzhang/local.ubuntu.new.star.vlinkage.com;
        index index.html index.htm index.php;

        # Make site accessible from http://localhost/
        server_name local.ubuntu.new.star.vlinkage.com;

        #include        yii.conf;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to index.html
                #try_files $uri $uri/ /index.html;
                try_files $uri $uri/ /index.php?$args;
                # Uncomment to enable naxsi on this location
                # include /etc/nginx/naxsi.rules
                index index.php;
        }

        location /doc/ {
                alias /usr/share/doc/;
                autoindex on;
                allow 127.0.0.1;
                deny all;
        }
}
```

这里的配置主要是这里

```ini
location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to index.html
                #try_files $uri $uri/ /index.html;
                try_files $uri $uri/ /index.php?$args;
                # Uncomment to enable naxsi on this location
                # include /etc/nginx/naxsi.rules
                index index.php;
        }
```

当然也可以使用下面的方式

```ini
location / {
    if (!-e $request_filename)
    {
        rewrite ^(.*)$  /index.php last;
    }
}
```

接下来是yii的配置

```php
'urlManager'=>array(
            'urlFormat'=>'path',
            'showScriptName'=>false,
            'rules'=>array(
                '<controller:\w+>/<id:\d+>'=>'<controller>/view',
                '<controller:\w+>/<action:\w+>/<id:\d+>'=>'<controller>/<action>',
                '<controller:\w+>/<action:\w+>'=>'<controller>/<action>',
            ),
        ),
```

这里面关键的是这里

```php
'showScriptName'=>false,
```

不然index.php还是会有的，在自己的项目中请注意这里
