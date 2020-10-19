import os
import unittest

#  调用测试用例的路径
from datetime import datetime

from configuration.path_config import p
from HTMLTestRunnerNew import HTMLTestRunner

# 测试用例的路径：

# 自动发现测试用例
def zdfx():
    loader = unittest.TestLoader()
    # 自动发现测试用例 传入路径
    suite = loader.discover(p.csyl_path())
    # 设置测试report
    # REPORT_PATH + 时间戳字符串 + 后缀名 .html
    report_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    report_file = os.path.join(p.report(), report_name + '.html')
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(report, verbosity=2)
        runner.run(suite)


zdfx()
