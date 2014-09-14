Title: 使用devstack部署openstack环境
Slug: use-devstack-deploy-openstack
Date: 2014-09-14 21:55
Category: blog
Tags: tech, openstack
Author: Yingcai FENG

devstack是一套openstack的部署脚本，对openstack初学者而言，是最好不过的openstack部署脚本了。

devstack的官方网站为`devstack.org`。官方网站上已经对devstack的用途有介绍，这里介绍一下我在测试中使用到的一些注意问题。

devstack整套脚本放在github中，使用下面的命令clone到本地：

    git clone https://github.com/openstack-dev/devstack.git

下载完成后，需要进行一个简单的配置的，在官网中给出了一个最小的配置[devstack-mini-config]。

然后，进入到目录中，以**普通用户**的权限执行stack.sh，进行openstack的安装。

    cd devstack && ./stack.sh

[devstack-mini-config]: http://devstack.org/configuration.html "Devstack minimal configuration"