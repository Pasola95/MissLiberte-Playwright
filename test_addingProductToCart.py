import pytest
from playwright.sync_api import Page, expect
import time


@pytest.mark.parametrize("product_url", ["https://missliberte.com/produkt/top-shape-z-bawelny-organicznej-leopard"])
def test_add_product_to_cart(page: Page, product_url: str):
    # 1. Open product page
    page.goto(product_url)

    # 2. Select S size
    time.sleep(2)
    size_select = (page.locator("//li[1]//label[1]"))
    size_select.check()

    # 3. Add product to cart
    time.sleep(2)
    add_to_cart_button = "//button[normalize-space()='Dodaj do koszyka']"
    page.click(add_to_cart_button)

    # 4. Open cart in mini-cart po-up
    cart_button = "div[class='header--row-top'] a[class='btn']"
    page.click(cart_button)

    # 5. Check that product is added to cart
    product_in_cart = "//a[contains(text(),'Top shape z bawełny organicznej | Léopard – S')]"
    expect(page.locator(product_in_cart)).to_be_visible()
    expect(page.locator(product_in_cart)).to_have_text("Top shape z bawełny organicznej | Léopard – L")

