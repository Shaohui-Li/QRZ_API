#coding=utf-8
import sys
sys.path.append(r"D:\project\quanrizhi\venv\lib\site-packages")
sys.path.append(r"D:\project\quanrizhi\venv\config")
import json
import requests
requests.packages.urllib3.disable_warnings()
from cookie_handle.cookie_action import Cookie_handle
class Request_ways():
    def __init__(self):
        self.sess = requests.Session()
    """封装接口请求  cookie_location表示cookie是web还是app"""
    def post_url(self,url,data,cookie,cookie_location,header=None):
        response=self.sess.post(url,data=data,cookies=cookie,headers=header,verify=False)
        if cookie_location!=None:
            cookie_data=response.cookies
            cook_value=requests.utils.dict_from_cookiejar(self.sess.cookies)
            Cookie_handle().write_cookie(cookie_location["location"],cook_value)
        res = response.text
        return res
    def get_url(self,url,data,cookie,cookie_location,header=None):
        response=self.sess.get(url,params=data,cookies=cookie,headers=header,verify=False)
        if cookie_location!=None:
            cookie_data=response.cookies
            cook_value=requests.utils.dict_from_cookiejar(cookie_data)
            Cookie_handle().write_cookie(cookie_location["location"],cook_value)
        res=response.text
        return res
    def do_request(self,url,method,data,cookie=None,cookie_location=None,header=None):
        if method=="POST":
            res=self.post_url(url,data,cookie,cookie_location,header)
        elif method=="GET":
            res=self.get_url(url,data,cookie,cookie_location,heade)
        try:
            res=json.loads(res)
        except:
            print(res)
            print("内容不是json格式")
        return res