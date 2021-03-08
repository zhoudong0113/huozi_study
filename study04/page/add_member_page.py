from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from study04.page.base_page import BasePage


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

        sleep(2)

        # return GetMenberPage(self.driver)
        return True

    def get_member(self):
        # self.wait_for_click(5,(By.CSS_SELECTOR,".member_colRight_memberTable_th_Checkbox"))

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.member_colRight_memberTable_td_Checkbox')))

        name_list = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child[2]')
        names = []
        for i in name_list:
            names.append(i.get_attribute("title"))
        print(names)
        return names