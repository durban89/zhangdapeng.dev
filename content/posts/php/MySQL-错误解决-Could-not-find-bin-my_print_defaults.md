---
title: "MySQL 错误解决“Could not find ./bin/my_print_defaults”"
date: "2025-06-27 10:59:23"
slug: "mysql-cuo-wu-jie-jue-could-not-find-binmy-print-defaults"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/27/MySQL-错误解决“Could-not-find-./bin/my-print-defaults”/"
  - "/2025/06/27/MySQL-错误解决“Could-not-find-./bin/my-print-defaults”.html"
  - "/MySQL-错误解决“Could-not-find-./bin/my-print-defaults”/"
  - "/MySQL-错误解决“Could-not-find-./bin/my-print-defaults”.html"
  - "/2025/06/27/MySQL-错误解决-Could-not-find-bin-my-print-defaults/"
  - "/2025/06/27/MySQL-错误解决-Could-not-find-bin-my-print-defaults.html"
  - "/2025/06/27/mysql-cuo-wu-jie-jue-could-not-find-binmy-print-defaults/"
  - "/2025/06/27/mysql-cuo-wu-jie-jue-could-not-find-binmy-print-defaults.html"
  - "/mysql-cuo-wu-jie-jue-could-not-find-binmy-print-defaults.html"
---
Mysql 错误解决“Could not find ./bin/my\_print\_defaults”

运行下面这条语句就可以搞定了。

```zsh
sudo mysql_install_db --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data &
```
