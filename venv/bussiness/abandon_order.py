#coding=utf-8
import sys
sys.path.append(r"D:\project\QRZ_API\venv")

from handle import excel_handle
from handle import Way_of_request
from cookie_handle import cookie_action
from handle import action
import json
import os
import time
import unittest
import random
from selenium import  webdriver,common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class abandon_order:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=20)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac=action.Action()
    def test_abandon_order(self):
        number = self.he.get_rows()
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data,encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number=="case_025":
                request_data["orderid"]=order_id
            request_data = json.dumps(request_data)
            hearder = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "Host": "ischool.xiaogj.com"
            }
            if if_run == "YES":
                result = self.hw.do_request(url, request_way, request_data, header=hearder, cookie=None,
                                take_headers=take_header)
            try:
                print(case_name)
                flag = result["result"]["msg"]
                if case_number=="case_021":
                    order_id=result["data"][0]["id"]
                result=json.dumps(result)
                if flag=="成功":
                    flag_value=True
                    self.he.write_cell_value(i,13,"Pass",sheetname="abandon_order")
                    self.he.write_cell_value(i,15,result,sheetname="abandon_order")
            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="abandon_order")
                self.he.write_cell_value(i, 13, "Fail",sheetname="abandon_order")
                return False
        return flag_value

if __name__=="__main__":
    if(abandon_order().test_abandon_order()):
        print("用例执行成功")
    else:
        print("用例执行失败")