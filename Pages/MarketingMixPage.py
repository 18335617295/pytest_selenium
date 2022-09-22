from selenium.webdriver.common.by import By
from libs.BaseAction import BaseAction


class MarketingMixPage(BaseAction):
    marketing_mix_url = "https://media.uat.haochezhu.club/mall/index.html#/marketingMix"
    server = By.XPATH, '//*[@class="van-icon van-icon-success"]'
    buy_button = By.XPATH, '//*[text()="立即下单"]'
    car_button = By.XPATH, '//*[text()="换车"]'
    car = By.XPATH, '//*[text()="阿尔法-罗密欧"]'

    def open_marketing_mix_page(self, url=marketing_mix_url):
        self.driver.get(url)

    def click_server_button(self, index=1):
        self.find_elements(self.server)[index].click()

    def click_buy_button(self):
        self.js_click(self.buy_button)
