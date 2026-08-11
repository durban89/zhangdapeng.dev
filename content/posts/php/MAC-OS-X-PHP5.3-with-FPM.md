---
title: "MAC OS X PHP5.3 with FPM"
date: "2025-06-11 10:33:56"
slug: "mac-os-x-php53-with-fpm"
categories: ["技术"]
tags: ["Unix", "PHP"]
aliases:
  - "/2025/06/11/MAC-OS-X-PHP5.3-with-FPM/"
  - "/2025/06/11/MAC-OS-X-PHP5.3-with-FPM.html"
  - "/MAC-OS-X-PHP5.3-with-FPM/"
  - "/MAC-OS-X-PHP5.3-with-FPM.html"
  - "/2025/06/11/mac-os-x-php53-with-fpm/"
  - "/2025/06/11/mac-os-x-php53-with-fpm.html"
  - "/mac-os-x-php53-with-fpm.html"
---
I’ve been considering diving into nginx for a bit now. Rumors of it’s speed and Cyrillic error messages have intrigued me. With recent forays into node.js apps and their requirement for a free port, I wanted to find a nice solution that complimented the evented speed of node.js without exposing a port publicly for each app. As it turns out Nginx is suited quite nicely to this. But that wasn’t where it ended. I found nginx to have a much more interesting and dynamic config language. And even beyond that it gave me a good excuse to learn more about running PHP as a FastCGI process and how PHP-FPM (baked in as of 5.3.3) fits into the picture. Not sure if MEMP is the correct acronym, but since I’ve seen talk of LEMP servers, I’ll run with it.（似乎说了一下为什么要使用PHP-FPM）  
  
MacPorts. If you’re not already familiar with it, I recommend reading up before proceeding.  
  
Since I already have MySQL set up and configured I won’t bother covering it here. It’s pretty well documented around the webs. The main focus here is going to be getting nginx installed and setting up PHP as a service to it with an emphasis on local development. No need to tweak this for production on my Macbook Pro.(这里说明了一下MacPorts是什么，给他带了什么好处)  
  
PHP 5.3.3 introduced PHP-FPM (FastCGI Process Manager) to the codebase. Building it requires a few extra config flags and generates a php-fpm binary. The binary will manage spawning cgi processes and handling the FastCGI passthru from nginx. Currently MacPorts does not have an option to build PHP with PHP-FPM. After some hacking on the current Portfile I arrived at a working solution. It includes the correct flags, a dependency on libevent, and a startup item.(这里介绍了一下什么是PHP-FPM)

First things first.

```sh
sudo port selfupdate
# recommended but probably not a requirement
sudo port upgrade outdated
sudo port uninstall inactive
```

(If you’ve already got the php5 package installed, uninstall it and it’s cohorts to ensure a clean install process going forward.)  
This is a bit of a hack and there’s probably a better way, like submitting a proper patch to MacPorts, but this will get the job done for today.

```sh
# replace this file with the Portfile from the gist below
/opt/local/var/macports/sources/rsync.macports.org/release/ports/lang/php5/Portfile
```

Then run the regular port install.

```sh
sudo port install nginx php5 +fastcgi php5-apc php5-mysql +mysqlnd
```

Next we’ll need to set up the configs. There’s two basic configs that require attention. First is the nginx config. Since this is just for a local development env we can be pretty lean on what we need.

下面是关于nginx的配置

```sh
# /opt/local/etc/nginx/nginx.conf

worker_processes  1;

error_log  /var/log/nginx/error.log;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile           on;
    keepalive_timeout  65;

    server {
      listen 80;
      server_name   ~^local\.(?.+?)\.com$;
      root  /Users/jason/Sites/$site/web;
      index  index.php index.html;

      location = /favicon.ico {
        log_not_found off;
      }

      location ~ \.php$ {
         fastcgi_pass   unix:/tmp/php-fpm.sock;
         fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
         include        fastcgi_params;
      }
    }
}
```

This is the config that I’m currently using as my generic site config. It has a few nice features. First the server name is matched against a regular expression. So any site that matches local.xxxx.com will be parsed and use the xxxx as a sub-directory in my Sites folder. This is nice. So I only need to create a new directory and add my local.xxxx.com domain to /etc/hosts pointed at 127.0.0.1 and I can immediately begin developing. Gone are the days of creating a new v-hosts file, enabling it, and restarting apache every time I want to play with a new site’s code. The other nicety here is we’re using a unix socket for the fastcgi passthru. This is unnoticeably faster on my Mac, but again frees up the need to be concerned with another open port on my system.  
It’s worth noting that any fastcgi\_param that you define in this config is available within PHP as a $\_SERVER variable.  
The second config is the FPM config. Copy /opt/local/etc/php-fpm.conf.default to /opt/local/etc/php-fpm.conf and open it up. Here are the important ones to modify:（下面是关于php-fpm的配置）

```sh
pid = /opt/local/var/run/php-fpm.pid
error_log = /opt/local/var/log/php-fpm.log
listen = /tmp/php-fpm.sock
listen.owner = _www
listen.group = _www
pm.max_children = 1
pm.start_servers = 1
pm.min_spare_servers = 1
pm.max_spare_servers = 1
pm.max_requests = 500
slowlog = /opt/local/var/log/php-fpm.log.slow
```

It’s pretty straight-forward. Lean cus we can. Save and continue.  
At this point we’ve got all the pieces in place. We just need a way to start/stop/restart nginx and FPM. I looked for a cleaner way to accomplish this but in the end it came down to a handful of aliases. Add these to your ~/.profile.（配置啊启动和关闭nginx，fpm）

```sh
# nginx
alias nginx_start='sudo launchctl load /Library/LaunchDaemons/org.macports.nginx.plist' 
alias nginx_stop='sudo launchctl unload /Library/LaunchDaemons/org.macports.nginx.plist' 
alias nginx_restart='nginx_stop; nginx_start;' 

# php-fpm
alias fpm_start='sudo launchctl load /Library/LaunchDaemons/org.macports.php-fpm.plist'
alias fpm_stop='sudo launchctl unload /Library/LaunchDaemons/org.macports.php-fpm.plist'
alias fpm_restart='fpm_stop; fpm_start'
```

（到这里，果然牛逼，直接放在自己的命令行里面）

Reopen the Terminal window to enable the new aliases. Start or restart nginx and FPM as the case may be.  
  
At this point you should be able to create a site directory, add a domain to /etc/hosts and drop in an index.php with phpinfo(); to verify that PHP is working.  
Hopefully this will be of some use to other aspiring MEMP devs out there.

来源：http://blog.jasonmooberry.com/2010/12/memp-php-5-3-with-fpm-and-nginx-via-macports/

