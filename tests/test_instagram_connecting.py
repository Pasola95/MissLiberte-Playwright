import random
import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_itm_instagram_connecting(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # New user registration
    page.goto("https://admin:111111@itm.ffflabel-dev.com/login")
    page.get_by_role("link", name="Zarejestruj się").click()
    page.get_by_label("Nazwa").fill("test")
    random_digits = random.randint(10000, 99999)
    page.get_by_label("E-mail").fill(f"ffflabel.test.itm+{random_digits}@gmail.com")
    page.get_by_label("Hasło", exact=True).fill("Pasola_123")
    page.get_by_label("Potwierdź hasło").fill("Pasola_123")
    page.get_by_text("Wyrażam zgodę na").click()
    page.get_by_text("Akceptuję regulamin.").click()
    page.get_by_role("button", name="Zarejestruj się", exact=True).click()

    # Personal information filling
    page.get_by_label("Imię").fill("Test")
    page.get_by_label("Nazwisko").fill("Test")
    page.locator("#gender").click()
    page.get_by_text("Mężczyzna").click()
    page.get_by_label("Numer PESEL").fill("70051141267")
    page.get_by_label("Adres nazwa ulicy").fill("Test")
    page.get_by_label("Kod pocztowy").fill("1111")
    page.get_by_label("Miasto").fill("Test")
    page.get_by_label("Numer telefonu").fill("12345678")
    page.get_by_label("IBAN / numer rachunku").fill("Test")
    page.get_by_label("Nazwa banku").fill("Test")
    page.get_by_role("button", name="Zapisz").click()
    page.get_by_role("button", name="Ok").click()

    # Connecting Instagram from Profile page
    page.get_by_role("link", name="Profil", exact=True).click()
    page.locator("//tr[@data-row-key='instagram']//button[@type='button']").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Zatwierdź").click()

    # Adding Instagram info
    page1 = page1_info.value
    page1.locator("//input[@id='email']").fill("pasola001@yopmail.com")
    page1.locator("//input[@id='pass']").fill("Pasola_123")
    page1.locator("//button[@id='loginbutton']").click()
    page1.get_by_role("button", name="Reconnect").click()
    page1.get_by_role("button", name="Zamknij").click()
    page1.close()

    # Logging out from account
    page.locator("header").get_by_role("img").nth(2).click()
    page.get_by_text("Wyloguj się").click()

    # Logining with Instagram
    with page.expect_popup() as page2_info:
        page.get_by_role("button", name="Zaloguj się przez Instagram").click()
    page2 = page2_info.value
    page2.get_by_role("button", name="Reconnect").click()

    # Removing account
    page.get_by_text("t", exact=True).click()
    page.get_by_text("Profil").click()
    page.get_by_role("button", name="Usuń konto").click()
    page.get_by_role("button", name="Tak").click()
    time.sleep(2)

