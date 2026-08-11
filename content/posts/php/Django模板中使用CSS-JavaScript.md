---
title: "Django模板中使用CSS, JavaScript"
date: "2025-06-12 11:49:32"
slug: "django-mu-ban-zhong-shi-yong-css-javascript"
categories: ["技术"]
tags: ["Django", "CSS", "JavaScript"]
aliases:
  - "/2025/06/12/Django模板中使用CSS,-JavaScript/"
  - "/2025/06/12/Django模板中使用CSS,-JavaScript.html"
  - "/Django模板中使用CSS,-JavaScript/"
  - "/Django模板中使用CSS,-JavaScript.html"
  - "/2025/06/12/Django模板中使用CSS-JavaScript/"
  - "/2025/06/12/Django模板中使用CSS-JavaScript.html"
  - "/2025/06/12/django-mu-ban-zhong-shi-yong-css-javascript/"
  - "/2025/06/12/django-mu-ban-zhong-shi-yong-css-javascript.html"
  - "/django-mu-ban-zhong-shi-yong-css-javascript.html"
---
### [测试环境](#1)

```python
(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/css'}),
(r'^js/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/js'}),
(r'^images/(?P</path><path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/django-demo/images'}),
```

模板中使用下述方式即可：

```html
<link href="/css/demo.css" type="text/css" rel="stylesheet">
```

注：可采用`os.path.dirname(globals()["__file__"])`来获得当前文件所在路径，比如

```python
(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(globals()["__file__"])+'/css'}),
```

可以使用os.path.abspath()函数返回此路径的绝对路径。  
\==============  
要在django的tempalte file中引用css、js、gif等静态文件，首先一条setting.py中DEBUG开关打开。

1、在project目录下建立一个存放静态文件的目录，如：medias

2、在url.py patterns中增加一行：

```python
(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
```

还要`from django.conf import setting`

3、在setting.py中加入一行：

```python
STATIC_PATH='./medias'
```

如此设置后，就可以在template file 中引用media中存放的静态文件了，如：

```html
<img src='/site_media/django.gif'>
```

### [线上环境](#2)

在使用Django开发的Web项目中是避免不了使用css、javascript、js等静态文件的，而对于这些静态文件的处理，django官 网这样写：Django itself doesn’t serve static (media) files, such as images, style sheets, or video. It leaves that job to whichever Web server you choose.就是说django本身不处理类似于图片、样式表、视频等静态文件，它将此项工作交给了你选择的Web服务器。  
在网上搜索到的django项目处理静态文件的示例中，大家似乎都在使用如下的方法让django处理静态文件：

```python
urlpatterns += patterns('', (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}), )
```

而对于django.views.static.serve方法，django官网说得很清楚：Using this method is inefficient and insecure. Do not use this in a production setting. Use this only for development.就是说这种方法是低效且不安全的，不要在生产环境使用此方法，只在开发环境使用。  
这时对于静态文件的处理，我们只能使用我们选择的Web服务器来处理了。比如使用nginx服务器的话，可以如下设置：

```shell
server {
    listen   80; ## listen for ipv4; this line is default and implied
    root /home/davidzhang/pythonweb/mysite/mysite;
    index    index.html index.htm;

    # Make site accessible from http://localhost/
    server_name local.ubuntu.python.blog.com;

    access_log /var/log/uwsgi/local.ubuntu.python.blog.access.log;
    error_log /var/log/uwsgi/local.ubuntu.python.blog.error.log;

    location / {
        include    uwsgi_params;
        uwsgi_pass    unix:///tmp/mysite.socket;
        #uwsgi_pass    127.0.0.1:9090;
    }
    location ^~ /static {                    #^~ 与 /static之间有空格
        alias /usr/local/lib/python2.7/dist-packages/Django-1.4.2-py2.7.egg/django/contrib/admin/static;
    }

    location ~* ^/(css|img|js)/.*$ {
        root /home/davidzhang/pythonweb/mysite/media;
        expires 12h;
        break;
    }

    location ~ ^.+\.(gif|jpg|png|ico|jpeg)$ {
        expires 3d;
    }
}
```
