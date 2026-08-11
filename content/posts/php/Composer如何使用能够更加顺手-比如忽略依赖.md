---
title: "composer如何使用能够更加顺手（比如忽略依赖）"
date: "2025-07-14 14:45:10"
slug: "composer-ru-he-shi-yong-neng-gou-geng-jia-shun-shou-bi-ru-hu-lve-yi-lai"
categories: ["技术"]
tags: ["PHP", "Composer"]
aliases:
  - "/2025/07/14/composer如何使用能够更加顺手（比如忽略依赖）/"
  - "/2025/07/14/composer如何使用能够更加顺手（比如忽略依赖）.html"
  - "/composer如何使用能够更加顺手（比如忽略依赖）/"
  - "/composer如何使用能够更加顺手（比如忽略依赖）.html"
  - "/2025/07/14/Composer如何使用能够更加顺手-比如忽略依赖/"
  - "/2025/07/14/Composer如何使用能够更加顺手-比如忽略依赖.html"
  - "/2025/07/14/composer-ru-he-shi-yong-neng-gou-geng-jia-shun-shou-bi-ru-hu-lve-yi-lai/"
  - "/2025/07/14/composer-ru-he-shi-yong-neng-gou-geng-jia-shun-shou-bi-ru-hu-lve-yi-lai.html"
  - "/composer-ru-he-shi-yong-neng-gou-geng-jia-shun-shou-bi-ru-hu-lve-yi-lai.html"
---
在用laravel做开发过程中

遇到一个问题，就是使用composer安装包

第一个问题，composer安装了什么，我看不到，我是不放心的，或者安装了哪些库，如果慢的话又是卡在了哪里

第二个问题，经常遇到，本地使用的库，在另外一个地方用不到，但是安装的时候总要依赖php的版本，但是又不想切换版本

下面这个命令解决了以上两个问题，其实之所以记录，就是想知道为什么同样的问题遇到了两次，我依然还是会忘记

```bash
composer install -vvv --ignore-platform-reqs
```

经过回忆，因为每次遇到了我没记录下来，另外是使用的这几次时间上相隔太远以至于没有了记忆。（注意上面命令中install与require的区别）

这里推荐一个composer的使用说明，比较详细，之前找了很多，都是写的很乱，无法详细的了解，想看的点击[这里](https://learnku.com/docs/composer/2018/03-cli/2084)。
