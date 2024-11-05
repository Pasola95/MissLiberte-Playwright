import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dompak-site.ffflabel-dev.com/#lang-target-content")
    page.get_by_role("link", name="English version").click()
    page.get_by_placeholder("Type number").click()
    page.get_by_placeholder("Type number").fill("12345")
    page.get_by_role("button", name="Track").click()
    page.get_by_role("heading", name=" Numer przesyłki:").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
