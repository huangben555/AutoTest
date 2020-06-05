# import sys
# from time import sleep
# from os.path import dirname, abspath
# from pyselenium.page.baidu_page import BaiduPage
# from pyselenium.conftest import *
#
#
# class TestSearch:
#     @pytest.mark.run(order=2)
#     def test_baidu_search_case1(self, browser, base_url):
#         page = BaiduPage(browser)
#         page.get(base_url)
#         page.search_input = 'request'
#         page.search_button.click()
#         sleep(2)
#         assert browser.title == 'request_百度搜索'
#
#     @pytest.mark.run(order=3)
#     def test_baidu_search_case2(self, browser, base_url):
#         page = BaiduPage(browser)
#         page.get(base_url)
#         page.search_input = 'http'
#         page.search_button.click()
#         sleep(2)
#         assert browser.title == 'http_百度搜索'
#
#     @pytest.mark.run(order=1)
#     def test_baidu_search_case3(self, browser, base_url):
#         page = BaiduPage(browser)
#         page.get(base_url)
#         page.search_input = 'django'
#         page.search_button.click()
#         sleep(2)
#         assert browser.title == 'django_百度搜索'
