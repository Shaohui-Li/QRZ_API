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
import datetime
from selenium import webdriver, common
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Add_advanced_clue_communication:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=31)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()

    def test_Add_advanced_clue_communication(self):
        number = self.he.get_rows()  # 获取用例表行数
        communication_date = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        next_communication_date=(datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            intention_list=range(0,6)
            intenion=random.choice(intention_list)
            if case_number == "case_052":
                request_data["commontime"] = communication_date
                request_data["type"] = type
                request_data["clueid"] = id
                request_data["clueadvancedstage"] = clueadvancedstage
                request_data["nextcomtime"]=next_communication_date
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
                if case_number == "case_050":
                    id = result["data"][0]["id"]
                if case_number == "case_046":
                    type=result["data"][1]["id"]
                if case_number=="case_051":
                    clueadvancedstage = result["data"][1]["id"]
                flag = result["result"]["msg"]
                result = json.dumps(result)
                if flag == "成功":
                    self.he.write_cell_value(i, 13, "Pass", sheetname="Add_advanced_clue_communication")
                    self.he.write_cell_value(i, 15, result, sheetname="Add_advanced_clue_communication")
                    flag_value = True
                else:
                    flag_value = False

            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="Add_advanced_clue_communication")
                self.he.write_cell_value(i, 13, "Fail", sheetname="Add_advanced_clue_communication")
                return False
        return flag_value


if __name__ == "__main__":
    if (Add_advanced_clue_communication().test_Add_advanced_clue_communication()):
        print("用例执行成功")
    else:
        print("用例执行成功")
