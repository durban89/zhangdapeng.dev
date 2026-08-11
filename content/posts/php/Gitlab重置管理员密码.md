---
title: "Gitlab重置管理员密码"
date: "2025-07-02 16:01:34"
slug: "gitlab-zhong-zhi-guan-li-yuan-mi-ma"
categories: ["技术"]
tags: ["Gitlab"]
aliases:
  - "/2025/07/02/Gitlab重置管理员密码/"
  - "/2025/07/02/Gitlab重置管理员密码.html"
  - "/Gitlab重置管理员密码/"
  - "/Gitlab重置管理员密码.html"
  - "/2025/07/02/gitlab-zhong-zhi-guan-li-yuan-mi-ma/"
  - "/2025/07/02/gitlab-zhong-zhi-guan-li-yuan-mi-ma.html"
  - "/gitlab-zhong-zhi-guan-li-yuan-mi-ma.html"
---
第一步：

```bash
#Gitlab安装路径
cd /home/git/gitlab
＃进入Rails控制台
sudo -u git -H bundle exec rails console production
```

第二步：

```bash
sudo gitlab-rails console
```

or

```bash
sudo gitlab-rake rails console
```

第三步：找到对应的用户直接修改

```bash
user = User.find_by(email: 'xx@xx')
user.password = 'secret_pass'
user.password_confirmation = 'secret_pass'
user.save
```

如果不知道具体的邮箱，可以通过find来查找

```bash
user = User.find(1)
```

然后重新执行如上修改密码的步骤。

