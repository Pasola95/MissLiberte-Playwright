from playwright.sync_api import expect
from pages.home_page import NewsletterPopup
from conftest import BASE_URL

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


def test_newsletter_popup_warning_validation(page):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto(BASE_URL)
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Check 'Policy' checkbox and click on 'Sign Up' button
    NewsletterPopup(page).subscribe_to_newsletter(username="", email="")

    # Check that warning message is shown for 'Name' field
    expect(page.locator(newsletter_popup.name_warning_locator)).to_be_visible(timeout=20000)
    # Check that warning message is shown for 'Email' field
    expect(page.locator(newsletter_popup.email_warning_locator)).to_be_visible(timeout=20000)


def test_newsletter_popup_reopening(page):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto(BASE_URL)
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Close pop-up and check that it closed
    newsletter_popup.click_close_popup_button()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).not_to_be_visible()

    # Reopen Newsletter popup
    page.locator(newsletter_popup.open_popup_locator).click()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()


def test_checkbox_links_validation(page, context):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto(BASE_URL)
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Click on "Privacy Policy" link and validate URL in the new tab
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Politykę Prywatności").click()
    expect(new_page_info.value).to_have_url(BASE_URL + "/polityka-prywatnosci/")

    # Click on "Terms and Conditions" link and validate URL in the new tab
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Regulamin Sklepu").click()
    expect(new_page_info.value).to_have_url(BASE_URL + "/regulamin-sklepu/")


