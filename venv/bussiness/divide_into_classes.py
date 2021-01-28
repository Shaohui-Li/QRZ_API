# coding=utf-8
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


class divide_into_classes:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=24)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()

    def test_divide_into_classes(self):
        number = self.he.get_rows()  # 获取用例表行数
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number == "case_032":
                request_data["classstudentlist"][0]["classid"] = classid
                request_data["classstudentlist"][0]["studentid"] = studentid
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
                if case_number=="case_030":
                    studentid=result["data"][0]["baseinfo"]["id"]
                if case_number=="case_031":
                    classid=result["data"][0]["classid"]
                result = json.dumps(result)
                if flag == "成功":
                    flag_value=True
                    self.he.write_cell_value(i, 13, "Pass", sheetname="divide_into_classes")
                    self.he.write_cell_value(i, 15, result, sheetname="divide_into_classes")
            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="divide_into_classes")
                self.he.write_cell_value(i, 13, "Fail", sheetname="divide_into_classes")
                return False
        return flag_value

if __name__ == "__main__":
    if (divide_into_classes().test_divide_into_classes()):
        print("用例执行成功")
