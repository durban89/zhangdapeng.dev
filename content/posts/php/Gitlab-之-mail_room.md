---
title: "Gitlab 之 mail_room"
date: "2025-07-03 11:59:11"
slug: "gitlab-zhi-mail-room"
categories: ["技术"]
tags: ["Gitlab"]
aliases:
  - "/2025/07/03/Gitlab-之-mail-room/"
  - "/2025/07/03/Gitlab-之-mail-room.html"
  - "/Gitlab-之-mail-room/"
  - "/Gitlab-之-mail-room.html"
  - "/2025/07/03/gitlab-zhi-mail-room/"
  - "/2025/07/03/gitlab-zhi-mail-room.html"
  - "/gitlab-zhi-mail-room.html"
---
最近使用docker部署gitlab，启动后会有一个问题，不知道哪里会一直在执行mail\_room 这个命令，查看了下配置

```bash
## Reply by email
# Allow users to comment on issues and merge requests by replying to notification emails.
# For documentation on how to set this up, see http://doc.gitlab.com/ce/incoming_email/README.html
 gitlab_rails['incoming_email_enabled'] = true
#
# # The email address including the `%{key}` placeholder that will be replaced to reference the item being replied to.
# # The `+%{key}` placeholder is added after the user part, after a `+` character, before the `@`.
 gitlab_rails['incoming_email_address'] = "gitlab-incoming+%{key}@xxxx.com"
#
# # Email account username
# # With third party providers, this is usually the full email address.
# # With self-hosted email servers, this is usually the user part of the email address.
 gitlab_rails['incoming_email_email'] = "xx@xx"
# # Email account password
 gitlab_rails['incoming_email_password'] = "xxxxx"
#
# # IMAP server host
 gitlab_rails['incoming_email_host'] = "imap.xxxx.com"
# # IMAP server port
 gitlab_rails['incoming_email_port'] = 993
# # Whether the IMAP server uses SSL
 gitlab_rails['incoming_email_ssl'] = true
# # Whether the IMAP server uses StartTLS
 gitlab_rails['incoming_email_start_tls'] = true
#
# # The mailbox where incoming mail will end up. Usually "inbox".
 gitlab_rails['incoming_email_mailbox_name'] = "inbox"
#
```

这里是启动的。

错误日志提示

```bash
2016-08-23_02:07:08.56923 /opt/gitlab/embedded/lib/ruby/2.1.0/openssl/ssl.rb:240:in `post_connection_check': hostname "imap.xxxx.com" does not match the server certificate (OpenSSL::SSL::SSLError)
```

这里的是imap.xxx.com是一个腾讯企业邮箱的imap的配置，后来查看了下具体的配置，改为了imap.exmail.qq.com,还是报错

```bash
2016-08-23_02:21:11.00526 /opt/gitlab/embedded/lib/ruby/2.1.0/net/imap.rb:1158:in `get_tagged_response': ������Ч���߲�֧�� (Net::IMAP::BadResponseError)
2016-08-23_02:21:11.00553      	from /opt/gitlab/embedded/lib/ruby/2.1.0/net/imap.rb:1210:in `block in send_command'
2016-08-23_02:21:11.00574      	from /opt/gitlab/embedded/lib/ruby/2.1.0/net/imap.rb:1192:in `send_command'
2016-08-23_02:21:11.00578      	from /opt/gitlab/embedded/lib/ruby/2.1.0/net/imap.rb:373:in `starttls'
```

具体不知道啥原因，果断将true改为false。

```bash
## Reply by email
# Allow users to comment on issues and merge requests by replying to notification emails.
# For documentation on how to set this up, see http://doc.gitlab.com/ce/incoming_email/README.html
 gitlab_rails['incoming_email_enabled'] = false
#
```

