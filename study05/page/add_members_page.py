from study05.page.base_page import BasePage


class AddMembers(BasePage):

    def add_manually(self):
        self.parse_action("../data/add_menbers_page.yaml", "add_manually")
        return self

    def add_members(self):
        self.parse_action("../data/add_menbers_page.yaml", "add_members")


