---
title: "Django模板语言操作"
date: "2025-06-19 13:54:27"
slug: "django-mu-ban-yu-yan-cao-zuo"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/19/Django模板语言操作/"
  - "/2025/06/19/Django模板语言操作.html"
  - "/Django模板语言操作/"
  - "/Django模板语言操作.html"
  - "/2025/06/19/django-mu-ban-yu-yan-cao-zuo/"
  - "/2025/06/19/django-mu-ban-yu-yan-cao-zuo.html"
  - "/django-mu-ban-yu-yan-cao-zuo.html"
---
方法调用要比其他的查询稍微复杂一点，下面是需要记住的几点：

1，在方法查询的时候，如果一个方法触发了异常，这个异常会传递从而导致渲染失   
败，但是如果异常有一个值为True的`silent_variable_failure`属性，这个变量会渲染成空string：

代码

```bash
>>> t = Template("My name is {{ person.first_name }}.")   

>>> class PersonClas3:   

...      def first_name(self):   

...          raise AssertionError, "foo"  

>>> p = PersonClass3()   

>>> t.render(Context({"person": p}))   

Traceback (most recent call last):   

...   

AssertionError: foo   

>>> class SilentAssetionError(AssertionError):   

...      silent_variable_failure = True   

>>> class PersonClass4:   

...      def first_name(self):   

...          raise SilentAssertionError   

>>> p = PersonClass4()   

>>> t.render(Context({"person": p}))   

"My name is ."  
```

2，方法调用仅仅在它没有参数时起作用，否则系统将继续查找下一个类型(列表索引查询)

3，显然一些方法有副作用，让系统访问它们是很愚蠢的，而且很可能会造成安全性问题。

例如你有一个BankAccount对象，该对象有一个delete()方法，模板系统不应该允许做下面的事情

```bash
I will now delete this valuable data. {{ account.delete }} 
```

为了防止这种状况，可以在方法里设置一个方法属性`alters_data`

如果设置了`alters_data=True`的话模板系统就不会执行这个方法：

代码

```python
def delete(self):   

     # Delete the account   

delete.alters_data = True  
```

### [不合法的变量怎样处理](#1)

默认情况下如果变量不存在，模板系统会把它渲染成空string，例如：

代码

```bash
>>> from django.template import Template, Context   

>>> t = Template('Your name is {{ name }}.')   

>>> t.render(Context())   

'Your name is .'   

>>> t.render(Context({'var': 'hello'}))   

'Your name is .'   

>>> t.render(Context({'NAME': 'hello'}))   

'Your name is .'   

>>> t.render(Context({'Name': 'hello'}))   

'Your name is .'  
```

系统会静悄悄地显示错误的页面，而不是产生一个异常，因为这种情况通常是人为的错误。

在现实情形下，一个web站点因为一个模板代码语法的错误而变得不可用是不可接受的。

我们可以通过设置Django配置更改Django的缺省行为，第10章扩展模板引擎会我们会讨论这个

### [玩玩Context对象](#2)

大多数情况下你初始化Context对象会传递一个字典给Context()

一旦你初始化了Context，你可以使用标准Python字典语法增减Context对象的items：

代码

```bash
>>> from django.template import Context   

>>> c = Context({"foo": "bar"})   

>>> c['foo']   

'bar'   

>>> del c['foo']   

>>> c['foo']   

''  

>>> c['newvariable'] = 'hello'   

>>> c['newvariable']   

'hello'  
```

### [Context对象是一个stack，你可以push()和pop()](#3)

如果你pop()的太多的话它将触发django.template.ContextPopException：

代码

```bash
>>> c = Context()   

>>> c['foo'] = 'first level'   

>>> c.push()   

>>> c['foo'] = 'second level'   

>>> c['foo']   

'second level'   

>>> c.pop()   

>>> c['foo']   

'first level'   

>>> c['foo'] = 'overwritten'   

>>> c['foo']   

'overwritten'   

>>> c.pop()   

Traceback (most recent call last):   

...   

django.template.ContextPopException  
```

