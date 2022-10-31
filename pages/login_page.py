from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTER)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTER)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FOR_REGISTER)
        repeat_password_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        part_url = 'login'
        page_url = self.browser.current_url
        assert part_url in page_url, f"Page URL is incorrect, expect '{part_url}' in '{page_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

    def should_be_success_registration_message(self):
        assert self.is_element_present(*LoginPageLocators.MESSAGE_REGISTER_OK), "The user has not been registered"
