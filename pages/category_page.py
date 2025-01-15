from pages.base_page import BasePage
from playwright.sync_api import expect


class CategoryPage(BasePage):
    # Products Locators
    product_name = "//h2[normalize-space()='{}']"
    expand_filter_locator = "(//a[@role='button'][contains(text(),'Pokaż więcej')])[{}]"
    filter_checkbox = "//a[normalize-space()='{}']"
    reset_filters = "//button[contains(text(),'Wyczyść filtry')]"

    def is_product_visible(self, name):
        expect(self.page.locator(self.product_name.format(name))).to_be_visible()

    def is_product_not_visible(self, name):
        expect(self.page.locator(self.product_name.format(name))).not_to_be_visible()

    def expan_filter(self, place):
        self.page.locator(self.expand_filter_locator.format(place)).click()

    def select_filter(self, filter_name):
        self.page.locator(self.filter_checkbox.format(filter_name)).click()

