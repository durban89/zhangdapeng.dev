+++
title = "PHP2Shell (CVE-2026-109618 / CVE-2026-109619): Nginx Temporary Mitigation and Verification Guide"
date = 2026-11-08T10:00:00+08:00
lastmod = 2026-11-08T10:00:00+08:00
slug = "php2shell-nginx-mitigation-guide"
draft = false

tags = ["PHP", "Nginx", "Security Vulnerability", "Server Administration", "PHP2Shell"]
categories = ["Technology", "Linux", "Development"]

image = "./cover.png"
image_alt = "PHP2Shell security vulnerability mitigation with Nginx, featuring server protection, multipart request filtering, configuration verification, and PHP security upgrades."

toc = true
+++

# PHP2Shell (CVE-2026-109618 / CVE-2026-109619): Nginx Temporary Mitigation and Verification Guide

## 1. Vulnerability Overview

In October 2026, the PHP project disclosed two critical remote code execution vulnerabilities:

- CVE-2026-109618
- CVE-2026-109619

Collectively known in the security community as **PHP2Shell**, these vulnerabilities may allow unauthenticated attackers to execute arbitrary code on affected PHP servers.

Unlike typical application-level vulnerabilities, PHP2Shell involves memory management issues within the PHP interpreter itself. Exploitation may occur before normal application code is executed.

Therefore, having a WAF, SQL injection protection, or application-level security filters in place does not mean your server is protected against PHP2Shell.

According to the PHP security advisories, potentially affected deployment environments include:

- PHP-FPM
- Apache with mod_php
- php-cgi
- FrankenPHP
- LiteSpeed

The PHP project has highlighted Apache mod_php deployments as particularly concerning. However, other PHP deployment models capable of processing web requests should also be reviewed.

### 1.1 Affected Versions and Fixed Releases

| PHP Branch | Fixed Version |
|---|---|
| PHP 8.5 | 8.5.12 |
| PHP 8.4 | 8.4.27 |
| PHP 8.3 | 8.3.36 |
| PHP 8.2 | 8.2.35 |

PHP 8.1 and earlier versions are no longer covered by regular upstream security maintenance.

If you are running one of these older versions, prioritize migrating to a supported PHP release or verify whether your operating system vendor or commercial PHP provider offers an applicable security backport.

**Important:** Updating the PHP core is the only fundamental way to address the underlying vulnerability.

If an immediate PHP upgrade is not possible, you can introduce additional request restrictions at the Nginx layer as a temporary mitigation.

However, Nginx cannot fully fix PHP2Shell or guarantee protection against every possible exploitation method.

## 2. Temporary Nginx Mitigation

If you cannot upgrade PHP immediately, you can introduce request restrictions at the Nginx layer based on your application's requirements.

One important distinction: blocking `multipart/form-data` requests only restricts a particular category of HTTP traffic. It does not cover every potential PHP2Shell attack vector.

The following sections describe three possible configurations.

### Option A: Block All multipart/form-data Requests

**Suitable for:** PHP websites that do not support file uploads.

If your website does not provide image uploads, attachment uploads, file imports, or other multipart-based functionality, you can add the following rule to the corresponding Nginx `server` block:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Temporarily block multipart requests
    if ($http_content_type ~* "multipart/form-data") {
        return 403;
    }

    # Existing application configuration
    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    # Keep other PHP configuration unchanged
}
```

**Configuration details:**

- `$http_content_type`: Reads the client's `Content-Type` request header.
- `~*`: Performs a case-insensitive regular expression match.
- `return 403`: Immediately returns an HTTP 403 Forbidden response when the condition matches.

This approach is simple and suitable for websites that do not need to process file uploads.

However, it will also block legitimate upload requests if your application relies on them.

### Option B: Configuration for aaPanel (BT Panel)

For servers managed through aaPanel (BT Panel), you can introduce request restrictions through a shared Nginx configuration file.

**Step 1: Locate the Nginx configuration file**

Open:

```bash
/www/server/nginx/conf/pathinfo.conf
```

**Step 2: Add the blocking rule**

After confirming where this file is included and which configuration context it belongs to, add the following rule in an appropriate location:

```nginx
# Temporarily restrict multipart/form-data requests
if ($http_content_type ~* "multipart/form-data") {
    return 403;
}
```

Keep the existing PATH_INFO configuration unchanged.

**Step 3: Test the configuration and reload Nginx**

First, validate the Nginx configuration:

```bash
nginx -t
```

A successful result should look similar to:

```text
nginx: the configuration file syntax is ok
nginx: configuration file test is successful
```

Then reload Nginx:

```bash
nginx -s reload
```

If aaPanel uses a custom Nginx installation path, adjust the command according to your actual environment.

**Important considerations:**

Whether modifying `pathinfo.conf` affects all PHP websites depends on where and how the file is included in individual site configurations.

If the file is included only in specific locations or PHP configuration blocks, changing it once will not necessarily protect every website.

You can inspect its references using:

```bash
grep -R "pathinfo.conf" /www/server/nginx/conf/
```

Review the results carefully before deciding whether this approach provides sufficient coverage.

### Option C: Apply Restrictions Selectively While Preserving Upload Endpoints

**Suitable for:** Websites that support legitimate file uploads but want to restrict multipart requests on other application endpoints.

For example:

- The user avatar endpoint needs to accept uploads.
- Regular API endpoints do not need multipart requests.
- Upload functionality is available through clearly defined URLs.

In this situation, avoid using overly broad URI regular expressions to whitelist entire categories of requests.

A better approach is to configure upload endpoints separately and explicitly define which paths and HTTP methods are allowed.

For example:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Regular API endpoints do not accept multipart requests
    location /api/ {
        if ($http_content_type ~* "multipart/form-data") {
            return 403;
        }

        # Existing API proxy or PHP processing configuration
    }

    # Dedicated user avatar upload endpoint
    location = /api/v1/user/avatar {
        # Preserve the existing upload configuration.
        # Authentication, file size limits, and upload validation
        # should also be configured here.
    }
}
```

