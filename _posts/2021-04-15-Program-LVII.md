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
break [file:]function|line_number       在文件内部的函数或行数设置断点
delete bookmark|breakpoints|checkpoint  删除 bookmark|breakpoints|checkpoint等信息
clear [file:]function|line_number       删除文件内部的函数或行数设置的断点
disable breakpoint_number               禁用断点
enable breakpoint_number                启用断点
ignore breakpoint_number [count]        忽略断点count次，默认一直忽略
watch variable                          监视变量发生变化，暂停允许
awatch                                  监视被访问时，发生变化，暂停运行
rwatch                                  监视被访问时，暂停运行
start [args]                            启动程序带参数或者不带参数，并运行临时断点到 main 函数
run [args]                              启动程序带参数或者不带参数
backtrace / where                       程序中的当前位置和表示如何到达当前位置的栈跟踪
print EXPRESSION                        打印 EXPRESSION 数值
continue                                继续运行程序
next                                    下一步继续运行程序，不进入函数内部
stop                                    下一步继续运行程序，进入函数内部
finish                                  执行完当前函数，暂停
edit [file:]function|line_number        编辑文件内部的函数/行数的内容                    
set args| variable                      设置输入参数，变量等
cd                                      改变工作路径
directory                               增加搜索源文件目录
list [file:]function|line_number        显示文件内部的函数/行数的内容
info                                    显示各种信息
show argv                               显示输入参数，变量等信息
whatis                                  查看变量类型信息
ptype                                   查看变量类型信息，包括结构体信息
gcore                                   生成 core 文件
quit / kill                             退出 GDB
help [CMD]                              查看 CMD 的文档
```

## 案例
### 1. 单进程程序调试
```
设置断点，运行，查看变量和源码，退出等基本操作
```

```c
/* 源文件: a.c */
#include <stdio.h>

int add(int x, int y) {
    return x+y;
}

