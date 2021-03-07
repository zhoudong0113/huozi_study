from selenium.webdriver.common.by import By

from study04.page.base_page import BasePage


class GetMenberPage(BasePage):

    def get_member(self):
        self.wait_for_click(5,(By.CSS_SELECTOR,".member_colRight_memberTable_th_Checkbox"))
        names = []
        name_list = self.driver.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child[2]")
        for i in name_list:
            names.append(i.get_attribute("title"))
        return names