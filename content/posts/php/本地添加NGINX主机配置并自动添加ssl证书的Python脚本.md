---
title: "本地添加NGINX主机配置并自动添加ssl证书的Python脚本"
date: "2025-06-30 16:55:11"
slug: "ben-di-tian-jia-nginx-zhu-ji-pei-zhi-bing-zi-dong-tian-jia-ssl-zheng-shu-de-python-jiao-ben"
categories: ["技术"]
tags: ["Python", "NGINX", "SSL", "Ubuntu", "Linux"]
aliases:
  - "/2025/06/30/本地添加NGINX主机配置并自动添加ssl证书的Python脚本/"
  - "/2025/06/30/本地添加NGINX主机配置并自动添加ssl证书的Python脚本.html"
  - "/本地添加NGINX主机配置并自动添加ssl证书的Python脚本/"
  - "/本地添加NGINX主机配置并自动添加ssl证书的Python脚本.html"
  - "/2025/06/30/ben-di-tian-jia-nginx-zhu-ji-pei-zhi-bing-zi-dong-tian-jia-ssl-zheng-shu-de-python-jiao/"
  - "/2025/06/30/ben-di-tian-jia-nginx-zhu-ji-pei-zhi-bing-zi-dong-tian-jia-ssl-zheng-shu-de-python-.html"
  - "/ben-di-tian-jia-nginx-zhu-ji-pei-zhi-bing-zi-dong-tian-jia-ssl-zheng-shu-de-python-jiao-ben.html"
---
## [代码逻辑](#daimaluoji)

