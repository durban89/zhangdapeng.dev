---
title: "Spark Web 请求api接口的方法"
date: "2025-07-03 11:08:32"
slug: "spark-web-qing-qiu-api-jie-kou-de-fang-fa"
categories: ["技术"]
tags: ["Spark"]
aliases:
  - "/2025/07/03/Spark-Web-请求api接口的方法/"
  - "/2025/07/03/Spark-Web-请求api接口的方法.html"
  - "/Spark-Web-请求api接口的方法/"
  - "/Spark-Web-请求api接口的方法.html"
  - "/2025/07/03/spark-web-qing-qiu-api-jie-kou-de-fang-fa/"
  - "/2025/07/03/spark-web-qing-qiu-api-jie-kou-de-fang-fa.html"
  - "/spark-web-qing-qiu-api-jie-kou-de-fang-fa.html"
---
这里使用了com.github.kevinsawicki.http这个包

maven【很不错的包管理器】安装方式：

```bash
<dependency>
    <groupId>com.github.kevinsawicki</groupId>
    <artifactId>http-request</artifactId>
    <version>6.0</version>
</dependency>
```

使用方法

```java
import com.github.kevinsawicki.http.HttpRequest;
```

//这里只演示post提交的方法

```java
HttpRequest request = HttpRequest.post("http://xxxx.xxxx.xxxx.xxxx:8895/xxxxxx/general2/xxxx/xxxxxx.html");
request.part("data", "data");
request.part("sign", "sign");
if (request.ok()) {
    BufferedReader reader = request.bufferedReader();
    StringBuffer strBuffer = new StringBuffer();
    String inputLine;
    try {
        while ((inputLine = reader.readLine()) != null) {
            strBuffer.append(inputLine);
        }
    } catch (Exception e) {
        System.out.println(e);
    }
    reader.close();
    //到这里就把数据解出来了，针对于java，还是有点小麻烦，
    HashMap<String, String> jsonMap = JSON.parseObject(strBuffer.toString(), new HashMap<String, String>().getClass());
    System.out.println(jsonMap);
    for (String key : jsonMap.keySet()) {
        String str = jsonMap.get(key);
        System.out.println(key + ":" + str);
    }
    System.out.println("Status was updated");
}
```

//好了到这里就可以了，说实话java是底层语言吧，是的，我们用的php是的估计都是人家用c封装好的了，直接一个curl就能得到结果了，你也可以用java写个curl，也不是啥问题

========================================

=Spark Framework - A tiny Java web framework==

========================================


