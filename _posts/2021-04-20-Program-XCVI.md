---
title: 每天学一个 Windows 命令：color
published: true
categories: [program]
---

## 简介
```
设置默认的控制台前景和背景颜色。
```

## 用法
```cmd
color [ATTR]             指定控制台输出的颜色属性
```

## 参数
```
颜色属性 ATTR 由两个十六进制数字指定, 
第一个对应于背景，第二个对应于前景（文字颜色）。
如果 attr 只有一个十六进制数字，则对应前景，背景色默认为黑色。
每个数字可以为以下任何值:

    0 = 黑色       8 = 灰色
    1 = 蓝色       9 = 淡蓝色
    2 = 绿色       A = 淡绿色
    3 = 浅绿色     B = 淡浅绿色
    4 = 红色       C = 淡红色
    5 = 紫色       D = 淡紫色
    6 = 黄色       E = 淡黄色
    7 = 白色       F = 亮白色

如果没有给定任何参数，此命令会将颜色还原到启动时的颜色。
这个值来自当前控制台窗口、/T 命令行开关或 Defaultcolor 注册表值。
如果尝试使用相同的前景和背景颜色来执行 color 命令，
color 命令会将 ERRORLEVEL 设置为 1。
```

## 示例
```cmd
color fc  修改当前窗口背景颜色为亮白色，前景色为淡红色
color 3   修改当前窗口背景颜色为黑色，前景色为浅绿色
color     修改当前窗口为默认颜色
```