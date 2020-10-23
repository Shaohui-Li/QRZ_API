#coding=utf-8
import warnings
import sys
sys.path.append(r"D:\project\QRZ\venv")
from bussiness import Login,add_clue
import HTMLTestRunner
import os
from handle import reboat_request
import time
import datetime
import unittest

class Test_API(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print("测试开始")
        
    def test_login(self):
        result=Login.Login().login()
        self.assertTrue(result)
    def test_addclue(self):
        result=add_clue.addclue().test_add_clue()
        self.assertTrue(result)
    def tearDown(self) -> None:
        print("测试结束")


if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_API("test_login"))
    suite.addTest(Test_API("test_addclue"))
    time_name=str(time.strftime("%m-%d_%H-%M-%S", time.localtime())).strip(" ")
    report_name=time_name+"全日智API冒烟测试结果.html"
    report_path = os.path.dirname(os.getcwd()) + "\\Report\\"+report_name
    picture_name = datetime.datetime.now().strftime("%Y{y}%m{m}%d{d}").format(y="年", m="月", d="日", )
    report_picture = picture_name +"API冒烟报告"
    with open(report_path,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title=report_picture,description="全日智API测试报告")
        result=runner.run(suite)
        print(result)
    f.close()
    piture_path=reboat_request.Reboat_request().html_to_img(report_path)
    reboat_request.Reboat_request().upload_img(piture_path)
    reboat_request.Reboat_request().reboat_upload_file(report_path)
    media_id = reboat_request.Reboat_request().reboat_upload_file(report_path)
    reboat_request.Reboat_request().reboat_fileadress(media_id)
