from selenium.webdriver.common.by import By
from study04.page.add_member_page import AddMember
from study04.page.base_page import BasePage


class HomePage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    #到添加成员界面
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    #到首页界面
    def goto_home(self):
        self.find(By.ID,"menu_index")
        return True
