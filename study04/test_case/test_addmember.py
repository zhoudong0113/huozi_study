import pytest
from study04.page.home_page import HomePage


class TestDemo:
    def setup(self):
        self.HomePage = HomePage()

    def teardown(self):
        self.HomePage.quit()

    def test_addmember(self):
        name = "ceshi01251"
        acctid = "ceshi01261"
        phone = "13990909822"

        assert self.HomePage.goto_add_member().addmember(name,acctid,phone).get_member()
