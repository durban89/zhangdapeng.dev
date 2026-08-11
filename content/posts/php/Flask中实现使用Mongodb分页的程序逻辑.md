---
title: "Flask中实现使用Mongodb分页的程序逻辑"
date: "2025-06-30 14:09:00"
slug: "flask-zhong-shi-xian-shi-yong-mongodb-fen-ye-de-cheng-xu-luo-ji"
categories: ["技术"]
tags: ["Python", "MongoDB", "Flask"]
aliases:
  - "/2025/06/30/Flask中实现使用Mongodb分页的程序逻辑/"
  - "/2025/06/30/Flask中实现使用Mongodb分页的程序逻辑.html"
  - "/Flask中实现使用Mongodb分页的程序逻辑/"
  - "/Flask中实现使用Mongodb分页的程序逻辑.html"
  - "/2025/06/30/flask-zhong-shi-xian-shi-yong-mongodb-fen-ye-de-cheng-xu-luo-ji/"
  - "/2025/06/30/flask-zhong-shi-xian-shi-yong-mongodb-fen-ye-de-cheng-xu-luo-ji.html"
  - "/flask-zhong-shi-xian-shi-yong-mongodb-fen-ye-de-cheng-xu-luo-ji.html"
---
实现的逻辑如下：

```python
page = int(request.args.get('page')) if request.args.get('page') else 1
    pagesize = 20
    prev_page = page - 1 if page - 1 else 1
    next_page = page + 1
 
    # 关键字查询
    keywords = request.args.get('keywords')
    start_date = request.args.get('start_date') 
    end_date = request.args.get('end_date')
 
    params = []
    params_query = {}
    if keywords:
        params.append({'title':{'$regex':'^%s' %keywords }})
        params_query['keywords'] = keywords
 
    if start_date and end_date:
        start = '%s 00:00:00' % start_date
        end = '%s 23:59:59' % end_date
        start = int(time.mktime(time.strptime(start,'%Y-%m-%d %H:%M:%S')))
        end = int(time.mktime(time.strptime(end,'%Y-%m-%d %H:%M:%S')))
        params.append({'create_time':{'$gt':start}})
        params.append({'create_time':{'$lte':end}})
 
        params_query['start_date'] = start_date
        params_query['end_date'] = end_date
 
    if params:
        # if len(params) == 1:
        #   where = params
        # else:
        where = {'$and':params} 
        itunes_sum = mongo.db.itunes.find(where).count()
        itunes = mongo.db.itunes.find(where).skip((page - 1) * pagesize).sort('create_time',-1).limit(pagesize)
    else:
        itunes_sum = mongo.db.itunes.count()
        itunes = mongo.db.itunes.find().skip((page - 1) * pagesize).sort('create_time',-1).limit(pagesize)
     
    return render_template(
            'front/spider_itunes.html',
            itunes=itunes,
            itunes_sum=itunes_sum,
            title=u"iTunes爬虫",
            prev_page=prev_page,
            next_page=next_page,
            params=params_query
    )
```

mongodb还是别扭点，常用就好了。


