from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def should_be_product_in_basket_and_promo_calc(self):
    product_price = ''
    product_title = ''

    def put_product_to_the_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_data_on_product_page(self):
        self.should_be_product_price()
        self.should_be_product_title()
        self.should_be_available_product()
        self.should_be_button_add_to_basket()

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

    def should_be_product_in_basket(self):
        self.should_be_message_add_product_ok()
        self.should_be_adding_product_price()

    def should_be_message_add_product_ok(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_PRODUCT_OK), "Product was not added"
        assert self.product_title == self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_OK).text, \
            "Product title != Product title in the basket "

    def should_be_adding_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_PRODUCT_PRICE_OK), "Product price was not added"
        assert self.product_price == self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_PRICE_OK).text,\
            "Product price != product price in basket"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_PRODUCT_OK), \
            "Success message is presented, but should not be"

    def should_disappear_success_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_PRODUCT_OK), \
            "Success message is presented, but should not be"
