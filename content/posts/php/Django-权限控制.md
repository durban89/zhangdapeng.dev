---
title: "Django 权限控制"
date: "2025-06-20 14:13:10"
slug: "django-quan-xian-kong-zhi"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django-权限控制/"
  - "/2025/06/20/Django-权限控制.html"
  - "/Django-权限控制/"
  - "/Django-权限控制.html"
  - "/2025/06/20/django-quan-xian-kong-zhi/"
  - "/2025/06/20/django-quan-xian-kong-zhi.html"
  - "/django-quan-xian-kong-zhi.html"
---
关于 django 权限控制，也是出于项目需求，一般的项目都差不多需要这样的权限控制

在django中，这里实现的其实是最简单的控制，非登录用户禁止访问产品管理界面，在django中只需要在view函数中增加`@login_required`修饰符即可:

```python
@login_required
def woman(request):
    if request.user.is_authenticated():
        user = request.user;
    else:
        user = request.user;

    items_woman = Woman.objects.filter(is_show=0).order_by('-create_date')[:10]

    return render_to_response('accounts/woman.html',{'user':user,'action':'woman','items':items_woman},context_instance=RequestContext(request))
```

修饰符实现了如下功能：  
  
如果用户没有登录，重定向到/account/login/，并且把当前绝对url作为next参数用get方法传递过去；  
如果已经正常登录，则直接正常执行视图函数；  
  
这样例子中需要的功能就实现了。但是这充其量是“登录限制”，而更常见的需求是“访问控制”，即区分已经登录的用户，对不同的视图有不同的访问权限。因为我们的例子中没有涉及到，所以只把相关的做法简单例举在下面：  
  
访问控制通过django的`request.user.has_perm()`实现，函数返回true和false。表示该用户是否有权限，而权限是auth应用中定义的Permission类型；User与Permission是many-to-many的关系  

django还提供了一个`@permission_required`修饰符，来限定view函数只有在User具有相应权限的情况下才能访问  

django对于每个模型类，自动增加add,change,delete三种权限，以便于控制权限，也可以自己设定自己的权限  
  
这部分代码可以自己实现

