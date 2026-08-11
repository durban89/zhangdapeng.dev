---
title: "Django 模板 HTML 分段输出"
date: "2025-06-20 10:36:41"
slug: "django-mu-ban-html-fen-duan-shu-chu"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django-模板-HTML-分段输出/"
  - "/2025/06/20/Django-模板-HTML-分段输出.html"
  - "/Django-模板-HTML-分段输出/"
  - "/Django-模板-HTML-分段输出.html"
  - "/2025/06/20/django-mu-ban-html-fen-duan-shu-chu/"
  - "/2025/06/20/django-mu-ban-html-fen-duan-shu-chu.html"
  - "/django-mu-ban-html-fen-duan-shu-chu.html"
---
之前使用php输出html代码的时候，可以使用二维数组，这样子就可以进行循环输出html，但是在django中，有了一个更牛逼的方法就是，不需要自己去分组啦，直接使用计数器就很方便的

```html
<div id='container'>
{% for item in items %}
    {% if forloop.counter0|divisibleby:"4" %}
    <ul class="thumbnails">
    {% endif %}
        <li class="listitem span3">
            <div class="thumbnail">
                <a target='_blank' title='{{ item.title }}' href='{% url gifts_detail item.id %}'>
                    <img alt="{{ item.title }}" src="{{ MEDIA_URL }}{{ item.large_image }}" width="192" height="288">
                </a>
                <section style="margin-top:10px">
                    <div class="progress progress-striped active progress-success">
                        <div class="bar" style="width: {% widthratio item.feeling item.feeling|add:item.no_feeling 100 %}%;"></div>
                    </div>
                </section>
                <section style="margin-top:10px">
                    <div class="progress progress-striped active progress-danger">
                        <div class="bar" style="width: {% widthratio item.no_feeling item.feeling|add:item.no_feeling 100 %}%;"></div>
                    </div>
                </section>
                <section class="" style="margin-top:10px">
                    <a class="btn btn-primary have_feeling" href="#" onclick="Dajaxice.walkerfree.feeling(feeling_callback, {'id':'{{ item.id }}','type':'gift'});return false;">有感觉</a>
                    <a class="btn btn-primary no_feeling" href="#" onclick="Dajaxice.walkerfree.no_feeling(no_feeling_callback,{'id':'{{ item.id }}','type':'gift'});return false;">没感觉</a>
                    <input type='hidden' value='gift' name='type'>
                </section>
            </div>
        </li>
    {% if forloop.last or forloop.counter|divisibleby:"4" %}
    </ul>
    {% endif %}
{% endfor %}
</div>
```

完全可以按照自己的分组需求进行分组输出啦
