class MainPage:
    def __init__(self, page):
        self.page = page
        self.acceptance_checkbox = page.locator("//input[@name='your-acceptance']")

    def check_acceptance(self):
        self.acceptance_checkbox.check()