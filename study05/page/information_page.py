from study05.page.address_page import Address
from study05.page.base_page import BasePage


class InformationPage(BasePage):

    def goto_address(self):
        self.parse_action("../data/information_page.yaml", "goto_address")
        return Address(self.driver)
