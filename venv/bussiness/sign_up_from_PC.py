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

class sign_up_from_PC:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=16)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac=action.Action()
    
    def test_sign_up_from_PC(self):
        number = self.he.get_rows(16)
        phone=self.ac.createPhone()#生成随机手机号码
        name=self.ac.create_name()#生成随机姓名
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i,1)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data,encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number=="case_019":
                request_data["baseinfo"]["phone"]=phone
                request_data["baseinfo"]["name"]=name
                request_data["familyinfos"][0]["name"]="全日智API父亲姓名"
                request_data["familyinfos"][1]["name"] = "全日智API母亲姓名"
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
                flag = result["result"]["msg"]
                result=json.dumps(result)
                if flag=="成功":
                    self.he.write_cell_value(i,13,"Pass",sheetname="sign_up_from_pc")
                    self.he.write_cell_value(i,15,result,sheetname="sign_up_from_pc")
                    return True
            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="sign_up_from_pc")
                self.he.write_cell_value(i, 13, "Fail",sheetname="sign_up_from_pc")
                return False

if __name__=="__main__":
    if(sign_up_from_PC().test_sign_up_from_PC()):
        print("用例执行成功")
