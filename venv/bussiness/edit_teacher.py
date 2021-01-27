# coding=utf-8
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
from selenium import webdriver, common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class addclue:
    def __init__(self):
        self.he = excel_handle.Excel_handle()
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()
        self.he2 = excel_handle.Excel_handle("D:\project\QRZ_API\\venv\config\\腾飞电话号码.xls")
    

    def test_add_clue(self):
        number = self.he.get_rows(1)
        number1=self.he2.get_rows()
        phone = self.ac.createPhone()  # 生成随机手机号码
        name = self.ac.create_name()  # 生成随机姓名
        # print(name,chardet.detect(name))
        # print(name,chardet.detect(name))
        for b in range(2, number1 + 1):
            data2 = self.he.get_rows_value(b)
        for i in range(2, number + 1):
            base_url = "https://schooltest.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i, 1)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number == "case_003":
                request_data["query"] = employ_name
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
                result = json.dumps(result)
                if flag == "成功":
                    self.he.write_cell_value(i, 13, "Pass", sheetname="add_clue")
                    self.he.write_cell_value(i, 15, result, sheetname="add_clue")
                    return True
            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="add_clue")
                self.he.write_cell_value(i, 13, "Fail", sheetname="add_clue")
                return False


if __name__ == "__main__":
    if (addclue().test_add_clue()):
        print("用例执行成功")
    # Test_addclue().login()
