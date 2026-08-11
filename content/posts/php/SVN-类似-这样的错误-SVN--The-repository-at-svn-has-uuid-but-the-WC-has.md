---
title: "svn 类似 这样的错误”svn: The repository at 'svn://xxxxx' has uuid 'XXXX', but the WC has 'XXXX'“"
date: "2025-06-24 15:29:45"
slug: "svn-lei-si-zhe-yang-de-cuo-wu-svn-the-repository-at-svnxxxxx-has-uuid-xxxx-but-the-wc-has-xxxx"
categories: ["技术"]
tags: ["SVN"]
aliases:
  - "/2025/06/24/svn-类似-这样的错误”svn:-The-repository-at-'svn://xxxxx'-has-uuid-'XXXX',-but-the-WC-has-'XXXX/"
  - "/2025/06/24/svn-类似-这样的错误”svn:-The-repository-at-'svn://xxxxx'-has-uuid-'XXXX',-but-the-WC-has-'.html"
  - "/svn-类似-这样的错误”svn:-The-repository-at-'svn://xxxxx'-has-uuid-'XXXX',-but-the-WC-has-'XXXX'“/"
  - "/svn-类似-这样的错误”svn:-The-repository-at-'svn://xxxxx'-has-uuid-'XXXX',-but-the-WC-has-'XXXX'“.html"
  - "/2025/06/24/SVN-类似-这样的错误-SVN-The-repository-at-svn-has-uuid-but-the-WC-has/"
  - "/2025/06/24/SVN-类似-这样的错误-SVN-The-repository-at-svn-has-uuid-but-the-WC-has.html"
  - "/2025/06/24/svn-lei-si-zhe-yang-de-cuo-wu-svn-the-repository-at-svnxxxxx-has-uuid-xxxx-but-the-wc-h/"
  - "/2025/06/24/svn-lei-si-zhe-yang-de-cuo-wu-svn-the-repository-at-svnxxxxx-has-uuid-xxxx-but-the-.html"
  - "/svn-lei-si-zhe-yang-de-cuo-wu-svn-the-repository-at-svnxxxxx-has-uuid-xxxx-but-the-wc-has-xxxx.html"
---
首先到你新建的svn仓库的目录外面，执行类型下面的命令

```bash
svnadmin setuuid svn仓库目录 uuid值
```

如：

```bash
svnadmin setuuid /var/svnroot/social_spider_php_client d34213a8-9156-4794-bef9-0b69dbbc01cf
```

如果你不知道uuid是多少，你可以看看你报错的那段代码：

***这里举一个我的实例***

我是想将我的david_spider_php_server仓库改为social_spider_php_client仓库，然后将代码都传到social_spider_php_client仓库

在我执行这段代码的时候：

```bash
svn switch --relocate svn://192.168.0.123/david_spider_php_server svn://192.168.0.123/social_spider_php_client ./
```

显示下面的错误：

```bash
svn: E195009: The repository at 'svn://192.168.0.123/social_spider_php_client' has uuid '7062f65b-c345-4f53-b375-9132776ade26', but the WC has 'd34213a8-9156-4794-bef9-0b69dbbc01cf'
```

于是我取用了uuid"d34213a8-9156-4794-bef9-0b69dbbc01cf"

服务器端执行如下代码:

```bash
svnadmin setuuid /var/svnroot/social_spider_php_client d34213a8-9156-4794-bef9-0b69dbbc01cf
```

然后再在客户端执行：

```bash
svn switch --relocate svn://192.168.0.123/david_spider_php_server svn://192.168.0.123/social_spider_php_client ./
```

如果一切正常，就说明没有什么问题了。

后面又遇到了一个关键的错误，在执行svn更新的操作的时候，出现了

```bash
svn: E160006: 没有版本 1
```

遇到这个错误该怎么办呢，我的解决办法是

```bash
export一份，然后重新部署
svn expor 源 新
svn co svn地址 新
```

