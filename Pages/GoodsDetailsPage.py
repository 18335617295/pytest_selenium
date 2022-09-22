from selenium.webdriver.common.by import By

from libs.BaseAction import BaseAction


class GoodsDetailsPage(BaseAction):
    order_button = By.XPATH, '//*[text()="立即下单"]'
    add_shopping_cart = By.XPATH, '//*[text()="加入购物车"]'

    def click_order_button(self):
        self.execute_script(self.click_js, self.find_element(self.order_button))

    def click_add_shopping_cart(self):
        self.execute_script(self.click_js, self.find_element(self.add_shopping_cart))