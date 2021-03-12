---
title: 如何学习 docker (II)
published: true
categories: [program]
tags: [docker]
---

Docker 架构：
> ![](/images/docker-structure.jpg)  
> 在 Docker Client 敲入命令调用 Docker API 来操作 Docker Host  
> Docker Host 可以从 Docke Registry 上拉镜像到本机，也可以用本机镜像创建一个容器并运行  

Docker 仓库 (Registry)
> * 集中存放镜像文件的场所
> * 每个镜像文件有不同的标签（不同的版本）
> * 最大的开放仓库是 [Docker Hub](https://hub.docker.com/) 存放了数量庞大的镜像供用户下载
> * 国内的公开仓库包括阿里云，网易云等
> * 仓库分为公开仓库(public)和私有仓库(private)两种形式

Docker 镜像（Image）
> * 创建容器的模板
> * 一个镜像可以创建很多容器

Docker 容器（Container）
> * 容器是镜像生成的运行实例
> * Docker 利用容器独立运行一个或一组应用（服务）
> * 每个容器之间是相互隔离的
> * 它可以被启用、开始、停止、删除
