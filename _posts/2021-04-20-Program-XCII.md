---
title: Windows 和 WSL 之间的文件操作
published: true
categories: [program]
---

## Windows 访问 Linux 文件
> 通过 \\wsl$ 访问 Linux 文件时将使用 WSL 分发版的默认用户。  
> 因此，任何访问 Linux 文件的 Windows 应用都具有与默认用户相同的权限

## Linux 访问 Windows 文件
> 在从 WSL 访问 Windows 文件时，可以直接使用/mnt/{Windows盘符}进入对应的盘中。