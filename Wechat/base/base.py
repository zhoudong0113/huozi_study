import json

import requests
from requests import session


class Base:
    def __init__(self):
        """
        实例化session
        获取token并存入session
        """
        self.session = requests.Session()
        self.token = self.get_token()
        self.session.params = {"access_token": self.get_token()}

    def session_close(self):
        self.session.close()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            'corpid': "wwb72e8db07ce2a932",
            'corpsecret': "bmr3ZhFknF1H0VXtYmQwF8nNt-xTfQSI5UrdNDpRp4U"
        }
        r = self.session.get(url,params=params)
        print(r)
        token = r.json()["access_token"]
        return token

    def send(self,url,method,*args,**kwargs):
        r = self.session.request(url=url, method=method,*args,**kwargs)
        return r

