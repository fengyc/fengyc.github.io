Title: 在Ubuntu中安装RabbitVCS
Date: 2014-09-18 15:56
Category: blog
Tags: tech, linux
Slug: install-rabbitvcs-in-ubuntu
Author: Yingcai FENG

RabbitVCS是Linux下的图形化版本管理软件，支持SVN/GIT，官网是[rabbitvcs.org](http://www.rabbitvcs.org/)，PPA网站是[rabbitvcs-ppa](https://launchpad.net/~rabbitvcs/+archive/ubuntu/ppa)。

RabbitVCS的操作很像Windows下的小乌龟:-)，支持把操作集成到图形界面的右键菜单中，与TortoiseSVN是同样的，非常方便。

安装的方法在PPA站点上有介绍，根据自己的系统的版本，把源加入到系统中，在14.04中，示例为：

    cat > /etc/apt/sources.list.d/rabbitvcs.list <<EOF
    deb http://ppa.launchpad.net/rabbitvcs/ppa/ubuntu trusty main
    EOF
