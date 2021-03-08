import pytest
from study04.page.home_page import HomePage


class TestDemo:
    def setup(self):
        self.HomePage = HomePage()

    def teardown(self):
        self.HomePage.quit()

    def test_addmember(self):
        name = "ceshi0125"
        acctid = "ceshi0126"
        phone = "13990909849"

        assert self.HomePage.goto_add_member().addmember(name,acctid,phone)

        #这那写的有问题
        # names = self.HomePage.goto_add_member().addmember(name, acctid, phone).get_member()
        # print(names)
        # assert name in names

        # 这那写的有问题
        # page = self.HomePage.goto_add_member()
        # page.addmember(name,acctid,phone)
        # names = page.get_member()
        # print(names)
        # assert name in names

