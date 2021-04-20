---
 title : 僵尸进程和孤儿进程 简介
 published : true 
 categories : [program]
---

## 简要概述
>
　　没有父进程的进程就是孤儿进程，孤儿进程会被 init 进程领养，成为一个准守护进程。如果进程他爹活着，但是不给子进程收尸（wait/waitpid），子进程就会变成僵尸。  
　　在 UNIX 系统中，一个进程结束了，但是他的父进程没有等待(调用 wait/waitpid)他，那么他将变成一个僵尸进程。通过 ps 命令查看其带有 defunct 的标志。僵尸进程是一个早已死亡的进程，但在进程表(processs table)中仍占了一个位置(slot)。 但是如果该进程的父进程已经先结束了，那么该进程就不会变成僵尸进程。因为每个进程结束的时候，系统都会扫描当前系统中所运行的所有进程，看看有没有哪个进程是刚刚结束的这个进程的子进程，如果是的话，就由 Init 进程来接管他，成为他的父进程，从而保证每个进程都会有一个父进程。而 Init 进程会自动 wait 其子进程，因此被 Init 接管的所有进程都不会变成僵尸进程。

## 原理分析
>
　　每个 Unix 进程在进程表里都有一个进入点(entry)，核心进程执行该进程时使用到的一切信息都存储在进入点。当用 ps 命令察看系统中的进程信息时，看到的就是进程表中的相关数据。当以 fork 系统调用建立一个新的进程后，核心进程就会在进程表中给这个新进程分配一个进入点，然后将相关信息存储在该进入点所对应的进程表内。这些信息中有一项是其父进程的识别码。  
　　子进程的结束和父进程的运行是一个异步过程，即父进程永远无法预测子进程到底什么时候结束。那么会不会因为父进程太忙来不及 wait 子进程，或者说不知道子进程什么时候结束，而丢失子进程结束时的状态信息呢？不会。因为 UNIX 提供了一种机制可以保证，只要父进程想知道子进程结束时的状态信息，就可以得到。这种机制就是：当子进程走完了自己的生命周期后，它会执行 exit 系统调用，内核释放该进程所有的资源，包括打开的文件，占用的内存等。但是仍然为其保留一定的信息(包括进程号，退出码，退出状态，运行时间等)，这些数据会一直保留到系统将它传递给它的父进程为止，直到父进程通过 wait / waitpid 来取时才释放。

## 解决方法
>
1. 父进程通过 wait 和 waitpid 等函数等待子进程结束，这会导致父进程挂起。
　　执行 wait 或 waitpid 系统调用，则子进程在终止后会立即把它在进程表中的数据返回给父进程，此时系统会立即删除该进入点。在这种情形下就不会产生 defunct 进程。
2. 如果父进程很忙，那么可以用 signal 函数为 SIGCHLD 安装 handler 。在子进程结束后，父进程会收到该信号，可以在 handler 中调用 wait 回收。
3. 如果父进程不关心子进程什么时候结束，那么可以用 signal(SIGCLD, SIG_IGN) 或 signal(SIGCHLD, SIG_IGN)通知内核，自己对子进程的结束不感兴趣，那么子进程结束后，内核会回收，并不再给父进程发送信号
4. fork 两次，父进程 fork 一个子进程，然后继续工作，子进程 fork 一个孙进程后退出，那么孙进程被 init 接管，孙进程结束后， init 会回收。不过子进程的回收还要自己做。