import logging

from Pages.Page import Page
from conf.GlobalConfig import GlobalConfig
from libs import utils
from libs.Base import Base
from libs.BaseAction import create_diver
from libs.Requests import Requests


class BaseTest(Base):
    driver = proxy = server = None
    request = Requests()

    @classmethod
    def setup_class(cls):
        cls.driver, cls.proxy, cls.server = create_diver()
        cls.page = Page(cls.driver)
        # cls.path = f"{utils.get_path(cls.__name__)}"
        # cls.api = utils.yaml_file(f"{cls.__name__}", None, cls.path, "Api")
        # if "://" not in cls.api:
        #     cls.api = utils.get_ip(str(cls.__bases__[0])) + utils.yaml_file(f"{cls.__name__}", None, cls.path, "Api")
        # cls.Insert = utils.yaml_file(f"{cls.__name__}", None, cls.path, "InsertDB")
        # # uat环境mysql用到的需要全部连接  同步toc类 teardown  关闭, 类变量创建
        # if GlobalConfig.ENV == "uat":
        #     cls.tp_sql = MySqlHandler(f"gd_tp_{GlobalConfig.ENV}")
        #     cls.ump_sql = MySqlHandler(f"gd_ump_{GlobalConfig.ENV}")
        #     cls.items_sql = MySqlHandler(f"gd_items_{GlobalConfig.ENV}")
        #     cls.performance_sql = MySqlHandler(f"gd_performance_{GlobalConfig.ENV}")
        # else:
        #     cls.tp_sql = MySqlHandler(f"gd_aep")
        #     cls.ump_sql = MySqlHandler(f"gd_ump")
        #     cls.items_sql = MySqlHandler(f"gd_items")
        #     cls.performance_sql = MySqlHandler(f"gd_performance")

    @classmethod
    def setup_method(cls):
        # if cls.Insert:
        #     if cls.path == "tp":
        #         cls.tp_sql.exe_cute_all(cls.Insert)
        #     if cls.path == "ump":
        #         cls.ump_sql.exe_cute_all(cls.Insert)
        #     if cls.path == "items":
        #         cls.items_sql.exe_cute_all(cls.Insert)
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        cls.server.stop()
        # if not GlobalConfig.MAIN_ENV:
        #     GlobalConfig.ENV = "uat"
        # cls.tp_sql.close_database()
        # cls.ump_sql.close_database()
        # cls.items_sql.close_database()
        pass

    def assert_equal(self, expect, actual, message, ignoreType=False):
        """
        断言等于
        :param expect: 预期
        :param actual: 实际
        :param message: 错误消息
        :param ignoreType: true 忽略类型校验
        :return:
        """
        if ignoreType:
            assert str(expect) == str(actual), message
        else:
            assert expect == actual, message

    def assert_no_equal(self, expect, actual, message, ignoreType=False):
        """
        断言不等于
        :param expect: 预期
        :param actual: 实际
        :param message: 错误消息
        :param ignoreType: true 忽略类型校验
        :return:
        """
        if ignoreType:
            assert str(expect) != str(actual), message
        else:
            assert expect != actual, message

    def assert_in(self, expect, actual, message):
        """
        断言
        :param expect: 预期
        :param actual: 实际
        :param message: 错误消息
        :return:
        """
        assert actual in expect, message
