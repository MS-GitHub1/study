import unittest
from comon.log_handel import logger
from ddt import ddt,data
from DataState.register import login_sj
from interface.register import Inter
@ddt
class Test_Login(unittest.TestCase):
    @data(*login_sj)
    def test_login(self,test_info):
        # msg="O"
        url = "http://120.78.128.25:8766/futureloan"
        c = Inter().login(url=url+test_info["test_url"], body=eval(test_info["test_data"]), headers=eval(test_info["test_header"]))
        logger.info(test_info["test_data"])
        try:
            self.assertEqual(test_info["test_except"],c["msg"])
        except AssertionError as error:
            print(error)
            raise error




