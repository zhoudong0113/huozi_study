from study05.page.app import App


class TestSign:
    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_address().goto_members().add_manually().add_members()
