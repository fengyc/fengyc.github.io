Title: 利用pelican在github上搭建博客的办法
Date: 2014-08-22 20:20
Modified: 2014-08-26 14:12
Category: blog
Tags: github, python
Slug: pelican-github-blog
Author: Yingcai FENG

发现能在github上搭建博客之后，经过一翻寻找之后，学会了使用pelican建立起整个博客系统。

pelican使用python语言编写，支持markdown(.md)/reStructuredText(.rst)语法。对程序员而言，用它来编写博客内容是最好不过了，而且放在github上，也给人一种不明觉历的感觉:-)

这篇文章记录在ubuntu 14.04下，使用pelican和github搭建博客的过程。

<!-- PELICAN_END_SUMMARY -->

## 安装过程

**在github上建立博客项目**

在github上建立一个账号，并建立一个公共项目，项目名为"账号.github.io"，不需要建立README等，保持项目为空白，如：
    https://github.com/abc/fengyc.github.io

**安装准备环境**

    apt-get install -y --force-yes git python-pip python-dev virtualenv

**把项目clone到本地**

    mkdir blog
    cd blog
    git init
    git remote add origin https://github.com/fengyc.github.io.git
    git fetch

**建立virtualenv环境**

    mkdir .env
    virtualenv .env

**激活virtualenv环境**

    source .env/bin/activate 

**安装pelican和Markdown**  
在激活了virtualenv的前提下安装，避免污染python环境

    pip install pelican
    pip install Markdown

**建立源分支**

    git checkout -b source
    pelican-quickstart

请根据自己的实际环境选择向导中的变量

**编写第一个页面**
用markdown语法编写一个页面，如([pelican-getting_started])：

    Title: My super title
    Date: 2010-12-03 10:20
    Category: Python
    Tags: pelican, publishing
    Slug: my-super-post
    Author: Alexis Metaireau
    Summary: Short version for index and feeds

    This is the content of my super blog post.

**编译并发布**

    make html
    pip install ghp-import
    git branch gp-pages
    ghp-import output
    git checkout master
    git merge gh-pages
    git push --all

## pelican主题
pelican提供了很多的主题供用户使用，首先把主题下载到本地：

    git clone https://github.com/getpelican/pelican-themes.git

然后，进入到主题目录中，安装主题

    cd pelican-themes
    pelican-themes -i gum

## 增加DISQUS作为讨论组
先到DISQUS([disqus])申请一个账号，并建立一个讨论组。记录下讨论组的shortname，然后记录到配置文件中：

    DISQUS_SITENAME=zenmass

## 使用google analytics([google-analytics])
申请一个google analytics账号，建立一个项目，然后把跟踪ID填入到配置文件中：

    GOOGLE_ANALYTICS=

[pelican-getting_started]: http://docs.getpelican.com/en/3.3.0/getting_started.html "pelican参考页面"
[disqus]: http://disqus.com/ "DISQUS申请"
[google-analytics]: http://www.google.cn/intl/zh-CN/analytics/ "Google Analytics申请"

