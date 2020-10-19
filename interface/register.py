from comon.log_handel import logger
from comon.request import Request as RE
import json

class Inter:
    def __init__(self):
        pass

    # 登录接口
    def login(self,url,body,**kwargs):
        url = RE(url)
        res=url.re_post(body,**kwargs)
        return json.loads(res)
    #
    def register (self,url,body,**kwargs):
        url = RE(url)
        res=url.re_post(body,**kwargs)
        return json.loads(res)




# if __name__ == '__main__':
#
#     url= "http://120.78.128.25:8766/futureloan/member/login"
#
#     hea = {"Content-Type":'application/json',"X-Lemonban-Media-Type":'lemonban.v2'}
#
#     ti = {"mobile_phone":"13891291198","pwd":"hello1223"}
#
#     # R = Request(url)
#     # c=R.res(request='pot',body=ti,headers=hea)
#
#     c = Inter().register(url=url,body=ti,headers=hea)
#     print(c)