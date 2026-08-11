---
title: "在Django 模板template 中实现加法，减法，乘法，除法运算"
date: "2025-06-26 11:15:41"
slug: "zai-django-mu-ban-template-zhong-shi-xian-jia-fa-jian-fa-cheng-fa-chu-fa-yun-suan"
categories: ["技术"]
tags: ["Django", "Python"]
aliases:
  - "/2025/06/26/在Django-模板template-中实现加法，减法，乘法，除法运算/"
  - "/2025/06/26/在Django-模板template-中实现加法，减法，乘法，除法运算.html"
  - "/在Django-模板template-中实现加法，减法，乘法，除法运算/"
  - "/在Django-模板template-中实现加法，减法，乘法，除法运算.html"
  - "/2025/06/26/在Django-模板template-中实现加法-减法-乘法-除法运算/"
  - "/2025/06/26/在Django-模板template-中实现加法-减法-乘法-除法运算.html"
  - "/2025/06/26/zai-django-mu-ban-template-zhong-shi-xian-jia-fa-jian-fa-cheng-fa-chu-fa-yun-suan/"
  - "/2025/06/26/zai-django-mu-ban-template-zhong-shi-xian-jia-fa-jian-fa-cheng-fa-chu-fa-yun-suan.html"
  - "/zai-django-mu-ban-template-zhong-shi-xian-jia-fa-jian-fa-cheng-fa-chu-fa-yun-suan.html"
---
感觉很赞的一个设计，django的模板里面是用一个tags可以实现，加法，减法，乘法，除法的运算。嘿嘿

先看一下django 官方的解释

>  For creating bar charts and such, this tag calculates the ratio of a given  
>     value to a maximum value, and then applies that ratio to a constant.  
>   
>     For example::  
>   
>         <img src='bar.gif' height='10' width='{% widthratio this_value max_value 100 %}' />  
>   
>     Above, if `this_value` is 175 and `max_value` is 200, the image in  
>     the above example will be 88 pixels wide (because 175/200 = .875;  
>     .875 * 100 = 87.5 which is rounded up to 88).

这说明，widthratio 通常用来显示图表，比例时用的，一个数字占了多少百分比等。但仔细想想，如果将某些数字变成特定的数字，不就是乘除法运算了吗？请看：

```
乘法 A*B: {% widthratio A 1 B %}
除法 A/B: {% widthratio A B 1 %}

利用 add 这个filter ,可以做更疯狂的事:

计算 A^2: {% widthratio A 1 A %}
计算 (A+B)^2: {% widthratio A|add:B 1 A|add:B %}
计算 (A+B) * (C+D): {% widthratio A|add:B 1 C|add:D %}
```

变量也是可以加的哦

---

当然，这种方法在django中实现乘除法比较变态，看起来也不爽，更好的方法，是可以扩展自己的标签。在后面打算自己扩展一个计算乘法的标签，应该好很多。  
  
在django中实现其它一些简单的计算，参考这篇文章：http://www.yihaomen.com/article/python/186.htm  
  
用django template tag 的方式实现可以参考这篇文章：  
http://www.yihaomen.com/article/python/339.htm

---

参看文章：

<http://www.yihaomen.com/article/python/338.htm>

<http://www.sharejs.com/codes/python/6463>

