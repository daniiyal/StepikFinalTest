from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKETLINK = (By.CSS_SELECTOR, ".basket-mini .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATIONBUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADDTOCART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")

class BasketPageLocators():
    BASKETITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTYTEXT = (By.CSS_SELECTOR, "#content_inner p")
