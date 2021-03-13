from study06.page.base_page import BasePage


class EditorialMembers(BasePage):

    def editorial_members(self):
        self.parse_action("../data/editorial_members_page.yaml", "editorial_members")