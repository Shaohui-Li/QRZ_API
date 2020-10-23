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

class Test_addstudent(unittest.TestCase):
    def setUp(self):
        self.he = excel_handle.Excel_handle()
        self.hw = Way_of_request.Request_ways()
        self.ha = cookie_action.Cookie_handle()
        self.ac = action.Action()
    def login(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        driver.get("https://schooltest.xiaogj.com")
        time.sleep(1)
        driver.find_elements_by_class_name("el-input__inner")[0].send_keys("admin@demo")
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys("Qrz888888")
        driver.find_element_by_class_name("entry-login").click()
        WebDriverWait(driver, 20, 0.5).until(EC.element_to_be_clickable(((By.CLASS_NAME,"photo"))))
        fulltime_session = driver.get_cookie("xgj_fulltime_session")["value"]
        # print(sessionid["value"].split("=")[1])
        fulltime_session="xgj_fulltime_session="+str(fulltime_session)
        self.ha.write_cookie("cookie",fulltime_session)
        return fulltime_session
    def test_add_student(self):
        number = self.he.get_rows(3)#获取用例表行数
        phone=self.ac.createPhone()#生成随机手机号码
        name=self.ac.create_name()#生成随机姓名
        id=self.ac.id_number()#生成身份证号码
        # print(name,chardet.detect(name))
        # print(name,chardet.detect(name))
        for i in range(2, number + 1):
            base_url = "https://schooltest.xiaogj.com"
            cur_time = int(round(time.time() * 1000))
            data = self.he.get_rows_value(i,3)
            case_number, case_name, if_run, pre_condition, request_way, take_header, action_cookie, interface, appid, request_data, expect_way, expect_value, result, wrong_data, return_data, inherit_element = data
            url = base_url + interface
            request_data = json.loads(request_data,encoding="utf-8")
            request_data["_t_"] = cur_time
            if case_number == "case_002":
                request_data["baseinfo"]["phone"] = phone
                request_data["baseinfo"]["name"] = name
            if case_number=="case_004":
                clue_id=result["data"][0]["id"]
                processid=result["data"][0]["processid"]
                academicid=result["data"][0]["periodid"]
                campusid=result["data"][0]["campusid"]
                nextprocessnodeid=result["data"][0]["nodebranch"]
                processnodeid=result["data"][0]["processnodeid"]
                processinstanceid=result["data"][0]["processinstanceid"]
                request_data["id"][0]=clue_id
                request_data["processid"]=processid
                request_data["academicid"]=academicid
                request_data["campusid"]=campusid
                if len(nextprocessnodeid)>=2:
                    request_data["nextprocessnodeid"]=nextprocessnodeid[1]["id"]
                else:
                    request_data["nextprocessnodeid"] ="0"
                request_data["processnodeid"]=processnodeid
                request_data["processinstanceid"][0] = processinstanceid
                isPass=1#是否通过  1通过 0不通过
                request_data["isPass"] = isPass
            request_data = json.dumps(request_data)
            if case_number=="case_005":#注意学段id和校区id
                request_data["keyword"]=name
            print(request_data)
            hearder = {
                "Content-Type": "application/json",
                "Connection": "keep-alive",
                "Content-Length": "110",
                "Host": "schooltest.xiaogj.com",
                "User-Agent": "Apache-HttpClient/4.5.12 (Java/1.8.0_251)"
            }
            hearder["Cookie"]=self.login()
            if if_run == "YES":
                result = self.hw.do_request(url, request_way, request_data, header=hearder, cookie=None,
                                cookie_location=None)
                print(result)
            try:
                flag = result["result"]["msg"]
                if flag=="成功":
                    self.he.write_cell_value(i,13,"Pass",sheetname="check_clue")
                self.assertEqual("成功",flag)
            except Exception as E:
                self.he.write_cell_value(i, 13, "Fail",sheetname="check_clue")
    def tearDown(self):
        print("测试结束")
if __name__=="__main__":
    unittest.main()
