Title: Windows桌面共享
Date: 2014-08-29 21:00
Category: blog
Tags: windows
Slug: windows-desktop-sharing
Author: Yingcai FENG

最近在做一个windows桌面共享的项目，找了一系列的方法：

**视频广播方式**

视频广播方式可能是最具备跨平台特性的方式。在本地程序录制桌面的视频，或者基于硬件直接录制然后播放，然后实时发送到各个客户端。这种思想有很多的实现方式，而且整个结构很容易理解和扩展。

录制的方式，总结了一下，找到下面的录制方式：

1. windows GDI 截图
2. directShow 直接录制
3. mirror driver 或 mini port 驱动录制
4. ffmpeg 录制 

为了降低分享桌面的主机的负载，可以引入特定的视频广播服务器，由服务器进行视频转发。具体的协议可通过udp/rtsp等实现。

这种方式具备与平台无关的特性，视频录制方式可随时扩展，而通过标准的接口把数据提交到转发服务器。但实现起来，需要做的工作也很多，需要理解基本的视频处理知识，实现一个良好的系统框架。

**Windows Desktop Sharing**

如果是只针对windows平台，通过windows desktop sharing，工作量可以减少很多。

windows desktop sharing是基于rdp的一套API，提供非常简单快捷实现桌面共享的功能。根据在[MSDN]上的介绍，这个功能是微软从Vista开始提供的功能，而且在[BLOG]中提到，这个功能是微软的 "Windows Meeting Space" 和 "Remote Assistance" 的基础。

目前粗略看了一下MSDN上的介绍，它的核心对象就是RDPSession和RDPViewer两个，其它的操作在这两个对象的基础上进行。

除了支持桌面共享，这个API还支持很多有意思的功能，比较连接反转（Reverse Connect）、应用程序窗口共享、虚拟通道等等。

目前准备使用Windows Desktop Sharing来实现一个系统原型，评测一下效果。

[MSDN]: http://msdn.microsoft.com/en-us/library/bb968809.aspx "MSDN Windows Desktop Sharing"
[BLOG]: http://blogs.msdn.com/b/rds/archive/2007/03/08/windows-desktop-sharing-api.aspx "Remote Desktop Service Blog"
---
Yingcai FENG
