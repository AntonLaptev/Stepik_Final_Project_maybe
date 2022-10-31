# этот файл может выполняться в тестах всех поддиректорий
import pytest
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose language browser")


@pytest.fixture(scope="function")
def user_lang(request):
    user_language = request.config.getoption("language")
    return user_language


@pytest.fixture(scope="function")
def browser(request, user_lang):
    browser_name = request.config.getoption("browser_name")
    # browser = None
    if browser_name == "chrome":
        print(f"\nstart {browser_name} browser (user language - {user_lang}) for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nstart {browser_name} browser, user language {user_lang} for test..")
        options = Options()
        options.set_preference("intl.accept_languages", user_lang)
        browser = Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
