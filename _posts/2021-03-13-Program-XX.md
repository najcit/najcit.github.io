---
title: 如何使用 Github Action
published: true
categories: [program]
tags: [github]
---

GitHub Action 是什么
> GitHub 把持续集成中的很多操作，比如抓取代码、运行测试、登录远程服务器，发布到第三方服务
> 等这些操作就称为 Actions。

GitHub Action 的基本术语
> 工作流程（workflow）：持续集成一次运行的过程，就是一个 workflow。  
> 任务（job）：一个 workflow 由一个或多个 jobs 构成，含义是一次持续集成的运行，可以完成多个任务。  
> 步骤（step）：每个 job 由多个 step 构成，一步步完成。  
> 动作（action）：每个 step 可以依次执行一个或多个 action。  

GitHub Action 配置文件
> GitHub Actions 的配置文件叫做 workflow 文件，  
> 存放在代码仓库的 .github/workflows 目录。  
> 1. name
> 2. on
> 3. jobs
