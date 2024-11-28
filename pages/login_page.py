from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    email_field_locator = "//input[@id='username']"
    pass_field_locator = "//input[@id='password']"
    login_button_locator = "//p[@class='form-row']//button"
    alert_locator = "//ul[@role='alert']"

    def logining_with_user(self, email="pasola.test1234@yopmail.com", password="Pasola_123"):
        self.page.locator(self.email_field_locator).fill(email)
        self.page.locator(self.pass_field_locator).fill(password)
        self.page.locator(self.login_button_locator).click()

    def check_alert_message(self, message):
        expect(self.page.locator(self.alert_locator)).to_have_text(message)




