---
title: 编写 Windows 服务程序的五个步骤
published: true
categories: [program]
---

Windows 服务被设计用于需要在后台运行的应用程序以及实现没有用户交互的任务。为了学习这种控制台应用程序的基础知识，C（不是C++）是最佳选择。本文将建立并实现一个简单的服务程序，其功能是查询系统中可用物理内存数量，然后将结果写入一个文本文件。最后，你可以用所学知识编写自己的 Windows 服务。

　　当初我写第一个NT 服务时，我到 MSDN 上找例子。在那里我找到了一篇 Nigel Thompson 写的文章：“Creating a Simple Win32 Service in C++”，这篇文章附带一个 C++ 例子。虽然这篇文章很好地解释了服务的开发过程，但是，我仍然感觉缺少我需要的重要信息。我想理解通过什么框架，调用什么函数，以及何时调用，但 C++ 在这方面没有让我轻松多少。面向对象的方法固然方便，但由于用类对底层 Win32 函数调用进行了封装，它不利于学习服务程序的基本知识。这就是为什么我觉得 C 更加适合于编写初级服务程序或者实现简单后台任务的服务。在你对服务程序有了充分透彻的理解之后，用 C++ 编写才能游刃有余。当我离开原来的工作岗位，不得不向另一个人转移我的知识的时候，利用我用 C 所写的例子就非常容易解释 NT 服务之所以然。

　　服务是一个运行在后台并实现勿需用户交互的任务的控制台程序。Windows NT/2000/XP 操作系统提供为服务程序提供专门的支持。人们可以用服务控制面板来配置安装好的服务程序，也就是 Windows 2000/XP 控制面板|管理工具中的“服务”（或在“开始”|“运行”对话框中输入 services.msc /s——译者注）。可以将服务配置成操作系统启动时自动启动，这样你就不必每次再重启系统后还要手动启动服务。

　　本文将首先解释如何创建一个定期查询可用物理内存并将结果写入某个文本文件的服务。然后指导你完成生成，安装和实现服务的整个过程。 

　　第一步：主函数和全局定义

　　首先，包含所需的头文件。例子要调用 Win32 函数（windows.h）和磁盘文件写入（stdio.h）：

#include <windows.h>
#include <stdio.h>

　　接着，定义两个常量：

#define SLEEP_TIME 5000
#define LOGFILE "C:\\MyServices\\memstatus.txt"

　　SLEEP_TIME 指定两次连续查询可用内存之间的毫秒间隔。在第二步中编写服务工作循环的时候要使用该常量。

　　LOGFILE 定义日志文件的路径，你将会用 WriteToLog 函数将内存查询的结果输出到该文件，WriteToLog 函数定义如下：

int WriteToLog(char* str)
{
　FILE* log;
　log = fopen(LOGFILE, "a+");
　if (log == NULL)
　　return -1;
　fprintf(log, "%s\n", str);
　fclose(log);
　return 0;
}

　　声明几个全局变量，以便在程序的多个函数之间共享它们值。此外，做一个函数的前向定义：

SERVICE_STATUS ServiceStatus; 
SERVICE_STATUS_HANDLE hStatus; 

void ServiceMain(int argc, char** argv); 
void ControlHandler(DWORD request); 
int InitService();

　　现在，准备工作已经就绪，你可以开始编码了。服务程序控制台程序的一个子集。因此，开始你可以定义一个 main 函数，它是程序的入口点。对于服务程序来说，main 的代码令人惊讶地简短，因为它只创建分派表并启动控制分派机。

void main() 
{ 
　SERVICE_TABLE_ENTRY ServiceTable[2];
　ServiceTable[0].lpServiceName = "MemoryStatus";
　ServiceTable[0].lpServiceProc = (LPSERVICE_MAIN_FUNCTION)ServiceMain;

　ServiceTable[1].lpServiceName = NULL;
　ServiceTable[1].lpServiceProc = NULL;

　// 启动服务的控制分派机线程
　StartServiceCtrlDispatcher(ServiceTable); 
}

　　一个程序可能包含若干个服务。每一个服务都必须列于专门的分派表中（为此该程序定义了一个 ServiceTable 结构数组）。这个表中的每一项都要在 SERVICE_TABLE_ENTRY 结构之中。它有两个域：

