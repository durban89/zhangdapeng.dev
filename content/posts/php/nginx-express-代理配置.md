---
title: "nginx + express 代理配置"
date: "2025-07-10 10:23:34"
slug: "nginx-express-dai-li-pei-zhi"
categories: ["技术"]
tags: ["NGINX", "ExpressJS"]
aliases:
  - "/2025/07/10/nginx-+-express-代理配置/"
  - "/2025/07/10/nginx-+-express-代理配置.html"
  - "/nginx-+-express-代理配置/"
  - "/nginx-+-express-代理配置.html"
  - "/2025/07/10/nginx-express-代理配置/"
  - "/2025/07/10/nginx-express-代理配置.html"
  - "/2025/07/10/nginx-express-dai-li-pei-zhi/"
  - "/2025/07/10/nginx-express-dai-li-pei-zhi.html"
  - "/nginx-express-dai-li-pei-zhi.html"
---
在node项目中，经常会有遇到需要获取访问URL地址的时候，同时也会遇到协议的问题，有时候，当我们的网站是https的时候，也希望在express中或者其他的node框架中获取到的URL地址协议也是https。  
但是奇怪的是express通过req.protocol获取到的仍然是http，经过试验通过nginx的配合能够很好的解决此方案。

示例如下：

```bash
location / {
    proxy_pass http://127.0.0.1:8080/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto https;
}
```

希望对看到的你有一些帮助。

类似的，在其他node框架中，比如koajs中，也会遇到类似的问题，配置方式也可以参考此方式，具体是否见效，需要读者自己去实践了，果然是实践出真知，按照正常来说，这些逻辑本不应该这么复杂，但是从代理的角度的来考虑的话，既然做了代理，就需要做的完整一些，需要我们对nginx代理有更多的了解。 本次的分享主要是结合了上次TypeScript + Express的一篇文章，我在进行线上部署的时候遇到的一些小知识点。
