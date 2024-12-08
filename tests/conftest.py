from playwright.sync_api import sync_playwright
import pytest



@pytest.fixture(scope="function", autouse=True)
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function", autouse=True)
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

