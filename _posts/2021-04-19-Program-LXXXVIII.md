---
title: 每天学一个 Linux 命令： column
published: true
categories: [program]
---

## 简介
```
按照多列的格式化输出内容
```

## 用法
```
column [-entx] [file]
       [-c columns] [file]
       [-s sep] [file]
```

## 参数
```
-s      指定分割字符集合
-t      以表格的形式输出内容
-x      优先格式化列内容
-n      当分隔符在一起的时候，保留空白内容的位置
-e      不要忽略空行
```

## 示例
```
mount | column -tn -s ' ' # 以空格为分隔符，以表格的形式输出 mount 的内容
tmpfs        on  /mnt/wsl                   type  tmpfs        (rw,relatime)
tools        on  /init                      type  9p           (ro,relatime,dirsync,aname=tools;fmask=022,loose,access=client,trans=fd,rfd=6,wfd=6)
none         on  /dev                       type  devtmpfs     (rw,nosuid,relatime,size=4859524k,nr_inodes=1214881,mode=755)
······
```
