import os, sys
import time
import pytest
import click

sys.path.append('C:\\PycharmProjects\\AutoTest')
from pyselenium.conftest import *
from pyselenium.utils.ddt_readCSV import DDT


def init_env(now_time):
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "\\image")


def run():
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    init_env(now_time)
    html_report = os.path.join(REPORT_DIR, now_time, "report.html")
    xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
    option_list = ["--html=" + html_report,
                   "--junit-xml=" + xml_report,
                   "--self-contained-html",
                   "-s", "-v"]
    if 'rerunNum' in os.environ:
        option_list.extend(["--reruns", os.environ['rerunNum']])
    if 'testEnviron' in os.environ:
        option_list.extend(["--cmdopt", os.environ['testEnviron']])
    if 'testCases' in os.environ:
        test_cases_dict = DDT.read_csv_toDict()
        test_cases_list = os.environ['testCases'].replace(' ', '').split(',')
        print('test_cases_list is:', test_cases_list)
        for test_case_name in test_cases_list:
            test_case = test_cases_dict[test_case_name]
            print('test_cases is:', test_case)
            option_list.extend([test_case])
        print('os.environ is:', os.environ['testCases'])
    else:
        pass
    print('option_list is:', option_list)
    pytest.main(option_list)


if __name__ == "__main__":
    run()
