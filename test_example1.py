import re, time
from playwright.sync_api import Page, expect


def test_popup_close(page: Page):
    page.goto("https://missliberte.com/")

    # Click on 'close' button
    news_close_button = page.locator('//span[@class="ic-close close-modal"]')
    news_close_button.click()

    time.sleep(2)