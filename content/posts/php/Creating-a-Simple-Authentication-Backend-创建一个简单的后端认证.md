---
title: "Creating a Simple Authentication Backend(创建一个简单的后端认证)"
date: "2025-06-20 11:33:37"
slug: "creating-a-simple-authentication-backend-chuang-jian-yi-ge-jian-dan-de-hou-duan-ren-zheng"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Creating-a-Simple-Authentication-Backend(创建一个简单的后端认证)/"
  - "/2025/06/20/Creating-a-Simple-Authentication-Backend(创建一个简单的后端认证).html"
  - "/Creating-a-Simple-Authentication-Backend(创建一个简单的后端认证)/"
  - "/Creating-a-Simple-Authentication-Backend(创建一个简单的后端认证).html"
  - "/2025/06/20/Creating-a-Simple-Authentication-Backend-创建一个简单的后端认证/"
  - "/2025/06/20/Creating-a-Simple-Authentication-Backend-创建一个简单的后端认证.html"
  - "/2025/06/20/creating-a-simple-authentication-backend-chuang-jian-yi-ge-jian-dan-de-hou-duan-ren-zhe/"
  - "/2025/06/20/creating-a-simple-authentication-backend-chuang-jian-yi-ge-jian-dan-de-hou-duan-ren.html"
  - "/creating-a-simple-authentication-backend-chuang-jian-yi-ge-jian-dan-de-hou-duan-ren-zheng.html"
---
Creating a Simple Authentication Backend

最近由于自己的一个项目需求，使用django的时候，要使用前端认证，但是django已经写好了一个关于后端用户认证的逻辑，但是自己追求完善一个前端用户的登录和注册的逻辑，查找了很多的资料。下面是一篇关于如何设置的文章

===================================================

This is only a simple backend and isn't really useful beyond an example. More experienced users may want to skip this step  
  
For this example we are going to check to see if a user matching the username exists and that the password is their username in reverse.  
  
So, assuming you have a user called admin, the following would be correct;  
  
Username: admin  
Password: nimda

```python
# import the User object
from django.contrib.auth.models import User

# Name my backend 'MyCustomBackend'
class MyCustomBackend:

    # Create an authentication method
    # This is called by the standard Django login procedure
    def authenticate(self, username=None, password=None):

        try:
            # Try to find a user matching your username
            user = User.objects.get(username=username)

            #  Check the password is the reverse of the username
            if password == username[::-1]:
                # Yes? return the Django user object
                return user
            else:
                # No? return None - triggers default login failed
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

Making Django use your new Authentication Backend.  
  
In your settings.py add  
  
AUTHENTICATION\_BACKENDS = ( 'path.to.your.MyCustomBackend', )  
  
You might have 'project.backend.MyCustomBackend' - this could be backend.py in your project file, with a class name of MyCustomBackend  
  
Yes, security wise this is pretty pointless, but its demonstrating how a simple authentication backend works.  
Creating a Custom Authentication Backend  
\===================================================

最后我没有实现，也许是自己操作的问题，但是自己后来又细致的想了一下，既然django已经有了一个用户认证的逻辑了，并且是可以设置用户的权限和逻辑的，我觉得是可以直接使用的，不必要自己写一个了，不过对于逻辑的实现，其实是很简单的。从完成项目的角度来说，我觉得，既然已经选择了使用一个框架，就不必去追求逻辑的自我实现，如果是学习的目的的话，我到觉得这个可以细致的研究一下，O(∩\_∩)O~
