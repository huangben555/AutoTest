import os, sys
import time
import pytest
import click

sys.path.append('C:\\PycharmProjects\\AutoTest')

from pyselenium.conftest import *


def init_env(now_time):
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "\\image")


# @click.command()
# @click.option('-m', default=None, help='输入运行模式：run 或 debug.')
# def run(m):
#     if m is None or m == "run":
#         now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
#         init_env(now_time)
#         html_report = os.path.join(REPORT_DIR, now_time, "report.html")
#         xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
#         pytest.main(["-s", "-v", cases_path,
#                     "--html=" + html_report,
#                     "--junit-xml=" + xml_report,
#                     "--self-contained-html",
#                     "--reruns", rerun])
#     elif m == "debug":
#         pytest.main(["-v", "-s", cases_path])


if __name__ == "__main__":
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    init_env(now_time)
    html_report = os.path.join(REPORT_DIR, now_time, "report.html")
    xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
    pytest.main(["-s", "-v", cases_path,
                 "--html=" + html_report,
                 "--junit-xml=" + xml_report,
                 "--self-contained-html",
                 "--reruns", rerun,
                 "-n", "3",
                 "--cmdopt", 'stg2'])
