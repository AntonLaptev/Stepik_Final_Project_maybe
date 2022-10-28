from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def should_be_product_in_basket_and_promo_calc(self):
    product_price = ''
    product_title = ''

    def should_be_product_data(self):
        self.should_be_product_price()
        self.should_be_product_title()
        self.should_be_available_product()
        self.should_be_button_add_to_basket()

    def should_be_product_in_basket(self):
        self.should_be_message_add_product_ok()
        self.should_be_adding_product_price()

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "There is no product price on product page"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "There is no product title on product page"
        self.product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def should_be_available_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_AVAILABLE), "Product is not available"

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "ADD_TO_BASKET_BUTTON is not "\
                                                                                    "available"

    def should_be_message_add_product_ok(self):
        assert self.product_title in self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_OK).text, \
                                                                                            "Product was not added "

    def should_be_adding_product_price(self):
        assert self.product_price in self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_PRICE_OK).text,\
                                                                                        "Product price was not added"

    def put_product_to_the_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
