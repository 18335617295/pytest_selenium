from libs.utils import *


class ShoppingCartCheck:
    @staticmethod
    def calculate_price_check(cls):
        time.sleep(2)
        result = cls.proxy.har
        interface_list = get_interface(result, "calculate-price")
        interface_list.reverse()
        response = json.loads(interface_list[0]["response"]["content"]["text"])["data"]
        cls.log.info(response)
