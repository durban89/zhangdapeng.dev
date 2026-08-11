---
title: "Django创建登录和注册，注销"
date: "2025-06-20 11:50:39"
slug: "django-chuang-jian-deng-lu-he-zhu-ce-zhu-xiao"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Django创建登录和注册，注销/"
  - "/2025/06/20/Django创建登录和注册，注销.html"
  - "/Django创建登录和注册，注销/"
  - "/Django创建登录和注册，注销.html"
  - "/2025/06/20/Django创建登录和注册-注销/"
  - "/2025/06/20/Django创建登录和注册-注销.html"
  - "/2025/06/20/django-chuang-jian-deng-lu-he-zhu-ce-zhu-xiao/"
  - "/2025/06/20/django-chuang-jian-deng-lu-he-zhu-ce-zhu-xiao.html"
  - "/django-chuang-jian-deng-lu-he-zhu-ce-zhu-xiao.html"
---
第一步：创建应用

```python
python manage.py startapp accounts
```

第二步：url规则添加

```python
#用户的处理中心
url(r'^accounts/$','accounts.views.index',name='accounts_home'),
url(r'^accounts/register$','accounts.views.register',name='accounts_register'),
url(r'^accounts/login$','accounts.views.login',name='accounts_login'),
url(r'^accounts/logout$','accounts.views.logout',name='accounts_logout'),
```

第三步：action的添加

```python
#!-*- coding=utf-8 -*-

'''
用户中心
'''
def home(request):
    pass

'''
用户注册页
'''
def register(request):
    pass

'''
用户登录页
'''
def login(request):
    pass

'''
用户注销页accounts
'''
def logout(request):
    pass
```

第四步：template文件（模板文件的添加）的添加  
注册页面（这个页面根据自己的需求定义，项目不同，设计不同）

登录页面（这个页面根据自己的需求定义，项目不同，设计不同）

个人中心（这个页面根据自己的需求定义，项目不同，设计不同）  
  
第五步：完善action

```python
#!-*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User



def home(request):
    '''用户中心'''
    if request.user.is_authenticated():
        user = request.user;
    else:
        user = request.user;
    return render_to_response('accounts/home.html',{'user':user},context_instance=RequestContext(request));

def register(request):
    '''用户注册页'''
    template_var = {}
    form = RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            repassword = form.cleaned_data["repassword"]
            if password != repassword:
                return HttpResponse('重复登录密码与登录密码不一致');
            user = User.objects.create_user(username, email, password)
            user.save()
            validate_login(request, email, password)
            return HttpResponseRedirect(reverse("accounts_home"))
    return render_to_response('accounts/register.html',{'form':form},context_instance=RequestContext(request));

def validate_login(request, username, password):
    '''验证用户登录'''
    return_value = False
    user = authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            return_value = True
        else:
            messages.add_message(request, messages.INFO, _(u'此账户尚未激活，请联系管理员'))
    else:
        messages.add_message(request, messages.INFO, _(u'此账户不存在，请联管理员'))

    return return_value

def login(request):
    '''用户登录页'''
    template_var = {}
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            validate_login(request, form.cleaned_data["username"], form.cleaned_data["password"])
            return HttpResponseRedirect(reverse('accounts_home'))
    template_var["form"] = form
    return render_to_response('accounts/login.html', template_var, context_instance=RequestContext(request));


def logout(request):
    '''用户注销页'''
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"登录账号"), widget=forms.TextInput(attrs={'placeholder':'登录账号','class':'input-block-level'}))
  
    password=forms.CharField(label=_(u"登录密码"), 
widget=forms.PasswordInput(attrs={'placeholder':'登录密码','class':'input-block-level'}))

class RegisterForm(forms.Form):
    '''注册表单'''
    username=forms.CharField(label=_(u"登录账号"), widget=forms.TextInput(attrs={'placeholder':'登录账号','class':'input-block-level'}))
    email=forms.EmailField(label=_(u"邮件地址"), widget=forms.TextInput(attrs={'placeholder':'登录邮箱','class':'input-block-level'}))
    password=forms.CharField(label=_(u"登录密码"), widget=forms.PasswordInput(attrs={'placeholder':'登录密码','class':'input-block-level'}))
    repassword=forms.CharField(label=_(u"重复登录密码"), widget=forms.PasswordInput(attrs={'placeholder':'重复登录密码','class':'input-block-level'}))

    def clean_username(self):
        '''验证昵称'''
        username = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not username:
            return self.cleaned_data["username"];
        raise forms.ValidationError(_(u"该昵称已经被使用"));

    def clean_email(self):
        '''验证email'''
        email = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not email:
            return self.cleaned_data["email"];
        raise forms.ValidationError(_(u"改邮箱已经被使用"));
```
