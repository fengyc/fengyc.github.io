Title: 在Ubuntu中安装Oracle JDK
Date: 2014-09-18 13:02
Category: blog
Tags: tech, linux, java
Slug: install-oracle-jdk-in-ubuntu
Author: Yingcai FENG

尽管OpenJDK发展到现在已经能兼容绝大多数的标准Java应用场景，但是在某些微小的方面，仍然存在一点小问题。在Ubuntu中安装的Eclipse，使用OpenJDK时，使用内置的浏览器会有点问题，因此，我需要转换到Oracle的JDK。

可以手工安装OracleJDK，比较烦琐。可以通过已打包好的PPA，进行安装：

    add-apt-repository ppa:webupd8team/java
    apt-get update
    apt-get install oracle-java7-installer

webupd8的官方网站为[webupd8.org](http://www.webupd8.org/)。他们提供了一系列的软件包，见[packages](http://www.webupd8.org/p/ubuntu-ppas-by-webupd8.html)。
