from .pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.should_be_product_data()       # проверка и получение цены, наличия, названия товара
    page.put_product_to_the_basket()    # нажимаем добавить в корзину
    page.solve_quiz_and_get_code()      # в алерте решаем задачку получаем код для проверки
    page.should_be_product_in_basket()  # проверка алертов что товар в корзине, имя товара и цена верные
