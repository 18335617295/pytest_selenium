from selenium.webdriver.common.by import By
from libs.BaseAction import BaseAction


class BmePage(BaseAction):
    bme_url = "https://media.uat.haochezhu.club/mall/index.html#/bme/index"
    server = By.XPATH, '//*[@aria-checked="false"]'
    buy_button = By.XPATH, '//*[@class="go-buy"]'
    car_button = By.XPATH, '//*[text()="换车"]'
    car = By.XPATH, '//*[text()="阿尔法-罗密欧"]'

    def open_bme_page(self, url=bme_url):
        self.driver.get(url)

    def click_server(self):
        self.click(self.server)

    def click_buy_button(self):
        self.js_click(self.buy_button)

    def click_car_button(self):
        self.click(self.car_button)

    def click_car(self):
        self.click(self.car)
