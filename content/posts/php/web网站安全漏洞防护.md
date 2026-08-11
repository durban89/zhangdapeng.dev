---
title: "web网站安全漏洞防护"
date: "2025-07-15 10:28:50"
slug: "web-wang-zhan-an-quan-lou-dong-fang-hu"
categories: ["技术"]
tags: ["漏洞"]
aliases:
  - "/2025/07/15/web网站安全漏洞防护/"
  - "/2025/07/15/web网站安全漏洞防护.html"
  - "/web网站安全漏洞防护/"
  - "/web网站安全漏洞防护.html"
  - "/2025/07/15/web-wang-zhan-an-quan-lou-dong-fang-hu/"
  - "/2025/07/15/web-wang-zhan-an-quan-lou-dong-fang-hu.html"
  - "/web-wang-zhan-an-quan-lou-dong-fang-hu.html"
---
最近网站被发现有漏洞，网安管的越来越严格了

简单说就是需要做一些基本的配置

配置如下

```bash
server_tokens off; # 隐藏版本号
proxy_hide_header X-Powered-By; # 关闭 x-powerd-by
proxy_cookie_path / "/; Path=/; Secure; HttpOnly";
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";
add_header X-Frame-Options SAMEORIGIN;
add_header Content-Security-Policy  "default-src 'self' *.qeeniao.com; script-src 'self' 'unsafe-inline' 'unsafe-hashes' *.qeeniao.com https://hm.baidu.com; style-src 'self' 'unsafe-inline' 'unsafe-hashes' *.qeeniao.com";
add_header X-XSS-Protection "1; mode=block";
add_header X-Content-Type-Options nosniff;
add_header Cache-Control  max-age=3600;

if ($request_method ~* OPTIONS) {
    return 403;
}  

```

只要在nginx的配置中加入这几项
