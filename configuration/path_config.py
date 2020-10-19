from os.path import *
import os
class Path:
    # 配置文件路径
    def con_path(self):
        path = dirname(dirname(abspath(__file__)))
        config_path = os.path.join(path+'/configuration/seeting.ini')
        return config_path

    # 测试用例的路径设置
    def csyl_path(self):
        path = dirname(dirname(abspath(__file__)))
        csyl_path = os.path.join(path+'/test')
        return csyl_path

    # 测试报告路径
    def report(self):
        path = dirname(dirname(abspath(__file__)))
        report_path = os.path.join(path+'/report')
        return report_path


p = Path()





if __name__ == '__main__':
    print(p.con_path())
    print(p.csyl_path())
    print(p.report())