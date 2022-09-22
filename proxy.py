# import time
#
# from browsermobproxy import Server
#
# server = Server("/Users/bxcl/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()
# proxy.new_har(options={'captureHeaders': True, 'captureContent': True})
# while True:
#     print(proxy.har)
#     time.sleep(10)
import inspect
import os


def test():
    print(os.path.abspath(os.path.dirname(__file__)))
