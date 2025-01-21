import glob
import os
from datetime import datetime

import pytest
from config import BASE_URL
from pages.home_page import HomePage

# Auto adding date and time to report name
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"./report/report_{timestamp}.html"

    config.option.htmlpath = report_path

# Auto deletion of old reports
def pytest_sessionstart(session):
    report_dir = "./report/"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Save only last 5 reports
    reports = sorted(glob.glob(f"{report_dir}/report_*.html"))
    for report in reports[:-5]:
        os.remove(report)

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
