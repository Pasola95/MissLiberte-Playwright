import re
from playwright.sync_api import Page, expect
import time


def test_popup_close(page: Page):
    page.goto("https://missliberte.com/")

    # Click on 'close' button
    checkbox = (page.locator("//input[@name='your-acceptance']"))
    checkbox.check()

    time.sleep(2)

