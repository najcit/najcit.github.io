---
title: Git 如何合并，删除修改等操作 commit
published: true
categories: [program]
tags: [git]
---

使用 git 保存代码时，经常会出现解决一个问题多次提交 commit的现象，或者需要要删除某一次 commit，或者修改 commit 注释等操作。 为了使代码简洁，所以在工作不忙的时候，对 commit 做整理，以美化 commit 的日志，也方便别人使用。  

## 常见的四个需求

1. git 合并 commit
2. git 删除 commit
3. git 修改 commit 注释
4. git 修改 commit 文件


## 操作步骤
1. git log 查看 commit 日志
2. git rebase -i HEAD~n 对日志进行压缩，n是距离当前commit的第几个commit的计数，进入到 vim[]()
   ![](/images/rebase-commit.png)  
   下面是对图片的中文说明，每一个 commit id 前面的操作表示指令类型，git 为我们提供了以下几个命令：  
   * pick：保留该 commit（缩写： p)   
   * reword：保留该 commit ，但我们要修改该 commit 的注释（缩写： r)   
   * edit：保留该 commit ，但我要停下来修改该提交（不仅仅修改注释）（缩写： e)   
   * squash：将该 commit 和前一个 commit 合并（缩写： s)   
   * fixup：将该 commit 和前一个 commit 合并， 但我们不保留该 commit 的注释信息（缩写： f)   
   * exec：执行 shell 命令（缩写： x)   
3. 按i键进入到 vim 编辑状态， 按照自己的需要修改，按x键保存退出，或则q键取消退出  
   合并使用 s 或者 f  
   删除使用 d  
   修改注释使用 r  
   修改文件使用 e  
4. 同步远程仓库，使用 git push -f 强制覆盖远程的仓库的 commit 日志