　　lpServiceName: 指向表示服务名称字符串的指针；当定义了多个服务时，那么这个域必须指定； 
　　lpServiceProc: 指向服务主函数的指针（服务入口点）； 

　　分派表的最后一项必须是服务名和服务主函数域的 NULL 指针，文本例子程序中只宿主一个服务，所以服务名的定义是可选的。

　　服务控制管理器（SCM：Services Control Manager）是一个管理系统所有服务的进程。当 SCM 启动某个服务时，它等待某个进程的主线程来调用 StartServiceCtrlDispatcher 函数。将分派表传递给 StartServiceCtrlDispatcher。这将把调用进程的主线程转换为控制分派器。该分派器启动一个新线程，该线程运行分派表中每个服务的 ServiceMain 函数（本文例子中只有一个服务）分派器还监视程序中所有服务的执行情况。然后分派器将控制请求从 SCM 传给服务。

　　注意：如果 StartServiceCtrlDispatcher 函数30秒没有被调用，便会报错，为了避免这种情况，我们必须在 ServiceMain 函数中（参见本文例子）或在非主函数的单独线程中初始化服务分派表。本文所描述的服务不需要防范这样的情况。

　　分派表中所有的服务执行完之后（例如，用户通过“服务”控制面板程序停止它们），或者发生错误时。StartServiceCtrlDispatcher 调用返回。然后主进程终止。

　　第二步：ServiceMain 函数

　　Listing 1 展示了 ServiceMain 的代码。该函数是服务的入口点。它运行在一个单独的线程当中，这个线程是由控制分派器创建的。ServiceMain 应该尽可能早早为服务注册控制处理器。这要通过调用 RegisterServiceCtrlHadler 函数来实现。你要将两个参数传递给此函数：服务名和指向 ControlHandlerfunction 的指针。

　　它指示控制分派器调用 ControlHandler 函数处理 SCM 控制请求。注册完控制处理器之后，获得状态句柄（hStatus）。通过调用 SetServiceStatus 函数，用 hStatus 向 SCM 报告服务的状态。

　　Listing 1 展示了如何指定服务特征和其当前状态来初始化 ServiceStatus 结构，ServiceStatus 结构的每个域都有其用途：

　　dwServiceType：指示服务类型，创建 Win32 服务。赋值 SERVICE_WIN32； 

　　dwCurrentState：指定服务的当前状态。因为服务的初始化在这里没有完成，所以这里的状态为 SERVICE_START_PENDING； 

　　dwControlsAccepted：这个域通知 SCM 服务接受哪个域。本文例子是允许 STOP 和 SHUTDOWN 请求。处理控制请求将在第三步讨论； 

　　dwWin32ExitCode 和 dwServiceSpecificExitCode：这两个域在你终止服务并报告退出细节时很有用。初始化服务时并不退出，因此，它们的值为 0； 

　　dwCheckPoint 和 dwWaitHint：这两个域表示初始化某个服务进程时要30秒以上。本文例子服务的初始化过程很短，所以这两个域的值都为 0。 

　　调用 SetServiceStatus 函数向 SCM 报告服务的状态时。要提供 hStatus 句柄和 ServiceStatus 结构。注意 ServiceStatus 一个全局变量，所以你可以跨多个函数使用它。ServiceMain 函数中，你给结构的几个域赋值，它们在服务运行的整个过程中都保持不变，比如：dwServiceType。

　　在报告了服务状态之后，你可以调用 InitService 函数来完成初始化。这个函数只是添加一个说明性字符串到日志文件。如下面代码所示：

// 服务初始化
int InitService() 
{ 
　int result;
　result = WriteToLog("Monitoring started.");
　return(result); 
}

　　在 ServiceMain 中，检查 InitService 函数的返回值。如果初始化有错（因为有可能写日志文件失败），则将服务状态置为终止并退出 ServiceMain：

error = InitService(); 
if (error) 
{
　// 初始化失败，终止服务
　ServiceStatus.dwCurrentState = SERVICE_STOPPED; 
　ServiceStatus.dwWin32ExitCode = -1; 
　SetServiceStatus(hStatus, &ServiceStatus); 
　// 退出 ServiceMain
　return; 
}

　　如果初始化成功，则向 SCM 报告状态：

// 向 SCM 报告运行状态 
ServiceStatus.dwCurrentState = SERVICE_RUNNING; 
SetServiceStatus (hStatus, &ServiceStatus);

