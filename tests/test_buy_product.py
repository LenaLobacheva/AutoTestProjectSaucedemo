import time

import pytest as pytest
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

# @pytest.mark.run(order=3)
def test_buy_product_1(set_group):
    driver = webdriver.Firefox(executable_path='C:\\Users\\MGaming\\PycharmProjects\\resource\\geckodriver.exe')

    print('Start Test 1')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print('Finish test 1')
    # time.sleep(10)
    driver.quit()

# @pytest.mark.run(order=1)
def test_buy_product_2(set_group):
    driver = webdriver.Firefox(executable_path='C:\\Users\\MGaming\\PycharmProjects\\resource\\geckodriver.exe')

    print('Start Test 2')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print('Finish test 2')
    # time.sleep(10)
    driver.quit()

# @pytest.mark.run(order=2)
def test_buy_product_3(set_up):
    driver = webdriver.Firefox(executable_path='C:\\Users\\MGaming\\PycharmProjects\\resource\\geckodriver.exe')

    print('Start Test 3')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print('Finish test 3')
    # time.sleep(10)
    driver.quit()



