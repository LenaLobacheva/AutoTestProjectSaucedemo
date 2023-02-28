from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


def supper():
    pass


class Client_information_page(Base):

    def __init__(self, driver):
        supper().__init__(driver)
        self.driver = driver

    # Locators

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    zip_code = '//*[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    # Getters - создали методы, которые используют локаторы. К которым указали,что используем явное ожидание в течение 30 секунд
    # указали, что главным элементом должно быть - кликабельность

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions - описываем, что именно будем делать с локаторами

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('input first name')
    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('input last name')
    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('input zip code')
    def click_continue_button(self):
        self.get_continue_button().click()
        print('click continue button')

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_zip_code("1234")
        self.click_continue_button()



