from study06.page.base_page import BasePage
from study06.page.editorial_members_page import EditorialMembers


class PersonalInformation(BasePage):

    def goto_editorial_members(self):
        self.parse_action("../data/personal_information_page.yaml", "goto_editorial_members")
        return EditorialMembers(self.driver)