---
title: "Scrapy 实现MySQLdb Pipline存储数据"
date: "2025-06-30 14:09:07"
slug: "scrapy-shi-xian-mysqldb-pipline-cun-chu-shu-ju"
categories: ["技术"]
tags: ["Python", "Scrapy", "MySQL"]
aliases:
  - "/2025/06/30/Scrapy-实现MySQLdb-Pipline存储数据/"
  - "/2025/06/30/Scrapy-实现MySQLdb-Pipline存储数据.html"
  - "/Scrapy-实现MySQLdb-Pipline存储数据/"
  - "/Scrapy-实现MySQLdb-Pipline存储数据.html"
  - "/2025/06/30/scrapy-shi-xian-mysqldb-pipline-cun-chu-shu-ju/"
  - "/2025/06/30/scrapy-shi-xian-mysqldb-pipline-cun-chu-shu-ju.html"
  - "/scrapy-shi-xian-mysqldb-pipline-cun-chu-shu-ju.html"
---
这里使用的是MySQLdb-Python，用着还行，嘿嘿

代码看这里的

```python
from scrapy.contrib.exporter import XmlItemExporter,JsonItemExporter,JsonLinesItemExporter,CsvItemExporter
from scrapy import signals,log
from scrapy.exceptions import DropItem
import datetime,pymongo
import MySQLdb
 
class MysqlDBPipline(object):
    def __init__(self,mysql_host,mysql_db,mysql_user,mysql_passwd):
        self.mysql_host = mysql_host
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
     
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_passwd=crawler.settings.get('MYSQL_PASSWD'),
            mysql_db=crawler.settings.get('MYSQL_DB')
        )
     
    def open_spider(self,spider):
        try:
            self.conn = MySQLdb.connect(
                            user=self.mysql_user, 
                            passwd=self.mysql_passwd, 
                            db=self.mysql_db, 
                            host=self.mysql_host, 
                            charset="utf8", 
                            use_unicode=True
                        )
            self.cursor = self.conn.cursor()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
     
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
                         
    def process_item(self,item,spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
                 
        if valid:
            for n in range(len(item['title'])):
                try:
                    value = [item['title'][n],item['url'][n],item['create_time']]
                    self.cursor.execute('INSERT INTO itunes (title,url,create_time) VALUES (%s,%s,%s)',value)
                    self.conn.commit()
                except MySQLdb.Error,e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                     
            log.msg("Question added to MySQLdb database!", level=log.DEBUG, spider=spider)
             
        return item
```

配置文件加入

```python
ITEM_PIPELINES = {
    'apple.pipelines.MysqlDBPipline':100
}
```