```python
import os
import sys
import argparse
import logging
import subprocess
from typing import List, Dict, Optional
import tempfile
import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('nginx_config_manager')

class NginxConfigManager:
    """Nginx配置管理类"""
    
    def __init__(self, config_dir: str = '/etc/nginx/conf.d', 
                 nginx_bin: str = '/usr/sbin/nginx',
                 ssl_dir: str = '/etc/ssl'):
        """
        初始化Nginx配置管理器
        
        Args:
            config_dir: Nginx配置文件目录
            nginx_bin: Nginx可执行文件路径
            ssl_dir: SSL证书存放目录
        """
        self.config_dir = config_dir
        self.nginx_bin = nginx_bin
        self.ssl_dir = ssl_dir
        
        # 确保配置目录存在
        if not os.path.exists(config_dir):
            logger.error(f"配置目录 {config_dir} 不存在")
            sys.exit(1)
            
        # 确保SSL目录存在
        if not os.path.exists(ssl_dir):
            os.makedirs(ssl_dir, exist_ok=True)
            logger.info(f"创建SSL证书目录: {ssl_dir}")
    
    def create_site_config(self, server_name: str, root_dir: str, 
                           port: int = 80, ssl: bool = False, 
                           additional_directives: Optional[List[str]] = None) -> str:
        """
        创建网站配置文件内容
        
        Args:
            server_name: 服务器名称(域名)
            root_dir: 网站根目录
            port: 监听端口
            ssl: 是否启用SSL
            additional_directives: 额外的配置指令
            
        Returns:
            配置文件内容字符串
        """
        # 基本配置模板
        config = [
            f"server {{",
            f"    listen {port}{' ssl' if ssl else ''};",
            f"    server_name {server_name};",
            f"    root {root_dir};"
        ]
        
        # 添加SSL相关配置(如果启用)
        if ssl:
            config.extend([
                f"    ssl_certificate {self.ssl_dir}/certs/{server_name}.crt;",
                f"    ssl_certificate_key {self.ssl_dir}/private/{server_name}.key;",
                "    ssl_protocols TLSv1.2 TLSv1.3;",
                "    ssl_prefer_server_ciphers on;",
                "    ssl_session_cache shared:SSL:10m;",
                "    ssl_session_timeout 10m;"
            ])
        
        # 添加默认位置块
        config.extend([
            "    location / {",
            "        try_files $uri $uri/ =404;",
            "    }"
        ])
        
        # 添加额外指令
        if additional_directives:
            config.extend(additional_directives)
            
        config.append("}")
        
        return "\n".join(config)
    
    def write_config_file(self, server_name: str, config_content: str) -> str:
        """
        写入配置文件
        
        Args:
            server_name: 服务器名称(用于生成文件名)
            config_content: 配置文件内容
            
        Returns:
            配置文件路径
        """
        # 生成配置文件名(基于服务器名称)
        config_filename = f"{server_name.replace('.', '_')}.conf"
        config_path = os.path.join(self.config_dir, config_filename)
        
        try:
            with open(config_path, 'w') as f:
                f.write(config_content)
            logger.info(f"配置文件已写入: {config_path}")
            return config_path
        except Exception as e:
            logger.error(f"写入配置文件失败: {e}")
            sys.exit(1)
    
    def test_config(self) -> bool:
        """测试Nginx配置"""
        try:
            result = subprocess.run(
                [self.nginx_bin, '-t'], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                logger.info("Nginx配置测试成功")
                return True
            else:
                logger.error(f"Nginx配置测试失败: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"执行配置测试时出错: {e}")
            return False
    
    def reload_nginx(self) -> bool:
        """重新加载Nginx服务"""
        try:
            # 先尝试优雅重启
            result = subprocess.run(
                [self.nginx_bin, '-s', 'reload'], 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                logger.info("Nginx已重新加载")
                return True
            else:
                logger.error(f"重新加载Nginx失败: {result.stderr}")
                return False
        except Exception as e:
            logger.error(f"执行Nginx重载时出错: {e}")
            return False
    
    def generate_self_signed_ssl(self, server_name: str, days: int = 365) -> None:
        """
        生成自签名SSL证书
        
        Args:
            server_name: 服务器名称(域名)
            days: 证书有效期天数
        """
        # 证书和私钥路径
        cert_path = os.path.join(self.ssl_dir, "certs", f"{server_name}.crt")
        key_path = os.path.join(self.ssl_dir, "private", f"{server_name}.key")
        
        # 检查证书是否已存在
        if os.path.exists(cert_path) and os.path.exists(key_path):
            cert_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(cert_path))
            expires_at = cert_mtime + datetime.timedelta(days=days)
            now = datetime.datetime.now()
            
            if expires_at > now:
                logger.info(f"SSL证书已存在且有效: {cert_path}")
                return
            else:
                logger.info(f"SSL证书已过期，重新生成: {cert_path}")
        
        logger.info(f"生成自签名SSL证书: {server_name}")
        
        try:
            # 创建临时配置文件
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                config = f"""
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
x509_extensions = v3_req

[dn]
C = CN
ST = State
L = City
O = Organization
OU = Unit
CN = {server_name}

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = {server_name}
DNS.2 = www.{server_name}
"""
                f.write(config)
                config_path = f.name
            
            # 生成私钥和证书
            subprocess.run(
                [
                    'openssl', 'req', '-x509', '-nodes', 
                    '-days', str(days), 
                    '-newkey', 'rsa:2048', 
                    '-keyout', key_path, 
                    '-out', cert_path, 
                    '-config', config_path,
                    '-extensions', 'v3_req'
                ],
                check=True,
                capture_output=True
            )
            
            # 设置正确的权限
            os.chmod(key_path, 0o600)
            os.chmod(cert_path, 0o644)
            
            logger.info(f"SSL证书生成成功: {cert_path}")
        except subprocess.CalledProcessError as e:
            logger.error(f"生成SSL证书失败: {e.stderr.decode()}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"生成SSL证书时出错: {e}")
            sys.exit(1)
        finally:
            # 删除临时配置文件
            if os.path.exists(config_path):
                os.remove(config_path)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Nginx配置管理工具')
    parser.add_argument('--server-name', required=True, help='服务器名称(域名)')
    parser.add_argument('--root-dir', required=True, help='网站根目录')
    parser.add_argument('--port', type=int, default=80, help='监听端口(默认: 80)')
    parser.add_argument('--ssl', action='store_true', help='启用SSL')
    parser.add_argument('--dry-run', action='store_true', help='仅生成配置不应用')
    parser.add_argument('--generate-ssl', action='store_true', help='生成自签名SSL证书')
    parser.add_argument('--ssl-days', type=int, default=365, help='SSL证书有效期天数(默认: 365)')
    
    args = parser.parse_args()
    
    # 初始化配置管理器
    manager = NginxConfigManager()
    
    # 生成SSL证书(如果需要)
    if args.generate_ssl or args.ssl:
        manager.generate_self_signed_ssl(args.server_name, args.ssl_days)
    
    # 创建配置内容
    additional_directives = [
        f"    access_log /var/log/nginx/{args.server_name.replace('.', '_')}_access.log;",
        f"    error_log /var/log/nginx/{args.server_name.replace('.', '_')}_error.log;"
    ]
    
    config_content = manager.create_site_config(
        server_name=args.server_name,
        root_dir=args.root_dir,
        port=args.port,
        ssl=args.ssl,
        additional_directives=additional_directives
    )
    
    # 写入配置文件
    config_path = manager.write_config_file(args.server_name, config_content)
    
    # 显示配置内容
    logger.info(f"生成的配置内容:\n{config_content}")
    
    if args.dry_run:
        logger.info("执行dry-run模式，配置未应用")
        sys.exit(0)
    
    # 测试配置
    if not manager.test_config():
        logger.error("配置测试失败，已回滚更改")
        # 删除生成的配置文件
        os.remove(config_path)
        sys.exit(1)
    
    # 重新加载Nginx
    if not manager.reload_nginx():
        logger.error("重新加载Nginx失败，配置可能未生效")
        sys.exit(1)
    
    logger.info(f"成功添加并应用Nginx配置: {args.server_name}")

if __name__ == "__main__":
    main()        


```

