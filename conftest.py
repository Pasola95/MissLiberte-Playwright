import pytest
from config import BASE_URL
from pages.home_page import HomePage


@pytest.fixture
# Open Home page without Newsletter popup
def home_page(page):
    home_page = HomePage(page)
    page.goto(BASE_URL)
    home_page.close_popup()
    return home_page


@pytest.fixture
# Open Home page with Newsletter popup
def news_home_page(page):
    page.goto(BASE_URL)
