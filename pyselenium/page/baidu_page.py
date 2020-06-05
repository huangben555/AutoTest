# from pyselenium.base import BasePage
#
#
#  class BaiduPage(BasePage):
#     def search_input(self, search_key):
#         self.by_id('kw').send_keys(search_key)
#
#     def search_button(self):
#         self.by_id('su').click()

from poium import Page, PageElement, PageElements


class BaiduPage(Page):
    search_input = PageElement(id_='kw', describe='搜索框')
    search_button = PageElement(id_='su', describe='搜素按钮')
    setting = PageElement(link_text='设置', describe='设置下拉框')
    search_setting = PageElement(css='./setpref', describe='搜索设置选项')
    saving_setting = PageElement(css='./prefpanelgo', describe='保存设置')
    search_result = PageElement(xpath='//*[@id="9"]/h3/a', describe='搜索结果')