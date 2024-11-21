import random
from pages.base_page import BasePage



class NewsletterPopup(BasePage):
    # Locators
    random = random.randint(10000, 99999)
    username_input_locator = "//input[@placeholder='Wpisz imię']"
    email_input_locator = "//input[@placeholder='Wpisz adres e-mail']"
    policy_checkbox_locator = "//input[@name='your-acceptance']"
    popup_is_visible_locator = "div#newsletter_modal[style='display: flex;']"
    success_message_locator = "//div[@class='subscribe-success']"
    name_warning_locator = "span[data-name='your-name'] span[class='wpcf7-not-valid-tip']"
    email_warning_locator = "span[data-name='your-email'] span[class='wpcf7-not-valid-tip']"
    close_popup_locator = "//span[@class='ic-close close-modal']"
    open_popup_locator = "//div[@class='container header-bar--container']"

    def subscribe_to_newsletter(self, username="Test", email=f"pasola.test{random}@yopmail.com", button="ZAPISZ SIĘ"):
        self.page.locator(self.username_input_locator).fill(username)
        self.page.locator(self.email_input_locator).fill(email)
        self.page.locator(self.policy_checkbox_locator).check()
        self.page.get_by_role("button", name=f"{button}").click()

    def click_close_popup_button(self):
        self.page.locator(self.close_popup_locator).click()
