---
title: 如何学习 Docker (IV)
published: true
categories: [program]
tags: [docker]
---

Docker 常用操作
> Docker 删除所有无名称的镜像（悬空镜像）: 
```sh
docker rmi $(docker images -f "dangling=true" -q)
```
> Docker 删除所有镜像：
```sh
docker rmi -f $(docker images -qa)
```

