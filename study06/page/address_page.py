from study06.page.base_page import BasePage
from study06.page.personal_information_page import PersonalInformation


class Address(BasePage):
    def search(self):
        ele = self.parse_action("../data/address_page.yaml","search")
        print(ele)
        return PersonalInformation(self.driver)

