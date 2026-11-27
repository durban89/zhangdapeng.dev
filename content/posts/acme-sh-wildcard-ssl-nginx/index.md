+++
title = "Managing Wildcard SSL Certificates with acme.sh: DNS Validation and Nginx Deployment"
description = "A practical guide to issuing and deploying Let's Encrypt wildcard SSL certificates using acme.sh, including manual DNS validation with Alibaba Cloud, Nginx integration, non-root permissions, and network considerations for servers in mainland China."
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

# Managing Wildcard SSL Certificates with acme.sh

When deploying websites or configuring Nginx reverse proxies, SSL/TLS certificates are essential for enabling secure HTTPS connections.

Consider a domain with multiple subdomains:

- example.com
- www.example.com
- api.example.com
- admin.example.com

Managing individual certificates for every subdomain can become inconvenient, especially when it comes to renewal and deployment.

A wildcard SSL certificate provides a more convenient solution. It allows a single certificate to cover a primary domain and its matching first-level subdomains.

In this article, we will explore how to use **acme.sh, Let's Encrypt, and Nginx** to issue and deploy wildcard certificates.

We will also cover manual DNS validation without API credentials, network considerations for servers in mainland China, and permission management when running acme.sh as a non-root user.

## 1. What Is acme.sh?

[acme.sh](https://github.com/acmesh-official/acme.sh) is an open-source ACME client written entirely in Shell.

It automates the process of issuing, renewing, and deploying SSL/TLS certificates.

Its main features include:

- Lightweight implementation with minimal dependencies.
- Support for Let's Encrypt, ZeroSSL, and other certificate authorities.
- Support for single-domain, multi-domain, and wildcard certificates.
- HTTP and DNS validation methods.
- DNS API integrations with many DNS providers.
- Automated certificate deployment to Nginx and Apache.
- Scheduled renewal checks.

For developers managing multiple domains or subdomains, acme.sh provides a convenient certificate management solution.

## 2. Installing acme.sh

First, install the required dependencies.

For Ubuntu or Debian:

```bash
sudo apt update

sudo apt install -y curl git cron
```

Under normal network conditions, you can use the official installation script:

```bash
curl https://get.acme.sh | sh -s email=your_email@example.com
```

By default, acme.sh is installed in:

```text
~/.acme.sh/
```

Reload your shell environment:

```bash
source ~/.bashrc
```

Alternatively, reconnect to your SSH session.

### Network Considerations for Servers in Mainland China

If your server is hosted in mainland China, downloading installation scripts directly from GitHub may result in connection timeouts or failures.

There are several alternatives:

1. Use a trusted domestic Git mirror.
2. Download the source code on a machine with reliable GitHub access and upload it using SCP.
3. Use a network environment that can access the official GitHub repository.

For example, after downloading the source code:

```bash
git clone [<trusted-mirror-url>](https://gitee.com/neilpang/acme.sh.git)

cd acme.sh

./acme.sh --install -m your_email@example.com
```

Make sure the mirror is trustworthy and preferably synchronized with the official repository.

For servers with limited GitHub connectivity, avoid enabling automatic upgrades without first verifying network access:

```bash
acme.sh --upgrade --auto-upgrade
```

Manual upgrades may be more reliable in restricted network environments.

## 3. Set Let's Encrypt as the Default CA

After installation, configure Let's Encrypt as the default certificate authority:

```bash
acme.sh --set-default-ca --server letsencrypt
```

Future certificate requests will then use Let's Encrypt by default.

## 4. Issuing a Wildcard Certificate

Wildcard certificates generally require DNS-01 validation.

For example, we want a certificate covering:

```text
example.com
*.example.com
```

An important detail:

**A certificate covering only `*.example.com` does not automatically cover `example.com`.**

Therefore, it is recommended to include both the primary domain and the wildcard domain in the same certificate request.

acme.sh supports two main approaches for DNS validation:

- Automatic DNS validation through provider APIs.
- Manual DNS validation by adding TXT records yourself.

Let's look at the manual approach first.

### 4.1 Using Manual DNS Validation

If you do not want to store Alibaba Cloud AccessKey credentials on your server, you can use acme.sh's manual DNS mode.

Run:

```bash
acme.sh --issue --dns \
  -d example.com \
  -d '*.example.com' \
  --yes-I-know-dns-manual-mode-enough-go-ahead-please
```

acme.sh will generate the TXT records required for domain ownership verification.

Example output:

```text
Domain: '_acme-challenge.example.com'
TXT value: 'xxxxxxxxxxxx'

Domain: '_acme-challenge.example.com'
TXT value: 'yyyyyyyyyyyy'
```

Since both the primary domain and wildcard domain are included, you may need to add two TXT records.

### 4.2 Adding TXT Records in Alibaba Cloud DNS

Log in to the Alibaba Cloud console:

Cloud DNS → Select your domain → DNS Settings → Add Record.

Configure the records using the values generated by acme.sh.

| Setting | Value |
|---|---|
| Record Type | TXT |
| Host Record | _acme-challenge |
| Record Value | TXT value generated by acme.sh |
| TTL | Default value |

If two TXT values are generated, add both records separately.

Both records can use the same host record, but their values must remain different.

Do not overwrite the first record when adding the second one.

### 4.3 Verifying TXT Records

Use dig to check whether the DNS records have propagated:

```bash
dig TXT _acme-challenge.example.com +short
```

Make sure the returned values contain the verification strings generated by acme.sh.

### 4.4 Completing Certificate Issuance

After the TXT records become available, execute:

```bash
acme.sh --renew -d example.com \
  --yes-I-know-dns-manual-mode-enough-go-ahead-please
```

Once validation succeeds, the certificate will be issued.

One important limitation:

**Manual DNS mode does not support fully unattended automatic renewal.**

Each renewal requires generating new verification values, manually updating the TXT records, and running the renewal command again.

If you want unattended renewal, consider DNS API validation or DNS Alias mode instead.

## 5. DNS Alias: Automatic Renewal Without Storing Main Domain API Credentials

If you do not want to store Alibaba Cloud API credentials on your server but also want to avoid manually updating TXT records, DNS Alias mode is worth considering.

The idea is straightforward:

1. Keep your primary domain hosted on Alibaba Cloud.
2. Prepare a separate auxiliary domain hosted by a DNS provider that supports API automation, such as Cloudflare.
3. Create a CNAME record in Alibaba Cloud pointing the ACME challenge to the auxiliary domain.
4. Use the auxiliary domain's DNS API to manage TXT records automatically.

For example:

```text
_acme-challenge.example.com
    CNAME
_acme-challenge.otherdomain.com
```

Then issue the certificate using:

```bash
acme.sh --issue --dns dns_cf \
  -d example.com \
  -d '*.example.com' \
  --challenge-alias otherdomain.com
```

This approach avoids storing the primary domain's Alibaba Cloud API credentials on the server.

Make sure the auxiliary domain uses a DNS provider supported by acme.sh and that its API credentials are configured correctly.

## 6. Installing Certificates for Nginx

After issuing the certificate, you need to install it into a directory accessible to Nginx.

The recommended approach is to use:

```bash
--install-cert
```

instead of manually copying files with `cp` or creating symbolic links with `ln -s`.

The reason is that acme.sh remembers the destination paths and reload command.

When a certificate is renewed, acme.sh can automatically copy the updated files to the target directory and reload Nginx.

### 6.1 Create the Certificate Directory

For example:

```bash
sudo mkdir -p /etc/nginx/ssl
```

### 6.2 Install the Certificate

You can also specify your own certificate filenames:

```bash
acme.sh --install-cert -d example.com \
  --key-file /etc/nginx/ssl/my_wildcard.key \
  --fullchain-file /etc/nginx/ssl/my_wildcard.crt \
  --reloadcmd "sudo systemctl reload nginx"
```

There are two important options:

- `--key-file`: Specifies the private key destination.
- `--fullchain-file`: Specifies the full certificate chain destination.

Nginx should use the full certificate chain rather than only the server certificate.

Certificate filenames are completely customizable. You can use `.crt`, `.pem`, or other extensions, as long as the paths match your Nginx configuration.

Remember to create the destination directory before installing the certificate.

## 7. Configuring Nginx for Wildcard Certificates

After installing the certificate, configure your Nginx virtual host.

Example:

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

Notice that `server_name` contains both:

```nginx
example.com *.example.com;
```

The same certificate can therefore be used for the primary domain and matching first-level subdomains.

However, wildcard certificates have an important limitation.

`*.example.com` matches:

```text
www.example.com
api.example.com
admin.example.com
```

It does not match multi-level subdomains such as:

```text
test.api.example.com
```

### 7.1 Test and Reload Nginx

After modifying the configuration, validate the syntax:

```bash
sudo nginx -t
```

If the configuration is valid, reload Nginx:

```bash
sudo systemctl reload nginx
```

## 8. Verifying Wildcard Certificate Coverage

You can use OpenSSL to inspect the Subject Alternative Name (SAN) extension:

```bash
openssl x509 \
  -in /etc/nginx/ssl/my_wildcard.crt \
  -noout \
  -ext subjectAltName
```

A successful wildcard certificate should produce output similar to:

```text
X509v3 Subject Alternative Name:
    DNS:example.com, DNS:*.example.com
```

This confirms that both the primary domain and wildcard domain are included.

## 9. Running acme.sh as a Non-Root User

Another practical issue occurs when acme.sh is installed under a regular Linux user account while Nginx certificate files are stored under:

```text
/etc/nginx/ssl/
```

Even if the user has sudo privileges, acme.sh cannot automatically write to system directories or reload Nginx without the necessary permissions.

There are two main issues:

1. The regular user cannot write to the certificate directory.
2. Automatic renewal may fail when `systemctl reload nginx` requires an interactive sudo password.

### 9.1 Granting Certificate Directory Access

Assume the current Linux user is `ubuntu`.

Create the directory:

```bash
sudo mkdir -p /etc/nginx/ssl
```

One simple approach is to assign ownership to the current user:

```bash
sudo chown -R $USER:$USER /etc/nginx/ssl
```

This allows acme.sh to write certificate files directly.

If you prefer to preserve root ownership, consider using ACLs to grant write access to the specific user instead of changing the entire directory's ownership.

Changing the directory owner does not prevent Nginx from reading the certificates.

Nginx normally uses a root-owned master process to load certificate files. Root retains the ability to read files regardless of their ownership.

However, private key permissions should remain restrictive. Avoid making private keys readable by unnecessary users.

### 9.2 Allowing Passwordless Nginx Reload

During automatic renewal, acme.sh needs to execute:

```bash
sudo systemctl reload nginx
```

Without a suitable sudoers rule, the scheduled renewal process may fail because it cannot enter a password interactively.

First, find the actual systemctl path:

```bash
which systemctl
```

Assume the result is:

```text
/usr/bin/systemctl
```

Create a dedicated sudoers configuration:

```bash
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/systemctl reload nginx" \
  | sudo tee /etc/sudoers.d/acme-nginx
```

Set the required permissions:

```bash
sudo chmod 0440 /etc/sudoers.d/acme-nginx
```

Test the configuration:

```bash
sudo systemctl reload nginx
```

If the command succeeds without asking for a password, the configuration is working.

This rule only allows the specified user to reload Nginx without a password. It does not grant passwordless access to every sudo command.

### 9.3 Installing Certificates as the Regular User

Once the directory permissions and sudoers rule are configured, run the installation command directly as the regular user:

```bash
acme.sh --install-cert -d example.com \
  --key-file /etc/nginx/ssl/my_wildcard.key \
  --fullchain-file /etc/nginx/ssl/my_wildcard.crt \
  --reloadcmd "sudo systemctl reload nginx"
```

One important warning:

**Do not prepend `sudo` to the acme.sh command.**

Avoid:

```bash
sudo acme.sh --install-cert -d example.com
```

Running acme.sh under sudo may cause it to use root's environment and certificate directory:

```text
/root/.acme.sh/
```

However, the certificate you previously issued belongs to the regular user's acme.sh installation.

Keep certificate issuance, installation, and renewal under the same Linux user.

## 10. Useful acme.sh Maintenance Commands

Here are some commands useful for daily certificate management.

List issued certificates:

```bash
acme.sh --list
```

Force a renewal test:

```bash
acme.sh --renew -d example.com --force
```

Upgrade acme.sh:

```bash
acme.sh --upgrade
```

Enable automatic upgrades:

```bash
acme.sh --upgrade --auto-upgrade
```

The last option should only be enabled after verifying that the server can reliably access the upgrade source.

## 11. Conclusion

acme.sh provides a convenient way to automate SSL certificate issuance, deployment, and renewal.

The DNS validation approaches covered in this article serve different needs:

| Method | Characteristics | Best For |
|---|---|---|
| DNS API | Automatically manages TXT records | Fully automated renewal |
| Manual DNS | Requires no API credentials | Users comfortable with manual renewal |
| DNS Alias | Keeps primary domain API credentials off the server | Automation with credential isolation |

For most production environments, DNS API or DNS Alias is preferable because it reduces manual maintenance.

However, successful certificate issuance is only part of the deployment process.

You also need to configure the correct Nginx certificate paths, file permissions, and reload commands.

When running acme.sh as a non-root user, handling directory permissions and passwordless Nginx reload in advance is particularly important.

**The ultimate goal is not simply to obtain an SSL certificate, but to build a reliable certificate management workflow that can run continuously with minimal manual intervention.**