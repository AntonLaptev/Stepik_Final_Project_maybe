from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, promo_product_page_link)  # инициализируем Page Object, передаем   драйвер и url
    page.open()  # открываем страницу
    page.should_be_data_on_product_page()  # проверка и получение цены, наличия, названия товара
    page.put_product_to_the_basket()  # нажимаем добавить в корзину
    page.solve_quiz_and_get_code()  # в алерте решаем задачку получаем код для проверки
    page.should_be_product_in_basket()  # проверка алертов что товар в корзине, имя товара и цена верные


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.put_product_to_the_basket()
    page.should_not_see_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_not_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.put_product_to_the_basket()
    page.should_disappear_success_message_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'qweq345uefhue'
        page = ProductPage(browser, product_page_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_success_registration_message()
        login_page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_page_link)
        page.open()
        page.should_not_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, promo_product_page_link)
        page.open()
        page.should_be_data_on_product_page()
        page.put_product_to_the_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_in_basket()
