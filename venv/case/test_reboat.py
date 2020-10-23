from handle import excel_handle
from handle import Way_of_request
from cookie_handle import cookie_action
from handle import action
import json
import os
import time
import unittest
import random
class test_reboat():
    def __init__(self):
        self.hw = Way_of_request.Request_ways()
    def reboat_test(self):
        data={
        "msgtype": "markdown",
        "markdown": {
                "content": "测试执行用例总数：<font color='comment'>XX</font>例；\n"
                           "执行成功用例数：<font color='info'>XX</font>例；\n"
                           "执行失败用例数: <font color='warning'>XX</font>例。"
        }
   }
        request_data = json.dumps(data)
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            
        }
        result=self.hw.do_request("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99","POST",data=request_data,header=hearder)
        return print(result)
if __name__=="__main__":
    test_reboat().reboat_test()