---
title: "Python 面向对象 －类的创建"
date: "2025-06-25 09:57:40"
slug: "python-mian-xiang-dui-xiang-lei-de-chuang-jian"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/25/Python-面向对象-－类的创建/"
  - "/2025/06/25/Python-面向对象-－类的创建.html"
  - "/Python-面向对象-－类的创建/"
  - "/Python-面向对象-－类的创建.html"
  - "/2025/06/25/python-mian-xiang-dui-xiang-lei-de-chuang-jian/"
  - "/2025/06/25/python-mian-xiang-dui-xiang-lei-de-chuang-jian.html"
  - "/python-mian-xiang-dui-xiang-lei-de-chuang-jian.html"
---
python 的面向对象的操作，使用起来还是比较简单的，比较简洁化，gowhich举个简单的例子－类的创建。代码如下

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#Filename:objvar.py
class Person:
    '''Represents a person'''
    population = 0
    def __init__(self,name):
        '''Initializes the person's data. '''
        self.name = name
        print '(Initializes %s)' % self.name
        
        #When this person is created, he/she
        #adds to the population
        Person.population += 1
        
    def __del__(self):
        ''' I am dying. '''
        print '%s says bye.' % (self.name)
        self.__class__.population -= 1
        
        if self.__class__.population != 0:
            print 'There are still %d people left.' % self.__class__.population
        else:
            print 'I am last one'
            
    def sayHi(self):
        ''' Greeting by the person, Really, That's all it does '''
        print 'Hi ,my name is %s.' % self.name
        
        
    def howMany(self):
        ''' prints the current population. '''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population
            
durban = Person('Durban')
durban.sayHi()
durban.howMany()
david = Person('David')
david.sayHi()
david.howMany()
durban.sayHi()
durban.howMany()
```

gowhich得到的结果如下：

```bash
(Initializes Durban)
Hi ,my name is Durban.
I am the only person here.
(Initializes David)
Hi ,my name is David.
We have 2 persons here.
Hi ,my name is Durban.
We have 2 persons here.
Durban says bye.
There are still 1 people left.
David says bye.
I am last one
```

第一次使用，发现`__del__`这个函数的奇妙之处，就是对象消逝的时候被调用，类似于释放内存的功能。

> Python中所有的类成员（包括数据成员）都是 公共的 ，所有的方法都是 有效的 。  
> 只有一个例外：如果你使用的数据成员名称以 双下划线前缀 比如`__privatevar`，Python的名称管理体系会有效地把它作为私有变量。  
> 这样就有一个惯例，如果某个变量只想在类或对象中使用，就应该以单下划线前缀。而其他的名称都将作为公共的，可以被其他类/对象使用。记住这只是一个惯例，并不是Python所要求的（与双下划线前缀不同）。  
> 同样，注意`__del__`方法与 destructor 的概念类似。

