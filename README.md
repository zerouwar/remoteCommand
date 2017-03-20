# remoteCommand
Simple Remote execution of command with Python（用python实现的简单远程执行命令）
一个客户端，一个服务端，服务端开启一个端口，接受客户端的TCP请求，根据配置文件里的可执行命令列表来决定是否执行命令，并把执行的结果返回给客户端。

# exe使用方法
## 服务端
在server文件夹里面，dist文件夹存放的是可运行exe。修改server.json文件的配置
port：服务端监听端口
permit_commands：允许执行的命令列表

## 客户端
在client文件夹下，dist文件夹存放的是可运行exe。修改client.properties文件
ip ： 服务端的ip
port = 服务端开启的端口
wait_time = 1 每次发送完命令等待的超时时间（秒）

# PS 
可以搭配ngrok，来让外网可以访问本地电脑，在团队合作中，有时前端需要经常修改页面来测试，用这个脚本可以不需要叫后台手动更新。不过脚本本身只是远程执行命令而已，所以前提是命令是正确的。