The following directive uses an exact URI match:

```nginx
location = /api/v1/user/avatar
```

This prevents unrelated paths from being treated as authorized upload endpoints.

Additional precautions:

- Require authentication and authorization for upload endpoints.
- Restrict uploaded file sizes and permitted file types.
- Avoid configuring upload directories as locations where PHP files can be executed.
- Upgrade PHP as soon as possible rather than relying on upload endpoint whitelisting indefinitely.

**Important:** Whitelisted upload endpoints may still be vulnerable to PHP2Shell. This configuration is only a traffic management strategy, not a security exemption from the vulnerability.

## 3. Verifying the Nginx Mitigation

After applying the configuration, perform both positive and negative tests to confirm that Nginx behaves as expected without disrupting normal application traffic.

It is important to distinguish between two different objectives:

- **Configuration verification:** Confirming that Nginx processes requests according to the configured rules.
- **Vulnerability verification:** Confirming that the underlying PHP installation has been patched.

The following curl tests only verify Nginx request restrictions. They do not prove that PHP2Shell has been fixed or that the server is no longer vulnerable.

### 3.1 Verify That multipart Requests Are Blocked

Use curl to send a POST request with a multipart content type:

```bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: multipart/form-data; boundary=----TestBoundary"
```

Expected result:

```text
HTTP/2 403
```

If the server returns HTTP 403, the request has matched the corresponding Nginx blocking rule.

Note that this test primarily verifies request-header matching behavior. It is not an actual vulnerability exploitation test and does not prove that every multipart request or alternative attack path has been blocked.

### 3.2 Verify That JSON API Requests Still Work

Next, send a regular POST request using JSON:

```bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

Expected result:

```text
HTTP/2 200
```

The actual response code depends on your application.

For example:

- `200`: The request was processed successfully.
- `400`: The request parameters are invalid.
- `401`: Authentication is required.
- `403`: The request is not authorized.
- `405`: The endpoint does not support the POST method.

The objective is to confirm that normal application requests are not incorrectly blocked by the newly introduced multipart restriction.

### 3.3 Verify That GET Requests Still Work

Use a GET request to check basic website accessibility:

```bash
curl -i https://yourdomain.com/
```

Expected result:

```text
HTTP/2 200
```

A response of `301` or `302` may also be normal, depending on whether your website uses HTTPS redirection or other application-level redirects.

### 3.4 Check Whether the Nginx Configuration Loaded Successfully

In addition to HTTP request testing, inspect the Nginx configuration and running processes.

**Validate the configuration:**

```bash
nginx -t
```

**Check Nginx processes:**

```bash
ps aux | grep nginx
```

**Inspect the error log:**

```bash
tail -n 100 /www/wwwlogs/nginx_error.log
```

Adjust the log path according to your actual Nginx installation and website configuration.

### 3.5 A Common Mistake When Testing with curl

When testing POST requests, make sure you understand the difference between these two options:

- `-i`: Includes HTTP response headers in the output.
- `-I`: Sends a HEAD request and retrieves response headers.

For example:

```bash
curl -i -X POST https://your-api.com \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

This is an appropriate way to test a POST request.

