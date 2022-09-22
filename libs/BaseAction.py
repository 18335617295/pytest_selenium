import time

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from libs.Base import Base
from libs.Requests import Requests


class BaseAction(Base):
    click_js = "arguments[0].click();"
    scrollbar_js = "window.scrollTo(0,1000)"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element: tuple, timeout=10, poll_frequency=1):
        """
        :param element: 元素信息 (方式，值)
        :param timeout: 定位超时时间
        :param poll_frequency: 定位时间间隔
        :return: 元素
        """
        try:
            self.log.info(f"开始定位元素：{element}")
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda x: x.find_element(element[0], element[1]))
        except Exception as e:
            self.log.error(e)
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda x: x.find_element(element[0], element[1]))

    def find_elements(self, element: tuple, timeout=10, poll_frequency=1):
        try:
            self.log.info(f"开始定位元素：{element}")
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda x: x.find_elements(element[0], element[1]))
        except Exception as e:
            self.log.error(e)
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                lambda x: x.find_elements(element[0], element[1]))

    def click(self, element: tuple, **kwargs):
        time.sleep(1)
        self.log.info(f"开始点击元素：{element}")
        return self.find_element(element, **kwargs).click()

    def js_click(self, element: tuple, **kwargs):
        self.log.info(f"开始点击元素：{element}")
        return self.execute_script(self.click_js, self.find_element(element, **kwargs))

    def send_keys(self, element: tuple, *keys, **kwargs):
        element = self.find_element(element, **kwargs)
        element.clear()
        self.log.info(f"开始输入按键：{element}")
        return element.send_keys(*keys)

    def get_attribute(self, element: tuple, name, **kwargs):
        """
        根据属性名称获取属性值
        :param element:
        :param name:
        :param kwargs:
        :return:
        """
        return self.find_element(element, **kwargs).get_attribute(name)

    def is_displayed(self, element: tuple, **kwargs):
        """
        :param element: 元素信息 (方式，值)
        :param kwargs:
        :return:
        """
        return self.find_element(element, **kwargs).is_displayed()

    def is_enabled(self, element: tuple, **kwargs):
        """
        :param element:
        :param kwargs:
        :return:
        """
        return self.find_element(element, **kwargs).is_enabled()

    def location(self, element: tuple, **kwargs):
        return self.find_element(element, **kwargs).location()

    def size(self, element: tuple, **kwargs):
        return self.find_element(element, **kwargs).size()

    def text(self, element: tuple, **kwargs):
        return self.find_element(element, **kwargs).text()

    def execute_script(self, *script):
        return self.driver.execute_script(*script)

    def switch_to_window(self, index):
        return self.driver.switch_to.window(self.driver.window_handles[index])

    def switch_to_frame(self, element):
        if isinstance(element, tuple):
            return self.driver.switch_to.frame(self.find_element(element))
        else:
            return self.driver.switch_to.frame(element)


def create_diver(url="", mobile=False):
    if not url:
        url = "https://media.uat.haochezhu.club/mall/index.html#/mainIndex"
    server = Server("/Users/bxcl/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    request = Requests()
    proxy = server.create_proxy()
    mobile_emulation = {'deviceName': 'iPhone X'}
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    # 解决问题不是私密问题
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-urlfetcher-cert-requests')
    if mobile:
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        cookie = request.get_token_to_c().get_dict()
    else:
        cookie = request.get_cookie_to_b().get_dict()
    driver = webdriver.Chrome(chrome_options=options)
    proxy.new_har(options={'captureHeaders': True, 'captureContent': True})
    cookie_dict = {
        'domain': '.haochezhu.club',
        'expiry': int(time.time()) + 10 * 60 * 60,
        'httpOnly': False,
        'name': 'X-PASSPORT-TOKEN',
        'path': '/',
        'sameSite': 'Lax',
        'secure': False,
        'value': '9C877E234BCCD0EEB9AD33CC7260E8E3'
    }
    for k in cookie:
        new_cookie = {"name": k, "value": cookie[k]}
        cookie_dict.update(new_cookie)
    driver.get(url)
    driver.add_cookie(cookie_dict)
    return driver, proxy, server