### [if/else](#4)

`{% raw %}{% if %}{% endraw %}`标签计算一个变量值，如果是“true”，即它存在、不为空并且不是false的boolean值   
系统则会显示`{% raw %}{% if %}{% endraw %}`和`{% raw %}{% endif %}{% endraw %}`间的所有内容：

代码

```bash
{% if today_is_weekend %}   

    <p>Welcome to the weekend!</p>  

{% else %}   

    <p>Get back to work.</p>  

{% endif %}  
```

`{% raw %}{% if %}{% endraw %}`标签接受and，or或者not来测试多个变量值或者否定一个给定的变量，例如：

代码

```bash
{% if athlete_list and coach_list %}   

     Both athletes and coaches are available.   

{% endif %}   

{% if not athlete_list %}   

     There are no athletes.   

{% endif %}   

{% if athlete_list or coach_list %}   

     There are some athletes or some coaches.   

{% endif %}   

{% if not athlete_list or coach_list %}   

     There are no athletes or there are some coaches.   

{% endif %}   

{% if athlete_list and not coach_list %}   

     There are some athletes and absolutely no coaches.   

{% endif %}  
```

`{% raw %}{% if %}{% endraw %}`标签不允许同一标签里同时出现and和or，否则逻辑容易产生歧义，例如下面的标签是不合法的：

代码

```bash
{% if athlete_list and coach_list or cheerleader_list %}  
```

如果你想结合and和or来做高级逻辑，只需使用嵌套的`{% raw %}{% if %}{% endraw %}`标签即可：

代码

```bash
{% if athlete_list %}   

     {% if coach_list or cheerleader_list %}   

         We have athletes, and either coaches or cheerleaders!   

     {% endif %}   

{% endif %}  
```

多次使用同一个逻辑符号是合法的：

代码

```bash
{% if athlete_list or coach_list or parent_list or teacher_list %}  
```

没有`{% raw %}{% elif %}{% endraw %}`标签，使用嵌套的`{% raw %}{% if %}{% endraw %}`标签可以做到同样的事情：

代码

```bash
{% if athlete_list %}   

    <p>Here are the athletes: {{ athlete_list }}.</p>  

{% else %}   

    <p>No athletes are available.</p>  

     {% if coach_list %}   

        <p>Here are the coaches: {{ coach_list }}.</p>  

     {% endif %}   

{% endif %}  
```

确认使用`{% raw %}{% endif %}{% endraw %}`来关闭`{% raw %}{% if %}{% endraw %}`标签，否则Django触发TemplateSyntaxError

### [for](#5)

`{% raw %}{% for %}{% endraw %}`标签允许你按顺序遍历一个序列中的各个元素

Python的for语句语法为for X in Y，X是用来遍历Y的变量

每次循环模板系统都会渲染`{% raw %}{% for %}{% endraw %}`和`{% raw %}{% endfor %}{% endraw %}`之间的所有内容

例如，显示给定athlete_list变量来显示athlete列表：

代码

```bash
<ul>  

{% for athlete in athlete_list %}   

    <li>{{ athlete.name }}</li>  

{% endfor %}   

</ul>  
```

在标签里添加reversed来反序循环列表：

代码

```bash
{% for athlete in athlete_list reversed %}   

...   

{% endfor %}   
```

`{% raw %}{% for %}{% endraw %}`标签可以嵌套：

```bash
{% for country in countries %}   

    <h1>{{ country.name }}</h1>  

    <ul>  

     {% for city in country.city_list %}   

        <li>{{ city }}</li>  

     {% endfor %}   

    </ul>  

{% endfor %}  
```

系统不支持中断循环，如果你想这样，你可以改变你想遍历的变量来使得变量只包含你想遍历的值

类似的，系统也不支持continue语句

