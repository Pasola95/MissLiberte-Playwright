from playwright.sync_api import expect

from config import TEST_CAT
from pages.category_page import CategoryPage


def test_filtering_by_size(page):
    category = CategoryPage(page)

    # Open Test category and check that both product are visible
    page.goto(TEST_CAT)
    category.is_product_visible("TEST PRODUCT 1")
    category.is_product_visible("TEST PRODUCT 2")

    # Select "S" size in filters
    category.expan_filter("1")
    category.select_filter("S")

    # Check that only Product with S size is selected
    category.is_product_visible("TEST PRODUCT 1")
    category.is_product_not_visible("TEST PRODUCT 2")


def test_filtering_by_color(page):
    category = CategoryPage(page)

    # Open Test category and check that both product are visible
    page.goto(TEST_CAT)
    category.is_product_visible("TEST PRODUCT 1")
    category.is_product_visible("TEST PRODUCT 2")

    # Select "Black" color in filters
    category.expan_filter("2")
    category.select_filter("Czarny")

    # Check that only Product with S size is selected
    category.is_product_visible("TEST PRODUCT 2")
    category.is_product_not_visible("TEST PRODUCT 1")


def test_filter_resetting(page):
    category = CategoryPage(page)

    # Open Test category
    page.goto(TEST_CAT)

    # Check "Reset filter" button is not visible by default
    expect(page.locator(category.reset_filters)).not_to_be_visible()

    # Select any filter and check that
    category.select_filter("Biały")
    expect(page.locator(category.reset_filters)).to_be_visible(timeout=20000)

    # Click on "Reset filter" button
    page.locator(category.reset_filters).click()
    expect(page.locator(category.reset_filters)).not_to_be_visible()








