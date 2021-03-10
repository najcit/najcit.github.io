---
title: 如何学习 docker
published: true
categories: [program]
tags: [docker]
---

Docker 三个基本概念
> * 镜像（Image）
> * 容器（Container）
> * 仓库（Repository）

Docker 典型使用场景:
> * 让应用快速打包与容易自动化部署
> * 创建轻量、私密的 PAAS(Platform as a Service) 环境
> * 实现自动化测试和持续的集成/部署

Docker 可以解决的项目痛点:
> * 需要频繁的升级，可以充分利用 docker 的镜像版本快速升级回退;
> * 开发，测试，线上的代码运行环境经常变更，每当你查了半天 bug，最后竟然是环境不一致的时候;
> * 销售演示或者 POC(Proof of Concept) 的 demo， 启动后无历史数据，免去清理数据的苦恼，但其实也有，但是便捷;
> * 项目体量过大，进行了微服务改造，需要统一管理，docker-compose 可以了解一下;
> * 占用资源过多，可以利用 docker 资源配额和设置启动策略，提升稳定性;
> * 整合开源服务，随着 docker 使用的普及，越来越多的开源项目提供了 docker 镜像部署。

Docker 运行环境限制:
> * 必须是64位机器上运行，目前仅支持 x86_64 和 AMD64，32系统不支持;
> * 系统的 Linux 内核必须是3.8或者更高，内核支持 Device Mapper，AUFS，VFS，btrfs 等存储格式;
> * 内核必须支持 cgroups 和命名空间。