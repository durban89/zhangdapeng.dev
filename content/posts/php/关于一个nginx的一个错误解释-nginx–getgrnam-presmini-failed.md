---
title: "关于一个nginx的一个错误解释“nginx – getgrnam (“presmini”) failed”"
date: "2025-06-11 10:34:08"
slug: "guan-yu-yi-ge-nginx-de-yi-ge-cuo-wu-jie-shi-nginx-getgrnam-presmini-failed"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/06/11/关于一个nginx的一个错误解释“nginx-–-getgrnam-(“presmini”)-failed”/"
  - "/2025/06/11/关于一个nginx的一个错误解释“nginx-–-getgrnam-(“presmini”)-failed”.html"
  - "/关于一个nginx的一个错误解释“nginx-–-getgrnam-(“presmini”)-failed”/"
  - "/关于一个nginx的一个错误解释“nginx-–-getgrnam-(“presmini”)-failed”.html"
  - "/2025/06/11/关于一个nginx的一个错误解释-nginx–getgrnam-presmini-failed/"
  - "/2025/06/11/关于一个nginx的一个错误解释-nginx–getgrnam-presmini-failed.html"
  - "/2025/06/11/guan-yu-yi-ge-nginx-de-yi-ge-cuo-wu-jie-shi-nginx-getgrnam-presmini-failed/"
  - "/2025/06/11/guan-yu-yi-ge-nginx-de-yi-ge-cuo-wu-jie-shi-nginx-getgrnam-presmini-failed.html"
  - "/guan-yu-yi-ge-nginx-de-yi-ge-cuo-wu-jie-shi-nginx-getgrnam-presmini-failed.html"
---
I got this error after installing nginx and trying to run passenger for my ruby apps. I understood that I needed to run nginx as the same user I was using to run my ruby apps. To do this, I had to use the “user” directive in the nginx.conf file to define the startup user to be “presmini” (the same user running my ruby apps). What I screwed up was that the failure（他也遇到了，其实我也遇到了）

```sh
[emerg]: getgrnam(“presmini”) failed in /opt/nginx/conf/nginx.conf:1
```

上面是错误提示的说明。

is that I wasn’t explicity defining a group in the nginx.conf file, and so it was defaulting to something that does exist. Since I’m on a mac, I just changed the “user” directive in the nginx.conf file to:

原因是没有添加组

```sh
user presmini staff
```

修改成类似这样的就可以了
