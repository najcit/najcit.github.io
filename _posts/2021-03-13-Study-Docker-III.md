---
title: 如何学习 Docker (III)
published: true
categories: [program]
tags: [docker]
---

Docker 基本信息操作
> * docker info ： 显示 Docker 系统信息，包括镜像和容器数
> * docker inspect: 获取容器/镜像的元数据（JSON格式）
> * docker version : 显示 Docker 版本信息

Docker 容器基本操作
> * docker run ： 创建一个容器，并运行
> * docker start ： 启动容器
> * docker stop : 停止容器
> * docker restart : 重启容器
> * docker kill : 向正在运行的容器的进程发送 SIGKILL 信号
> * docker rm ： 删除容器
> * docker create ： 依据镜像创建容器
> * docker exec: 在运行的容器中运行命令
> * docker pause : 暂停一个或多个容器中的所有进程
> * docker unpause : 恢复一个或多个容器中的所有进程

Docker 镜像基本操作
> * docker commit ： 利用容器创建一个新的镜像
> * docker cp ： 在容器和主机之间复制文件/文件夹
> * docker diff : 检查容器文件系统上文件或目录的更改情况
> * docker images : 查看镜像
> * docker rmi ： 删除一个或多个镜像
> * docker tag ： 给镜像打一个标记
> * docker import : 从 tar 归档文件中创建镜像
> * docker ps : 列出容器
> * docker top : 查看容器中的进程运行情况
> * docker logs ： 提取容器的日志
> * docker port : 列出运行的容器的端口映射
> * docker export : 将容器的文件系统导出为 tar 文件

Docker 仓库基本操作
> * docker login ： 登入镜像仓库
> * docker logout ： 登出镜像仓库
> * docker pull ： 从镜像仓库中拉取或更新镜像
> * docker push ： 推送或更新镜像仓库中镜像
> * docker search ： 从 DockerHub 查找镜像

