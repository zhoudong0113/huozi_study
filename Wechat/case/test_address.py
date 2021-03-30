from Wechat.base.address import Address


class TestAddress:
    data = {
        "userid": "zhd012",
        "name": "zhd012",
        "alias": "测试11",
        "mobile": "192001232247",
        "department": [1]
    }

    def setup(self):
        self.address = Address()

    def teardown(self):
        self.address.delete_member(self.data["userid"])

    def test_create(self):
        # 数据处理,创建成员前确保没这个成员
        self.address.delete_member(self.data["userid"])
        #创建用户
        r = self.address.create_member(self.data)
        print(r)
        # 用户信息是不是正确
        assert r.get("errmsg") == "created"
        r = self.address.get_member(self.data["userid"])
        print(r)
        assert r.get("name") == self.data["name"]

    def test_crate(self):
        #查找成员
        self.address.create_member(self.data)
        r = self.address.get_member(self.data["userid"])
        print(r)
        assert r.get("name") == self.data["name"]

    def test_update(self):
        #更新成员
        self.address.create_member(self.data["userid"])
        self.address.get_member(self.data["userid"])
        new_name = "李三321"
        self.data["name"] = new_name
        r = self.address.update_member(self.data)
        assert r.get("errmsg") == "updated"
        r = self.address.get_member(self.data["userid"])
        assert r.get("name") == new_name

    def test_delete(self):
        #删除成员
        s = self.address.create_member(self.data)
        print(s)
        z = self.address.get_member(self.data["userid"])
        print(z)
        r = self.address.delete_member(self.data["userid"])
        print(r)
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member(self.data["userid"])
        assert r.get("errcode") == 60111