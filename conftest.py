import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--user_language', action='store', default=None, help="Choose user_language:")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("user_language")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if user_language == None:
        raise pytest.UsageError("--user_language is empty")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
