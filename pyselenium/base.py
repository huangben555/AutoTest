import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    def get_title(self):
        return self.driver.title