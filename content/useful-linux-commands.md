Title: 常用Linux命令
Slug: useful-linux-commands
Date: 2014-09-13 13:57
Modified: 2014-09-13 13:57
Category: blog
Tags: tech, linux, shell
Author: Yingcai FENG

本文整理一些常用的Linux命令，以及shell编程中使用到常用语句。

## shell中判断

使用`if`进行判断

    if [ <condition> ]; then
        # Do something
    fi

包含多个分支，使用`if-elif`

    if [ <condition> ]; then
        # Do something
    elif [ <condition> ]; then
        # Do somethin
    fi
    
## watch查看命令多次执行的结果

watch能多次执行命令，并把命令的结果显示出来，支持每隔n秒执行一次命令，并把执行结果的差异显示。

    watch -n <seconds> -d <commands>

## tar压缩打包
常用的tar参数包括：

+ `-c` 创建包
+ `-x` 解包
+ `-v` 显示处理的文件
+ `-z` gzip格式
+ `-j` bzip2格式
+ `-f` 文档名，后面应立即使用包文档路径参数

示例：

    tar -xvf a.tar.gz
    tar -zcvf a.tar.gz  a/
    tar -jcvf a.tar.bz2 a/
    
## scp远程拷贝
为了把远程服务器上的内容拷贝下来，首先需要在远程服务器上安装ssh服务，然后在本地使用`scp`命令通过ssh把内容拷贝下来。`scp`命令与`cp`的操作类似：

    scp -r <username@server:/server_path> <local_path>
    
其中`-r`表示recursive，用于拷贝目录。需要把本地内容拷贝到服务器，则把两个路径调换位置：

    scp -r <localpath> <username@server:/server_path>
    
