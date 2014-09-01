Title: Windows桌面共享2
Date: 2014-09-01 23:20
Category: blog
Tags: tech, windows, C#
Slug: windowns-desktop-sharing-2
Author: Yingcai FENG

经过一天的尝试，使用Windows Desktop Sharing API写了一点原型代码，并运行起来查看效果。

我是使用C#来调用这个API的（本身是COM，可以由Visual Studio自动添加包装）。原型系统的代码分为服务器端（Sharer）和客户端（Attendee）,只是简单地把整个桌面全部共享出来。下面，是一些编程中的核心的内容。

## Sharer端

在Sharer端，首先要引入API的COM，名称为`rdpcomapi 1.0 Type Library`，文件路径为`C:\Windows\System32\rdpencom.dll`。在引入的同时，Visual Studio会自动把这个COM进行包装，从而在项目的引用中可看到`RDPCOMAPILib`这个库，而查看其属性，会看到路径为项目某个目录下的`Interop.RDPCOMAPILib.dll`。在引入之后，可通过Visual Studio的对象查看器，查看这个dll里面包含的内容。

Sharer端，以`RDPSession`接口为突破口，其它的操作都围绕这个接口进行。首先，创建接口的实例（在测试中，Sharer端只用了一个实例）：

    private RDPSession rdpSession = new RDPSessionClass();

然后，就需要在这个实例正式开始连接之前，做初始化的准备，比如属性设置：

    rdpSession.Properties["DrvConAttach"] = false;
    ...
    
上面是在1:M的模式下，微软建议使用mirror driver静态加载模式，具体请查看MSDN的相关内容。

Desktop Sharing支持应用程序和窗口过滤，只需要在RDPSession中进行简单的设置，即可以把不需要的共享的应用程序和窗口屏蔽。根据MSDN上的说法，这个过程分成两种，如果应用程序被共享，那么它的窗口不管是什么共享状态，都会被共享；如果应用程序被禁止共享，那么则要根据窗口的共享状态来决定是否共享。

    rdpSession.ApplicationFilter.Enabled = true;
    RDPSRAPIApplicationList appList = rdpSession.ApplicationFilter.Applications;
    RDPSRAPIWindowList windownList = rdpSession.ApplicationFilter.Windows;
    ……
    
以上内容进行应用程序和窗口过滤。

还可以对一系列的事件进行监听，对Attendee连接、应用状态变化、窗口状态变化等等，进行事件处理，具体的通过`RDPSession.On*`来处理。

完成初始化之后，通过

    rdpSession.Open()
    
正式开启共享会话。在Win7上，这时会提示`正在运行的程序与windows 的某些可视元素不兼容`，我怀疑这是mirror driver的问题，我调试时查看了`rdpSession.colordepth`，发现只有24位。

此后，就需要通过创建`Invitation`，建立会话邀请：

    RDPSRAPIInvitation invitation = rdpSession.Invitations.CreateInvitation("123", "123", "123", 1);
    string connString = invitation.ConnectionString;

ConnectionString是一个简单xml格式的字符串，包含了Sharer主机多个IP信息，还有一个类似于一次性邀请码之类的字符串。ConnectionString最好是能自动传递，避免人工输入时出错。Attendee端在加入到会话时，需要到这个字符串。

## Attendee端

Attendee端的工作相对简单一点。

首先，Attendee端要引入AxRDPViewer控件。在Visual Studio的`工具箱`窗口，右键->选择项，找到AxRDPViewer控件，加入到`工具箱`中。

直接把AxRDPViewer控件拉到一个窗口，设置名字为rdpViewer。

按照Sharer的设置，rdpViewer也需要设置相关的properties，如：

    rdpViewer.Properties["PortId"] = 4580;
    rdpViewer.Properties["PortProtocol"] = 2;
    ……
    
如果需要监听会话事件，与Sharer端一样，设置相应的`rdpView.On*`处理事件。

## 性能和评估

Win7下的RDP，有专门的mirror driver驱动，性能比普通的截图方式要好很多。在使用普通的办公软件的话，如果没有大规模的刷新，大概占用20-40KB/S左右。但是遇到像播放视频这种，是需要到很大的带宽的。试过一个高清的视频，分辨率为1024x576，播放时占用了5-6MB/S左右，这也是没有办法的事:-(

目前，我并没有找到Desktop Sharing的组播或广播方式。如果只能以点对点进行桌面共享，是无法适应大规模的演示、上课等需求的。国内这方面的公开资料并不多，可能都是各家厂商的核心技术所在。看到一些帖子，说是通过GDI勾子或者是mirror driver的方式实现，原理上感觉还算是靠谱。

利用这个功能，还是可以做一个简单的小组共享软件，在人数不多的情况下，效果还可以。我准备有空的时间弄一个玩玩。

真正要实现大规模的桌面共享，看来还需要看看mirror driver相关的内容，需要自己手工截图进行，进行UDP广播。带有Desktop Sharing的Windows，都会有RDP Encoder Mirror Driver，可以试着用一用，具体看[Using "RDP Encoder Mirror Driver" to Capture Screen]。

[Using "RDP Encoder Mirror Driver" to Capture Screen]: http://www.codeproject.com/Articles/716128/Using-RDP-Encoder-Mirror-Driver-to-Capture-Screen "使用RDP的Mirror Driver"

---
Yingcai FENG at SYSU
