from pages.base_page import BasePage
from pages.locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        email_field.send_keys(email)

        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD1)
        password1_field.send_keys(password)

        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD2)
        password2_field.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        submit_button.click()