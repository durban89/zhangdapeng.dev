---
title: "Scrapy 实现Mongodb Pipline存储数据"
date: "2025-06-30 14:09:04"
slug: "scrapy-shi-xian-mongodb-pipline-cun-chu-shu-ju"
categories: ["技术"]
tags: ["Python", "Scrapy", "MongoDB"]
aliases:
  - "/2025/06/30/Scrapy-实现Mongodb-Pipline存储数据/"
  - "/2025/06/30/Scrapy-实现Mongodb-Pipline存储数据.html"
  - "/Scrapy-实现Mongodb-Pipline存储数据/"
  - "/Scrapy-实现Mongodb-Pipline存储数据.html"
  - "/2025/06/30/scrapy-shi-xian-mongodb-pipline-cun-chu-shu-ju/"
  - "/2025/06/30/scrapy-shi-xian-mongodb-pipline-cun-chu-shu-ju.html"
  - "/scrapy-shi-xian-mongodb-pipline-cun-chu-shu-ju.html"
---
这里只提供一下代码：具体逻辑很简单

需要安装的就是pymongo

```python
from scrapy.contrib.exporter import XmlItemExporter,JsonItemExporter,JsonLinesItemExporter,CsvItemExporter
from scrapy import signals,log
from scrapy.exceptions import DropItem
import datetime,pymongo
import MySQLdb
  
class MongoDBPipeline(object):
    def __init__(self,mongo_server,mongo_port,mongo_db,mongo_collection):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection
          
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGO_SERVER'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )
          
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_server,self.mongo_port)
        self.db = self.client[self.mongo_db]
        self.collection = self.mongo_collection
          
    def close_spider(self,spider):
        self.client.close()
          
    def process_item(self,item,spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            for n in range(len(item['title'])):
                self.db[self.collection].insert(
                    {
                        'url':item['url'][n],
                        'title':item['title'][n],
                        'create_time':item['create_time']
                    }
                )
                  
            # self.db[self.collection].insert(dict(item))
            log.msg("Question added to MongoDB database!", level=log.DEBUG, spider=spider)
              
        return item
```

同时不要忘记了加进来实现，配置文件加入下面代码

```python
ITEM_PIPELINES = {
    'apple.pipelines.MongoDBPipeline':200
}
```

