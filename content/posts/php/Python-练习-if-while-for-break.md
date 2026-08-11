---
title: "Python 练习 {if} {while} {for} {break}"
date: "2025-06-24 16:17:42"
slug: "python-lian-xi-if-while-for-break"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/24/Python-练习-{if}-{while}-{for}-{break}/"
  - "/2025/06/24/Python-练习-{if}-{while}-{for}-{break}.html"
  - "/Python-练习-{if}-{while}-{for}-{break}/"
  - "/Python-练习-{if}-{while}-{for}-{break}.html"
  - "/2025/06/24/Python-练习-if-while-for-break/"
  - "/2025/06/24/Python-练习-if-while-for-break.html"
  - "/2025/06/24/python-lian-xi-if-while-for-break/"
  - "/2025/06/24/python-lian-xi-if-while-for-break.html"
  - "/python-lian-xi-if-while-for-break.html"
---
### [if操作](#1)

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#! Filename: if_statements.py
number = 23
guess = int(raw_input('Enter an integer:'))
if guess == number:
    print 'Congratulations, you guessed it.'
    print 'but you do not win any prizes!'
elif guess < number:
    print 'No, it is little higher than that'
else:
    print 'No, it is little lower than that'
    
print 'Done'
```

### [while操作](#2)

```python
#!/usr/bin/env python
#!_*_ codng=utf-8 -*-
#!Filename: while.py
number = 23;
running = True

while running:
    guess = int(raw_input('Enter an integer:'))
    if guess == number:
        print 'Congratulations, you guessed it'
        running = False
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that '
        
else:
    print 'The while loop is over'
    
print 'Done'
```

### [for操作](#3)

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#Filename: for.py
for i in range(1,5):
    print i
else:
    print 'The for loop is over'
```

### [break操作](#4)

```python
#!/usr/bin/env python
#!_*_ coding=utf-8 _*_
#FileName:break.py
while True:
    s = raw_input("Enter something:")
    if s == 'quit':
        break;
    else:
        print 'Length of the string is ', len(s)
print 'Done'
```

gowhich说输出结果，自己copy测试一下就知道了，嘿嘿

