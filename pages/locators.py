from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".table-striped>tbody>tr:nth-child(4)>td")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>div>strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>div>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

