from selenium.webdriver.common.by import By

from libs.BaseAction import BaseAction


class OrderStoreListPage(BaseAction):
    select_store = By.XPATH, '//*[@aria-checked="false"]'
    submit_button = By.XPATH, '//*[text()="选择此网点下单"]/parent::div'

    def click_select_store(self):
        self.click(self.select_store)

    def click_submit_button(self):
        self.execute_script(self.click_js, self.find_element(self.submit_button))
