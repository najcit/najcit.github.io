---
title: 每天学一个 Linux 命令： passwd / gpasswd
published: true
categories: [program]
---

## 简介
```
passwd  用来改变用户密码
gpasswd 管理用户组用户及密码
```

## 用法
```bash
passwd  [option] [username] [password]
gpasswd [option] [username] [usergroup]
```

## 参数
```
passwd
    -a 查看所有用户的状态，与 -S 一起使用
    -d 删除密码
    -e 强制过期用户的密码
    -f 强迫用户下次登录时必须修改口令
    -w 口令要到期提前警告的天数
    -k 更新只能发送在过期之后
    -l 停止账号使用
    -S 显示密码信息
    -u 启用已被停止的账户
    -x 指定口令最长存活期
    -n 指定口令最短存活期

gapsswd
    -a, --add USER                添加用户到组
    -d, --delete USER             从组中移除用户
    -Q, --root CHROOT_DIR         改变用户 root 目录
    -r, --remove-password         移除用户组的密码
    -R, --restrict                限制用户登陆组
    -M, --members USER            设置用户组用户
    -A, --administrators ADMIN    设置用户组管理员用户
```

## 示例
```bash
passwd -Sa                      # 查看登陆用户的状态
root P 04/27/2021 0 99999 7 -1
daemon L 04/23/2020 0 99999 7 -1
bin L 04/23/2020 0 99999 7 -1
sys L 04/23/2020 0 99999 7 -1
sync L 04/23/2020 0 99999 7 -1
games L 04/23/2020 0 99999 7 -1
man L 04/23/2020 0 99999 7 -1
lp L 04/23/2020 0 99999 7 -1

passwd -S root                   # 查看用户 root 的状态
root P 04/27/2021 0 99999 7 -1

passwd test                     # 修改用户 test 的密码

gpasswd test                    # 修改用户组 test 的密码

gpasswd -a test root            # 添加用户 test 到用户组 root

gpasswd -d test root            # 删除用户 test 从用户组 root

gpasswd -M test，test2 root     # 设置用户组 root 的用户 test, test2
```
