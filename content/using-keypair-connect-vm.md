Title: Openstack中使用Keypair连接到VM
Date: 2014-09-17 14:33
Category: blog
Tags: tech, openstack
Slug: using-keypair-connect-vm
Author: Yingcai FENG

通常，系统的用户名和密码都是安装过程中指定的，然后通过安全的渠道交到最终使用者的手中。这种传统的方式在进行大规模的服务器管理时就非常麻烦，因为每台机器都需要指定用户名和密码，导致需要管理的密码数量非常庞大。如果需要更改密码，还需要逐个来修改！！

在云计算中无法使用这种方式来管理虚拟机系统。镜像的开发者无法得知谁是最终的用户，最终用户无法确保开发者会不会用默认的用户名和密码来干坏事。

因此，云计算普通会采用一种在系统第一次运行时把用户名密码注入到系统的办法，Openstack与Amazon的AWS都使用这样的办法来管理，但是不是通过用户名密码，而是通过一对密钥对。密钥对是用户自己生成的，可以在多台服务器上使用，用户使用私钥连接到各个服务器。

在Openstack Dashboard上，生成一对KeyPair。公钥保存在Openstack上，私钥在生成时直接下载到用户本地。Openstack的私钥保存为一个.pem文件。

密钥对生成之后，在启动实例时，为VM指定一个此密钥对。那么在VM初始化时，当网络初始化完成之后，安装在VM系统里面的初始化工具，向`169.254.169.254`这个特殊的IP地址，向Openstack请求VM的元数据（metadata），元数据中包含了VM的密钥对中的公钥。然后，初始化工具把此公钥安装到`/root/.ssh/authorized_keys`中。

putty可以使用私钥登录到VM上，但需要做一点工作。putty使用的私钥文件格式是`.ppk`，需要把`.pem`文件转换为`.ppk`文件。使用puttygen这个图形化工具，转换的工作十分简单，见[winscp-puttygen](http://winscp.net/eng/docs/ui_puttygen)。




