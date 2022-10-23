import pytest                       #этот файл может выполняться в тестах всех поддиректорий
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
 #запуск браузера
 
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',help="Choose lang")
    
@pytest.fixture(scope="function")
def user_lang(request):
    user_language = request.config.getoption("language")
    return user_language

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        options=Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = Firefox(options=options)
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()