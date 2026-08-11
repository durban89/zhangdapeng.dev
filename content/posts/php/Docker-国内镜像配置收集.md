---
title: "Docker 国内镜像配置收集"
date: "2025-07-03 11:59:22"
slug: "docker-guo-nei-jing-xiang-pei-zhi-shou-ji"
categories: ["技术"]
tags: ["Docker"]
aliases:
  - "/2025/07/03/Docker-国内镜像配置收集/"
  - "/2025/07/03/Docker-国内镜像配置收集.html"
  - "/Docker-国内镜像配置收集/"
  - "/Docker-国内镜像配置收集.html"
  - "/2025/07/03/docker-guo-nei-jing-xiang-pei-zhi-shou-ji/"
  - "/2025/07/03/docker-guo-nei-jing-xiang-pei-zhi-shou-ji.html"
  - "/docker-guo-nei-jing-xiang-pei-zhi-shou-ji.html"
---
Docker 国内镜像配置收集

//DaoCloud

```bash
docker-machine ssh default
sudo sed -i "s|EXTRA_ARGS='|EXTRA_ARGS='--registry-mirror=http://723acd29.m.daocloud.io |g" /var/lib/boot2docker/profile
```

//灵雀云

```bash
docker-machine ssh default
sudo sh -c "echo EXTRA_ARGS='--registry-mirror=http://houchaohann.m.alauda.cn' >>/var/lib/boot2docker/profile
```

//是速云

```bash
docker-machine create -d virtualbox --engine-registry-mirror http://dapeng89.m.tenxcloud.net mydocker
```

