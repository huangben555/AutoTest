import sys
from time import sleep
from os.path import dirname, abspath
from pyselenium.page.baidu_page import BaiduPage
from pyselenium.conftest import *
from pyselenium.utils.ddt_readCSV import DDT

url = 'https://wwww.baidu.com'


@pytest.mark.incremental
class TestSearch:

    @pytest.mark.parametrize(argnames='search_key1, search_key2',
                             argvalues=DDT.read_CSV(['parameterIn', 'parameterOut']),
                             ids=DDT.read_CSV('comments'))
    @pytest.mark.run(order=3)
    def test_baidu_search_case1(self, browser, search_key1, search_key2):
        page = BaiduPage(browser)
        page.get(url)
        page.search_input = search_key1
        page.search_button.click()
        sleep(2)
        assert browser.title == search_key2
        sleep(5)

    # @pytest.mark.run(order=1)
    # def test_baidu_search_case2(self, browser):
    #     page = BaiduPage(browser)
    #     page.get(url)
    #     page.search_input = 'selenium'
    #     page.search_button.click()
    #     sleep(2)
    #     assert browser.title == 'selenium_百度搜索'
    #
    # @pytest.mark.run(order=2)
    # def test_baidu_search_case3(self, browser, base_url):
    #     page = BaiduPage(browser)
    #     page.get(url)
    #     page.search_input = 'python'
    #     page.search_button.click()
    #     sleep(2)
    #     assert browser.title == 'python_百度搜索'
