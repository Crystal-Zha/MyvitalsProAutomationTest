import os
import threading
import unittest
import time

import HtmlTestRunner

# 脚本路径
from HtmlTestRunner import HTMLTestRunner

path = os.path.dirname(os.path.realpath(__file__))
# test_cases用例
case_path = os.path.join(path, 'test_cases')


# 执行用例，返回discover
def add_case(rule="test*.py"):
    """
    discover方法查找目录下要执行的测试用例脚本
    .discover方法里面有3个参数：
    case_path:用例所在的目录
    pattern：这个是匹配脚本名称的规则，例如：test*.py意思是匹配所有以test开头的脚本
    top_level_dir：这个是顶级目录的名称，一般默认等于None
    """
    # 如果不存在这个testCases文件夹，就自动创建一个
    if not os.path.exists(case_path): os.mkdir(case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


# 执行报告
def run_case(discover):
    report_path = os.path.join(path, 'report')
    now = time.strftime("%Y-%m-%d-%H-%M-%S")  # 最新的报告
    report_abspath = os.path.join(report_path, now + "result.html")  # 报告位置
    rp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=rp, title="测试报告", description="用例执行的情况")

    runner.run(discover)
    return report_abspath


