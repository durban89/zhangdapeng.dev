---
title: "Django的ajax的调用-AJAX libraries-django-dajaxice"
date: "2025-06-20 11:50:51"
slug: "django-de-ajax-de-diao-yong-ajax-libraries-django-dajaxice"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django的ajax的调用-AJAX-libraries-django-dajaxice/"
  - "/2025/06/20/Django的ajax的调用-AJAX-libraries-django-dajaxice.html"
  - "/Django的ajax的调用-AJAX-libraries-django-dajaxice/"
  - "/Django的ajax的调用-AJAX-libraries-django-dajaxice.html"
  - "/2025/06/20/django-de-ajax-de-diao-yong-ajax-libraries-django-dajaxice/"
  - "/2025/06/20/django-de-ajax-de-diao-yong-ajax-libraries-django-dajaxice.html"
  - "/django-de-ajax-de-diao-yong-ajax-libraries-django-dajaxice.html"
---
对于项目中，尤其是对于做web开发的话，页面的ajax的调用是少不了的，不过在使用django的框架的时候，已经很方便的提供了一个使用ajax 的库了，就是django-dajaxice，其如果安装都是很简单的，只要按照[http://django-dajaxice.readthedocs.org/en/latest/installation.html](http://django-dajaxice.readthedocs.org/en/latest/installation.html这个说明自行执行就好了。)这个说明进行安装，进行配置就好了，然后记得重新启动一下在运行就好了

往往会遇到这样的情况就是自己的static文件找不到，比如dajaxice.core.js这个文件找不到，千万不要试着去复制，那样是没有用的

只要记得同步一下static文件就好了

执行那个这个命令

```bash
python manage.py collectstatic
```

为了确定确实存在我们需要的文件，建议执行一下这个命令

```bash
python ./manage.py findstatic dajaxice/dajaxice.core.js
```

如果输出这个结果

```bash
Found 'dajaxice/dajaxice.core.js' here:
  /tmp/tmpusCiQ2
```

说明这个文件是存在，那么执行上面的命令就没有什么问题啦

这里我将自己的示例代码贴一下

ajax.py

```python
#! -*- coding=utf-8 -*-
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})
    
@dajaxice_register
def feeling(request):
    return simplejson.dumps({'message':'有感觉加1'})

@dajaxice_register
def no_feeling(request):
    return simplejson.dumps({'message':'没有感觉加1'})
```

home.html

```html
{% extends "base.html" %}
{% load staticfiles %}
{% load dajaxice_templatetags %}

{% block title %}享受购物的感觉{% endblock %}

{% block css %}
<link rel="stylesheet" href="{% static "waterfall/css/reset.css" %}">
<link rel="stylesheet" href="{% static "waterfall/css/waterfall.css" %}">
{% endblock %}

{% block content %}
<div class="container-fluid">
    <div class="row-fluid">
        <div class="span12">
            
            <div id='container'>
                {% if items_woman %}
                {% for item in items_woman %}
                <div class="item" >
                    <a target='_blank' title='{{ item.title }}' href='{{ item.url_address }}'>
                        <img src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
                    </a>
                    <h3>{{ item.title|slice:"10" }}</h3>
                    <p>{{ item.description|slice:"100" }}</p>
                    <p>
                        <a class="btn btn-primary" target='_blank' href="{{ item.url_address }}">浏览</a> 
                        <a class="btn have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback);">有感觉</a>
                        <a class="btn no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback);">没感觉</a>
                        <input type='hidden' value='woman' name='type'>
                    </p>
                </div>
                {% endfor %}
                {% endif %}

                {% if items_man %}
                {% for item in items_man %}
                <div class="item" >
                    <a target='_blank' title='{{ item.title }}' href='{{ item.url_address }}'>
                        <img src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
                    </a>
                    <h3>{{ item.title|slice:"10" }}</h3>
                    <p>{{ item.description|slice:"100" }}</p>
                    <p>
                        <a class="btn btn-primary" target='_blank' href="{{ item.url_address }}">浏览</a>
                        <a class="btn have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback);">有感觉</a>
                        <a class="btn no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback);">没感觉</a>
                        <input type='hidden' value='man' name='type'>
                    </p>
                </div>
                {% endfor %}
                {% endif %}

                {% if items_gifts %}
                {% for item in items_gifts %}
                <div class="item" >
                    <a target='_blank' title='{{ item.title }}' href='{{ item.url_address }}'>
                        <img src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
                    </a>
                    <h3>{{ item.title|slice:"10" }}</h3>
                    <p>{{ item.description|slice:"100" }}</p>
                    <p>
                        <a class="btn btn-primary" target='_blank' href="{{ item.url_address }}">浏览</a> 
                        <a class="btn have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback);">有感觉</a>
                        <a class="btn no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback);">没感觉</a>
                        <input type='hidden' value='gifts' name='type'>
                    </p>
                </div>
                {% endfor %}
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% block js %}

<script type='text/javascript' src="{% static "waterfall/js/libs/handlebars/handlebars.js" %}"></script>
<script type='text/javascript' src="{% static "waterfall/js/waterfall.min.js" %}"></script>
<script>
$('#container').waterfall({
    itemCls: 'item',
    colWidth: 210,
    gutterWidth: 15,
    gutterHeight: 15,
    checkImagesLoaded: false,
    dataType: 'html',
    path: function(page) {
        return 'data/data.html?page=' + page;
    }
});
</script>
{% dajaxice_js_import %}
<script>
function my_js_callback(data){
    alert(data.message);
}
function feeling_callback(data){
    alert(data.message);
}
function no_feeling_callback(data){
    alert(data.message);
}
</script>
{% endblock %}

{% endblock %}
```
