---
title: 如何学习 Docker (III)
published: true
categories: [program]
tags: [docker]
---

Docker 基本信息操作
> * docker info ： 显示 Docker 系统信息，包括镜像和容器数
> ```sh
> ```
> * docker inspect
> <details>
> <summary>docker version : 显示 Docker 版本信息</summary>
> <pre><code>root@myhost:~# docker version
Client: Docker Engine - Community
 Version:           20.10.5
 API version:       1.41
 Go version:        go1.13.15
 Git commit:        55c4c88
 Built:             Tue Mar  2 20:18:20 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true
Server: Docker Engine - Community
 Engine:
  Version:          20.10.5
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       363e9a8
  Built:            Tue Mar  2 20:16:15 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.4
  GitCommit:        05f951a3781f4f2c1911b05e61c160e9c30eaa8e
 runc:
  Version:          1.0.0-rc93
  GitCommit:        12644e614e25b05da6fd08a38ffa0cfe1903fdec
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
> </code></pre>
> </details>

Docker 容器基本操作
> * docker run
> * docker start
> * docker stop
> * docker restart
> * docker kill
> * docker rm
> * docker create
> * docker exec
> * docker pause
> * docker unpause

Docker 镜像基本操作
> * docker commit
> * docker cp
> * docker diff
> * docker images
> * docker rmi
> * docker tag
> * docker import
> * docker ps
> * docker top
> * docker logs
> * docker port
> * docker export

Docker 仓库基本操作
> * docker login
> * docker logout
> * docker pull
> * docker push
> * docker search

