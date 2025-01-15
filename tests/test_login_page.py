from playwright.sync_api import expect

from conftest import BASE_URL
from pages.login_page import LoginPage


def test_valid_logining(page):
    login_page = LoginPage(page)

    # Open main page and close newsletter popup
    page.goto(BASE_URL + 'moje-konto/')

    # Login with existing user
    login_page.logining_with_user()
    expect(page).to_have_url(BASE_URL + "moje-konto/orders/")

# Skip
# def test_login_invalid_email(page):
#     login_page = LoginPage(page)
#
#     # Open main page and close newsletter popup
#     page.goto(BASE_URL + 'moje-konto/')
#
#     # Try to log in with not existing user
#     login_page.logining_with_user(email="pasola.fail@yopmail.com")
#     # Check alert message
#     login_page.check_alert_message("Nieznany adres e-mail")

