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
> 修改 Docker 容器的启动参数
```sh
docker update --restart=always [container]
```
> 修改 docker 容器的目录映射
```sh
```
> 修改 docker 容器的端口映射
```sh
```
