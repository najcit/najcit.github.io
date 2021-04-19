---
title: 每天学一个 Linux 命令：gdb
published: true
categories: [program]
---

## 简介
> gdb（GNU Debugger）是在 Unix 以及类 Unix 系统下的调试工具。功能极其强大。   
> gdb 可以在大多数流行的 UNIX 和 Microsoft Windows 变体以及 Mac OS X 上运行。  
> gdb 不仅可以在同一台计算机（本地）上执行，还可以在另一台计算机（远程）上或在模拟器上执行。  
> gdb 可以做四种主要的事情（以及支持这些事情的其他事情）来帮助你捕获行为中的错误：
>    * 启动你的程序，并指定可能影响其行为的所有内容。
>    * 使程序在指定条件下停止。
>    * 检查程序停止时发生的情况。
>    * 更改程序中的内容，以便你可以尝试纠正一个错误的影响，然后继续学习另一个错误。  

## 用法
```bash
gdb [参数] [程序 [core 文件 / 进程 ID]]        #调试不带命令行参数
gdb [参数] --args 程序 [程序参数]              #调试命令行参数
```

## 参数
```
选取调试程序及相关文件
  --args             指定程序的命令行参数
  --core=COREFILE    分析程序崩溃后产生的 core 文件
  --exec=EXECFILE    指定程序运行文件
  --pid=PID, -p      通过进程 PID 绑定当前运行的程序
  --directory=DIR    指定源文件目录
  --se=FILE          指定 symbol 文件和执行文件为 FILE
  --symbols=SYMFILE  指定 symbol 文件
  --readnow          设置开始时读取 symbol 文件
  --readnever        设置不读取 symbol 文件
  --write            设置可以写入执行文件和 core 文件
  --cd=DIR           设置当前工作目录
  --data-directory=DIR, -D
                     设置 GDB 的数据目录

设置调试命令
  --command=FILE, -x 执行指定文件里面的命令
  --init-command=FILE, -ix
                     在运行程序前,执行指定文件里面的命令
  --eval-command=COMMAND, -ex
                     指定一个 gdb 命令
  --init-eval-command=COMMAND, -iex
                     在运行程序前， 执行一个 gdb 命令
  --nh               设置不要读取 ~/.gdbinit 文件 (可以自定义命令的文件)
  --nx               设置不要读取任何地方的 gdbinit 文件

远程调试
  -b BAUDRATE        设置串口调试的波特率
  -l TIMEOUT         设置远程调试的时间延时

其他
  --tty=TTY          使用 tty 作为当前调试的程序的输入与输出
  -w                 使用 gdb GUI 调试
  --nw               不使用 gdb GUI 调试
  --tui              使用终端 ui 调试
  -q, --quiet, --silent
                     不输出多余的信息
  --return-child-result
                     GDB 以程序的退出码退出
  --configuration    打印 GDB 配置信息
  --version          打印 GDB 版本信息
```

## 命令
```
break [file:]function       Set a breakpoint at function (in file).
run [arglist]               Start your program (with arglist, if specified).
bt  Backtrace:              display the program stack.
print expression            Display the value of an expression.
continue                    Continue running your program (after stopping, e.g. at a breakpoint).
next                        Execute next program line (after stopping); step over any function calls in the line.
step
finish
edit [file:]function        look at the program line where it is presently stopped.
list [file:]function        type the text of the program in the vicinity of where it is presently stopped. Execute next program line (after stopping); step into any function calls in the line.
help [name]                 Show information about GDB command name, or general information about using GDB.
quit                        Exit from GDB.

next                
step                
continue                
print               
Backtrace       bt      
finish              
quit                
wachtpoint              
catchpoint              
delete      d       
clear   清除所有已定义的停止点         
disable     dis     
enable              
ignore      c 或者 fg     
until       u       
frame       f       
up              
down                
```

## 案例
### 1. 单进程程序调试

### 2. 多进程程序调试

### 3. 多线程程序调试