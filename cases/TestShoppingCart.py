from check.OrderCheck import OrderCheck
from check.ShoppingCartCheck import ShoppingCartCheck
from libs.BaseTest import BaseTest


class TestShoppingCart(BaseTest):

    def test_shopping_cart_order(self):
        self.page.home_page().open_home_page()
        self.page.home_page().click_spu()
        self.page.home_page().switch_to_window(1)
        self.page.goods_details_page().click_add_shopping_cart()
        self.page.shopping_cart_page().open_shopping_cart_page()
        self.page.shopping_cart_page().click_add_account()
        self.page.shopping_cart_page().click_all_button()
        self.page.shopping_cart_page().click_order_button()
        self.page.order_render_page().click_create_order()
        OrderCheck.cashier_desk(self)
        self.page.cashier_page().click_buy_way()
        self.page.cashier_page().click_buy_button()
        OrderCheck.pay_bound(self)

    def test_shopping_cart_valuation(self):
        self.page.home_page().open_home_page()
        self.page.home_page().click_spu()
        self.page.home_page().switch_to_window(1)
        self.page.goods_details_page().click_add_shopping_cart()
        self.page.shopping_cart_page().open_shopping_cart_page()
        ord_num = int(self.page.shopping_cart_page().get_goods_num())
        self.page.shopping_cart_page().click_add_account()
        add_num = int(self.page.shopping_cart_page().get_goods_num())
        assert add_num - ord_num == 1
        self.page.shopping_cart_page().click_minus_account()
        minus_num = int(self.page.shopping_cart_page().get_goods_num())
        assert add_num - minus_num == 1
        ShoppingCartCheck.calculate_price_check(self)
