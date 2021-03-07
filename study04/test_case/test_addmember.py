import pytest
from study04.page.home_page import HomePage


class TestDemo:
    def setup(self):
        self.HomePage = HomePage()

    def teardown(self):
        self.HomePage.goto_home()

    def test_addmember(self):
        name = "ceshi01"
        acctid = "ceshi01"
        phone = "13990909881"
        names = self.HomePage.goto_add_member().addmember(name,acctid,phone).get_member()
        print(names)