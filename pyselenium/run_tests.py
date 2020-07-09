import os, sys
import time
import pytest
import click

sys.path.append('C:\\PycharmProjects\\AutoTest')

from pyselenium.conftest import *


def init_env(now_time):
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "\\image")


def run():
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    init_env(now_time)
    html_report = os.path.join(REPORT_DIR, now_time, "report.html")
    xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
    option_list = ["-s", "-v", cases_path,
                   "--html=" + html_report,
                   "--junit-xml=" + xml_report,
                   "--self-contained-html",
                   "--cmdopt", 'stg2']
    if 'rerunNum' in os.environ:
        option_list.extend(["--reruns", os.environ['rerunNum']])
    else:
        pass
    if 'testCases' in os.environ:
        test_cases_dict = {'测试1': 'test_baidu_search_case1', '测试2': 'test_baidu_search_case2'}
        test_cases_list = os.environ['testCases'].replace(' ', '').split(',')
        test_cases = ''
        for test_case_name in test_cases_list:
            test_case = test_cases_dict[test_case_name]
            test_cases = test_cases + test_case + ', '
            print(test_cases)
            option_list.extend(["-k", os.environ['testCases']])
        print('os.environ is:', os.environ['testCases'])
    else:
        pass
    pytest.main(option_list)


if __name__ == "__main__":
    run()
