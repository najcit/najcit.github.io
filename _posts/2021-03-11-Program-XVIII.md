---
title: 如何学习 Docker (II)
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

Docker 主机（HOST）
> * 一个物理机或虚拟机
> * 用于运行 Docker 守护进程和多个容器
> * 可存放多个镜像
> * 也称为宿主机，node节点

Docker 守护程序（daemon）
> * 监听 Docker API 请求
> * 也会管理 Docker 对象，如：镜像、容器、网络、卷
> * 守护程序还可以与其他守护程序通信以管理 Docker 服务

Docker 客户端（client）
> * 客户端使用 Docker 命令或其他工具调用 Docker API
> * 当然也可以在 HOST 直接敲 Docker 命令
> * 客户端可以与多个 Docker 守护程序通信

Docker 镜像加速
> * 使用国内的镜像源加速
> * 复制以下代码执行
```sh
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://reg-mirror.qiniu.com"
  ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```