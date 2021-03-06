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

class checkclue:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=4)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()
    
    def test_check_clue(self):
        number = self.he.get_rows()#获取用例表行数
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number=="case_006":
                request_data["id"][0]=id
                request_data["processid"]=processid
                request_data["campusid"]=campusid
                request_data["nextprocessnodeid"]=nextprocessnodeid
                request_data["processnodeid"]=processnodeid
                request_data["processinstanceid"][0]=processinstanceid
            if case_number=="case_007":
                request_data["id"][0] = id
                request_data["processid"] = processid
                request_data["campusid"] = campusid
                request_data["nextprocessnodeid"] = "0"
                request_data["processnodeid"] = nextprocessnodeid
                request_data["processinstanceid"][0] = processinstanceid
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
                if case_number=="case_005":
                    id=result["data"][0]["id"]
                    processid=result["data"][0]["processid"]
                    campusid=result["data"][0]["campusid"]
                    nextprocessnodeid=result["data"][0]["nodebranch"][2]["processnodebranchid"]
                    processnodeid=result["data"][0]["nodebranch"][2]["processnodeid"]
                    processinstanceid=result["data"][0]["processinstanceid"]

                flag = result["result"]["msg"]
                result = json.dumps(result)
                if flag == "成功":
                    self.he.write_cell_value(i, 13, "Pass", sheetname="check_clue")
                    self.he.write_cell_value(i, 15, result, sheetname="check_clue")
                    flag_value = True
                else:
                    flag_value = False

            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="check_clue")
                self.he.write_cell_value(i, 13, "Fail", sheetname="check_clue")
                return False
        return flag_value

if __name__=="__main__":
    if (checkclue().test_check_clue()):
        print("用例执行成功")
