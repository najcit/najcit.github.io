---
title: Windows进程的创建与销毁
published: true
categories: [program]
---

Windows进程的创建与销毁
内容及要求：
① 掌握Windows进程的创建和销毁API的调用方法；编程代码，在程序中创建和销毁一个Word进程；
② 能够挂起和激活被创建进程的主线程；
③ 通过Windows进程管理器查看系统进程列表的变化。
实验指导：
①创建进程的API
BOOL CreateProcess(
  LPCTSTR lpApplicationName,
  LPTSTR lpCommandLine,
  LPSECURITY_ATTRIBUTES lpProcessAttributes,
  LPSECURITY_ATTRIBUTES lpThreadAttributes,
  BOOL bInheritHandles,
  DWORD dwCreationFlags,
  LPVOID lpEnvironment,
  LPCTSTR lpCurrentDirectory,
  LPSTARTUPINFO lpStartupInfo,
  LPPROCESS_INFORMATION lpProcessInformation
);
例程：
void main( VOID ){
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );
    // Start the child process. 
    if( !CreateProcess( NULL, // No module name (use command line). 
        "MyChildProcess", // Command line. 
        NULL,             // Process handle not inheritable. 
        NULL,             // Thread handle not inheritable. 
        FALSE,            // Set handle inheritance to FALSE. 
        0,                // No creation flags. 
        NULL,             // Use parent's environment block. 
        NULL,             // Use parent's starting directory. 
        &si,              // Pointer to STARTUPINFO structure.
        &pi )             // Pointer to PROCESS_INFORMATION structure.
    ) {
        ErrorExit( "CreateProcess failed." );
    }
    // Wait until child process exits.
    WaitForSingleObject( pi.hProcess, INFINITE );
    // Close process and thread handles. 
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
}
② 销毁进程API
BOOL TerminateProcess(
  HANDLE hProcess,
  UINT uExitCode
);
③ 挂起进程的主线程API
DWORD SuspendThread(
  HANDLE hThread
);
④激活进程的主线程API
DWORD ResumeThread(
  HANDLE hThread
);