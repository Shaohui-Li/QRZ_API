#coding=utf-8
from handle import excel_handle
from handle import Way_of_request
from cookie_handle import cookie_action
import json
import os
import time
import unittest
class test_login(unittest.TestCase):
    def setUp(self):
        self.he=excel_handle.Excel_handle()
        self.hw=Way_of_request.Request_ways()
        self.ha=cookie_action.Cookie_handle()
    def test_login(self):
        number=self.he.get_rows(0)
        for i in range(2,number+1):
            base_url="https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data=self.he.get_rows_value(i)
            case_number,case_name,if_run,pre_condition,request_way,take_header,action_cookie,interface,appid,request_data,expect_way,expect_value,result,wrong_data,return_data,inherit_element=data
            url=base_url+interface
            request_data=json.loads(request_data)
            request_data["_t_"]=cur_time
            request_data = json.dumps(request_data)
            hearder = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "Content-Length": "110",
                "Host": "schooltest.xiaogj.com",
                "User-Agent": "Apache-HttpClient/4.5.12 (Java/1.8.0_251)"
            }
            cookie_location={"location": "seesion"}
            if if_run=="YES":
                result=self.hw.do_request(url,request_way,request_data,header=hearder,cookie=None,cookie_location=cookie_location)

            try:
                flag = result["result"]["msg"]
                if flag=="成功":
                    self.he.write_cell_value(i,13,"Pass")
                self.assertEqual("成功",flag)
            except Exception as E:
                self.he.write_cell_value(i, 13, "Fail")
    def tearDown(self):
        print("测试结束")

if __name__=="__main__":
    unittest.main()