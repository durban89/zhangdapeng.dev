---
title: "MongoDB 3.0版本 配置文件格式"
date: "2025-07-01 11:54:27"
slug: "mongodb-30-ban-ben-pei-zhi-wen-jian-ge-shi"
categories: ["技术"]
tags: ["MongoDB"]
aliases:
  - "/2025/07/01/MongoDB-3.0版本-配置文件格式/"
  - "/2025/07/01/MongoDB-3.0版本-配置文件格式.html"
  - "/MongoDB-3.0版本-配置文件格式/"
  - "/MongoDB-3.0版本-配置文件格式.html"
  - "/2025/07/01/mongodb-30-ban-ben-pei-zhi-wen-jian-ge-shi/"
  - "/2025/07/01/mongodb-30-ban-ben-pei-zhi-wen-jian-ge-shi.html"
  - "/mongodb-30-ban-ben-pei-zhi-wen-jian-ge-shi.html"
---
配置文件的格式变了

是这样子的啦：

```bash
systemLog:
   destination: file
   path: "/var/log/mongodb/mongodb.log"
   logAppend: true
storage:
   journal:
      enabled: trueprocessManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
   
...
```

如果想要添加其他参数，请到这里查看吧：http://docs.mongodb.org/manual/reference/configuration-options/


