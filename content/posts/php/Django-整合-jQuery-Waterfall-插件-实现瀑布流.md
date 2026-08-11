---
title: "Django 整合 jQuery Waterfall 插件 实现瀑布流"
date: "2025-06-24 14:46:03"
slug: "django-zheng-he-jquery-waterfall-cha-jian-shi-xian-pu-bu-liu"
categories: ["技术"]
tags: ["Django", "jQuery"]
aliases:
  - "/2025/06/24/Django-整合-jQuery-Waterfall-插件-实现瀑布流/"
  - "/2025/06/24/Django-整合-jQuery-Waterfall-插件-实现瀑布流.html"
  - "/Django-整合-jQuery-Waterfall-插件-实现瀑布流/"
  - "/Django-整合-jQuery-Waterfall-插件-实现瀑布流.html"
  - "/2025/06/24/django-zheng-he-jquery-waterfall-cha-jian-shi-xian-pu-bu-liu/"
  - "/2025/06/24/django-zheng-he-jquery-waterfall-cha-jian-shi-xian-pu-bu-liu.html"
  - "/django-zheng-he-jquery-waterfall-cha-jian-shi-xian-pu-bu-liu.html"
---
## [Django实现瀑布流](#1)

需要Waterfall插件，[jQuery Waterfall插件的使用](https://www.gowhich.com/blog/415)这一节已经说过了

这里使用的时候可能会比较简短，跟上一篇文章有太多的不一样，不过这里使用的时候，调用的是html格式的数据。

Django Server端代码如下：

```python
def ajax(request):
    '''ajax请求数据'''
    if request.user.is_authenticated():
        user = request.user
    else:
        user = request.user
    try:
        items = Gifts.objects.filter(is_show = 0).order_by('-create_date')[10:20]
    except:
        items = []

    return render_to_response('home/ajax.html',{'action':'home','items':items,'user':user},context_instance=RequestContext(request))
```

ajax.html代码如下:

```javascript
{% load staticfiles %}
{% load dajaxice_templatetags %}

{% if items %}
{% for item in items %}
<div class="item" >
    <a target='_blank' title='{{ item.title }}' href='{{ item.url_address }}'>
        <img src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
    </a>
    <h3>{{ item.title|slice:"10" }}</h3>
    <p>{{ item.description|slice:"100" }}</p>
    <p>
        <a class="btn btn-primary" target='_blank' href="{{ item.url_address }}">浏览</a>
        <a class="btn have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback, {'id':'{{ item.id }}','type':'woman'});return false;">有感觉</a>
        <a class="btn no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback,{'id':'{{ item.id }}','type':'woman'});return false;">没感觉</a>
        <input type='hidden' value='woman' name='type'>
    </p>
</div>
{% endfor %}
{% endif %}
```

因为是调用的html格式的数据，这里就直接的将数据展示出来了。

调用数据的页面的html代码如下：

```html
<div id='container'>
    {% if items %}
    {% for item in items %}
    <div class="item" >
        <a target='_blank' title='{{ item.title }}' href='{{ item.url_address }}'>
            <img src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
        </a>
        <h3>{{ item.title|slice:"10" }}</h3>
        <p>{{ item.description|slice:"100" }}</p>
        <p>
            <a class="btn btn-primary" target='_blank' href="{{ item.url_address }}">浏览</a> 
            <a class="btn have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback, {'id':'{{ item.id }}','type':'woman'});return false;">有感觉</a>
            <a class="btn no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback,{'id':'{{ item.id }}','type':'woman'});return false;">没感觉</a>
            <input type='hidden' value='woman' name='type'>
        </p>
    </div>
    {% endfor %}
    {% endif %}
</div>
```

调用的script如下：

```javascript
<script type='text/javascript' src="/static/js/jquery-1.8.3.min.js"></script>
<script type='text/javascript' src="/static/waterfall/js/libs/handlebars/handlebars.js"></script>    
<script type='text/javascript' src="/static/waterfall/js/waterfall.min.js"></script>
```

瀑布流的实现部分如下：

```javascript
$(function(){
    $('#container').waterfall({
        itemCls: 'item',
        colWidth: 210,
        gutterWidth: 15,
        gutterHeight: 15,
        checkImagesLoaded: false,
        dataType: 'html',
        path: function(page) {
            return '/ajax/?page=' + page;
        }

    });
    $('.container-block').css({'visibility':'visible'})
});
```

