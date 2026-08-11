---
title: "eui_skins文件夹外eui文件不加载的怎么处理"
date: "2025-07-11 11:15:22"
slug: "eui-skins-wen-jian-jia-wai-eui-wen-jian-bu-jia-zai-de-zen-me-chu-li"
categories: ["技术"]
tags: ["Egret"]
aliases:
  - "/2025/07/11/eui-skins文件夹外eui文件不加载的怎么处理/"
  - "/2025/07/11/eui-skins文件夹外eui文件不加载的怎么处理.html"
  - "/eui-skins文件夹外eui文件不加载的怎么处理/"
  - "/eui-skins文件夹外eui文件不加载的怎么处理.html"
  - "/2025/07/11/eui-skins-wen-jian-jia-wai-eui-wen-jian-bu-jia-zai-de-zen-me-chu-li/"
  - "/2025/07/11/eui-skins-wen-jian-jia-wai-eui-wen-jian-bu-jia-zai-de-zen-me-chu-li.html"
  - "/eui-skins-wen-jian-jia-wai-eui-wen-jian-bu-jia-zai-de-zen-me-chu-li.html"
---
eui\_skins文件夹外eui文件不加载的怎么处理

修改egretProperties.json配置文件（关闭Egret UI Editor的情况下）

加入如下配置

```json
"eui": {
  "exmlRoot": [
    "resource/eui_skins",
    "resource/scene"
  ],
  "themes": [
    "resource/default.thm.json"
  ],
  "exmlPublishPolicy": "commomjs"
},
```

默认配置是没有这个选项的
