Title: 在Ubuntu中安装WPS
Date: 2014-09-20 15:20
Category: blog
Tags: blog 
Slug: install-wps-in-ubuntu
Author: Yingcai FENG

WPS的官网上已经提供了.deb安装包，但是只有32位的版本，目前还没有64位的版本。现在的电脑配置基本上都超4G内存了，使用64位的系统才能更好地利用更多内存，现在的Linux大部分都使用64位了。尽管WPS还没有推出64位的版本，但能在Linux上发行，已经是很大的进步。

64位的系统要安装32位的软件，还需要动动脑筋。原来Ubuntu是提供一个`ia32-libs`安装包，把32位系统所需要的软件包都一起装了。在14.04上，并没有在官方的源中找到这个包。

然而，尝试了一下之后，发现还是能把WPS装上。过程如下：

首先，到[wps](http://community.wps.cn/download/)网站上下载wps，我下载了`wps-office_9.1.0.4751~a15_i386.deb`。并下载字体包 `wps-office-fonts_1.0_all.deb`。

现在，开启32位支持：

    dpkg --add-architecture i386
    apt-get update
    
然后，直接尝试安装WPS：

    dpkg -i wps-office_9.1.0.4751~a15_i386.deb
    
安装过程会报错，但是WPS还是安装了，然后用

    apt-get -f install
    
会把WPS依赖的32位的软件包安装上去。那么，继续安装字体包：

    dpkg -i wps-office-fonts_1.0_all.deb 
    
完成后，就可以使用WPS了。