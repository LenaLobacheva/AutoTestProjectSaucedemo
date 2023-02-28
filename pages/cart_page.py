from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


def supper():
    pass


class Cart_page(Base):


    def __init__(self, driver):
        supper().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = '//button[@id="checkout"]'

    # Getters - создали методы, которые используют локаторы. К которым указали,что используем явное ожидание в течение 30 секунд
    # указали, что главным элементом должно быть - кликабельность

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions - описываем, что именно будем делать с локаторами

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('click checkout button')

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()



