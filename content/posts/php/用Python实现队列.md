---
title: "用Python实现队列"
date: "2025-06-27 14:14:54"
slug: "yong-python-shi-xian-dui-lie"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/27/用Python实现队列/"
  - "/2025/06/27/用Python实现队列.html"
  - "/用Python实现队列/"
  - "/用Python实现队列.html"
  - "/2025/06/27/yong-python-shi-xian-dui-lie/"
  - "/2025/06/27/yong-python-shi-xian-dui-lie.html"
  - "/yong-python-shi-xian-dui-lie.html"
---
**用Python实现队列**

```python
#!/usr/bin/env python
queue = []
 
def enQ():
    queue.append(raw_input('Enter new string:').strip())
 
def deQ():
    if len(queue) == 0:
        print 'Can not pop from an empty queue'
    else:
        print 'Removed [',queue.pop(0),']'
 
def viewQ():
    print queue
 
CMDS = {'e':enQ,'d':deQ,'v':viewQ}
 
def showMenu():
    pr = '''
    (E)nqueue
    (D)equeue
    (V)iewqueue
    (Q)uit
    Enter choice:
    '''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choice = q
 
            print '\n You Picked:[%s]' % choice
 
            if choice not in 'devq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
 
        CMDS[choice]()
 
if __name__ == '__main__':
    showMenu()
```


