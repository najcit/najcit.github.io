---
title: 每天学一个 Linux 命令： jobs / fg / bg
published: true
categories: [program]
---

## 简介
```
jobs    查看当前有多少后台运行的命令
fg      将后台中的命令调至前台继续运行, 如果后台中有多个命令，
        可以用 fg %jobnumber 将选中的命令调出，
        %jobnumber 是通过 jobs 命令查到的后台正在执行的命令的序号(不是pid)
bg      将一个在后台暂停的命令，变成继续执行，可以用 bg %jobnumber 将选中的命令调出，
        %jobnumber 是通过 jobs 命令查到的后台正在执行的命令的序号(不是pid)
&       放在一个命令的后面，可以把这个命令放到后台执行
ctrl+z  可以将一个正在前台执行的命令放到后台，并且暂停
```

## 用法
```
jobs [option]   显示 后台进程信息
fg [%jobnumber] 将后台进程放到前台运行
bg [%jobnumber] 将后台进程放到前台运行
```

## 参数
```
-l        列出 PID 信息
-n        列出状态发生变化的进程
-p        只列出 PID 信息
-r        只列出运行的进程
-s        只列出停止的进程
```

## 示例
```bash
ping baidu.com &    # 后台运行 ping 命令
job -l              # 查看后台进程信息
fg                  # 调整 ping 到前台运行
【Ctrl+Z】            # 暂停 ping 运行
bg                  # 后台运行 ping
```
