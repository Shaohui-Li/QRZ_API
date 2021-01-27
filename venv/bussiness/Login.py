#coding=utf-8
import sys
sys.path.append(r"D:\project\QRZ_API\venv")
from handle import excel_handle
from handle import Way_of_request
from cookie_handle import cookie_action
import json
import time

class Login:
    def __init__(self):
        self.he = excel_handle.Excel_handle()
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
    def login(self):
        number = self.he.get_rows(0)
        returl="https%3A%2F%2Fschooltest.xiaogj.com%2Findex.html"
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data)
            request_data["_t_"] = cur_time   
            print(url,request_data)
            print(request_data)
            request_data = json.dumps(request_data)
            hearder = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "Host": "ischool.xiaogj.com"
            }
            cookie_location = {"location": "seesion"}
            if if_run == "YES":
                result = self.hw.do_request(url, request_way, request_data, header=hearder, cookie=None,
                                            take_headers=take_header)
            try:

                print("result=",result)
                flag = result["result"]["msg"]
                if flag == "成功":
                    flag_value=True
                    self.he.write_cell_value(i, 13, "Pass")
            except Exception as E:
                print(E)
                self.he.write_cell_value(i, 13, "Fail")
                return False
        return flag_value


if __name__=="__main__":
    if(Login().login()):
        print("登录执行成功")