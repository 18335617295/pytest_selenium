import time

from selenium.webdriver.common.by import By

from libs.BaseAction import BaseAction


class OrderRenderPage(BaseAction):
    create_order = By.XPATH, '//*[text()="立即下单"]'
    select_store = By.XPATH, '//*[@class="epair-shop"]'

    def click_create_order(self):
        time.sleep(1)
        self.js_click(self.create_order)

    def click_select_store(self):
        self.click(self.select_store)
