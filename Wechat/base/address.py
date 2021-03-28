from Wechat.base.base import Base


class Address(Base):

    def create_member(self,data):
        #创建成员方法
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = self.send(url,"post",json=data)
        return r.json()

    def get_member(self,data):
        #读取成员
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.send(url,"get",json=data)
        return r.json()

    def update_member(self,data):
        #更新成员
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        r = self.send(url,"post",json=data)
        return r.json()

    def delete_member(self,data):
        #删除成员
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = self.send(url,"get",json=data)
        return r.json()