import os
import time
import random
import hashlib
import math

config  = {
    "port":8090
}

settings = {
    "debug":False,
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"template")
}


#webview config

webviw_config = {
    "appkey":"0ed128bcf133f1b7de7113d8b795aebe",
    "appSecret":"c25b2f08928d"
}


#数据库配置
dbconfig = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "pwd":"123456",
    "dbname":"webim",
    "charset":"utf8"
}
class Api():
    def __init__(self):
        self.AppKey = webviw_config['appkey']
        #self.Nonce  = self.getNonce()
        self.CurTime= time.time()
        self.CurTime = str(self.CurTime)
        self.CurTime = int(self.CurTime[0:10])
        self.appSecret = webviw_config['appSecret']
        #print(self.CurTime)
        #print(type(self.CurTime))
        self.checkSum()

    #获取随机串
    def getNonce(self):
        self.randstr = "0123456789abcdef"
        self.noncestr = ''
        noncestr = list()
        for i in range(len(self.randstr)):
             noncestr.append(self.randstr[random.randrange(1, len(self.randstr))])

        self.noncestr = ''.join(noncestr)

    #header签名
    def checkSum(self):
        self.getNonce()
        #temp = str(self.AppKey)+str(self.noncestr)+str(self.CurTime)
        #temp = [self.AppKey,self.noncestr,str(self.CurTime)]
        #tempstr = ''.join(temp)
        tempstr = "%s%s%s" % (self.appSecret, self.noncestr, self.CurTime)

        print(tempstr)
        sha = hashlib.sha1(tempstr.encode("utf-8"))
        self.checksumstr = sha.hexdigest()
