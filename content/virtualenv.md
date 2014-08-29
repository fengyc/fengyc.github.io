Title: 使用virtualenv建立python开发环境
Date: 2014-08-28 20:20
Category: blog
Tags: tech, python
Slug: virtualenv
Author: Yingcai FENG

在python开发中，经常性需要安装一系列的依赖库。如果使用root用户安装到系统的python环境中，容易导致python目录越来越庞大。而后面更加麻烦的是，当开发完成之后，不知道该删除哪些依赖库了，因此也不敢删了。现在的Linux发行版中，各种组件对python环境的依赖很强，不小心删错了，绝对会让人追悔莫及！

为此，我们绝对需要把我们的开发环境与系统的python环境隔离，让依赖库只在开发目录下存在，不会影响到系统python环境。使用virtualenv工具，可以轻易地帮助我们达成目的。

<!-- PELICAN_END_SUMMARY -->

virtualenv工具建立一个项目专用的python环境，在该环境中，有独立的`bin include lib local`等目录，里面会有一个单独的python环境。

如果要在建立一个virtualenv环境(目录为.env)，使用命令：

    virtualenv .env

然后，使用命令：

    tree -d .env

可以查看到整个目录的树结构

    ├── bin
    ├── include
    │   └── python2.7 -> /usr/include/python2.7
    ├── lib
    │   └── python2.7
    │       ├── config -> /usr/lib/python2.7/config
    │       ├── distutils
    │       ├── encodings -> /usr/lib/python2.7/encodings
    │       ├── lib-dynload -> /usr/lib/python2.7/lib-dynload
    │       └── site-packages
    │           ├── _markerlib
    │           ├── pip
    │           │   ├── backwardcompat
    │           │   ├── commands
    │           │   ├── vcs
    │           │   └── _vendor
    │           │       ├── colorama
    │           │       ├── distlib
    │           │       │   └── _backport
    │           │       ├── html5lib
    │           │       │   ├── filters
    │           │       │   ├── serializer
    │           │       │   ├── treeadapters
    │           │       │   ├── treebuilders
    │           │       │   ├── treewalkers
    │           │       │   └── trie
    │           │       ├── _markerlib
    │           │       └── requests
    │           │           └── packages
    │           │               ├── chardet
    │           │               └── urllib3
    │           │                   ├── contrib
    │           │                   ├── packages
    │           │                   │   └── ssl_match_hostname
    │           │                   └── util
    │           ├── pip-1.5.6.dist-info
    │           ├── setuptools
    │           │   ├── command
    │           │   └── tests
    │           └── setuptools-3.6.dist-info
    └── local
        ├── bin -> /home/fengyingcai/hello/bin
        ├── include -> /home/fengyingcai/hello/include
        └── lib -> /home/fengyingcai/hello/lib

然后，使用命令：

    source .env/bin/activate

就可以激活这个virtualenv环境，这时，会看到在命令提示前，会有

    (.env)

的提示

如果要退出，使用命令:

    deactivate

Yingcai FENG at SYSU
