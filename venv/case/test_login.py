#coding=utf-8
from handle import excel_handle
from handle import Way_of_request
from cookie_handle import cookie_action
import json
import os
import time
class test_login:
    def __init__(self):
        self.he=excel_handle.Excel_handle()
        self.hw=Way_of_request.Request_ways()
        self.ha=cookie_action.Cookie_handle()
    def test_login(self):
        base_url="https://schooltest.xiaogj.com"
        cur_time = int(round(time.time() * 1000))
        data=self.he.get_rows_value(2)
        case_number,case_name,if_run,pre_condition,request_way,take_header,action_cookie,interface,appid,data,expect_way,expect_value,result,wrong_data,return_data,inherit_element=data
        i=self.he.get_rows()
        url=base_url+interface
        data = data = json.loads(data)
        data["_t_"]=cur_time
        data = json.dumps(data)
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Content-Length": "110",
            "Host": "schooltest.xiaogj.com",
            "User-Agent": "Apache-HttpClient/4.5.12 (Java/1.8.0_251)"
        }
        if if_run=="YES":
            result=self.hw.do_request(url,request_way,data,header=hearder,cookie=None,cookie_location=None)
            cookie=result["token"]
            result=str(result)
            self.he.write_cell_value(2,13,result)
            print(result)
            if action_cookie=="write":
                self.ha.write_cookie("qrz_token",cookie)
        else:
            pass

                
            

if __name__=="__main__":
    test_login().test_login()