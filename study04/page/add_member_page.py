from selenium.webdriver.common.by import By
from study04.page.base_page import BasePage
from study04.page.member_page import GetMenberPage


class AddMember(BasePage):
    # base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def addmember(self,name,acctid,phone):
        #输入姓名
        self.find(By.ID,'username').send_keys(name)


        # self.find(By.ID,"memberAdd_english_name").sendkeys()

        #输入账号
        self.find(By.ID,'memberAdd_acctid').send_keys(acctid)

        #输入手机号
        self.find(By.ID,'memberAdd_phone').send_keys(phone)

        #保存成员信息
        self.find(By.CSS_SELECTOR,".js_btn_save").click()

        return GetMenberPage(self.driver)