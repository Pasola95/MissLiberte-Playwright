import pytest

BASE_URL = "https://missliberte-new.ffflabel-dev.com"


@pytest.fixture
def setup_and_teardown():
    # Before
    print("Setup: Preparing test environment")
    yield
    # After
    print("Teardown: Cleaning up resources")
