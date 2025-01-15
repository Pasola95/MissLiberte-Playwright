from playwright.sync_api import expect

from pages.home_page import HomePage
from config import BASE_URL, TEST_CAT


# Skip
# def test_newsletters_popup_success_subscription(page):
#     newsletter_popup = NewsletterPopup(page)
#
#     # Open main page and wait for newsletter pop-up
#     page.goto(BASE_URL)
#     expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()
#
#     # Enter valid information and click on 'Sign Up' button
#     newsletter_popup.subscribe_to_newsletter()
#
#     # Check that subscribe was succeeded
#     expect(page.locator(newsletter_popup.success_message_locator)).to_be_visible(timeout=20000)


def test_newsletter_popup_warning_validation(page,news_home_page):
    newsletter_popup = HomePage(page)

    # Check 'Policy' checkbox and click on 'Sign Up' button
    HomePage(page).subscribe_to_newsletter(username="", email="")

    # Check that warning message is shown for 'Name' field
    expect(page.locator(newsletter_popup.name_warning_locator)).to_be_visible(timeout=20000)
    # Check that warning message is shown for 'Email' field
    expect(page.locator(newsletter_popup.email_warning_locator)).to_be_visible(timeout=20000)


def test_newsletter_popup_reopening(page):
    newsletter_popup = HomePage(page)

    # Open main page and wait for newsletter pop-up
    page.goto(BASE_URL)
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Close pop-up and check that it closed
    newsletter_popup.close_popup()

    # Reopen Newsletter popup
    page.locator(newsletter_popup.open_popup_locator).click()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()


def test_checkbox_links_validation(page, context):
    newsletter_popup = HomePage(page)

    # Open main page and wait for newsletter pop-up
    page.goto(BASE_URL)
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Click on "Privacy Policy" link and validate URL in the new tab
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Politykę Prywatności").click()
    expect(new_page_info.value).to_have_url(BASE_URL + "polityka-prywatnosci/")

    # Click on "Terms and Conditions" link and validate URL in the new tab
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Regulamin Sklepu").click()
    expect(new_page_info.value).to_have_url(BASE_URL + "regulamin-sklepu/")


def test_main_categories_opening(page, home_page):
    home_page = HomePage(page)

    # Open Main categories
    home_page.open_category("WSZYSTKIE", "shop-collection/")


def test_sub_categories_openings(page, home_page):
    home_page = HomePage(page)

    # Open Sub categories
    home_page.open_sub_category("Kontakt", "kontakt/")


def test_language_switching(page, home_page):
    home_page = HomePage(page)

    # Switch language to ENG
    home_page.switch_language("ENG")
    # Switch language to PL
    home_page.switch_language("PL")


def test_main_logo_redirecting(page):
    # Open Test category and click on main icon in header
    page.goto(TEST_CAT)
    page.locator(HomePage(page).logo_icon).click()
    # Check that main page is opened
    expect(page).to_have_url(BASE_URL)


def test_navigation_buttons_opening(page, home_page):
    header = HomePage(page)

    # Click on "Wishlist", "My Account" and "Cart" icons and check page opening
    header.open_wishlist()
    header.open_my_account()
    header.open_cart()

