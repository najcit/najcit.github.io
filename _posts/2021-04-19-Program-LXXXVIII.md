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
head -n 5 /etc/passwd                          # 查看 /etc/passwd 的前五行内容
root:x:0:0:root,02,02,03,04:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync

head -n 5 /etc/passwd | column -tn -s :        # 以 : 为分隔符，表格的形式输出内容
root    x  0  0      root,02,02,03,04  /root      /bin/bash
daemon  x  1  1      daemon            /usr/sbin  /usr/sbin/nologin
bin     x  2  2      bin               /bin       /usr/sbin/nologin
sys     x  3  3      sys               /dev       /usr/sbin/nologin
sync    x  4  65534  sync              /bin       /bin/sync
```
