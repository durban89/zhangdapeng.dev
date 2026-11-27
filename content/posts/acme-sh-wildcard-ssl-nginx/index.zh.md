+++
title = "使用 acme.sh 申请和管理通配符 SSL 证书：从 DNS 验证到 Nginx 自动部署"
description = "详细介绍如何使用 acme.sh 申请 Let's Encrypt 通配符 SSL 证书，支持阿里云手动 DNS 验证、Nginx 证书安装、普通用户权限配置以及中国大陆服务器网络环境适配。"
date = 2026-11-27T09:00:00+08:00
lastmod = 2026-11-27T09:00:00+08:00
draft = false
categories = ["Development"]
tags = ["Linux", "Nginx", "SSL", "HTTPS", "acme.sh", "Let's Encrypt", "DNS"]
slug = "acme-sh-wildcard-ssl-nginx"

toc = true

image = "cover.png"
image_alt = "Automated wildcard SSL certificate management with acme.sh, Nginx, and Let's Encrypt"
+++

# 使用 acme.sh 申请和管理通配符 SSL 证书

在部署网站或配置 Nginx 反向代理时，SSL/TLS 证书是实现 HTTPS 安全访问的重要组成部分。

如果拥有多个子域名，例如：

- example.com
- www.example.com
- api.example.com
- admin.example.com

为每个子域名单独申请证书，不仅增加管理成本，也让后续续期变得更加繁琐。

这时可以考虑使用通配符证书（Wildcard Certificate），通过一张证书覆盖主域名和多个一级子域名。

本文介绍如何使用 **acme.sh + Let's Encrypt + Nginx** 实现通配符证书的申请和部署，同时介绍不使用 DNS API 密钥的手动验证方式，以及普通用户运行 acme.sh 时需要注意的权限问题。

## 1. 什么是 acme.sh？

