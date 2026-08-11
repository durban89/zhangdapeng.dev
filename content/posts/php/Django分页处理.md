---
title: "Django分页处理"
date: "2025-06-20 11:50:47"
slug: "django-fen-ye-chu-li"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django分页处理/"
  - "/2025/06/20/Django分页处理.html"
  - "/Django分页处理/"
  - "/Django分页处理.html"
  - "/2025/06/20/django-fen-ye-chu-li/"
  - "/2025/06/20/django-fen-ye-chu-li.html"
  - "/django-fen-ye-chu-li.html"
---
关于Django的分页处理

后端逻辑操作是这样的：

```python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from man.models import Man

def home(request):
    if request.user.is_authenticated():
        user = request.user;
    else:
        user = request.user;
    items_mans = Man.objects.filter(is_show=0).order_by('-create_date').all()
    paginator_man = Paginator(items_mans,8)
    page = request.GET.get('page',1)
    try:
        items_man = paginator_man.page(page)
    except PageNotAnInteger:
        items_man = paginator_man.page(1)
    except EmptyPage:
        items_man = paginator_man.page(paginator_man.num_pages)

    return render_to_response('man/home.html',{
        'action':'man',
        'items_man':items_man,
        'user':user
        })
```

前端的页面处理是这样的

```html
<div class="row-fluid">
    <div class="span12">
        <div class="pagination pagination-centered">
            <ul>
                {% if items_man.has_previous %}
                    <li>
                        <a href="?page={{ items_man.previous_page_number }}">上一页</a>
                    </li>
                {% endif %}
                <li class='disabled'>
                    <a class="">
                        {{ items_man.number }} / {{ items_man.paginator.num_pages }}
                    </a>
                </li>
                {% if items_man.has_next %}
                <li>
                    <a href="?page={{ items_man.next_page_number }}">下一页</a>
                </li>
                {% endif %}
            </ul>
        </div>
    </div>
</div>
```