Do not accidentally use uppercase `-I` when you intend to test POST behavior, as it can cause the request method to differ from what you expect and produce misleading results.

## 4. Additional Temporary Security Hardening

Besides Nginx-level request restrictions, you should also strengthen security across the PHP runtime environment, operating system permissions, and network access controls.

### 4.1 Review PHP Configuration

You can inspect relevant PHP settings using:

```bash
php -i | grep -E "memory_limit|session.upload_progress.enabled"
```

If upload progress tracking is not required by your application, consider disabling it:

```ini
session.upload_progress.enabled = Off
```

However, it is important to understand that:

Disabling upload progress tracking does not fix PHP2Shell and should not be considered a reliable vulnerability mitigation.

Also, avoid setting:

```ini
memory_limit = -1
```

This removes PHP's memory usage limit and may allow abnormal requests to consume excessive server memory, increasing the risk of denial-of-service attacks.

### 4.2 Restrict PHP Runtime Account Permissions

Review the permissions of your PHP-FPM runtime accounts.

Recommended practices include:

- Do not run PHP-FPM workers as root.
- Use separate runtime accounts for different websites whenever possible.
- Restrict PHP processes from accessing sensitive system directories.
- Avoid granting PHP runtime accounts unnecessary administrative privileges.
- Apply appropriate read and write permissions to upload directories.

Even if remote code execution occurs, proper privilege isolation can help reduce the potential impact of a compromise.

### 4.3 Investigate Suspicious PHP Processes

For PHP servers exposed to the public internet, regularly inspect running processes and suspicious system activity.

Pay particular attention to:

- PHP-FPM workers unexpectedly spawning shell processes.
- PHP processes launching unknown external programs.
- Unusual file download activity.
- Unexpected or unfamiliar scheduled tasks.
- Recently created suspicious PHP files.
- Unexpected modifications or new files within web directories.

If suspicious activity is discovered, do not simply restart PHP-FPM or delete logs.

Preserve relevant logs and forensic evidence, then investigate whether the server has already been compromised.

## 5. Permanent Solution: Upgrade PHP

Nginx-level restrictions are only temporary mitigation measures. They cannot replace the security patches provided by the PHP project.

The corresponding fixed releases listed in this guide are:

```text
PHP 8.5.12
PHP 8.4.27
PHP 8.3.36
PHP 8.2.35
```

Upgrade your PHP installation to the corresponding fixed release or a later security release within the same supported branch.

Before upgrading, follow these recommended steps:

1. Back up your website code, databases, and PHP configuration.
2. Identify the current PHP version and deployment model.
3. Check compatibility between your PHP extensions and application code.
4. Complete upgrade testing in a staging environment.
5. Upgrade PHP in production.
6. Restart or reload PHP-FPM as required.
7. Verify the PHP version and service status.
8. Test critical application functionality, including file uploads, authentication, payments, and other essential workflows.

**Check the PHP CLI version:**

```bash
php -v
```

Keep in mind that the PHP CLI version may differ from the PHP-FPM version used by your website.

For aaPanel, Docker, or environments running multiple PHP versions, verify each PHP runtime instance that actually handles web requests.

Otherwise, you may end up with an upgraded CLI installation while your website continues running an outdated and vulnerable PHP-FPM instance.

## 6. Conclusion

PHP2Shell is a security vulnerability involving the PHP runtime itself. It cannot be fully addressed through application-level filtering or a single Nginx configuration rule.

If an immediate upgrade is not possible, consider the following temporary risk-reduction measures:

- Restrict unnecessary `multipart/form-data` requests based on your application's requirements.
- Apply independent access controls to upload endpoints that must remain available.
- Disable unnecessary PHP upload progress tracking, without treating this as a vulnerability fix.
- Restrict permissions assigned to PHP-FPM runtime accounts.
- Investigate suspicious processes, files, and system activity.
- Upgrade to a PHP release containing the official security fixes or a vendor-provided security backport.

**The key takeaway: Nginx request filtering is an additional defensive measure, not a complete solution to PHP2Shell.**

For PHP services directly exposed to the public internet, prioritize security upgrades.

If a vulnerable system cannot be patched immediately and presents a significant risk, consider restricting or isolating its public internet access until the necessary security updates have been applied.

## 7. References

- PHP Official Website: https://www.php.net/
- PHP Official Release Information: https://www.php.net/releases/
- CISA: https://www.cisa.gov/
- Canadian Centre for Cyber Security: https://www.cyber.gc.ca/

Continue monitoring official PHP security advisories and security updates from your operating system vendor to ensure that relevant patches are applied promptly.
