---
title: "x509: certificate signed by unknown authority 这个问题也许没有你想的那么复杂"
date: "2025-07-03 14:20:35"
slug: "x509-certificate-signed-by-unknown-authority-zhe-ge-wen-ti-ye-xu-mei-you-ni-xiang-de-na-me-fu-za"
categories: ["技术"]
tags: ["x509", "certificate"]
aliases:
  - "/2025/07/03/x509:-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂/"
  - "/2025/07/03/x509:-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂.html"
  - "/x509:-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂/"
  - "/x509:-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂.html"
  - "/2025/07/03/x509-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂/"
  - "/2025/07/03/x509-certificate-signed-by-unknown-authority-这个问题也许没有你想的那么复杂.html"
  - "/2025/07/03/x509-certificate-signed-by-unknown-authority-zhe-ge-wen-ti-ye-xu-mei-you-ni-xiang-de-na/"
  - "/2025/07/03/x509-certificate-signed-by-unknown-authority-zhe-ge-wen-ti-ye-xu-mei-you-ni-xiang-d.html"
  - "/x509-certificate-signed-by-unknown-authority-zhe-ge-wen-ti-ye-xu-mei-you-ni-xiang-de-na-me-fu-.html"
---
`x509: certificate signed by unknown authority` 这个问题也许没有你想的那么复杂

起初是遇到了个问题

我就更新了个cdn的证书

结果golang的http库无法正常请求接口，php的file_get_contents也无法正常请求接口

报错信息

golang的http库反馈的是 x509: certificate signed by unknown authority

php的file_get_contents 反馈的是 error:14090086:SSL routines:ssl3_get_server_certificate:certificate verify failed on line 1

经过多种的猜测，发现执行完这个命令后一切都恢复了正常

```bash
yum update ca-certificates -y
```


