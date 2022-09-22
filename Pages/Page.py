from Pages.BmePage import BmePage
from Pages.GoodsDetailsPage import GoodsDetailsPage
from Pages.HomePage import HomePage
from Pages.MarketingMixPage import MarketingMixPage
from Pages.OrderRenderPage import OrderRenderPage
from Pages.OrderStoreListPage import OrderStoreListPage
from Pages.CashierPage import CashierPage
from Pages.ShoppingCartPage import ShoppingCartPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        return HomePage(self.driver)

    def bme_page(self):
        return BmePage(self.driver)

    def order_render_page(self):
        return OrderRenderPage(self.driver)

    def order_store_list_page(self):
        return OrderStoreListPage(self.driver)

    def cashier_page(self):
        return CashierPage(self.driver)

    def goods_details_page(self):
        return GoodsDetailsPage(self.driver)

    def shopping_cart_page(self):
        return ShoppingCartPage(self.driver)

    def marketing_mix_page(self):
        return MarketingMixPage(self.driver)
