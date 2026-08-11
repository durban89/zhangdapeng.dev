---
title: "Python Web开发中常用的第三方库"
date: "2025-06-30 14:09:10"
slug: "python-web-kai-fa-zhong-chang-yong-de-di-san-fang-ku"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/30/Python-Web开发中常用的第三方库/"
  - "/2025/06/30/Python-Web开发中常用的第三方库.html"
  - "/Python-Web开发中常用的第三方库/"
  - "/Python-Web开发中常用的第三方库.html"
  - "/2025/06/30/python-web-kai-fa-zhong-chang-yong-de-di-san-fang-ku/"
  - "/2025/06/30/python-web-kai-fa-zhong-chang-yong-de-di-san-fang-ku.html"
  - "/python-web-kai-fa-zhong-chang-yong-de-di-san-fang-ku.html"
---
在这里我将介绍一些Python Web开发中常用的第三方库。基本适用于Django以外的Web框架(Pyramid, Flask, Tornado, Web.py, Bottle等).

## [ORM](#1)

SQLAlchemy， 在ORM方面，首选SQLAlchemy，没有之一!

支持SQLite, PostgreSQL, MySQL, Oracle, MS-SQL, Firebird, Sybase等主流关系数据库系统

支持的Python环境有Python2、Python3，PyPy以及Jython。

主要的特性请移步 Key Features of SQLAlchemy

推荐和数据库迁移工具Alemic搭配使用

MongoEngine， 如果你用MongoDB，推荐MongoEngine.

## [Template Engine](#2)

在模板引擎方便选择也是比较多， 有Chameleon、Jinja2、Mako等可供选择，用过Chameleon和Jinja2，性能都非常好.

## [Form Engine](#3)

WTForms，推荐！

## [Cache Engine & Session Store](#4)

Beaker 缓存和Session管理首选Beaker， 没有之一！ 可以搭配文件、dbm、memcached、内存、数据库、NoSQL等作为存储后端. 如果你用Pyramid作为Web框架，那么可以直接使用pyramid\_beaker.

## [环境构建](#5)

buildout 很强大，参考 用Buildout来构建Python项目

virtualenv 这个大家应该都用过，简单易用

## [任务队列](#6)

Celery （芹菜）一个分布式异步任务队列， 很强大！

RQ 这是一个轻量级的任务队列，基于Redis， 可以尝试一下。

## [WebServer](#7)

Gunicorn , 推荐！

uWSGI

mod_wsgi，搭配Apache一起使用

## [工具](#8)

Fabric, 可以通过它完成自动化部署和常规的运维等工作。《Fabric-让部署变得简单》\_PPT

Supervisor 一个强大的进程管理工具，用来管理各种服务（比如Gunicorn、Celery等），服务挂掉时 Supervisor 会帮自动重启服务。

## [导出报表数据](#9)

Tablib，这个挺好用，支持导出Excel, JSON, YAML, HTML, TSV, CSV格式数据， 我创建了一个Pyramid插件可以集成到Pyramid项目中使用 pyramid\_tablib

导出PDF有reportlab、PyPDF2

## [第三方身份验证](#10)

velruse, 支持各大网站的身份验证， 国内部分我已经加入了Weibo、Douban、QQ、Taobao、Renren，并merge到主版本库中。欢迎使用！

## [Helper](#11)

webhelpers, 提供了一系列实用函数


