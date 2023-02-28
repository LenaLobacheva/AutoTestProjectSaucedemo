from base.base_class import Base

def supper():
    pass

class Finish_page(Base):

    def __init__(self, driver):
        supper().__init__(driver)
        self.driver = driver

    # Methods
    def finish(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()


