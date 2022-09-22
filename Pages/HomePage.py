from selenium.webdriver.common.by import By
from libs.BaseAction import BaseAction


class HomePage(BaseAction):
    home_url = "https://media.uat.haochezhu.club/mall/index.html#/mainIndex"
    bme = By.XPATH, '//*[text()="到店服务"]/preceding-sibling::div/div'
    spu = By.XPATH, '//*[@class="goodsBox"]/div'

    def open_home_page(self, url=home_url):
        self.driver.get(url)

    def click_bme(self):
        self.click(self.bme)

    def click_spu(self):
        self.click(self.spu)

