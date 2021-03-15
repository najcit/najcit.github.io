---
title: 如何学习 Docker (IV)
published: true
categories: [program]
tags: [docker]
---

## Docker 常用操作

Docker 删除所有无名称的镜像（悬空镜像）: 
>
```sh
docker rmi $(docker images -f "dangling=true" -q)
```

Docker 删除所有镜像：
>
```sh
docker rmi -f $(docker images -qa)
```

修改 Docker 容器的启动参数
>
```sh
docker update --restart=always [container]
```

修改 docker 容器的目录映射
> 1. 删除掉原来的容器，重新建立新的容器
```sh
docker rm -f [container]
docker run [option] [container]
```
> 2. 修改容器的配置文件
```sh
systemctl stop docker
cd /var/lib/docker/container/[container]/
vim config.v2.json # 搜索 MountPoint 并修改成新的目录
systemctl stop docker
```
> 3. 用现在的容器构建新的镜像，然后通过镜像创建新的容器
```sh
docker stop [old_container]
docker commit [old_container] [image]
docker run [option] [image]
dokcer rm [old_container]
docker rename [new_container] [old_container]
```

修改 docker 容器的端口映射
> 修改端口的方式和修改目录映射的方式是一致的，也可用上述3中方式  
> 需要注意的是在修改配置文件时，需要修改 HostPort 对应数值

解决容器内获取的时间和主机的时间不一样的问题
> 1. 在运行容器时，挂载 /etc/localtime 目录
```sh
docker run -d -v /etc/localtime:/etc/localtime:ro [container]
```
> 2. 复制主机的 /etc/localtime 到容器里面
```sh
docker cp /etc/localtime [container]:/etc/localtime
```

解决重新进入容器后，环境变量失效的问题
> 