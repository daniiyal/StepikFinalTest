from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOCART), "Нет кнопки добавления в корзину"

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADDTOCART)
        button.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        assert message == product_name, f"{product_name} is not {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.split(" ")[2]
        assert product_price in basket_price, f"{product_price} not equal {basket_price}"

    def should_not_be_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Сообщение есть"

    def should_dissapear_message(self):
        assert self.is_dissapeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), 'Сообщение не исчезло'
    
    