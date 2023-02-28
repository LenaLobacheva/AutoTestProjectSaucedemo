import time

from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page

def test_link_about():
    driver = webdriver.Firefox(executable_path='C:\\Users\\MGaming\\PycharmProjects\\resource\\geckodriver.exe')

    print('Start Test')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print('Test is done')
    time.sleep(10)
    driver.quit()







