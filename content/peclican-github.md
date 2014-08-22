Title: 利用pelican在github上搭建博客的办法
Date: 2014-08-22 20:20
Category: 博客
Tags: github
Slug: pelican-github
Author: Yingcai FENG
Summary: pelican github

# 简介
这是在ubuntu 14.04下，使用pelican和github搭建博客的过程
# github博客项目
在github上建立一个账号，并建立一个公共项目，项目名为"账号.github.io"，不需要建立README等，保持项目为空白，如：
<pre>
https://github.com/abc/abc.github.io
</pre>

# 安装
## 安装准备环境
\# apt-get install -y --force-yes python-pip python-dev virtualenv
## 把项目clone到本地
git clone https://github.com/abc/abc.github.io
## 建立virtualenv环境
<pre>
cd abc.github.io
mkdir .env
virtualenv .env
source .env/bin/activate
</pre>
## 安装pelican和Markdown
<pre>
pip install pelican
pip install Markdown
</pre>
## 建立源分支
<pre>
git checkout -b source
pelican-quickstart
</pre>
根据自己的实际环境选择向导中的变量
## 编写第一个页面
vi content/hello.md
用markdown语法编写一个页面，如(<a href="http://docs.getpelican.com/en/3.3.0/getting_started.html#writing-content-using-pelican">http://docs.getpelican.com/en/3.3.0/getting_started.html</a>)：
<pre>
Title: My super title
Date: 2010-12-03 10:20
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Alexis Metaireau
Summary: Short version for index and feeds

This is the content of my super blog post.
</pre>
## 编译并发布
<pre>
make html
pip install ghp-import
git branch gp-pages
ghp-import output
git checkout master
git merge gh-pages
git push --all
</pre>

