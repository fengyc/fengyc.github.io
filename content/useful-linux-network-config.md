Title: Linux网络配置
Date: 2014-09-13 20:20
Category: blog
Tags: tech, linux
Slug: useful-linux-network-config
Author: Yingcai FENG

## Ubuntu停用Network Manager

Desktop版本的Ubuntu，使用Network Manager来进行网络管理，它会导致在`/etc/network/interface`中的设置不生效。由于在进行一些网络功能的开发时，需要用到`/etc/network/interface`文件管理网络，需要停用Network Manager。

    service network-manager stop
    
并向`/etc/network/interface`中写入具体的配置

    cat>>/etc/network/interface<<EOF
    auto eth0
    iface eth0 inet static
    address 192.168.0.128
    netmask 255.255.255.0
    gateway 192.168.0.1
    dns-nameservers 192.168.0.1
    EOF

然后，使用
    
    ifdown --exclude=lo -a && ifup --exclude=lo -a
    
把网络重启。

## 为网卡增加配置多个IP

为了区分各个网络，需要使用多个网段。而在只有一个网卡的时候，就需要为这个网卡配置多个IP。实现的手段有两种：

1. 配置虚拟网络接口  
在`/etc/network/interface`中，增加类似`eth0:1`的接口，如：

        auto eth0:1
        iface eth0:1 inet static
        address a.b.c.d
        netmask a.b.c.d
        
2. 通过`ip addr add`命令  
`ip addr add`命令在网卡上增加一个地址，如：

        ip addr add 192.168.0.128/24 dev eth0

## Linux中DNS配置

一般，应该通过`/etc/network/interface`文件设置`dns-nameservers`来配置，`interface`文件中的配置，会被解析并自动更新到`/etc/resolv.conf`文件中。

如果需要临时修改DNS配置，也可以直接把DNS写入到`resolv.conf`中，如：

    echo 'nameserver 8.8.4.4' >> /etc/resolv.conf
    


