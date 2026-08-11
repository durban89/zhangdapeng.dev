---
title: "Django 模板里面for循环常用的方法"
date: "2025-06-19 10:48:14"
slug: "django-mu-ban-li-mian-for-xun-huan-chang-yong-de-fang-fa"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/19/Django-模板里面for循环常用的方法/"
  - "/2025/06/19/Django-模板里面for循环常用的方法.html"
  - "/Django-模板里面for循环常用的方法/"
  - "/Django-模板里面for循环常用的方法.html"
  - "/2025/06/19/django-mu-ban-li-mian-for-xun-huan-chang-yong-de-fang-fa/"
  - "/2025/06/19/django-mu-ban-li-mian-for-xun-huan-chang-yong-de-fang-fa.html"
  - "/django-mu-ban-li-mian-for-xun-huan-chang-yong-de-fang-fa.html"
---
`{% raw %}{% for %}{% endraw %}` 允许我们在一个序列上迭代。与Python的for 语句的情形类似，循环语法是 for X in Y ，Y是要迭代的序列  
而X是在每一个特定的循环中使用的变量名称。每一次循环中，模板系统会渲染在{% raw %}{% for %} and {% endfor %}{% endraw %}  中的所有内  
容。  
例如，给定一个运动员列表athlete_list 变量，我们可以使用下面的代码来显示这个列表：

```html
<ul>
{% for athlete in athlete_list %}
<li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

给标签增加一个reversed 使得该列表被反向迭代：

```html
{% for athlete in athlete_list reversed %}
...
{% endfor %}
```

可以嵌套使用 `{% raw %}{% for %}{% endraw %}` 标签：

```html
{% for country in countries %}
<h1>{{ country.name }}</h1>
<ul>

{% for city in country.city_list %}
<li>{{ city }}</li>
{% endfor %}
</ul>
{% endfor %}
```

Django不支持退出循环操作。如果我们想退出循环，可以改变正在迭代的变量，让其仅仅包含需要迭代的项目。同  
理，Django也不支持continue语句，我们无法让当前迭代操作跳回到循环头部。  
`{% raw %}{% for %}{% endraw %}` 标签在循环中设置了一个特殊的 `forloop` 模板变量。这个变量能提供一些当前循环进展的信息：  
forloop.counter 总是一个表示当前循环的执行次数的整数计数器。这个计数器是从1开始的，  
所以在第一次循环时`forloop.counter` 将会被设置为1。例子如下：

```html
{% for item in todo_list %}
<p>{{ forloop.counter }}: {{ item }}</p>
{% endfor %}
```

`forloop.counter0` 类似于 `forloop.counter` ，但是它是从0计数的。第一次执行循环时这个变量会被设置为0。  
`forloop.revcounter` 是表示循环中剩余项的整型变量。在循环初次执行时 `forloop.revcounter` 将被设置为序列中项的总  
数。最后一次循环执行中，这个变量将被置1。  
`forloop.revcounter0` 类似于 `forloop.revcounter` ，但它以0做为结束索引。在第一次执行循环时，该变量会被置为序  
列的项的个数减1。在最后一次迭代时，该变量为0。  
`forloop.first` 是一个布尔值。在第一次执行循环时该变量为True，在下面的情形中这个变量是很有用的。

```html
{% for object in objects %}
{% if forloop.first %}<li class="first">{% else %}<li>{% endif %}
{{ object }}
</li>
{% endfor %}
```

`forloop.last` 是一个布尔值；在最后一次执行循环时被置为True。一个常见的用法是在一系列的链接之间放置管道符`（|）`

```html
{% for link in links %}{{ link }}{% if not forloop.last %} | {% endif %}{% endfor %}
```

The above template code might output something like this::  
`Link1 | Link2 | Link3 | Link4 ` 

`forloop.parentloop` 是一个指向当前循环的上一级循环的 forloop 对象的引用（在嵌套循环的情况下）。例子在此：

```html
{% for country in countries %}
<table>
{% for city in country.city_list %}
<tr>
<td>Country #{{ forloop.parentloop.counter }}</td>
<td>City #{{ forloop.counter }}</td>
<td>{{ city }}</td>
</tr>
{% endfor %}
</table>
{% endfor %}
```

forloop 变量仅仅能够在循环中使用，在模板解析器碰到 `{% endfor %}` 标签时， forloop 就不可访问了。  
Context和forloop变量  
在一个`{% raw %}{% for %}{% endraw %}` 块中，已存在的变量会被移除，以避免 forloop 变量被覆盖。Django会把这个变量移动到  
`forloop.parentloop` 中。通常我们不用担心这个问题，但是一旦我们在模板中定义了 forloop 这个变量（当然我们反对这  
样做），在`{% raw %}{% for %}{% endraw %}` 块中它会在 `forloop.parentloop` 被重新命名。
