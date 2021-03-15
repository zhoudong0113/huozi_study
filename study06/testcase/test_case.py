from study06.page.app import App


class TestMember:
    def setup(self):
        self.app = App()

    def test_delete_member(self):
        assert self.app.goto_main().goto_address().search().goto_editorial_members().editorial_members()

