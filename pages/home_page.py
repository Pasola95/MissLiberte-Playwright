import random
from playwright.sync_api import expect
from config import BASE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    # Newsletters locators
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

    # Header locators
    category_name_locator = "//div[@class='header--row-bottom']//a[text()='{}']"
    language_switcher = "//div[@class='header--row-top'] //a[@title='{}']"
    logo_icon = "//div[@class='header--row-top']//div[@class='site-logo']"
    wishlist_button = "div[class='header--row-top'] a[href*=\"wishlist/\"]"
    my_account_button = "div[class='header--row-top'] a[href*=\"moje-konto/\"]"
    cart_button = "div[class='header--row-top'] a[href*=\"koszyk/\"]"

    # Newsletters modules
    def subscribe_to_newsletter(self, username="Jon", email=f"pasola.test{random}@gmail.com", button="ZAPISZ SIĘ"):
        self.page.locator(self.username_input_locator).fill(username)
        self.page.locator(self.email_input_locator).fill(email)
        self.page.locator(self.policy_checkbox_locator).check()
        self.page.get_by_role("button", name=f"{button}").click()

    def close_popup(self):
        self.page.locator(self.close_popup_locator).click()
        expect(self.page.locator(self.popup_is_visible_locator)).not_to_be_visible()

    def open_home_page(self):
        self.page.goto(BASE_URL)
        self.page.locator(self.close_popup_locator).click()
        expect(self.page.locator(self.popup_is_visible_locator)).not_to_be_visible()

    # Header modules
    def open_category(self, name, url):
        self.page.locator(self.category_name_locator.format(name)).click()
        expect(self.page).to_have_url(BASE_URL + f"{url}")

    def open_sub_category(self, name, url):
        self.page.locator(self.category_name_locator.format("Więcej")).hover()
        self.page.locator(self.category_name_locator.format(name)).click()
        expect(self.page).to_have_url(BASE_URL + f"{url}")

    def switch_language(self, language):
        self.page.locator(self.language_switcher.format(language)).click()
        expected_url = BASE_URL if language == "PL" else BASE_URL + "en/"
        expect(self.page).to_have_url(expected_url)

    def open_wishlist(self):
        self.page.locator(self.wishlist_button).click()
        expect(self.page).to_have_url(BASE_URL + "wishlist/")

    def open_my_account(self):
        self.page.locator(self.my_account_button).click()
        expect(self.page).to_have_url(BASE_URL + "moje-konto/")

    def open_cart(self):
        self.page.locator(self.cart_button).click()
        expect(self.page).to_have_url(BASE_URL + "koszyk/")
