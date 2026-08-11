---
title: "Python 面向对象"
date: "2025-06-25 09:57:54"
slug: "python-mian-xiang-dui-xiang"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/25/Python-面向对象/"
  - "/2025/06/25/Python-面向对象.html"
  - "/Python-面向对象/"
  - "/Python-面向对象.html"
  - "/2025/06/25/python-mian-xiang-dui-xiang/"
  - "/2025/06/25/python-mian-xiang-dui-xiang.html"
  - "/python-mian-xiang-dui-xiang.html"
---
python的面向对象中，关于继承这一块，使用起来与其他的语言大概木有什么区别，但是使用起来让人觉的很爽，一起看看其中的区别吧

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#!Filename: using_file.py
__author__ = 'Durban Zhang'
class SchoolMember:
    '''Represents any school member'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print 'Initialized SchoolMember: %s' % self.name
    def tell(self):
        '''Tell my detail '''
        print 'Name: "%s" Age: "%d"' % (self.name, self.age)
class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print 'Initialized Teacher %s :' % self.name
    def tell(self):
        '''Teacher Tell '''
        SchoolMember.tell(self)
        print 'Salary : "%d"' % self.salary
class Student(SchoolMember):
    '''Represents a students'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print 'Initialized Student %s :' % self.name
    def tell(self):
        '''Student tell'''
        SchoolMember.tell(self)
        print 'Marks: "%d"' % self.marks
t = Teacher('Durban',40,50000)
s = Student('David',20,100)
print #print a blank line
members = [t, s]
for member in members:
    member.tell()
```

要继承的类放在类的后面的圆括号中，对于要继承的父类，要在子类的init方法中调用父类的init方法。嘿嘿，是不是很简单

