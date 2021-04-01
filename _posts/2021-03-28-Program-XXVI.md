---
title: 每天学一个 Linux 命令：sed
published: true
categories: [program]
---

# 简介
sed 是一种流编辑器，也是文本处理中非常好的工具，配合正则使用更强大处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”，接着用 sed 命令处理缓冲区的内容，完成后输出到屏幕，接着处理下一行。文件内容并没有改变，除非使用 -i 选项。sed 主要用来编辑一个或多个文件，简化对文件的反复操作或者用来编写转换程序等。

# 用法
```bash
sed [options] [command] file(s)
sed [options] -f [script-file] file(s)
```

# 说明
```
  -n, --quiet, --silent
                 suppress automatic printing of pattern space
      --debug
                 annotate program execution
  -e script, --expression=script
                 add the script to the commands to be executed
  -f script-file, --file=script-file
                 add the contents of script-file to the commands to be executed
  --follow-symlinks
                 follow symlinks when processing in place
  -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if SUFFIX supplied)
  -l N, --line-length=N
                 specify the desired line-wrap length for the `l' command
  --posix
                 disable all GNU extensions.
  -E, -r, --regexp-extended
                 use extended regular expressions in the script
                 (for portability use POSIX -E).
  -s, --separate
                 consider files as separate rather than as a single,
                 continuous long stream.
      --sandbox
                 operate in sandbox mode (disable e/r/w commands).
  -u, --unbuffered
                 load minimal amounts of data from the input files and flush
                 the output buffers more often
  -z, --null-data
                 separate lines by NUL characters
      --help     display this help and exit
      --version  output version information and exit
```

# 命令
```
  a #在当前行下面插入文本
  i #在当前行上面插入文本
  c #把选定的行改为新的文本
  d #删除，删除选择的行
  D #删除模板块的第一行 
  s #替换指定字符
  h #拷贝模板块的内容到内存中的缓冲区
  H #追加模板块的内容到内存中的缓冲区
  g #获得内存缓冲区的内容，并替代当前模板块中的文本 
  G #获得内存缓冲区的内容，并追加到当前模板块文本的后面 
  l #列表不能打印字符的清单
  n #读取下一个输入行，用下一个命令处理新的行而不是用第一个命令
  N #追加下一个输入行到模板块后面并在二者间嵌入一个新行，改变当前行号码
  p #打印匹配的行
  P #(大写)打印模板的第一行
  q #退出Sed
  b #lable 分支到脚本中带有标记的地方，如果分支不存在则分支到脚本的末尾
  r #file 从file中读行
  t #label if分支，从最后一行开始，条件一旦满足或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾
  T #label 错误分支，从最后一行开始，一旦发生错误或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾
  w #file 写并追加模板块到file末尾**
  W #file 写并追加模板块的第一行到file末尾**
  ! #表示后面的命令对所有没有被选定的行发生作用** 
  = #打印当前行号码**
  # #把注释扩展到下一个换行符以前**
```