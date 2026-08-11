---
title: "Flask SqlAlchemy Like 查询"
date: "2025-07-22T18:31:27.567711+08:00"
draft: false
slug: "flask-sqlalchemy-like-cha-xun"
categories: ["技术"]
tags: ["Flask", "SqlAlchemy"]
aliases:
  - "/2025/07/22/flask-sqlalchemy-like-查询"
  - "/2025/07/22/flask-sqlalchemy-like-查询/"
---

SQLAlchemy 如何进行 mysql的Like查询呢？

```py
Article.query.join(Category).filter(Article.title.like("%%s%", name), Article.is_deleted == 0).order_by(Article.id.desc())
```
