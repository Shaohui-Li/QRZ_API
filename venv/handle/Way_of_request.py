#coding=utf-8
import sys
sys.path.append(r"D:\project\quanrizhi\venv\lib\site-packages")
sys.path.append(r"D:\project\quanrizhi\venv\config")
import json
import requests
requests.packages.urllib3.disable_warnings()
from cookie_handle.cookie_action import Cookie_handle
from handle.action import Action
class Request_ways():
    def __init__(self):
        self.ac=Action()
        self.sess = requests.Session()
    """封装接口请求  cookie_location表示cookie是web还是app"""
    def post_url(self,url,data,cookie,take_headers,header=None):
        if take_headers!=None:
            if self.ac.is_login():
                header["Cookie"]=Cookie_handle().get_cookie("seesion")
            else:
                self.ac.Login()
                header["Cookie"]=Cookie_handle().get_cookie("seesion")
        else:
            pass
        response=self.sess.post(url,data=data,cookies=cookie,headers=header,verify=False)
        res = response.text
        return res
    def get_url(self,url,data,cookie,take_headers,header=None):
        if take_headers!=None:
            if self.ac.is_login():
                header["Cookie"] = Cookie_handle().get_cookie("seesion")
            else:
                self.ac.Login()
                header["Cookie"] = Cookie_handle().get_cookie("seesion")
        else:
            pass
        response=self.sess.get(url,params=data,cookies=cookie,headers=header,verify=False,allow_redirects=True)
        res=response.text
        return res
    def do_request(self,url,method,data,cookie=None,take_headers=None,header=None):
        if method=="POST":
            res=self.post_url(url,data,cookie,take_headers,header)
        elif method=="GET":
            res=self.get_url(url,data,cookie,take_headers,header)
        try:
            res=json.loads(res)
        except:
            print(res)
            print("内容不是json格式")
        return res