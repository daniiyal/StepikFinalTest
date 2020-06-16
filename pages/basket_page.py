from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKETITEMS), "В корзине есть товары"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTYTEXT), "Нет сообщения о пустой корзине"