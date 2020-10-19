import requests
import json
from comon.log_handel import logger
class Request:
    def __init__(self,url):
        """
        :param url:  必须传入的url
        """
        self.url = url
    def re_get(self,*args,**kwargs):
        """
        :param args: get请求传入的参数
        :param kwargs:
        :return:
        """
        res = requests.get(self.url,*args,**kwargs)
        return res.text

    def re_post(self,body,*args,**kwargs):
        """
        :param body:  请求体
        :param headers:  请求头，以及其他的内容
        :param kwargs:
        :return:
        """
        res = requests.post(self.url,json.dumps(body),*args,**kwargs)
        return res.text


    def res(self,request,body,*args,**kwargs):
        logger.info("你输入的请求为{}".format(request))
        if request.lower() == "get":

            res = self.re_get(*args,**kwargs)
            return res
        elif request.lower() == "post":
            res = self.re_post(body,*args,**kwargs)
            return res
        else:
            # return '你输入请求error{}'.format(request)
             logger.info('该版本没有您输入这种请求的处理方法{}'.format(request))



if __name__ == '__main__':

    url= "http://120.78.128.25:8766/futureloan/member/register"

    hea = {"Content-Type":'application/json',"X-Lemonban-Media-Type":'lemonban.v2'}

    ti = {"mobile_phone":"13891291198","pwd":"hello1223"}

    R = Request(url)
    c=R.res(request='pot',body=ti,headers=hea)

