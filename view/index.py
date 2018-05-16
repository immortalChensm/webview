import tornado.web
import requests
import config
from model import db

from tornado.web import RequestHandler
class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write("hello,laobiao")


class createaccidHandler(RequestHandler):
    def get(self, *args, **kwargs):
        '''

        api = config.Api()

        url = "https://api.netease.im/nimserver/user/create.action"
        #url = "http://www.app.com/app/checksum.php"
        user_account = "jackcsm"
        header = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "AppKey":api.AppKey,
            "Nonce":api.noncestr,
            "CurTime":str(api.CurTime),
            "CheckSum":api.checksumstr
        }
        data = {
            "accid":user_account,
            "name":"杰克陈"
        }

        print(header)
        result = requests.post(url,headers=header,data=data)
        #print(result.json())
        self.write(result.text)

        '''
        model = db.db()
        model.get()


        #self.render("createaccid.html")

    def post(self, *args, **kwargs):

        data = {}
        data['accid'] = self.get_body_argument("accid")
        data['name']  = self.get_body_argument("name")
        data['mobile']= self.get_body_argument("mobile")
        if not data['accid']:
            self.write(dict(status=-1,msg='accid值不可为空'))
        elif not data['name']:
            self.write(dict(status=-1,msg='昵称不可为空'))
        elif not data['mobile']:
            self.write(dict(status=-1,msg='手机号要写'))

        api = config.Api()

        url = "https://api.netease.im/nimserver/user/create.action"
        # url = "http://www.app.com/app/checksum.php"
        user_account = "jackcsm"
        header = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            "AppKey": api.AppKey,
            "Nonce": api.noncestr,
            "CurTime": str(api.CurTime),
            "CheckSum": api.checksumstr
        }
        data = {
            "accid": user_account,
            "name": "杰克陈"
        }

        print(header)
        result = requests.post(url, headers=header, data=data)
        # print(result.json())
        self.write(result.text)
