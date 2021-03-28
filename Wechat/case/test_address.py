from Wechat.base.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()
        self.data = {
            "userid": "zhangsan4",
            "name": "张三4",
            "alias": "jackzhang4",
            "mobile": "14200000004",
            "department": [1]
        }

    def teardown(self):
        self.address.delete_member(self.data["userid"])

    def test_create(self):
        # 数据处理,创建成员前确保没这个成员
        self.address.delete_member(self.data["userid"])
        # 用户信息是不是正确
        r = self.address.create_member(self.data)
        print(r)
        assert r.get("errmsg") == "created"
        r = self.address.get_member(self.data["userid"])
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
        new_name = "李三"
        self.data["name"] = new_name
        r = self.address.update_member(self.data)
        assert r.get("errmsg") == "updated"
        r = self.address.create_member(self.data["userid"])
        assert r.get("name") == new_name

    def test_delete(self):
        #删除成员
        self.address.create_member(self.data["userid"])
        self.address.get_member(self.data["userid"])
        r = self.address.delete_member(self.data["userid"])
        assert r.get("errmsg") == "deleted"
        r = self.address.create_member(self.data["userid"])
        assert r.get("errcode") == 60111