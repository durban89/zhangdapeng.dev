---
title: "No visible @interface for 'AFHTTPSessionManager' declares the selector 'POST:parameters:progress:success:failure:'"
date: "2025-07-15 09:50:50"
slug: "no-visible-interface-for-afhttpsessionmanager-declares-the-selector-postparametersprogresssuccessfailure"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/15/No-visible-@interface-for-'AFHTTPSessionManager'-declares-the-selector-'POST:parameters/"
  - "/2025/07/15/No-visible-@interface-for-'AFHTTPSessionManager'-declares-the-selector-'POST:parame.html"
  - "/No-visible-@interface-for-'AFHTTPSessionManager'-declares-the-selector-'POST:parameters:progress:s/"
  - "/No-visible-@interface-for-'AFHTTPSessionManager'-declares-the-selector-'POST:parameters:progre.html"
  - "/2025/07/15/No-visible-interface-for-AFHTTPSessionManager-declares-the-selector-POST-parameters-pro/"
  - "/2025/07/15/No-visible-interface-for-AFHTTPSessionManager-declares-the-selector-POST-parameters.html"
  - "/2025/07/15/no-visible-interface-for-afhttpsessionmanager-declares-the-selector-postparametersprogr/"
  - "/2025/07/15/no-visible-interface-for-afhttpsessionmanager-declares-the-selector-postparametersp.html"
  - "/no-visible-interface-for-afhttpsessionmanager-declares-the-selector-postparametersprogresssucc.html"
---
这个提示意思是 `AFHTTPSessionManager` 中没有这个方法

原因：升级后导致，原来方法被废弃，应该换成新的方法，需要增加一些参数，具体看文档

我遇到的问题解决了 是因为我的`AFNetworking`版本是4.0

所以见上面的方法替换为下面的方法

```bash
POST:parameters:headers:progress:success:failure:
```

类似的

> GET  
> DELETE  
> PUT

都需要加对应的headers参数
