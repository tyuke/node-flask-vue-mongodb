# kankan
首先安装好python 这里的版本是python 3.6.5 在命令行输入python就可以查看python是否安装好


Flask的安装我是在http://docs.jinkan.org/docs/flask/installation.html#installation这看到的
现在使用的是win10的系统，其他系统的教程可以在该网址看到
下载好python后会自动安装好pip
现在只需要按住键盘win+R输入cmd


输入pip可以看到是否已经安装好


然后输入pip install virtualenv
不要问我这是什么，自己查
按照教程依次输入
mkdir myproject
cd myproject
virtualenv venv
venv\scripts\activate
pip install Flask
这样就安装好了
pip install flask_cors
安装这个是因为存在跨域问题

flask和mongodb数据库
https://flask-pymongo.readthedocs.io/en/latest/

pip install flask-pymongo
mongodb要自己下载安装好

/******* 这一步留在这，可以不用||
MongoDB数据库绑定服务ip地址设置（PS：如果不进行下述设置，默认ip为本机127.0.0.1地址）：
打开CMD，进入MongoDB安装的bin文件夹下，例如我的安装目录为：C:\Program Files\MongoDB\Server\3.2\bin
然后在CMD中输入mongod.exe --bind_ip yourIPadress
********/

flask和vue

https://www.cnblogs.com/yingqml/p/7205147.html?utm_source=debugrun&utm_medium=referral

先安装node
npm install --global vue-cli   安装vue脚手架

