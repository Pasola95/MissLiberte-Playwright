from conftest import BASE_URL
from pages.base_page import BasePage
from playwright.sync_api import expect


class CategoryPage(BasePage):
    # Locators
    category_name_locator = "//div[@class='header--row-bottom']//a[text()='{}']"

    def open_category(self, name, url):
        self.page.locator(self.category_name_locator.format(name)).click()
        expect(self.page).to_have_url(BASE_URL + f"{url}")

    def open_sub_category(self, name, url):
        self.page.locator(self.category_name_locator.format("Więcej")).hover()
        self.page.locator(self.category_name_locator.format(name)).click()
        expect(self.page).to_have_url(BASE_URL + f"{url}")
