from Othermethods.SimplSQL import sql
import unittest
from ddt import ddt,data
# 查询出登录页面中的sql数据
def login_sj():
    qu = 'select * from test_res'
    a=sql.check_all(qu)
    return a


login_sj = login_sj()

#
# @ddt
# class Test(unittest.TestCase):
#     @data(*a)
#     def test_qu(self,test_info):
#         print(test_info["test_data"])

