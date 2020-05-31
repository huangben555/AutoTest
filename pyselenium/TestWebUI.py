import pytest
from time import sleep
from selenium import webdriver
from pyselenium.page.baidu_page import BaiduPage


def search_key():
    search_list = ('selenium', 'ddt', 'python')
    return search_list


class TestBaidu:

    def setup_class(self):
        self.driver = webdriver.Chrome()

    # def test_baidu_search(self):
    #     page = BaiduPage(self.driver)
    #     page.open('https://wwww.baidu.com')
    #     page.search_input('selenium')
    #     page.search_button()
    #     sleep(2)
    #     assert page.get_title() == 'selenium_百度搜索'

    @pytest.mark.parametrize(argnames='search_key1', argvalues=search_key())
    def test_search(self, test_url, search_key1):
        page = BaiduPage(self.driver)
        page.open(test_url)
        page.search_input(search_key1)
        page.search_button()
        sleep(2)
        assert page.get_title() == search_key1 + '_百度搜索'

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main('-s TestWebUI.py')