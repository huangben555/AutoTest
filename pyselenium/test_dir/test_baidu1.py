import sys
from time import sleep
from os.path import dirname, abspath

sys.path.append('C:\\PycharmProjects\\AutoTest')

from pyselenium.page.baidu_page import BaiduPage
from pyselenium.conftest import *
from pyselenium.utils.ddt_readCSV import DDT
from pyselenium.utils.db import db

url = 'https://wwww.baidu.com'


@pytest.mark.incremental
class TestSearch:

    # @pytest.mark.parametrize(argnames='search_key1, search_key2',
    #                          argvalues=DDT.read_csv_toList(['parameterIn', 'parameterOut']),
    #                          ids=DDT.read_csv_toList('comments'))
    # @pytest.mark.run(order=3)
    # def test_baidu_search_case1(self, browser, search_key1, search_key2):
    #     page = BaiduPage(browser)
    #     page.get(url)
    #     page.search_input = search_key1
    #     page.search_button.click()
    #     sleep(1)
    #     assert browser.title == search_key2
    #     sleep(1)
    #
    @pytest.mark.run(order=1)
    def test_baidu_search_case2(self, browser, cmdopt):
        """备注"""
        page = BaiduPage(browser)
        page.get(url)
        page.search_input = 'pytest'
        page.search_button.click()
        sleep(1)
        connect, cursor = db.db_connect(cmdopt)
        sql = "INSERT INTO `sign_event` VALUES (3, '华为', 200, 1, '上海佘山', '2020-08-06 18:07:35.000000', '2020-03-01 16:10:34')"
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()
        assert browser.title == 'pytest_百度搜索'
    #
    # @pytest.mark.run(order=2)
    # def test_baidu_search_case3(self, browser):
    #     page = BaiduPage(browser)
    #     page.get(url)
    #     page.search_input = 'jenkins'
    #     page.search_button.click()
    #     sleep(2)
    #     assert browser.title == 'jenkins_百度搜索'


if __name__ == '__main__':
    TestSearch.test_fix_1(cmdopt='db_host')
