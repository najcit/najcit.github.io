---
title: 如何配置 Github Page 的自定义域名
published: true
---

在开通了 Github Page 后,可以通过 Github 提供的域名 <username>.github.io 来访问自己的页面, 其实 Github 提供好了自定义的域名的功能, 配置完成后,可以通过自己的域名来访问页面.
配置的思路就是, 首先需要一个自己的域名解析到github的地址上,这个方式有2个方式,一个是指定 ip，一个是指定域名，推荐后面，因为有可能 Github 的 ip 可能会在不同的时间会改变,但域名是不会改变的,然后Github 的 repository 中的 Setting 页面设置中的 Custom domain 中填入自己的域名即可.

# 步骤 1 自己的域名配置解析
> 域名解析-指向 ip  
> 
![](/images/dns-ip.jpeg)

> 域名解析-指向域名
>   
![](/images/dns-cname.jpeg)

# 步骤 2 Github Page 配置域名
> repository 中 Github Page 的配置
> 
![](/images/github-page.png)