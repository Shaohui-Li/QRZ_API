from handle import Way_of_request
import time
import json
from cookie_handle import cookie_action
class QRZ_login:

    def __init__(self):
        self.Rw=Way_of_request.Request_ways()
        self.ca=cookie_action.Cookie_handle()
    def login(self):
        url = "https://schooltest.xiaogj.com/Pc.do?appid=1&action=login"
        cur_time = int(round(time.time()*1000))
        hearder = {
            "Content-Type":"application/json",
            "Connection":"keep-alive",
            "Content-Length" : "110",
            "Host":"schooltest.xiaogj.com",
            "User-Agent":"Apache-HttpClient/4.5.12 (Java/1.8.0_251)"
        }
        user_info= {"_t_":cur_time,"username":"admin@schooldevp","password":"Qrz888888","website":"https://schooltest.xiaogj.com"}
        data=json.dumps(user_info)
        data2=self.Rw.post_url(url,data,header=hearder,cookie="",cookie_location="")
        print(data2)
        print(json.loads(data2)["token"])
    def add_clue(self):
        url="https://schooltest.xiaogj.com/Pc.do?appid=1&action=addcluestudent"
        cur_time = int(round(time.time() * 1000))
        cookie = self.ca.get_cookie("qrz_token")
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Host": "schooltest.xiaogj.com",
            "User-Agent": "Apache-HttpClient/4.5.12 (Java/1.8.0_251)",
            "Cookie":"xgj_fulltime_session=session_Id=f0b80f7a30bd15abbe93846bfa43c628%2458bfb06fda9b469e952269ae4af2dd4c"
        }
        user_info = {"_t_":cur_time,"baseinfo":{"campusid":"46228750007005","id":"","name":"小灰灰","sex":{"id":""},"phone":"17342245353","birthday":"","nationality":{"id":"","value":""},"nation":{"value":"","id":""},"idtype":{"value":"","id":""},"cardid":"","govstudentid":"","avatar":"","status":1,"areacode":"+86","nodebranch":[]},"recruitinfo":{"startschoolway":{"id":"","value":""},"majorid":"","nowschool":"","nowgrade":{"value":"","id":""},"postgrade":{"value":"","id":"1002280018888"},"hopetime":"","recommender":"","recommendername":"","semester":{"value":"","id":""},"cluestatus":{"value":"","id":""},"cluecategory":{"value":"","id":""},"employee":{"value":"","id":""},"teacherName":"","intention":0,"datafrom":{"value":"","id":""},"cluestudentid":"","createuser":{"value":"","id":""},"createtime":""},"familyinfos":[{"name":"","areacode":"+86","appellation":{"id":""},"phone":"","education":{"value":"","id":""},"workin":"","jobname":"","nativeplace":"","email":""}],"otherinfo":{"health":{"value":"","id":""},"allergy":"","register":{"province":{"value":"","id":""},"city":{"value":"","id":""},"area":{"value":"","id":""},"address":""},"relation":{"value":"","id":""},"resident":{"province":{"value":"","id":""},"city":{"value":"","id":""},"area":{"value":"","id":""},"address":""},"isstay":0,"likes":"","report":"","focus":"","hope":"","remark":"","clueimginfo":[],"cluestudentid":""},"cluestudentcustfieldinfo":[{"name":"Field6","fieldname":"申请课程","value":"","valuename":"","type":1,"fieldtype":4}]}
        data=json.dumps(user_info)
        data2 = self.Rw.post_url(url, data, header=hearder, cookie=None, cookie_location=None)
        print(data2)
if __name__=="__main__":
    QRZ_login().add_clue()