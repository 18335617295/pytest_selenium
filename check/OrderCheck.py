import time

from libs.utils import *


class OrderCheck:
    calculate_price_response = parent_order_no = None

    # 保养计价
    @staticmethod
    def calculate_price_check(cls):
        time.sleep(2)
        result = cls.proxy.har
        interface_list = get_interface(result, "calculate-price")
        interface_list.reverse()
        response = json.loads(interface_list[0]["response"]["content"]["text"])["data"]
        cls.log.info(interface_list)
        assert response["totalServicePrice"] > 0, "保养工时费等于0"
        assert response["totalPrice"] > 0, "商品总价格等于0"
        assert response["totalDiscountPrice"] + response["totalServicePrice"] + response["itemPrice"] == response[
            "originalTotalPrice"], "计价总和错误"
        OrderCheck.calculate_price_response = response

    # 收银台
    @staticmethod
    def cashier_desk(cls):
        time.sleep(2)
        result = cls.proxy.har
        interface_list = get_interface(result, "api/order/create")
        pay_type_query = get_interface(result, "payTypeQuery")
        pay_type_query = json.loads(pay_type_query[0]["response"]["content"]["text"])["data"]
        response = json.loads(interface_list[0]["response"]["content"]["text"])["data"]
        assert response["parentOrderNo"], "订单号为空"
        assert response["payNo"] in cls.driver.current_url, "支付单不一致"
        cls.log.info(response["price"])
        cls.log.info(pay_type_query["amount"])
        assert str(response["price"] / 10 / 10) == pay_type_query["amount"], "实际支付金额与订单不一致"

    # 支付成功回跳
    @staticmethod
    def pay_bound(cls):
        time.sleep(2)
        assert "order/orderList" in cls.driver.current_url, "支付回跳地址错误"