　　接着，启动工作循环。每五秒钟查询一个可用物理内存并将结果写入日志文件。

　　如 Listing 1 所示，循环一直到服务的状态为 SERVICE_RUNNING 或日志文件写入出错为止。状态可能在 ControlHandler 函数响应 SCM 控制请求时修改。
　　第三步：处理控制请求

　　在第二步中，你用 ServiceMain 函数注册了控制处理器函数。控制处理器与处理各种 Windows 消息的窗口回调函数非常类似。它检查 SCM 发送了什么请求并采取相应行动。

　　每次你调用 SetServiceStatus 函数的时候，必须指定服务接收 STOP 和 SHUTDOWN 请求。Listing 2 示范了如何在 ControlHandler 函数中处理它们。

　　STOP 请求是 SCM 终止服务的时候发送的。例如，如果用户在“服务”控制面板中手动终止服务。SHUTDOWN 请求是关闭机器时，由 SCM 发送给所有运行中服务的请求。两种情况的处理方式相同：

　　写日志文件，监视停止； 

　　向 SCM 报告 SERVICE_STOPPED 状态； 

　　由于 ServiceStatus 结构对于整个程序而言为全局量，ServiceStatus 中的工作循环在当前状态改变或服务终止后停止。其它的控制请求如：PAUSE 和 CONTINUE 在本文的例子没有处理。

　　控制处理器函数必须报告服务状态，即便 SCM 每次发送控制请求的时候状态保持相同。因此，不管响应什么请求，都要调用 SetServiceStatus。

 
图一 显示 MemoryStatus 服务的服务控制面板

　　第四步：安装和配置服务

　　程序编好了，将之编译成 exe 文件。本文例子创建的文件叫 MemoryStatus.exe，将它拷贝到C:\MyServices 文件夹。为了在机器上安装这个服务，需要用 SC.EXE 可执行文件，它是 Win32 Platform SDK 中附带的一个工具。（译者注：Visaul Studio .NET 2003 IDE 环境中也有这个工具，具体存放位置在：C:\Program Files\Microsoft Visual Studio .NET 2003\Common7\Tools\Bin\winnt）。使用这个实用工具可以安装和移除服务。其它控制操作将通过服务控制面板来完成。以下是用命令行安装 MemoryStatus 服务的方法：

sc create MemoryStatus binpath= c:\MyServices\MemoryStatus.exe

　　发出此创建命令。指定服务名和二进制文件的路径（注意 binpath= 和路径之间的那个空格）。安装成功后，便可以用服务控制面板来控制这个服务（参见图一）。用控制面板的工具栏启动和终止这个服务。


图二 MemoryStatus 服务的属性窗口

　　MemoryStatus 的启动类型是手动，也就是说根据需要来启动这个服务。右键单击该服务，然后选择上下文菜单中的“属性”菜单项，此时显示该服务的属性窗口。在这里可以修改启动类型以及其它设置。你还可以从“常规”标签中启动/停止服务。以下是从系统中移除服务的方法：

sc delete MemoryStatus

　　指定 “delete” 选项和服务名。此服务将被标记为删除，下次西通重启后，该服务将被完全移除。 

　　第五步：测试服务

　　从服务控制面板启动 MemoryStatus 服务。如果初始化不出错，表示启动成功。过一会儿将服务停止。检查一下 C:\MyServices 文件夹中 memstatus.txt 文件的服务输出。在我的机器上输出是这样的：

Monitoring started.
273469440
273379328
273133568
273084416
Monitoring stopped.

　　为了测试 MemoryStatus 服务在出错情况下的行为，可以将 memstatus.txt 文件设置成只读。这样一来，服务应该无法启动。

　　去掉只读属性，启动服务，在将文件设成只读。服务将停止执行，因为此时日志文件写入失败。如果你更新服务控制面板的内容，会发现服务状态是已经停止。

　　开发更大更好的服务程序

　　理解 Win32 服务的基本概念，使你能更好地用 C++ 来设计包装类。包装类隐藏了对底层 Win32 函数的调用并提供了一种舒适的通用接口。修改 MemoryStatus 程序代码，创建满足自己需要的服务！为了实现比本文例子所示范的更复杂的任务，你可以创建多线程的服务，将作业划分成几个工作者线程并从 ServiceMain 函数中监视它们的执行。
