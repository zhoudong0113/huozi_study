from study05.page.add_members_page import AddMembers
from study05.page.base_page import BasePage


class Address(BasePage):

    def goto_members(self):
        self.parse_action("../data/address_page.yaml", "goto_members")
        return AddMembers(self.driver)
