import random
from pages.base_page import BasePage


class NewsletterPopup(BasePage):
    # Locators
    username_input_locator = "//input[@placeholder='Wpisz imię']"
    email_input_locator = "//input[@placeholder='Wpisz adres e-mail']"
    policy_checkbox_locator = "//input[@name='your-acceptance']"
    popup_is_visible_locator = "div#newsletter_modal[style='display: flex;']"
    success_message_locator = "//div[@class='subscribe-success']"
    name_warning_locator = "span[data-name='your-name'] span[class='wpcf7-not-valid-tip']"
    email_warning_locator = "span[data-name='your-email'] span[class='wpcf7-not-valid-tip']"
    # policy_checkbox_warning = "span[data-name='your-name'] span[class='wpcf7-not-valid-tip']"
    close_popup_locator = "//span[@class='ic-close close-modal']"
    open_popup_locator = "//div[@class='container header-bar--container']"

    def enter_username(self, username="Test"):
        self.page.locator(self.username_input_locator).fill(username)

    def enter_email(self, email=f"pasola.test{random.randint(10000, 99999)}@yopmail.com"):
        self.page.locator(self.email_input_locator).fill(email)

    def policy_check(self):
        self.page.locator(self.policy_checkbox_locator).check()

    def click_submit_button(self, button="ZAPISZ SIĘ"):
        self.page.get_by_role("button", name=f"{button}").click()

    def click_close_popup_button(self):
        self.page.locator(self.close_popup_locator).click()

