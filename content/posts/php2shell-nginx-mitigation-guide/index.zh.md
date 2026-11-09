+++ 
title = "PHP2Shell（CVE-2026-109618 / CVE-2026-109619）漏洞：Nginx 临时防御与验证指南" 
date = 2026-11-08T10:00:00+08:00
lastmod = 2026-11-08T10:00:00+08:00
slug = "php2shell-nginx-mitigation-guide" 
draft = false 
tags = ["PHP", "Nginx", "安全漏洞", "运维", "PHP2Shell"] 
categories = ["技术分享", "安全防护"] 
+++

PHP2Shell（CVE-2026-109618 / CVE-2026-109619）漏洞：Nginx 临时防御与验证指南
一、漏洞背景

2026 年 10 月，PHP 官方披露了两个严重的远程代码执行漏洞：

CVE-2026-109618
CVE-2026-109619

这两个漏洞在社区中被称为 PHP2Shell，均可能导致未经身份验证的攻击者在受影响的 PHP 服务上执行任意代码，风险等级为严重。

与常见的 PHP 应用层漏洞不同，PHP2Shell 涉及 PHP 解释器底层的内存管理问题，攻击可能发生在正常业务代码执行之前。

因此，即使业务系统已经部署了 WAF、SQL 注入防护或应用层安全过滤，也不能据此认为 PHP2Shell 已经得到有效防御。

根据 PHP 官方安全公告，受影响的环境包括：

PHP-FPM
Apache + mod_php
php-cgi
FrankenPHP
LiteSpeed

PHP 官方认为，使用 Apache mod_php 的环境风险尤其值得关注，但其他提供 Web 请求处理能力的 PHP 部署方式同样需要排查。

1.1 受影响版本与修复版本
PHP 分支	修复版本
PHP 8.5	8.5.12
PHP 8.4	8.4.27
PHP 8.3	8.3.36
PHP 8.2	8.2.35

PHP 8.1 及更早版本已经停止上游常规安全维护。使用这些版本的用户，应优先考虑迁移到受支持版本，或者确认操作系统及商业供应商是否提供了对应的安全补丁。

特别提醒：修复 PHP 核心组件才是根本解决方案。

如果暂时无法完成 PHP 升级，可以通过 Nginx 限制部分高风险请求，作为过渡期间的辅助防护措施。但需要明确：Nginx 无法完整修复 PHP2Shell，也不能保证拦截所有利用方式。

二、Nginx 临时防御方案

在无法立即升级 PHP 的情况下，可以根据业务实际情况，在 Nginx 层面增加请求限制。

需要注意，拦截 multipart/form-data 请求仅仅是针对特定请求类型的流量限制，并不代表已经覆盖 PHP2Shell 的全部攻击路径。

以下提供三种配置方式。

方案 A：全局拦截 multipart 请求

适用场景：完全不涉及文件上传的 PHP 网站。

如果网站没有图片上传、附件上传、文件导入等业务，可以考虑在对应的 Nginx server 配置块中增加以下规则：

nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 临时限制 multipart 请求
    if ($http_content_type ~* "multipart/form-data") {
        return 403;
    }

    # 原有业务配置
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    # 其他 PHP 配置保持不变
}


配置说明：

$http_content_type：读取客户端请求中的 Content-Type 请求头。
~*：不区分大小写的正则匹配。
return 403：匹配后直接返回 HTTP 403，不再进入后续业务处理。

这种方式配置简单，适合不需要处理文件上传请求的网站。

但如果网站存在正常的文件上传业务，该规则也会将其一并拦截。

方案 B：宝塔面板（BT Panel）配置

对于使用宝塔面板管理 Nginx 的服务器，可以通过公共配置文件增加请求限制。

操作步骤：

第一步：找到 Nginx 配置文件

打开：

/www/server/nginx/conf/pathinfo.conf

第二步：增加拦截规则

在确认该文件的实际引用位置及配置上下文后，将以下规则添加到适当的位置：

nginx
# 临时限制 multipart/form-data 请求
if ($http_content_type ~* "multipart/form-data") {
    return 403;
}


原有 PATH_INFO 配置保持不变。

第三步：检查配置并重新加载 Nginx

建议先执行配置检查：

bash
nginx -t


如果输出类似：

text
nginx: the configuration file syntax is ok
nginx: configuration file test is successful


说明配置语法检查通过。

