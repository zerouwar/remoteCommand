import json
import os
import socket
from email import charset

#静态变量配置
import time

PORT = 80
NOT_PERMITTED_COMMAND = "不允许执行该命令!"
DATA_SIZE = 1024
COMMANDS = []

#加载配置文件
def loadConfig():
    try:
        f = open("server.json","Ur",encoding="utf-8")
    except:
        print("找不到配置文件server.json，2秒后退出")
        time.sleep(2)
        exit()
    config = json.load(f)
    global COMMANDS,PORT
    COMMANDS = config["permit_commands"]
    PORT = int(config["port"])
#是否是可允许的命令
def isPermitted(client_command):
    global COMMANDS
    for comm in COMMANDS:
        if(comm==client_command):
            return True
    return False

#读取配置文件
loadConfig()
#开启监听
sk = socket.socket()
ip_port = ("127.0.0.1",PORT)
sk.bind(ip_port)
sk.listen(1)
print("开始监听",PORT)
while True:
    conn,address = sk.accept()

    client_data = str(conn.recv(DATA_SIZE),"utf-8")

    print(time.strftime('%H-%M-%S',time.localtime(time.time()))+",收到命令:"+client_data)

    result = ""
    if(isPermitted(client_data)):
        output = os.popen(client_data)
        result = output.read()
    else:
        result = NOT_PERMITTED_COMMAND

    conn.sendall(bytes(result,"utf-8"))