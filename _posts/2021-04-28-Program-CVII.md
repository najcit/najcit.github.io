---
title: 每天学一个 Windows 命令： find / findstr
published: true
categories: [program]
---

## 简介
```
find / findstr 在文件中搜索字符串，输出包含字符串的所有行
findstr 参数设置更高级一些
```

## 用法
```cmd
find [OPTIONS] "STRING" FILE
findstr [OPTIONS] "STRING" FILE
```

## 参数
```
find
    /v         显示所有未包含指定字符串的行
    /c         仅显示包含字符串的行数
    /n         显示行号
    /i         搜索字符串时忽略大小写
    /off[line] 不要跳过具有脱机属性集的文件

findstr
    /b         在一行的开始配对模式
    /e         在一行的结尾配对模式
    /l         按字使用搜索字符串
    /r         将搜索字符串作为正则表达式使用
    /s         在当前目录和所有子目录中搜索匹配文件
    /i         指定搜索不分大小写
    /x         打印完全匹配的行
    /v         只打印不包含匹配的行
    /n         在匹配的每行前打印行数
    /m         如果文件含有匹配项，只打印其文件名
    /o         在每个匹配行前打印字符偏移量
    /p         忽略有不可打印字符的文件
    /off[line] 不跳过带有脱机属性集的文件
    /a:attr    指定有十六进位数字的颜色属性
    /f:file    从指定文件读文件列表 (/ 代表控制台)
    /c:string  使用指定字符串作为文字搜索字符串
    /g:file    从指定的文件获得搜索字符串 (/ 代表控制台)
    /d:dir     查找以分号为分隔符的目录列表

正则表达式:
  .        通配符: 任何字符
  *        重复: 以前字符或类出现零或零以上次数
  ^        行位置: 行的开始
  $        行位置: 行的终点
  [class]  字符类: 任何在字符集中的字符
  [^class] 补字符类: 任何不在字符集中的字符
  [x-y]    范围: 在指定范围内的任何字符
  \x       Escape: 元字符 x 的文字用法
  \<xyz    字位置: 字的开始
  xyz\>    字位置: 字的结束
```

## 示例
```cmd
find /i /n "test" test.txt                 # 在 test.txt 文件中搜索 test 字符串

findstr /n "hello there" x.y               # 在文件 x.y 中寻找 "hello" 或 "there"

findstr /n /c:"hello there" x.y            # 在文件 x.y 中寻找 "hello there"

findstr /n /a:4 "button" *.html            # 在当前所有 .html 文件中搜索 button 并用颜色(红色)标记
```