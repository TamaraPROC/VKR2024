import pytest
from playwright.sync_api import sync_playwright

# Список браузеров для тестирования
browsers = ['chromium', 'firefox',  'edge', ]

@pytest.fixture(params=browsers)
def browser(request):
    browser_name = request.param
    with sync_playwright() as p:
        if browser_name == 'chromium':
            browser = p.chromium.launch(headless=False)
        elif browser_name == 'firefox':
            browser = p.firefox.launch(headless=False)
        elif browser_name == 'webkit':
            browser = p.webkit.launch(headless=False)
        elif browser_name == 'edge':
            browser = p.chromium.launch(headless=False, channel="msedge")
        elif browser_name == 'chrome_mob':
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                **p.devices['iPhone ']
            )
            page = context.new_page()
            yield page
            context.close()
            return
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()