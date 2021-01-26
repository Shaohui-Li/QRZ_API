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

class allot_teacher:
    def __init__(self):
        self.he = excel_handle.Excel_handle(index=12)
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()
    def login(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("https://ischool.xiaogj.com")
        time.sleep(1)
        driver.find_elements_by_class_name("el-input__inner")[0].send_keys("admin@schooltest2")
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys("Qrz888888")
        driver.find_element_by_class_name("entry-login").click()
        WebDriverWait(driver, 20, 0.5).until(EC.element_to_be_clickable(((By.CLASS_NAME, "photo"))))
        fulltime_session = driver.get_cookie("xgj_fulltime_session")["value"]
        # print(sessionid["value"].split("=")[1])
        fulltime_session = "xgj_fulltime_session=" + str(fulltime_session)
        self.ha.write_cookie("cookie", fulltime_session)
        driver.quit()
        return fulltime_session
    def test_allot_teacher(self):
        number = self.he.get_rows(12)#获取用例表行数
        for i in range(2, number + 1):
            base_url = "https://ischool.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i, 2)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            print(data)
            url = base_url + interface
            request_data = json.loads(request_data, encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number=="case_015":
                request_data["ids"][0]=id
            request_data = json.dumps(request_data)
            hearder = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "Host": "ischool.xiaogj.com"
            }
            hearder["Cookie"] = self.login()
            if if_run == "YES":
                result = self.hw.do_request(url, request_way, request_data, header=hearder, cookie=None,
                                            cookie_location=None)
            try:
                print(result)
                if case_number=="case_005":
                    id=result["data"][0]["id"]
                flag = result["result"]["msg"]
                result = json.dumps(result)
                if flag == "成功":
                    self.he.write_cell_value(i, 13, "Pass", sheetname="allot_teacher")
                    self.he.write_cell_value(i, 15, result, sheetname="allot_teacher")
                    flag_value = True
                else:
                    flag_value = False

            except Exception as E:
                self.he.write_cell_value(i, 15, result, sheetname="allot_teacher")
                self.he.write_cell_value(i, 13, "Fail", sheetname="allot_teacher")
                return False
        return flag_value

if __name__=="__main__":
    if (allot_teacher().test_allot_teacher()):
        print("用例执行成功")
    else:
        print("执行失败")
