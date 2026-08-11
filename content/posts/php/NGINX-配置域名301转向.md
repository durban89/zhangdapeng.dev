---
title: "NGINX 配置域名301转向"
date: "2025-07-03 11:08:04"
slug: "nginx-pei-zhi-yu-ming-301-zhuan-xiang"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/07/03/NGINX-配置域名301转向/"
  - "/2025/07/03/NGINX-配置域名301转向.html"
  - "/NGINX-配置域名301转向/"
  - "/NGINX-配置域名301转向.html"
  - "/2025/07/03/nginx-pei-zhi-yu-ming-301-zhuan-xiang/"
  - "/2025/07/03/nginx-pei-zhi-yu-ming-301-zhuan-xiang.html"
  - "/nginx-pei-zhi-yu-ming-301-zhuan-xiang.html"
---
嗯，今晚记录下，由于最近观察google 分析工具发现我网站存在 www.gowhich.com 和 gowhich.com 同时存在的一些问题，建议将其中的一个做301跳转，这个还是超级简单，不过还是记录一下吧，方便记性不好的。

绑定对应的域名当然没有问题了。

```bash
server {
    listen 80;
    server_name gowhich.com www.gowhich.com *.gowhich.com ;  
}
```

上面主要展示了主要的部分，后面还是要根据你自己的需要去配置。

```bash
server {
    listen 80;
    server_name gowhich.com www.gowhich.com *.gowhich.com ;    
    if ($host != 'www.gowhich.com') {
      rewrite ^/(.*)$ http://www.gowhich.com/$1 permanent;    
    }
}
```

或者可以使用等于的判断

```bash
server {
    listen 80;
    server_name gowhich.com www.gowhich.com *.gowhich.com ;    
    if ($host = 'gowhich.com') {
      rewrite ^/(.*)$ http://www.gowhich.com/$1 permanent;    
    }
}
```

第二个更有针对性吧。

这里有几个问题需要注意一下：

1. 上述配置文件的if语句与括号必须以一个空格隔开，否则Nginx会报nginx: [emerg] unknown directive “if($host” in…错误。
2. Nginx的条件判断不等于是!=，等于是=，注意这里的等于只有一个等于号，如果写成==，则Nginx会报nginx: [emerg] unexpected “==” in condition in…错误。
3. 301永久转向配置成功后，浏览器可能会有记忆效应，比如说IE。所以一旦配置并利用浏览器访问过页面，那么你更改了301转向配置后，这个页面可能依旧是上次的转向，建议清除浏览器缓存，或者尝试访问其他页面，也可以在url的?问号后面加上一些随机的参数，避免浏览器的缓存记忆效应。

配置完成后，可以使用nginx -s reload命令进行平滑的更新配置（不重启Nginx）。


