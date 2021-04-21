---
title: 每天学一个 Windows 命令：ipconfig
published: true
categories: [program]
---

## 简介
```
ipconfig 用于显示当前的 TCP/IP 的网络配置，刷新动态主机配置协议和域名系统设置。不带参数的 ipconfig 可以显示所有的适配器的 IP 地址，子网掩码，默认网关。
```

## 用法
```cmd
ipconfig [/allcompartments] [/? | /all |
         /renew [ADAPTER] | /release [ADAPTER] |
         /renew6 [ADAPTER] | /release6 [ADAPTER] |
         /flushdns | /displaydns | /registerdns |
         /showclassid ADAPTER |
         /setclassid ADAPTER [CLASSID] |
         /showclassid6 ADAPTER |
         /setclassid6 ADAPTER [CLASSID] ]
```

## 参数
```
/?               显示此帮助消息
/all             显示完整配置信息。
/release         释放指定适配器的 IPv4 地址。
/release6        释放指定适配器的 IPv6 地址。
/renew           更新指定适配器的 IPv4 地址。
/renew6          更新指定适配器的 IPv6 地址。
/flushdns        清除 DNS 解析程序缓存。
/registerdns     刷新所有 DHCP 租用并重新注册 DNS 名称
/displaydns      显示 DNS 解析程序缓存的内容。
/showclassid     显示适配器允许的所有 DHCP 类 ID。
/setclassid      修改 DHCP 类 ID。
/showclassid6    显示适配器允许的所有 IPv6 DHCP 类 ID。
/setclassid6     修改 IPv6 DHCP 类 ID。

对于 release 和 renew，如果未指定适配器 ADAPTER (允许使用通配符 * 和 ?)，
则会释放或更新所有绑定到 TCP/IP 的适配器的 IP 地址租用。
对于 setclassid 和 setclassid6，如果未指定 CLASSID，则会删除 CLASSID。
```

## 示例
```cmd
ipconfig                           显示所有适配器的基本信息
ipconfig /all                      显示所有适配器的详细信息
ipconfig /renew                    更新所有适配器
ipconfig /renew EL*                更新所有名称以 EL 开头的连接
ipconfig /release *Con*            释放所有匹配的连接，例如“有线以太网连接 1”或“有线以太网连接 2”
ipconfig /allcompartments          显示有关所有隔离舱的信息
ipconfig /allcompartments /all     显示有关所有隔离舱的详细信息
ipconfig /registerdns              初始化 DNS 和 IP 配置
ipconfig /flushdns                 清除 DNS 客户端缓存信息
ipconfig /displaydns               查看 DNS 客户端缓存信息
```