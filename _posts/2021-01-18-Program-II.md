---
title: 如何使用 Github Pages
published: true
categories: [program]
tags: [github]
---

**想拥有一个自定义的博客, 可以比较方便的写文章和记录总结, 并且方便和免费的.**
**按照以下步骤就可以完成.**

开始前, 简单说下主要的思路, 使用 Github 账户中的 repository 的 Github Pages 功能即可, 在 repository 中保存 md(markdown) 格式的文本文件, 在通过设置, 可以直接渲染出一个网页效果, 供自己和大家浏览,只要我们更新 md 文件, 即可更改网页内容

## [](#header-1)1. 注册或登录 [Github](https://github.com) 账户
> [Link to Github](https://github.com)

## [](#header-2)2. 在账户下创建一个 respository (username.github.io)
> 1. 名称必须是 username.github.io，如果账户名称是 abc, 则仓库名称是 abc.github.io
> 2. 权限设置为 Public 

## [](#header-3)3. 修改 respository 的 Setting 中关于 Github Pages 的内容
> 1. Source 设置渲染的指定分支下的指定路径，一般设置 main 分支下的 root 路径即可
> 2. Theme Choser 设置渲染的主题，可以点击选择给定的主题样式
> 3. Custom domain 设置自定义域名，需要自己有域名
> 4. Enforce HTTPS 是否强制使用 HTTPS 协议访问网站，只有是自定义域名下可以使用，使用 Github 默认的域名就是选中状态，不可更改

## [](#header-4)4. 在 repository 中创建 markdown 文件
> 使用 markdown 语法写博客，再更新到 repository 中，
稍等一会儿，访问 https://username.github.io (username 需替换成自己的用户名称) 可查看效果
