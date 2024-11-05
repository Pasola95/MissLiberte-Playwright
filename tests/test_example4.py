import random
from playwright.sync_api import Playwright, sync_playwright, expect

def register_user(page):
    page.goto("https://admin:111111@itm.ffflabel-dev.com/login")
    page.get_by_role("link", name="Zarejestruj się").click()
    page.get_by_label("Nazwa").fill("test")
    random_digits = random.randint(10000, 99999)
    email = f"ffflabel.test.itm+{random_digits}@gmail.com"
    page.get_by_label("E-mail").fill(email)
    page.get_by_label("Hasło", exact=True).fill("Pasola_123")
    page.get_by_label("Potwierdź hasło").fill("Pasola_123")
    # page.get_by_text("Wyrażam zgodę na").click()
    page.get_by_text("Akceptuję regulamin.").click()
    page.get_by_role("button", name="Zarejestruj się", exact=True).click()
    expect(page.get_by_role("link", name="Profil", exact=True)).to_be_visible()
    return email

def fill_personal_info(page):
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
    page.get_by_label("Nazwa bankу").fill("Test")
    page.get_by_role("button", name="Zapisz").click()
    expect(page.get_by_role("button", name="Ok")).to_be_visible()
    page.get_by_role("button", name="Ok").click()

def connect_instagram(page):
    page.get_by_role("link", name="Profil", exact=True).click()
    page.locator("//tr[@data-row-key='instagram']//button[@type='button']").click()
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Zatwierdź").click()
    popup = popup_info.value
    popup.locator("//input[@id='email']").fill("test_instagram_user@yopmail.com")
    popup.locator("//input[@id='pass']").fill("TestPassword_123")
    popup.locator("//button[@id='loginbutton']").click()
    expect(popup.get_by_role("button", name="Reconnect")).to_be_visible()
    popup.get_by_role("button", name="Reconnect").click()
    popup.get_by_role("button", name="Zamknij").click()
    popup.close()

def logout(page):
    page.locator("header").get_by_role("img").nth(2).click()
    page.get_by_text("Wyloguj się").click()

def login_with_instagram(page):
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Zaloguj się przez Instagram").click()
    popup = popup_info.value
    expect(popup.get_by_role("button", name="Reconnect")).to_be_visible()
    popup.get_by_role("button", name="Reconnect").click()
    popup.close()

def delete_account(page):
    page.get_by_text("t", exact=True).click()
    page.get_by_text("Profil").click()
    page.get_by_role("button", name="Usuń konto").click()
    page.get_by_role("button", name="Tak").click()

def test_itm_instagram_connecting(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        email = register_user(page)
        fill_personal_info(page)
        connect_instagram(page)
        logout(page)
        login_with_instagram(page)
        delete_account(page)
    finally:
        browser.close()
