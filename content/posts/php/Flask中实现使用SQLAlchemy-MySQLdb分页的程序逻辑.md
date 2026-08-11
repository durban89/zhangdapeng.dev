---
title: "Flask中实现使用SQLAlchemy  MySQLdb分页的程序逻辑"
date: "2025-06-30 14:08:58"
slug: "flask-zhong-shi-xian-shi-yong-sqlalchemy-mysqldb-fen-ye-de-cheng-xu-luo-ji"
categories: ["技术"]
tags: ["Python", "SQLAlchemy", "Flask", "MySQL"]
aliases:
  - "/2025/06/30/Flask中实现使用SQLAlchemy-MySQLdb分页的程序逻辑/"
  - "/2025/06/30/Flask中实现使用SQLAlchemy-MySQLdb分页的程序逻辑.html"
  - "/Flask中实现使用SQLAlchemy-MySQLdb分页的程序逻辑/"
  - "/Flask中实现使用SQLAlchemy-MySQLdb分页的程序逻辑.html"
  - "/2025/06/30/flask-zhong-shi-xian-shi-yong-sqlalchemy-mysqldb-fen-ye-de-cheng-xu-luo-ji/"
  - "/2025/06/30/flask-zhong-shi-xian-shi-yong-sqlalchemy-mysqldb-fen-ye-de-cheng-xu-luo-ji.html"
  - "/flask-zhong-shi-xian-shi-yong-sqlalchemy-mysqldb-fen-ye-de-cheng-xu-luo-ji.html"
---
逻辑的话还是蛮简单的，多查看一个文档就可以了。代码如下

```py
page = int(request.args.get('page')) if request.args.get('page') else 1
    pagesize = 20
    prev_page = page - 1 if page - 1 else 1
    next_page = page + 1
      
    # 关键字查询
    keywords = request.args.get('keywords')
    start_date = request.args.get('start_date') 
    end_date = request.args.get('end_date')
  
    params_query = {}
    query = Itunes.query
    if keywords:
        query = query.filter(Itunes.title.startswith(keywords))
        params_query['keywords'] = keywords
  
    if start_date and end_date:
        start = '%s 00:00:00' % start_date
        end = '%s 23:59:59' % end_date
        start = int(time.mktime(time.strptime(start,'%Y-%m-%d %H:%M:%S')))
        end = int(time.mktime(time.strptime(end,'%Y-%m-%d %H:%M:%S')))
          
        query = query.filter(Itunes.create_time > start)
        query = query.filter(Itunes.create_time <= end)
  
        params_query['start_date'] = start_date
        params_query['end_date'] = end_date
  
    if params_query: 
        itunes_sum = query.count()
        itunes = query.offset((page-1)*pagesize).limit(pagesize).all()
    else:
        itunes_sum = Itunes.query.count()
        itunes = Itunes.query.offset((page-1)*pagesize).limit(pagesize).all()
          
      
      
    return render_template(
            'front/spider_apple.html',
            itunes=itunes,
            itunes_sum=itunes_sum,
            title=u"Apple爬虫",
            prev_page=prev_page,
            next_page=next_page,
            params=params_query
    )
```