## [功能](#gongneng)

### [配置生成：](#gongneng-4)

可以为新网站生成基本的 Nginx 配置，支持 HTTP 和 HTTPS。

### [配置管理：](#gongneng-3)

将配置文件写入到指定目录，文件名基于服务器名称自动生成。

### [安全检查：](#gongneng-2)

在应用配置前会测试配置文件的有效性，防止错误配置导致 Nginx 无法启动。

### [自动重载：](#gongneng-1)

配置测试通过后会自动重新加载 Nginx 服务。

### [详细日志：](#gongneng-0)

提供详细的操作日志，方便排查问题。

### [SSL 证书生成：](#gongneng1)

- 使用 OpenSSL 生成 2048 位 RSA 密钥和自签名证书
- 支持设置证书有效期（默认为 365 天）
- 自动配置 Subject Alternative Name (SAN)
- 证书文件保存在/etc/nginx/ssl目录

### [证书管理：](#gongneng2)

- 检查证书是否存在和有效期
- 仅在证书不存在或已过期时重新生成
- 自动设置正确的文件权限

### [命令行参数：](#gongneng3)

- --generate-ssl：强制生成新的 SSL 证书
- --ssl-days：设置证书有效期天数
- --server-name：服务器名称(域名) example.com 
- --root-dir：网站根目录 /var/www/example.com
- --port：监听端口(默认: 80) 
- --dry-run：仅生成配置不应用
- --ssl：启用SSL

## [使用示例](#shiyongshili)

添加 HTTPS 网站并自动生成 SSL 证书：
```bash
sudo python nginx_config_manager.py \
  --server-name example.com \
  --root-dir /var/www/example \
  --port 443 \
  --ssl
```

仅生成 SSL 证书不修改 Nginx 配置：
```bash
sudo python nginx_config_manager.py \
  --server-name example.com \
  --generate-ssl \
  --ssl-days 730
```

添加 HTTPS 网站并使用现有证书：
```bash
sudo python nginx_config_manager.py \
  --server-name example.com \
  --root-dir /var/www/example \
  --port 443 \
  --ssl
```

## [注意事项](#zhuyishixiang)

- 运行此脚本需要有写入 Nginx 配置目录和执行 Nginx 命令的权限，建议使用 sudo 运行。
- 如果启用了 SSL，需要手动配置正确的证书路径。
- 脚本会自动为每个网站创建访问日志和错误日志。
- 需要系统已安装 OpenSSL 命令行工具
- 生成的是自签名证书，在浏览器中会显示不安全警告
- 自签名证书适用于开发环境或内部网站
- 生产环境建议使用 Let's Encrypt 等受信任的 CA 颁发的证书
