from playwright.sync_api import expect
from pages.newsletter_page import NewsletterPopup


def test_newsletters_popup_success_subscription(page):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto("https://missliberte-new.ffflabel-dev.com/")
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Enter valid information and click on 'Sign Up' button
    newsletter_popup.enter_username()
    newsletter_popup.enter_email()
    newsletter_popup.policy_check()
    newsletter_popup.click_submit_button()

    # Check that subscribe was succeeded
    expect(page.locator(newsletter_popup.success_message_locator)).to_be_visible(timeout=20000)


def test_newsletter_popup_warning_validation(page):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto("https://missliberte-new.ffflabel-dev.com/")
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Check 'Policy' checkbox and click on 'Sign Up' button
    newsletter_popup.policy_check()
    newsletter_popup.click_submit_button()

    # Check that warning message is shown for 'Name' field
    expect(page.locator(newsletter_popup.name_warning_locator)).to_be_visible(timeout=20000)
    # Check that warning message is shown for 'Email' field
    expect(page.locator(newsletter_popup.email_warning_locator)).to_be_visible(timeout=20000)
    # !!!Check that warning message is shown for Policy checkbox


def test_newsletter_popup_reopening(page):
    newsletter_popup = NewsletterPopup(page)

    # Open main page and wait for newsletter pop-up
    page.goto("https://missliberte-new.ffflabel-dev.com/")
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

    # Close pop-up and check that it closed
    newsletter_popup.click_close_popup_button()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).not_to_be_visible()

    # Reopen Newsletter popup
    page.locator(newsletter_popup.open_popup_locator).click()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).to_be_visible()

