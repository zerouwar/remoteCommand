import os
import socket

#静态变量配置
import time

IP = '127.0.0.1'
PORT = 80
WAIT_TIME = 1;
CHARSET = "utf-8"
ERROR_INFO = "貌似对方没响应，再重试一次"

#接收服务端的信息
def receive(sk):
    result = ""
    while True:
        time.sleep(WAIT_TIME)
        try:
            buf = sk.recv(1024)
        except:
            break
        result+=str(buf,CHARSET)
    if(len(result)!=0):
        return (True,result)
    else:
        return (False,"")

class Properties(object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getDict(self,strName,dictName,value):

        if(strName.find('.')>0):
            k = strName.split('.')[0]
            dictName.setdefault(k,{})
            return self.__getDict(strName[len(k)+1:],dictName[k],value)
        else:
            dictName[strName] = value
            return
    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'Ur')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#")!=-1:
                    line=line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1]= line[len(strs[0])+1:]
                    self.__getDict(strs[0].strip(),self.properties,strs[1].strip())
        except Exception as e:
            raise e
        else:
            pro_file.close()
        return self.properties
#读取配置文件
def readConfig():
    try:
        config = Properties("config.properties").getProperties()
    except:
        print("找不到配置文件config.properties，2秒后退出")
        time.sleep(2)
        exit()
    global IP,PORT,WAIT_TIME
    IP = config["ip"]
    PORT = int(config["port"])
    WAIT_TIME = int(config["wait_time"])
readConfig()
#开始发送命令
while(True):
    try:
        sk = socket.socket()
        address = (IP,PORT)
        sk.connect(address)
    except:
        print(IP,":",PORT," 无响应！")
        time.sleep(2)
        exit()
    command = input("insert your request:")
    if(command=="exit"):
        exit()
    sk.sendall(bytes(command,CHARSET))
    sk.setblocking(0)

    (is_connect,result) = receive(sk)

    if(is_connect == True):
        print(result)
    else:
        print(ERROR_INFO)


