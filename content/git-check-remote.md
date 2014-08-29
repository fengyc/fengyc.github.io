Title: git常用命令
Date: 2014-08-24 17:40
Modified: 2014-08-29 21:15
Category: blog
Tags: git
Slug: git-commands
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
    
**查看远程仓库**  
当git仓库clone到本地之后，如果忘记了具体的远程仓库地址，可通过以下的命令查看：

    git remove -v

**添加子模块**  
当项目需要引用到其它git仓库时，使用子模块

    git submodule add origin <URL>

**删除子模块**  
很奇怪，并没有`git submodule remove/delete`命令，只能通过先删除子模块目录，然后调整`.gitmodules`文件来实现

    git rm --cache <DIR>
    rm -rf <DIR>

然后修改`.gitmodules`实现

---
Yingcai FENG

