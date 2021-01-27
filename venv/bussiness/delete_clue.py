#coding=utf-8
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

class deleteclue:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=6)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()
    
    def test_delete_clue(self):
        number = self.he.get_rows(6)#获取用例表行数
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i, 2)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            print(data)
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number=="case_009":
                request_data["ids"][0]=id
                request_data["listcluesimpleinfo"][0]["id"]=id
                request_data["listcluesimpleinfo"][0]["name"]=name
                request_data["listcluesimpleinfo"][0]["phone"]=phone
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
                print(result)
                if case_number=="case_005":
                    id=result["data"][0]["id"]
                    name=result["data"][0]["name"]
                    phone=result["data"][0]["phone"]
                flag = result["result"]["msg"]
                result = json.dumps(result)
                if flag == "成功":
                    self.he.write_cell_value(i, 13, "Pass", sheetname="delete_clue")
                    self.he.write_cell_value(i, 15, result, sheetname="delete_clue")
                    flag_value = True
                else:
                    flag_value = False

            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="delete_clue")
                self.he.write_cell_value(i, 13, "Fail", sheetname="delete_clue")
                return False
        return flag_value

if __name__=="__main__":
    if (deleteclue().test_delete_clue()):
        print("用例执行成功")
    else:
        print("执行失败")
