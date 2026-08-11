---
title: "Spark Framework JSON解析"
date: "2025-07-03 11:08:35"
slug: "spark-framework-json-jie-xi"
categories: ["技术"]
tags: ["Spark"]
aliases:
  - "/2025/07/03/Spark-Framework-JSON解析/"
  - "/2025/07/03/Spark-Framework-JSON解析.html"
  - "/Spark-Framework-JSON解析/"
  - "/Spark-Framework-JSON解析.html"
  - "/2025/07/03/spark-framework-json-jie-xi/"
  - "/2025/07/03/spark-framework-json-jie-xi.html"
  - "/spark-framework-json-jie-xi.html"
---
这里使用了com.alibaba.fastjson这个包

maven【很不错的包管理器】安装方式：

```bash
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.12</version>
</dependency>
```

使用方法

```java
import com.alibaba.fastjson.JSON;
```

//字符串转换为可使用的对象【Map】

```java
String str = "";//这里就是一个json 字符串
JSON.parseObject(str);
HashMap<String, String> jsonMap = JSON.parseObject(str, new HashMap<String, String>().getClass());
//去除里面的值
for(String key : jsonMap.keySet()) {
    String str = jsonMap.get(key);
    System.out.println(key + ":" + str);
}
//将 对象 【HashMap】转化为json 字符串
HashMap<String, String> map = new HashMap<>();
map.put("data","data");
map.put("sign","sign");
String jsonString = JSON.toJSONString(map);
```

这里设置路由跟请求回调方法

```java
get("/jsontest", "application/json", (req, res) -> {
//实现结果的代码，比如上面生成的结果 jsonString
//return jsonString
});
```

========================================

==Spark Framework - A tiny Java web framework==

========================================


