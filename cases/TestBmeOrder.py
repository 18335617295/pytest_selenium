from check.OrderCheck import OrderCheck
from libs.BaseTest import BaseTest


class TestBmeOrder(BaseTest):

    def test_bme_order(self):
        self.page.bme_page().open_bme_page()
        self.page.bme_page().click_server()
        OrderCheck.calculate_price_check(self)
        self.page.bme_page().click_buy_button()
        self.page.order_render_page().click_select_store()
        self.page.order_store_list_page().click_select_store()
        self.page.order_store_list_page().click_submit_button()
        self.page.order_render_page().click_create_order()
        OrderCheck.cashier_desk(self)
        self.page.cashier_page().click_buy_way()
        self.page.cashier_page().click_buy_button()
        OrderCheck.pay_bound(self)