然后重新加载 Nginx：

bash
nginx -s reload


如果宝塔使用了自定义 Nginx 安装路径，应以实际安装环境为准。

注意事项：

pathinfo.conf 是否会影响所有 PHP 站点，取决于它在各个站点配置中的实际 include 位置。

如果文件只在部分 location 或特定 PHP 配置中被引用，就不能认为修改一次便会覆盖所有站点。

建议通过以下命令检查引用情况：

bash
grep -R "pathinfo.conf" /www/server/nginx/conf/


确认配置文件的引用范围后，再决定是否采用这种方式。

方案 C：局部限制，保留指定上传接口

适用场景：网站存在正常上传业务，但希望对其他 PHP 请求实施限制。

例如：

用户头像上传接口需要保留。
普通业务接口不需要接收 multipart 请求。
文件上传接口有明确的 URL 路径。

这种情况下，不建议使用宽泛的 URI 正则表达式直接放行一整类请求。

更合理的方式是将上传接口单独配置，并明确限制允许访问的请求路径和请求方法。

例如：

nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 普通业务接口不接受 multipart 请求
    location /api/ {
        if ($http_content_type ~* "multipart/form-data") {
            return 403;
        }

        # 原有 API 转发或 PHP 处理配置
    }

    # 单独配置需要保留的头像上传接口
    location = /api/v1/user/avatar {
        # 这里保留原有上传业务配置
        # 应同时配置认证、文件大小限制及上传校验
    }
}


这里使用精确匹配：

location = /api/v1/user/avatar

避免将类似路径误认为合法上传接口。

需要注意：

上传接口应当有独立的身份认证和权限校验。
应限制上传文件大小及允许的文件类型。
应避免将整个上传目录设置为可执行 PHP 的目录。
对于需要保留的上传接口，应尽快升级 PHP，而不是长期依赖白名单放行。

重要：白名单接口仍然可能受到 PHP2Shell 影响。 该配置只是业务流量管理策略，并不是针对漏洞的安全豁免。

三、Nginx 防御配置验证

配置完成后，需要进行基本的正向与反向测试，确保 Nginx 规则生效，同时没有意外影响普通业务接口。

这里需要区分两个概念：

配置验证：确认 Nginx 是否按照预期处理请求。
漏洞验证：确认 PHP 核心是否已经修复。

下面的 curl 测试只用于验证 Nginx 请求限制是否生效，不能作为 PHP2Shell 已经修复或不存在漏洞的证明。

3.1 验证 multipart 请求是否被拦截

使用 curl 发送带有 multipart/form-data 请求头的 POST 请求：

bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: multipart/form-data; boundary=----TestBoundary"


预期结果：

text
HTTP/2 403


如果返回 HTTP 403，说明当前请求命中了对应的 Nginx 拦截规则。

注意：该测试主要验证请求头匹配逻辑，并不构成真实漏洞利用测试，也不能证明所有 multipart 请求或其他攻击路径都已被阻断。

3.2 验证 JSON 接口是否正常

接下来，使用 JSON 格式发送普通 POST 请求：

bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'


预期结果：

text
HTTP/2 200


实际返回状态码需要根据业务接口判断。

例如：

200：请求处理成功。
400：请求参数不符合要求。
401：需要身份认证。
403：业务权限不足。
405：当前接口不支持 POST。

只要没有因为新增的 multipart 限制而错误拦截正常请求，就符合本项测试目的。

3.3 验证 GET 请求是否正常

使用 GET 请求检查网站基本访问是否正常：

bash
curl -i https://yourdomain.com/


预期结果：

text
HTTP/2 200


如果返回 301、302，也可能是正常的 HTTPS 跳转或业务重定向。

3.4 检查 Nginx 配置是否加载成功

除了 HTTP 请求测试，还可以检查 Nginx 配置和运行状态。

检查配置：

bash
nginx -t


检查 Nginx 进程：

bash
ps aux | grep nginx


检查错误日志：

bash
tail -n 100 /www/wwwlogs/nginx_error.log


日志路径应根据实际 Nginx 安装方式和站点配置调整。

3.5 curl 测试中的一个常见误区

在进行 POST 请求测试时，注意区分以下两个参数：

-i：输出 HTTP 响应头。
-I：发送 HEAD 请求并获取响应头。

例如：

bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'


这是正确的 POST 测试方式。