`{% raw %}{% for %}{% endraw %}`标签内置了一个forloop模板变量，这个变量含有一些属性可以提供给你一些关于循环的信息

1，forloop.counter表示循环的次数，它从1开始计数，第一次循环设为1，例如：

代码

```bash
{% for item in todo_list %}   

    <p>{{ forloop.counter }}: {{ item }}</p>  

{% endfor %}  
```

2，forloop.counter0类似于forloop.counter，但它是从0开始计数，第一次循环设为0   
3，forloop.revcounter表示循环中剩下的items数量，第一次循环时设为items总数，最后一次设为1   
4，forloop.revcounter0类似于forloop.revcounter，但它是表示的数量少一个，即最后一次循环时设为0   
5，forloop.first当第一次循环时值为True，在特别情况下很有用：

代码

```bash
{% for object in objects %}   

     {% if forloop.first %}<li class="first">{% else %}<li>{% endif %}   

     {{ object }}   

    </li>  

{% endfor %}  
```

6，forloop.last当最后一次循环时值为True

代码

```bash
{% for link in links %}{{ link }}{% if not forloop.last %} | {% endif %}{% endfor %}  
```

7，forloop.parentloop在嵌套循环中表示父循环的forloop：

代码

```bash
{% for country in countries %}   

    <table>  

     {% for city in country.city_list %}   

        <tr>  

            <td>Country #{{ forloop.parentloop.counter }} </td>  

            <td>City #{{ forloop.counter }}</td>  

            <td>{{ city }}</td>  

        </tr>  

     {% endfor %}   

    </table>  

{% endfor %}  
```

富有魔力的forloop变量只能在循环中得到，当模板解析器到达`{% raw %}{% endfor %}{% endraw %}`时forloop就消失了

如果你的模板context已经包含一个叫forloop的变量，Django会用`{% raw %}{% for %}{% endraw %}`标签替代它

Django会在for标签的块中覆盖你定义的forloop变量的值

在其他非循环的地方，你的forloop变量仍然可用

我们建议模板变量不要使用forloop，如果你需要这样做来访问你自定义的forloop，你可以使用forloop.parentloop

### [ifequal/ifnotequal](#6)

Django模板系统并不是一个严格意义上的编程语言，所以它并不允许我们执行Python语句

然而在模板语言里比较两个值并且在他们一致的时候显示一些内容，确实是一个在常见不过的需求了——所以Django提供了ifequal标签。

`{% raw %}{% ifequal %}{% endraw %}`比较两个值，如果相等，则显示`{% raw %}{% ifequal %}{% endraw %}`和`{% raw %}{% endifequal %}{% endraw %}`之间的所有内容：

代码

```bash
{% ifequal user currentuser %}   

    <h1>Welcome!</h1>  

{% endifequal %}  
```

参数可以是硬编码的string，单引号和双引号均可，下面的代码是合法的：

代码

```bash
{% ifequal section 'sitenews' %}   

    <h1>Site News</h1>  

{% endifequal %}   

{% ifequal section "community" %}   

    <h1>Community</h1>  

{% endifequal %}  
```

和`{% raw %}{% if %}{% endraw %}`一样，`{% raw %}{% ifequal %}{% endraw %}`标签支持`{% raw %}{% else %}{% endraw %}`

代码

```bash
{% ifequal section 'sitenews' %}   

    <h1>Site News</h1>  

{% else %}   

    <h1>No News Here</h1>  

{% endifequal %}  
```

其它的模板变量，strings，integers和小数都可以作为`{% raw %}{% ifequal %}{% endraw %}`的参数：

代码

```bash
{% ifequal variable 1 %}   

{% ifequal variable 1.23 %}   

{% ifequal variable 'foo' %}   

{% ifequal variable "foo" %}  
```

其它的Python类型，如字典、列表或booleans不能硬编码在`{% raw %}{% ifequal %}{% endraw %}`里面，下面是不合法的：

代码

