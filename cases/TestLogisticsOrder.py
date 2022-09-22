import time

from check.OrderCheck import OrderCheck
from libs.BaseTest import BaseTest


class TestLogisticsOrder(BaseTest):

    def test_logistics_order(self):
        self.page.home_page().open_home_page()
        self.page.home_page().click_spu()
        self.page.home_page().switch_to_window(1)
        self.page.goods_details_page().click_order_button()
        self.page.order_render_page().click_create_order()
        OrderCheck.cashier_desk(self)
        self.page.cashier_page().click_buy_way()
        self.page.cashier_page().click_buy_button()
        OrderCheck.pay_bound(self)