不要在需要测试 POST 请求时误用大写 -I，否则容易出现请求方法冲突，导致测试结果不符合预期。

四、其他临时安全加固措施

除了 Nginx 层面的请求限制，还建议从 PHP 运行环境、系统权限和网络访问等方面进行加固。

4.1 检查 PHP 配置

可以检查当前 PHP 配置：

bash
php -i | grep -E "memory_limit|session.upload_progress.enabled"


对于上传进度并非业务必需的应用，可以考虑关闭 PHP 上传进度功能：

ini
session.upload_progress.enabled = Off


但需要特别说明：

关闭上传进度功能并不能修复 PHP2Shell，也不能作为漏洞防御的可靠手段。

不要为了缓解该漏洞而设置：

ini
memory_limit = -1


该配置会取消 PHP 内存使用限制，可能使异常请求消耗大量服务器内存，增加拒绝服务风险。

4.2 限制 PHP 运行账户权限

建议检查 PHP-FPM 运行账户的权限：

不要使用 root 运行 PHP-FPM Worker。
尽量采用不同站点使用不同运行账户的方式。
限制 PHP 进程对系统敏感目录的访问权限。
避免 PHP 运行账户拥有不必要的系统管理权限。
对上传目录设置合理的读写权限。

即使出现远程代码执行，合理的权限隔离也有助于降低后续影响。

4.3 排查异常 PHP 进程

对于已经暴露在公网的 PHP 服务器，建议检查是否存在异常进程和可疑行为。

重点关注：

PHP-FPM Worker 是否异常启动 Shell 进程。
是否存在 PHP 进程启动未知外部程序的情况。
是否有异常的文件下载行为。
是否出现不明来源的定时任务。
是否存在近期新增的可疑 PHP 文件。
Web 目录中是否出现异常修改或新增文件。

如果发现可疑行为，不应仅通过重启 PHP-FPM 或清理日志来处理，应保留相关日志和证据，进一步排查是否已经发生入侵。

五、根本解决方案：升级 PHP

Nginx 临时规则只能作为过渡措施，不能替代 PHP 核心补丁。

PHP 官方已经发布对应安全版本：

text
PHP 8.5.12
PHP 8.4.27
PHP 8.3.36
PHP 8.2.35


建议根据当前 PHP 分支升级到对应修复版本或更高的安全版本。

升级前建议做好以下工作：

备份网站代码、数据库及 PHP 配置。
确认当前 PHP 版本和运行模式。
检查 PHP 扩展与业务代码兼容性。
在测试环境完成升级验证。
正式环境升级 PHP。
重启或重新加载 PHP-FPM。
检查 PHP 版本及服务运行状态。
验证网站上传、登录、支付及其他核心业务。

检查 PHP CLI 版本：

bash
php -v


注意：CLI 使用的 PHP 版本不一定与网站实际使用的 PHP-FPM 版本一致。

对于宝塔面板、Docker 或多 PHP 版本共存的环境，应分别检查实际提供 Web 服务的 PHP 运行实例，避免出现 CLI 已升级、网站仍运行旧版本的情况。

六、总结

PHP2Shell 是 PHP 底层安全漏洞，不能简单通过应用层过滤或单一 Nginx 规则彻底解决。

对于暂时无法完成升级的服务器，可以采取以下措施降低风险：

根据业务情况限制不必要的 multipart/form-data 请求。
对必要的上传接口实施独立的访问控制。
关闭非必要的 PHP 上传进度功能，但不要将其视为漏洞修复。
限制 PHP-FPM 运行账户权限。
排查异常进程、文件和系统行为。
尽快升级到 PHP 官方修复版本或供应商提供的安全回补版本。

最后强调：Nginx 临时拦截只是辅助防护，不是 PHP2Shell 的完整解决方案。

对于直接暴露在公网的 PHP 服务，建议优先安排安全升级。对于暂时无法修复且风险较高的系统，应考虑隔离公网访问，直到完成安全更新。

七、参考资料
PHP 官方安全公告：https://www.php.net/
PHP 官方安全更新发布信息：https://www.php.net/releases/
CISA：Critical Vulnerabilities in PHP Require Immediate Patching：https://www.cisa.gov/
Canadian Centre for Cyber Security：PHP2Shell 安全公告：https://www.cyber.gc.ca/

建议持续关注 PHP 官方安全公告及操作系统供应商的安全更新，及时完成后续补丁升级。