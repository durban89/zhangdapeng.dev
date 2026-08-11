---
title: "Android中Activity之间的跳转借助Intent"
date: "2025-07-03 11:58:39"
slug: "android-zhong-activity-zhi-jian-de-tiao-zhuan-jie-zhu-intent"
categories: ["技术"]
tags: ["Android"]
aliases:
  - "/2025/07/03/Android中Activity之间的跳转借助Intent/"
  - "/2025/07/03/Android中Activity之间的跳转借助Intent.html"
  - "/Android中Activity之间的跳转借助Intent/"
  - "/Android中Activity之间的跳转借助Intent.html"
  - "/2025/07/03/android-zhong-activity-zhi-jian-de-tiao-zhuan-jie-zhu-intent/"
  - "/2025/07/03/android-zhong-activity-zhi-jian-de-tiao-zhuan-jie-zhu-intent.html"
  - "/android-zhong-activity-zhi-jian-de-tiao-zhuan-jie-zhu-intent.html"
---
相对于iOS要简单的多了。哈哈。

```java
Intent intent = new Intent(MainActivity.this, OtherActivity.class);
intent.putExtra("key","value");
startActivity(intent);
```


