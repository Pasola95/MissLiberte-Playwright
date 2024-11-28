from playwright.sync_api import expect
from conftest import BASE_URL
from pages.category_page import CategoryPage
from pages.home_page import NewsletterPopup


def test_main_categories_opening(page):
    newsletter_popup = NewsletterPopup(page)
    category_page = CategoryPage(page)

    # Open main page and close newsletter popup
    page.goto(BASE_URL)
    newsletter_popup.click_close_popup_button()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).not_to_be_visible()

    # Open Main categories
    category_page.open_category("WSZYSTKIE", "/shop-collection/")
    category_page.open_category("Swim", "/kategoria-produktu/miss-liberte-swim/")
    category_page.open_category("Bielizna", "/kategoria-produktu/bielizna/")
    category_page.open_category("Biustonosze", "/kategoria-produktu/biustonosze/")
    category_page.open_category("Majtki", "/kategoria-produktu/majtki/")
    category_page.open_category("Body", "/kategoria-produktu/body/")
    category_page.open_category("Homewear", "/kategoria-produktu/homewear/")
    category_page.open_category("Sale", "/kategoria-produktu/sale/")
    category_page.open_category("Karty podarunkowe", "/karta-podarunkowa/")
    category_page.open_category("Last Pieces", "/kategoria-produktu/last-pieces/")


def test_sub_categories_openings(page):
    newsletter_popup = NewsletterPopup(page)
    category_page = CategoryPage(page)

    # Open main page and close newsletter popup
    page.goto(BASE_URL)
    newsletter_popup.click_close_popup_button()
    expect(page.locator(newsletter_popup.popup_is_visible_locator)).not_to_be_visible()

    # Open Sub categories
    category_page.open_sub_category("Kontakt", "/kontakt/")
    category_page.open_sub_category("Dobierz rozmiar", "/dobierz-rozmiar/")
    category_page.open_sub_category("Dostawy i płatności", "/dostawa-i-platnosci/")
    category_page.open_sub_category("Wymiany i zwroty", "/wymiana-i-zwrot/")
    category_page.open_sub_category("Jak kupić na prezent", "/na-prezent/")
    category_page.open_sub_category("O Miss Liberté", "/o-nas/")
    category_page.open_sub_category("Zrównoważona produkcja", "/zrownowazona-produkcja/")
    category_page.open_sub_category("Współpraca", "/wspolpraca/")

