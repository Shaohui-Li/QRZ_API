#coding=utf-8
import json
import os
import re
from handle.json_read import Json_read
base_path=os.path.dirname(os.getcwd())
class Cookie_handle:
    def __init__(self):
        self.sj=Json_read()
    def get_cookie(self,cookie_key):
        """获取cookie.json文件中的cookie"""
        data = self.sj.load_json("\\config\\cookie.json")
        return data[cookie_key]
    def write_cookie(self,cookie_key,cookies):
        """往cookie.json文件中写入cookie"""
        filename="\\config\\cookie.json"
        data={}
        data[cookie_key]=cookies
        data=json.dumps(data)
        file_path=base_path+filename
        self.sj.write_json_value(file_path,data)
    def get_request_cookie(self,data):
        """获取接口请求返回结果中的token"""
        cookie=re.search(r'"token":.+?\,',data)
        data=cookie.group().replace(",","")
        data=data.replace("\'","")
        data=data.replace("\"","")
        data=data.split(",")[0]
        # print(data)
        data=data.split(":")
        cookies={}
        #Cookie: tianyuyou_logininfo=a87b14cf3ec9fd3073bf52f7f278c8de
        cookies["tianyuyou_logininfo"]=data[1].strip()
        return cookies
if __name__=="__main__":
    jh=Cookie_handle()
    res={'error': None, 'result': {'data': {'token': '2348d856dc8d17f00ca6638c78a5d81d', 'mem_id': '697099', 'pokergame': '', 'subaccount': []}}, 'debug': {'get': {'config': 'user'}, 'post': {'action': 'user.login\n    ', 'appid': '1\n                   ', 'data': '{"username": "tyyx697099", "password": "123123", "devicecode": "webserver"}'}, 'exectime': 0.060477018356323, 'sql': ["SELECT * FROM `user` Where `username` = 'tyyx697099' ", "INSERT INTO `login_log`  SET `loginName`= 'tyyx697099',`login_time`= 1578290918,`loginIp`= '175.10.24.241',`user_id`= 319700,`mem_id`= 697099,`agent_id`= 0,`app_id`= 1,`imei`= ,`type`= 'webserver',`addres`= '因流量限制改成通过ip查询'", "SELECT id,mobile,status,agent_id,app_id FROM `c_members` Where `uname` = 'tyyx697099' ", 'UPDATE `user` SET `login_time`= 1578290918 Where `id` = 319700 ']}}
    res=json.dumps(res)
    cookie=jh.get_request_cookie(res)
    data3=jh.write_cookie("app",cookie)
    data2=jh.get_cookie("app")
    print(cookie)
    print(data2,data3)