---
title: 如何写 Python 脚本的第一行
published: true
categories: [program]
tags: [python]
---

#! 这个符号的名称，叫做 Shebang 或者 Sha-bang。长期以来，Shebang 都没有正式的中文名称。Linux中国翻译组的GOLinux将其翻译为“释伴”，即“解释伴随行”的简称，同时又是Shebang的音译。  
Shebang 通常出现在类 Unix 系统的脚本中第一行，作为前两个字符。在 Shebang 之后，可以有一个或数个空白字符，后接解释器的绝对路径，用于指明执行这个脚本文件的解释器。在直接调用脚本时，系统的程序载入器会分析 Shebang 后的内容，将这些内容作为解释器指令，并调用该指令，将载有 Shebang 的文件路径作为该解释器的参数，执行脚本，从而使得脚本文件的调用方式与普通的可执行文件类似。  
总结一下：
```
#! 必须连接在一起
#! 一句必须在文件的最开始，第一行
# 开头的语句一般情况下会被当成注释而忽略，所以Shebang 对文件的内容是没有影响的
#! 开头的一行会设置解释器运行环境
```
Python 脚本中的第一行应该是#!行，告诉计算机想让 Python 来执行。  
没有 #!，也能从 IDLE 运行，但从命令行运行就需要这一行。  
该行以 #! 开始，但剩下的内容取决于操作系统。  
1. 在 Windows 上，第一行是 ``` #! python3 ```
2. 在 OS X，第一行是 ```#! /usr/bin/env python3 ```
3. 在 Linux 上，第一行是 ``` #! /usr/bin/python3 ```  