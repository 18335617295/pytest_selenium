import time

from selenium.webdriver.common.by import By
from libs.BaseAction import BaseAction


class ShoppingCartPage(BaseAction):
    shopping_cart_url = "https://media.uat.haochezhu.club/mall/index.html#/shoppingCart"
    order_button = By.XPATH, '//*[text()="去结算"]'
    add_account = By.XPATH, '//*[@class="van-stepper__plus"]'
    num_account = By.XPATH, '//*[@class="van-stepper__input"]'
    minus_account = By.XPATH, '//*[@class="van-stepper__minus"]'
    all_button = By.XPATH, '//*[text()="全选"]'

    def open_shopping_cart_page(self, url=shopping_cart_url):
        time.sleep(1)
        self.driver.get(url)

    def click_order_button(self):
        self.execute_script(self.click_js, self.find_element(self.order_button))

    def click_add_account(self):
        self.click(self.add_account)

    def click_minus_account(self):
        self.click(self.minus_account)

    def click_all_button(self):
        self.execute_script(self.click_js, self.find_element(self.all_button))

    def get_goods_num(self):
        return self.get_attribute(self.num_account, "aria-valuenow")