int main(char **argv, int argc) {
    int x = 10;
    int y = 20;
    int num = add(x,y);
    printf("num = %d\n",num);
    return 0;
}
```

```bash
# 命令行编译程序
gcc -g a.c -o a     # 编译程序
gdb a               # 调试程序
```

```gdb
(gdb) start
Temporary breakpoint 1 at 0x1161: file a.c, line 7.
Starting program: /root/a
Temporary breakpoint 1, main (argv=0x555555555060 <_start>, argc=0) at a.c:7
7       int main(char **argv, int argc) {
(gdb) l
2
3       int add(int x,int y) {
4           return x+y;
5       }
6
7       int main(char **argv, int argc) {
8           int x = 10;
9           int y = 20;
10          int num = add(x,y);
11          printf("num = %d\n",num);
(gdb) l
12          return 0;
13      }
(gdb) b add
Breakpoint 2 at 0x555555555149: file a.c, line 3.
(gdb) c
Continuing.

Breakpoint 2, add (x=21845, y=1431654925) at a.c:3
3       int add(int x,int y) {
(gdb) n
4           return x+y;
(gdb) p x
$1 = 10
(gdb) p y
$2 = 20
(gdb) p x+y
$3 = 30
(gdb) info b
Num     Type           Disp Enb Address            What
2       breakpoint     keep y   0x0000555555555149 in add at a.c:3
        breakpoint already hit 1 time
(gdb) c
Continuing.
num = 30
[Inferior 1 (process 583) exited normally]
(gdb) q

```

### 2. 多进程程序调试
```
set follow-fork-mode parent|child   设置调试器的模式，
                                    parent -- fork 之后调试原进程，子进程不受影响，缺省值
                                    child  -- fork 之后调试新的进程，父进程不受影响
show follow-fork-mode               显示当前调试器的模式
set detach-on-fork on|off           设置 fork 之后是否 detach 进程中的其中一个，或控制住这两个进程
                                    on  -- 进程会 detach 然后独立运行，缺省值
                                    off -- 两个进程都受 gdb 控制
info inferiors                      显示所有进程
inferiors processid                 切换进程
catch fork                          让程序在 fork，vfork 或者 exec 调用的时候中断
detach inferiors processid          detach 指定进程，然后从 fork 列表里删除，进程会继续独立运行
kill inferiors  processid           杀死一个由指定的进程，然后从fork 列表里删除
```

```c
/* 源文件： b.c */
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int add(int x, int y) {
    return x+y;
}

int test() {
    int num = 0;
    pid_t pid  = fork();
    if(pid == 0) {
        while(1) {
            num = add(1,2);
            printf("child:pid:%d num = %d\n", getpid(), num);
            sleep(1);
        }
        exit(0);
    }

    while(1) {
        num = add(10,20);
        printf("parent:pid:%d num = %d\n", getpid(), num);
        sleep(1);
    }
    return 0;
}

int main(char **argv, int argc) {
    test();
    return 0;
}
```

```bash
gcc -g b.c -o b     # 编译程序
gdb b               # 调试程序
```

```gdb
(gdb) catch fork
Catchpoint 1 (fork)
(gdb) show follow-fork-mode
Debugger response to a program call of fork or vfork is "parent".
(gdb) show detach-on-fork
Whether gdb will detach the child of a fork is on.
(gdb) set detach-on-fork off
(gdb) start
Temporary breakpoint 2 at 0x125c: file b.c, line 30.
Starting program: /root/b
Temporary breakpoint 2, main (argv=0x0, argc=32767) at b.c:30
30      int main(char **argv, int argc) {
(gdb) l b.c:10
5
6       int add(int x, int y) {
7           return x+y;
8       }
9
10      int test() {
11          int num = 0;
12          pid_t pid  = fork();
13          if(pid == 0) {
14              while(1) {
(gdb) l
15                  num = add(1,2);
16                  printf("child:pid:%d num = %d\n", getpid(), num);
17                  sleep(1);
18              }
19              exit(0);
20          }
21
22          while(1) {
23              num = add(10,20);
24              printf("parent:pid:%d num = %d\n", getpid(), num);
(gdb) l
25              sleep(1);
26          }
27          return 0;
28      }
29
30      int main(char **argv, int argc) {
31          test();
32          return 0;
33      }
(gdb) b b.c:14
Breakpoint 3 at 0x5555555551e2: file b.c, line 15.
(gdb) b b.c:22
Breakpoint 4 at 0x55555555521f: file b.c, line 22.
(gdb) c
Continuing.
Catchpoint 1 (forked process 675), arch_fork (ctid=0x7ffff7fbd810) at ../sysdeps/unix/sysv/linux/arch-fork.h:49
49      ../sysdeps/unix/sysv/linux/arch-fork.h: No such file or directory.
(gdb) c
Continuing.
[New inferior 2 (process 675)]
Reading symbols from /root/b...
Reading symbols from /usr/lib/debug/lib/x86_64-linux-gnu/libc-2.31.so...
Thread 1.1 "b" hit Breakpoint 4, test () at b.c:22
23              num = add(10,20);
(gdb) info inferiors
  Num  Description       Executable
* 1    process 671       /root/b
  2    process 675       /root/b
(gdb) inferior 2
[Switching to inferior 2 [process 675] (/root/b)]
[Switching to thread 2.1 (process 675)]
#0  arch_fork (ctid=0x7ffff7fbd810) at ../sysdeps/unix/sysv/linux/arch-fork.h:49
49      ../sysdeps/unix/sysv/linux/arch-fork.h: No such file or directory.
(gdb) c
Continuing.
Thread 2.1 "b" hit Breakpoint 3, test () at b.c:14
15                  num = add(1,2);
(gdb) inferior 1
[Switching to inferior 1 [process 671] (/root/b)]
[Switching to thread 1.1 (process 671)]
#0  test () at b.c:22
23              num = add(10,20);
```

### 3. 多线程程序调试
```
info threads                        查询线程信息
thread threadid                     切换线程
thread apply [threadid] [all] args  对线程列表执行命令
set print thread-events             控制线程开始和结束时的打印信息
show print thread-events            显示线程打印信息的开关状态
```
```c
/* 源代码： c.c */
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

int add(int x,int y) {
    return x+y;
}

void* thread(void *args) {
    int num = 0;
    while(1) {
        num += add(1,2);
        sleep(1);
    }
}

int main(char** argv, int argc) {
    pthread_t tid;
    pthread_create(&tid, NULL, thread, NULL);
    int num = 0;
    while(1) {
        num += add(10,20);
        sleep(1);
    }
    return 0;
}
```

```bash
gcc -g c.c -o c -lpthread   # 编译程序
gdb c                       # 调试程序
```

```gdb
(gdb) b add
Breakpoint 1 at 0x1169: file c.c, line 6.
(gdb) s
The program is not being run.
(gdb) start
Temporary breakpoint 2 at 0x11b6: file c.c, line 18.
Starting program: /root/c
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 2, main (argv=0x555555555220 <__libc_csu_init>, argc=32767) at c.c:18
18      int main(char** argv, int argc) {
(gdb) c
Continuing.
[New Thread 0x7ffff7da3700 (LWP 713)]
[Switching to Thread 0x7ffff7da3700 (LWP 713)]

Thread 2 "c" hit Breakpoint 1, add (x=0, y=0) at c.c:6
6       int add(int x,int y) {
(gdb) info threads
  Id   Target Id                           Frame
  1    Thread 0x7ffff7da4740 (LWP 709) "c" add (x=0, y=0) at c.c:6
* 2    Thread 0x7ffff7da3700 (LWP 713) "c" add (x=0, y=0) at c.c:6
(gdb) c
Continuing.
[Switching to Thread 0x7ffff7da4740 (LWP 709)]

Thread 1 "c" hit Breakpoint 1, add (x=0, y=0) at c.c:6
6       int add(int x,int y) {
(gdb) info threads
  Id   Target Id                           Frame
* 1    Thread 0x7ffff7da4740 (LWP 709) "c" add (x=0, y=0) at c.c:6
  2    Thread 0x7ffff7da3700 (LWP 713) "c" 0x000055555555516d in add (x=0, y=0) at c.c:6
(gdb) thread 2
[Switching to thread 2 (Thread 0x7ffff7da3700 (LWP 713))]
#0  0x000055555555516d in add (x=0, y=0) at c.c:6
6       int add(int x,int y) {
(gdb) info threads
  Id   Target Id                           Frame
  1    Thread 0x7ffff7da4740 (LWP 709) "c" add (x=0, y=0) at c.c:6
* 2    Thread 0x7ffff7da3700 (LWP 713) "c" 0x000055555555516d in add (x=0, y=0) at c.c:6
(gdb) thread apply 1 bt

Thread 1 (Thread 0x7ffff7da4740 (LWP 709)):
#0  add (x=0, y=0) at c.c:6
#1  0x000055555555520b in main (argv=0x1, argc=-6600) at c.c:23
(gdb) thread apply 2 bt

Thread 2 (Thread 0x7ffff7da3700 (LWP 713)):
#0  0x000055555555516d in add (x=0, y=0) at c.c:6
#1  0x00005555555551a7 in thread (args=0x0) at c.c:13
#2  0x00007ffff7fa2609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#3  0x00007ffff7ec9103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
(gdb) thread apply all bt

Thread 2 (Thread 0x7ffff7da3700 (LWP 713)):
#0  0x000055555555516d in add (x=0, y=0) at c.c:6
#1  0x00005555555551a7 in thread (args=0x0) at c.c:13
#2  0x00007ffff7fa2609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#3  0x00007ffff7ec9103 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

Thread 1 (Thread 0x7ffff7da4740 (LWP 709)):
#0  add (x=0, y=0) at c.c:6
#1  0x000055555555520b in main (argv=0x1, argc=-6600) at c.c:23
(gdb) set print thread-events off
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/c
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
....
(gdb) set print thread-events on
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /root/c
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff7da3700 (LWP 756)]
....
(gdb) show print thread-events
Printing of thread events is off.
```

### 4. 程序core文件调试
```
程序崩溃了，一般会产生 core 文件。core 文件仅仅是一个内存映像(同时加上调试信息)，可以用调试寻找代码 bug。
core 文件的生成需要系统预先设置，使用命令 ulimit -c SIZE 设置生存的 core 文件的大小不超过 SIZE kb, 如果 SIZE 为 0, 则不会生存 core 文件。
使用 gdb --core core 启动，可以知道是什么程序生存这个 core 文件，知道了程序 d，就可以使用
gdb --core core d 来查看崩溃时，使用 bt(backtrace) 相关调试信息。
```

### 5. 运行的程序调试
```
首先查出进程的 PID, 使用 top 或 ps 即可，输入 gdb 程序 PID attach 到正在运行的程序，剩下的调试工作，可按照以上的各种场景来进行
还有另一种方法 attach 进程，先 gdb 启动，使用命令 attach PID 来 attach 进程
```

### 6. 远程程序调试
```
远程调试环境由宿主机 gdb 和目标机调试 stub 共同构成，两者通过串口或 TCP 连接。使用 GDB 标准程串行协议协同工作，实现对目标机上的系统内核和上层应用的监控和调试功能。我们最常用的是调试应用程序，就是采用 gdb+gdbserver 的方式进行调试。
1. 目标机上启动 gdbserver IP:PORT APP 
2. 宿主机上复制来 APP 程序
3. 宿主机上启动 gdb APP
4. 宿主机上 gdb 里面输入 target remote IP:PORT
5. 宿主机上可使用 gdb 命令调试目标机上的程序 APP
注意：本地调试环境下 gdb 通过 run/r 指令让程序运行。远程调试环境下，通过 gdbserver 已经运行了程序，gdb 通过 continue/c 让程序继续运行
```

## 参考
1. [gdb 手册](https://sourceware.org/gdb)
2. [gdb 详细使用手册](https://blog.csdn.net/andrewgithub/article/details/88210949)
3. [gdb+gdbserver 使用](https://blog.csdn.net/weixin_42045853/article/details/86549858)