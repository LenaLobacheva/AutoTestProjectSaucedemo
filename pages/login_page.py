from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


def supper():
    pass


class Login_page(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        supper().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@data-test='username']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//span[@class='title']"


    # Getters - создали методы, которые используют локаторы. К которым указали,что используем явное ожидание в течение 30 секунд
    # указали, что главным элементом должно быть - кликабельность

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions - описываем, что именно будем делать с локаторами

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('input user name')
    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')
    def click_login_button(self):
        self.get_login_button().click()
        print('click login_button')

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'PRODUCTS')


