Title: git常用命令
Slug: useful-git-commands
Date: 2014-08-24 17:40
Modified: 2014-09-14 17:40
Category: blog
Tags: git
Author: Yingcai FENG

本文章记录了git的日常使用中的常用命令。
<!-- PELICAN_END_SUMMARY -->

**下载远程仓库**

    git clone <URL>
    
**更新**  
    
    git pull
    
**推送**

    git push

**在本地工作目录指定远程仓库**

    git remote add <URL>
    
**取消本地修改**
    
    git checkout <FILE>    
    
**查看远程仓库**  
当git仓库clone到本地之后，如果忘记了具体的远程仓库地址，可通过以下的命令查看：

    git remove -v

**添加子模块**  
当项目需要引用到其它git仓库时，使用子模块

    git submodule add <URL>

**子模块初始化**
当一个git仓库被clone下来之后，子模块并不会被自动下载下来，使用下面的命令初始化各个子模块：

    git submodule update --init --recursive
    
某些时候，当子模块的目录存在的时候，会导致初始化出错，这时候，直接删除子模块的目录：

    rm -rf <子模块目录>

**删除子模块**  
很奇怪，并没有`git submodule remove/delete`命令，只能通过先删除子模块目录，然后调整`.gitmodules`文件来实现

    git rm --cache <DIR>
    rm -rf <DIR>

然后修改`.gitmodules`实现

---
Yingcai FENG

