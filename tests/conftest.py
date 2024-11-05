import pytest


@pytest.fixture()
def before_after_test():
    print("Before test!")
    yield  # Where the test runs
    print("After test!")
