Title: 常用Linux命令
Date: 2014-09-13 13:57
Modified: 2014-09-13 13:57
Category: blog
Tags: tech, linux, shell
Author: Yingcai FENG

本文整理一些常用的Linux命令，以及shell编程中使用到常用语句。

** shell中判断 **

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
    
** watch查看命令多次执行的结果 **

watch能多次执行命令，并把命令的结果显示出来，支持每隔n秒执行一次命令，并把执行结果的差异显示。

    watch -n <seconds> -d <commands>
        