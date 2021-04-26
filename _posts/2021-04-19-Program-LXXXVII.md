---
title: 每天学一个 Linux 命令： cut
published: true
categories: [program]
---

## 简介
```
从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段写至标准输出。
```

## 用法
```bash
cut [options] [file]
```

## 参数
```
-b ：以字节为单位进行分割，一般用于字母提取。
-c ：以字符为单位进行分割，一般用于中文提取。
-d ：自定义分隔符，默认为制表符。
-f ：与 -d 一起使用，指定显示哪个区域。
```

## 示例
```bash
who | cut -b 1-3                                # 显示 who 命令每行的前三个字节

cat cut.txt                                     # 查看一个包含中文的文本文件
周杰伦
邓紫棋
薛之谦
李荣浩
cat cut.txt | cut -c 1                          # 显示 cut.txt 每行内容的第一个字符，即第一个中文

head -n 5  /etc/passwd                          # 查看 /etc/passwd 的前五行内容
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
head -n 5  /etc/passwd | cut -d : -f 1          # 提取每行以 : 分割的第一个内容块
```
