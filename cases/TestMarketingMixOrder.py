import time

from check.OrderCheck import OrderCheck
from libs.BaseTest import BaseTest


class TestMarketingMixOrder(BaseTest):

    def test_marketing_mix_order(self):
        self.page.marketing_mix_page().open_marketing_mix_page()
        self.page.marketing_mix_page().click_server_button()
        self.page.marketing_mix_page().click_buy_button()
        time.sleep(5)
        self.page.order_render_page().click_create_order()
        time.sleep(10)
