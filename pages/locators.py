class BasePageLocators:
    LOGIN_LINK = ("css selector", "#login_link")
    LOGIN_LINK_INVALID = ("css selector",   "#login_link_inc")
    BASKET_BUTTON = ("css selector", ".btn-group a.btn-default")


class MainPageLocators:
    LOGIN_LINK = ("css selector", "#login_link")


class LoginPageLocators:
    LOGIN_FORM = ("id", "login_form")
    REGISTER_FORM = ("id", "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = ("class name", "btn-add-to-basket")
    PRODUCT_TITLE = ("css selector", ".product_main h1")
    PRODUCT_AVAILABLE = ("css selector", ".product_main .instock .icon-ok")
    PRODUCT_PRICE = ("css selector", ".product_main p.price_color")
    MESSAGE_ADD_PRODUCT_OK = ("css selector", ".alert-success  .alertinner strong")
    MESSAGE_ADD_PRODUCT_PRICE_OK = ("css selector", ".alert-info  .alertinner strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = ("id", "content_inner")
    PRODUCT_IN_BASKET = ("class name", "basket-items")
