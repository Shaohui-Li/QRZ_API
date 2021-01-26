#coding=utf-8
import warnings
import sys
sys.path.append(r"D:\project\QRZ_API\venv")
from bussiness import Login,add_clue,add_student,add_advanced_clue,add_employee,add_teacher,admit_clue,allot_teacher,check_clue
from bussiness import creat_order,creat_student_order,delete_clue,grab_clue,transfer_to_advanced_clue,transfer_to_advanced_cluepond,transfer_to_cluepond
from bussiness import sign_up_from_PC,sign_up_from_mobile,set_up_second_discount,receive_money,abandon_order,abandon_receipt
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
    def test_addstudent(self):
        result=add_student.addstudent().test_add_student()
        self.assertTrue(result)
    def test_add_advanced_clue(self):
        result = add_advanced_clue.add_advanced_clue().test_add_advanced_clue()
        self.assertTrue(result)
    def test_add_employee(self):
        result = add_employee.add_employee().test_add_employ()
        self.assertTrue(result)
    def test_add_teacher(self):
        result = add_teacher.add_teacher().test_add_teacher()
        self.assertTrue(result)
    def test_admit_clue(self):
        result = admit_clue.admit_clue().test_admit_clue()
        self.assertTrue(result)
    def test_allot_teacher(self):
        result = allot_teacher.allot_teacher().test_allot_teacher()
        self.assertTrue(result)
    def test_check_clue(self):
        result = check_clue.checkclue().test_check_clue()
        self.assertTrue(result)
    def test_creat_clue_order(self):
        result = creat_order.creat_clue_order().test_creat_clue_order()
        self.assertTrue(result)
    def test_creat_student_order(self):
        result = creat_student_order.creat_student_order().test_creat_student_order()
        self.assertTrue(result)
    def test_delete_clue(self):
        result = delete_clue.deleteclue().test_delete_clue()
        self.assertTrue(result)
    def test_grab_clue(self):
        result = grab_clue.grab_clue().test_grab_clue()
        self.assertTrue(result)
    def test_transfer_clue(self):
        result = transfer_to_advanced_clue.transfer_to_advanced_clue().test_transfer_clue()
        self.assertTrue(result)
    def test_transfer_to_advanced_cluepond(self):
        result = transfer_to_advanced_cluepond.transfer_to_advanced_cluepond().test_transfer_to_advanced_cluepond()
        self.assertTrue(result)
    def test_clue_pond(self):
        result = transfer_to_cluepond.transfer_to_clue_pond().test_clue_pond()
        self.assertTrue(result)
    def test_sign_up_from_PC(self):
        result = sign_up_from_PC.sign_up_from_PC().test_sign_up_from_PC()
        self.assertTrue(result)
    def test_sign_up_from_mobile(self):
        result = sign_up_from_mobile.sign_up_from_mobile().test_sign_up_from_mobile()
        self.assertTrue(result)
    def test_set_up_second_discount(self):
        result = set_up_second_discount.set_up_second_discount().test_set_up_second_discount()
        self.assertTrue(result)
    def test_receieve_money(self):
        result = receive_money.receieve_money().test_receieve_money()
        self.assertTrue(result)
    def test_abandon_order(self):
        result = abandon_order.abandon_order().test_abandon_order()
        self.assertTrue(result)
    def abandon_receipt(self):
        result = abandon_receipt.abandon_receipt().test_abandon_receipt()
        self.assertTrue(result)
    def tearDown(self) -> None:
        print("测试结束")


if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test_API("test_login"))
    suite.addTest(Test_API("test_addclue"))
    suite.addTest(Test_API("test_addstudent"))
    suite.addTest(Test_API("test_add_advanced_clue"))
    suite.addTest(Test_API("test_add_employee"))
    suite.addTest(Test_API("test_add_teacher"))
    suite.addTest(Test_API("test_admit_clue"))
    suite.addTest(Test_API("test_allot_teacher"))
    suite.addTest(Test_API("test_check_clue"))
    suite.addTest(Test_API("test_creat_clue_order"))
    suite.addTest(Test_API("test_creat_student_order"))
    suite.addTest(Test_API("test_delete_clue"))
    suite.addTest(Test_API("test_grab_clue"))
    suite.addTest(Test_API("test_transfer_clue"))
    suite.addTest(Test_API("test_transfer_to_advanced_cluepond"))
    suite.addTest(Test_API("test_clue_pond"))
    suite.addTest(Test_API("test_sign_up_from_PC"))
    suite.addTest(Test_API("test_sign_up_from_mobile"))
    suite.addTest(Test_API("test_set_up_second_discount"))
    suite.addTest(Test_API("test_receieve_money"))
    suite.addTest(Test_API("test_abandon_order"))
    suite.addTest(Test_API("abandon_receipt"))
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