[acme.sh](https://github.com/acmesh-official/acme.sh) 是一个使用 Shell 编写的开源 ACME 协议客户端，可以自动化完成 SSL/TLS 证书的申请、续期和部署。

它具有以下特点：

- 纯 Shell 实现，依赖较少。
- 支持 Let's Encrypt、ZeroSSL 等证书颁发机构。
- 支持单域名、多域名和通配符证书。
- 支持 HTTP 和 DNS 验证方式。
- 支持多种 DNS 服务商的 API 自动验证。
- 支持将证书自动部署到 Nginx、Apache 等 Web 服务器。
- 支持定时检查和自动续期。

对于需要管理多个域名或子域名的服务器来说，acme.sh 是一个比较方便的证书管理工具。

## 2. 安装 acme.sh

首先安装必要的依赖。

以 Ubuntu/Debian 为例：

```bash
sudo apt update

sudo apt install -y curl git cron
```

正常情况下，可以使用官方安装脚本：

```bash
curl https://get.acme.sh | sh -s email=your_email@example.com
```

安装完成后，acme.sh 默认会放在当前用户的：

```text
~/.acme.sh/
```

重新加载 Shell 环境：

```bash
source ~/.bashrc
```

也可以重新连接 SSH 终端。

### 中国大陆服务器的网络问题

如果服务器部署在中国大陆，直接从 GitHub 下载安装脚本可能遇到网络超时或连接失败。

可以考虑以下方式：

1. 使用可信任的国内 Git 镜像获取 acme.sh 源码。
2. 在网络正常的电脑上下载源码，再通过 SCP 上传到服务器。
3. 使用能够正常访问 GitHub 的网络环境完成安装。

例如，下载源码后在服务器上执行：

```bash
git clone [<trusted-mirror-url>](https://gitee.com/neilpang/acme.sh.git)

cd acme.sh

./acme.sh --install -m your_email@example.com
```

注意：镜像地址需要自行确认其可信度，优先使用官方仓库或经过验证的同步源。

对于国内服务器，不建议在没有确认网络可用性的情况下开启自动升级：

```bash
acme.sh --upgrade --auto-upgrade
```

因为自动升级可能需要访问 GitHub。可以根据实际网络情况选择手动升级。

## 3. 配置默认 CA

安装完成后，建议将默认 CA 设置为 Let's Encrypt：

```bash
acme.sh --set-default-ca --server letsencrypt
```

这样后续申请证书时，就可以默认使用 Let's Encrypt。

## 4. 申请通配符证书

通配符证书通常需要使用 DNS-01 验证方式。

例如：

```text
example.com
*.example.com
```

这里需要注意：

**只申请 *.example.com 并不能覆盖 example.com 本身。**

因此，建议同时申请主域名和通配符域名。

acme.sh 支持通过 DNS API 自动添加 TXT 记录，也支持完全手动添加 DNS 记录。

下面介绍不使用阿里云 API 密钥的手动 DNS 验证方式。

### 4.1 使用手动 DNS 模式

如果不希望在服务器上保存阿里云 AccessKey，可以使用 acme.sh 的手动 DNS 验证模式。

执行：

```bash
acme.sh --issue --dns \
  -d example.com \
  -d '*.example.com' \
  --yes-I-know-dns-manual-mode-enough-go-ahead-please
```

执行后，acme.sh 会生成需要添加的 TXT 验证记录。

示例：

```text
Domain: '_acme-challenge.example.com'
TXT value: 'xxxxxxxxxxxx'

Domain: '_acme-challenge.example.com'
TXT value: 'yyyyyyyyyyyy'
```

由于同时申请了主域名和通配符域名，可能需要添加两条 TXT 记录。

### 4.2 在阿里云手动添加 TXT 记录

登录阿里云控制台：

云解析 DNS → 找到对应域名 → 解析设置 → 添加记录。

按照 acme.sh 输出的信息添加 TXT 记录。

| 配置项 | 内容 |
|---|---|
| 记录类型 | TXT |
| 主机记录 | _acme-challenge |
| 记录值 | acme.sh 输出的 TXT value |
| TTL | 默认值即可 |

如果生成了两条 TXT 记录，需要分别添加。

注意：两条记录的主机记录可以相同，但记录值不同。不要直接覆盖第一条记录。

### 4.3 检查 TXT 记录是否生效

可以使用 dig 检查：

```bash
dig TXT _acme-challenge.example.com +short
```

确认返回结果包含 acme.sh 输出的验证值。

### 4.4 完成证书签发

DNS 记录生效后，执行：

```bash
acme.sh --renew -d example.com \
  --yes-I-know-dns-manual-mode-enough-go-ahead-please
```

验证成功后，证书就会生成。

需要特别注意：

**手动 DNS 模式无法实现完全自动续期。**

每次续期都需要重新生成验证值、手动添加 TXT 记录，再执行续期命令。因此，如果希望实现无人值守的自动续期，建议使用 DNS API 或 DNS Alias 模式。

## 5. DNS Alias：不暴露主域名 API 密钥的自动续期方案

如果既不想在服务器上保存阿里云 API 密钥，又不想每隔一段时间手动添加 TXT 记录，可以考虑 DNS Alias 模式。

它的核心思路是：

1. 主域名继续托管在阿里云。
2. 准备一个独立的辅助域名，并托管到支持 DNS API 的服务商，例如 Cloudflare。
3. 在阿里云添加一条 CNAME 记录，将 ACME 验证请求指向辅助域名。
4. 通过辅助域名的 DNS API 自动完成 TXT 记录管理。

例如：

```text
_acme-challenge.example.com
    CNAME
_acme-challenge.otherdomain.com
```

然后使用：

```bash
acme.sh --issue --dns dns_cf \
  -d example.com \
  -d '*.example.com' \
  --challenge-alias otherdomain.com
```

这种方式可以避免将主域名的阿里云 API 密钥保存在服务器上。

需要注意，辅助域名的 DNS 服务商必须得到 acme.sh 支持，并正确配置对应 API 凭据。

## 6. 将证书安装到 Nginx

证书签发完成后，需要将证书安装到 Nginx 使用的目录。

这里推荐使用 acme.sh 提供的：

```bash
--install-cert
```

而不是直接使用 cp 或 ln -s。

原因是 acme.sh 不仅可以将证书复制到指定目录，还能保存安装路径和重载命令。后续续期时，可以自动更新目标证书文件并执行 Nginx 重载。

### 6.1 创建证书目录

例如：

```bash
sudo mkdir -p /etc/nginx/ssl
```

### 6.2 安装证书

假设希望自定义证书文件名：

```bash
acme.sh --install-cert -d example.com \
  --key-file /etc/nginx/ssl/my_wildcard.key \
  --fullchain-file /etc/nginx/ssl/my_wildcard.crt \
  --reloadcmd "sudo systemctl reload nginx"
```

这里有两个重要参数：

- `--key-file`：指定私钥文件。
- `--fullchain-file`：指定完整证书链文件。

Nginx 的 `ssl_certificate` 应使用完整证书链，而不是单独的服务器证书。

文件名可以完全自定义，例如 `.crt`、`.pem` 等，只需要保证 Nginx 配置中的路径一致。

另外，目标目录必须提前创建。

## 7. Nginx 配置通配符证书

证书安装完成后，在 Nginx 站点配置文件中引用证书。

例如：

```nginx
server {
    listen 80;
    server_name example.com *.example.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    http2 on;

    server_name example.com *.example.com;

    ssl_certificate /etc/nginx/ssl/my_wildcard.crt;
    ssl_certificate_key /etc/nginx/ssl/my_wildcard.key;

    ssl_protocols TLSv1.2 TLSv1.3;

    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```

这里的 `server_name` 同时包含：

```nginx
example.com *.example.com;
```

因此，同一张证书就可以用于主域名和符合通配符匹配规则的一级子域名。

需要注意：

`*.example.com` 只能匹配一级子域名，例如：

```text
www.example.com
api.example.com
admin.example.com
```

不能匹配多级子域名，例如：

```text
test.api.example.com
```

### 7.1 检查 Nginx 配置

修改配置后，先检查语法：

```bash
sudo nginx -t
```

确认没有错误后执行：

```bash
sudo systemctl reload nginx
```

## 8. 如何验证证书包含通配符域名？

可以使用 OpenSSL 查看证书中的 Subject Alternative Name：

```bash
openssl x509 \
  -in /etc/nginx/ssl/my_wildcard.crt \
  -noout \
  -ext subjectAltName
```

如果输出类似：

```text
X509v3 Subject Alternative Name:
    DNS:example.com, DNS:*.example.com
```

就说明证书同时包含主域名和通配符域名。

## 9. 普通用户运行 acme.sh 时的权限问题

实际部署中，还有一个容易遇到的问题：

**acme.sh 安装时使用的是普通用户，而 Nginx 证书目录通常位于 /etc/nginx/ssl。**

即使当前用户拥有 sudo 权限，也不代表 acme.sh 在自动续期时可以直接写入系统目录。

主要涉及两个问题：

1. 普通用户没有权限写入 Nginx 证书目录。
2. 自动续期时执行 `systemctl reload nginx` 可能需要 sudo 密码。

### 9.1 解决证书目录写入权限

假设当前用户是 ubuntu。

可以创建证书目录，并将目录所有权交给当前用户：

```bash
sudo mkdir -p /etc/nginx/ssl

sudo chown -R $USER:$USER /etc/nginx/ssl
```

这样 acme.sh 就可以直接向目录写入证书。

如果希望保留 root 所有权，可以考虑使用 ACL 为指定用户单独授予目录写入权限，而不是直接修改整个目录的所有权。

需要注意，修改目录所有权不会自动影响 Nginx 的运行权限。Nginx 通常由 root 身份运行的 Master Process 读取证书文件。

同时应确保私钥权限足够严格，避免普通用户以外的其他账户读取。

### 9.2 配置 Nginx 免密重载

自动续期时，acme.sh 需要执行：

```bash
sudo systemctl reload nginx
```

如果没有免密 sudo 配置，定时任务可能因为无法交互输入密码而失败。

首先检查 systemctl 的实际路径：

```bash
which systemctl
```

假设输出：

```text
/usr/bin/systemctl
```

创建专用 sudoers 配置：

```bash
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/systemctl reload nginx" \
  | sudo tee /etc/sudoers.d/acme-nginx
```

设置正确权限：

```bash
sudo chmod 0440 /etc/sudoers.d/acme-nginx
```

测试：

```bash
sudo systemctl reload nginx
```

如果不需要输入密码并且执行成功，说明配置生效。

这里仅允许当前用户免密执行指定的 Nginx reload 命令，而不是授予所有 sudo 命令的免密权限。

### 9.3 使用普通用户安装证书

完成以上配置后，直接使用当前普通用户执行：

```bash
acme.sh --install-cert -d example.com \
  --key-file /etc/nginx/ssl/my_wildcard.key \
  --fullchain-file /etc/nginx/ssl/my_wildcard.crt \
  --reloadcmd "sudo systemctl reload nginx"
```

特别注意：

**不要在 acme.sh 前面添加 sudo。**

例如，不建议这样执行：

```bash
sudo acme.sh --install-cert -d example.com
```

因为 sudo 可能会让程序使用 root 用户的运行环境和 `~/.acme.sh/` 目录，而之前申请的证书属于普通用户。

## 10. 常用维护命令

日常管理中，可以使用以下命令。

查看已申请的证书：

```bash
acme.sh --list
```

强制测试续期：

```bash
acme.sh --renew -d example.com --force
```

升级 acme.sh：

```bash
acme.sh --upgrade
```

启用自动升级：

```bash
acme.sh --upgrade --auto-upgrade
```

最后一项需要确保服务器能够正常访问升级源。

## 11. 总结

通过 acme.sh，可以将 SSL 证书的申请、部署和续期整合到一套自动化流程中。

本文涉及的几种方案适用于不同的使用场景：

| 方案 | 特点 | 适用场景 |
|---|---|---|
| DNS API | 自动添加和删除 TXT 记录 | 希望全自动续期 |
| 手动 DNS | 不需要 API 密钥 | 不介意定期人工操作 |
| DNS Alias | 主域名不需要 API 密钥 | 希望兼顾自动化和密钥隔离 |

实际部署时，我更倾向于使用 DNS Alias 或 DNS API 方式，减少人工维护成本。

另外，证书申请成功并不意味着部署就结束了。还需要正确配置 Nginx 证书路径、文件权限和自动重载命令。

尤其是在使用普通用户运行 acme.sh 的情况下，提前处理好目录写入权限和 sudo 免密重载，才能保证后续自动续期真正生效。

**最终目标不是仅仅申请到一张 SSL 证书，而是建立一套能够长期稳定运行、无需频繁人工干预的证书管理流程。**