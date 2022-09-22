from selenium.webdriver.common.by import By
from libs.BaseAction import BaseAction


class CashierPage(BaseAction):
    buy_button = By.XPATH, '//*[text()=" 确认支付 "]'
    buy_way = By.XPATH, '//*[text()="支付宝"]'

    def click_buy_button(self):
        self.click(self.buy_button)

    def click_buy_way(self):
        self.click(self.buy_way)