```bash
{% ifequal variable True %}   

{% ifequal variable [1, 2, 3,]%}   

{% ifequal variable {'key': 'value'} %}
```

如果你需要测试某个变量是true或false，用{% if %}即可

### [注释](#7)

和HTML或编程语言如Python一样，Django模板语言允许注释{# #}，如：

代码

```bash
{# This is a comment #}
```

模板渲染时注释不会输出，一个注释不能分成多行

下面的模板渲染时会和模板中的内容一样，注释标签不会解析成注释

```bash
This is a {# comment goes here 
and spans another line #} 
test.
```

### [过滤器](#8)

本章前面提到，模板过滤器是变量显示前转换它们的值的方式，看起来像下面这样：

代码

```bash
{{ name|lower }} 
```

这将显示通过lower过滤器过滤后{{ name }}变量的值，它将文本转换成小写

使用(|)管道来申请一个过滤器

过滤器可以串成链，即一个过滤器的结果可以传向下一个

下面是escape文本内容然后把换行转换成p标签的习惯用法：

代码

```bash
{{ my_text|escape|linebreaks }}  
```

有些过滤器需要参数，需要参数的过滤器的样子：

代码

```bash
{{ bio|truncatewords:"30" }}  
```

这将显示bio标量的前30个字，过滤器参数一直使用双引号

下面是一些最重要的过滤器：

1，addslashed，在任何后斜线，单引号，双引号前添加一个后斜线

当你把一些文本输出到一个JavaScript字符串时这会十分有用

2，date，根据一个格式化string参数来格式化date或datetime对象，例如：

代码

```bash
{{ pub_date|date:"F j, Y" }}  
```

格式化string会在附录6定义

3，escape，避免给定的string里出现and符，引号，尖括号

当你处理用户提交的数据和确认合法的XML和XHTML数据时这将很有用

escape将作如下的一些转换：

代码

```bash
Converts & to &amp;   

Converts < to &lt;   

Converts > to &gt;   

Converts "(双引号) to &quot;   

Converts '(单引号) to &#39;   
```

4，length，返回值的长度，你可以在一个list或string上做此操作

或者在任何知道怎样决定自己的长度的Python对象上做此操作(即有一个__len__()方法的对象)

### [变量](#9)

变量的形式：{{ variable }}

使用句点 “.” 可以访问变量的属性.

例如{{ section.title }} 会被 section 对象的 title 属性替换.

如果你用到的变量不存在,模板系统会插入一个值:TEMPLATE_STRING_IF_INVALID ,这个值在settings中定义, 默认是一个空字符串.

### [过滤器](#10)

可以定制变量的显示格式。

{{ name|lower }}. 这将显示 {{ name }} 变量通过 lower 过滤后的值. 它将文本转换为小写.

{{ text|escape|linebreaks }} 用于将文本内容转义然后将换行转换成 <p> 标签

### [标签](#11)

{% 标签 %}

有些标签要求有开始标记和结束标记,例如： `{% raw %}{% block title %}My amazing site{% endblock %}{% endraw %}`

### [模板继承](#12)

模板继承允许你建立一个基本的”骨架”模板, 它包含你所有最常用的站点元素 并 定义了一些可以被子模板覆盖的block.

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>{% block title %}Gowhich{% endblock %}</title>
<link type="text/css" rel="stylesheet" href="style.css" />
</head>
<body>
   <div id="side">
       {% block side %}
       <ul>
           <li><a href="/index.html">主页</a></li>
           <li><a href="/blog/index.html">博客</a></li>
       </ul>
       {% endblock %}
   </div>
   <div id="content">
       {% block content %}{% endblock %}
   </div>
</body>
</html>
```

我们称它为 base.html, 定义了一些简单的 HTML 骨架文档, 你可以把它用到一些简单两列的网页上. “子” 模板的任务就是用内容填写这些空白的内容块.

### [子模板](#13)

如果你在模板中使用了 “`{% raw %}{% extends %}{% endraw %}`“ ,那么它必须是这个模板中的第一个模板 tag ，否则它就不工作

如果你需要在子模板中引用父模板中的 block 的内容,使用 “{{ block.super }}“ 变量.这在你希望在父模板的内容之后添加一些内容时会很有用.(你不必完全覆盖父模板的内容.)

### [自定义标签及过滤器库](#14)

某些应用提供自定义标签和过滤器库. 要在一个模板中访问它们, 使用 `{% raw %}{% load %}{% endraw %}` 标签:

```bash
{% load comments %} {% comment_form for blogs.entries entry.id with is_public yes %}
```

{% load %} 标签可接受空隔分隔的多个库的名字作为参数.{% load comments i18n %}

当你载入一个自定义标签或过滤器库, 只有当前模板可以使用这些标签/过滤器 — 继承链中不论是父模板还是子模板都不能使用使用这些标签和过滤器.

### [内建标签参考](#15)

block:定义一个能被子模板覆盖的块.

注释.模板引擎会忽略掉 `{% raw %}{% comment %}{% endraw %}` 和 `{% raw %}{% endcomment %}{% endraw %}` 之间的所有内容.

cycle：在循环时轮流使用给定的字符串列表中的值.

在循环之外, 在你第一次调用它时给这些字符串值定义一个不重复的名字,然后在循环中使用这个名字:

你可以使用任意数量的逗号分隔的值.只有一点请你注意,不要在值与值之间放任何空隔–仅仅只有一个逗号即可.

debug：输出完整的调试信息,包括当前的上下文及导入的模块信息.

filter：用来过滤变量的值

```bash
{% filter escape|lower %}

文本将被 HTML-转义, 并且全部转化为小写

{% end过滤器 %}
```

firstof：输出传递给它的第一个不是 False 的变量值. 如果所有的变量都是 False 那就不输出任何东西.

示例:

```bash
{% firstof var1 var2 var3 %}
```

它等价于:

```bash
{% if var1 %}
    {{ var1 }}
{% else %}{% if var2 %}
    {{ var2 }}
{% else %}{% if var3 %}
    {{ var3 }}
{% endif %}{% endif %}{% endif %}

<ul>

  {% for athlete in athlete_list %}

     <li>{{ athlete.name }}</li>

  {% endfor %}

</ul>

{% if athlete_list %}

  Number of athletes: {{ athlete_list|length }}

{% else %}

       No athletes.

{% endif %}
```

ifchanged：检查一个变量自上次循环之后是否发生了改变

and,“or“ 或 not

ifequal：若两个参数相等,输出一个内容块.

```bash
{% ifequal user.id comment.user_id %} …{% endifequal %}
```

ifnotequal：类似 ifequal, 只是它用来测试两个参数是否不等.

include：载入一个模板并根据当前上下文渲染它.用于在一个模板中包含其它模板.

模板名字可以是一个变量,也可以是一个字符串(带引号的字符串,无所谓单引号还是双引号).

```bash
{% include “foo/bar.html” %}

{% include template_name %}
```

load：装入一个自定义模板标签集.

now：显示当前日期, 根据给定的字符串决定输出格式.使用和 PHP 的 date() 函数一样的格式码。

spaceless：将HTML标签之间的空白格式化为一个空格. 空白包括空格,换行,制表符.

ssi：在页面中输出给定文件的内容.

`{% ssi /home/html/ljworld.com/includes/right_generic.html %}`如果提供了可选的 “parsed” 参数, 被包含文件的内容会使用当前的上下文作为模板代码进行求值处理:

```bash
{% ssi /home/html/ljworld.com/includes/right_generic.html parsed %}
```

要创建柱形图的话, 这个标签计算给定值与最大值的比率再乘以100,四舍五入为整数,最后输出这个整数.

```bash
<img src=”bar.gif” height=”10″ width=”{% widthratio this_value max_value 100 %}” />
```
