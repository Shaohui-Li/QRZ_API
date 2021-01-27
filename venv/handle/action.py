#coding=utf-8
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(rootPath)
import json
import random
from random import sample
import requests
import time
from cookie_handle.cookie_action import Cookie_handle
class Action:
    def createPhone(self):
        for k in range(10):
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                       "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                       "186", "187", "188", "189"]
            phone=random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
            return phone
    def GBK2312(self):
        # 随机生成名字最后一个字
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        last_name = bytes.fromhex(val).decode('gb2312')
        return last_name

    def create_name(self):  # 随机生成名字
        first_name_list = [
            '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
            '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
            '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
            '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
            '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
            '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
            '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        n = random.randint(0, len(first_name_list) - 1)
        first_name = first_name_list[n]
        # 随机取数组中字符，取到空字符则没有second_name
        second_name_list = [self.GBK2312(), '']
        n = random.randint(0, 1)
        second_name = second_name_list[n]
        last_name=self.GBK2312()
        name = first_name + second_name + last_name
        return name
    def id_number(self):
        number = ("".join(random.choice("0123456789") for i in range(2)))
        id=number + (str(round(time.time() * 10000)))
        return id
    def creat_sutdent_id(self):
        '''生成身份证前六位,n目前时湖南身份证号'''
        first_list = ["430000","430100","430101","430102","430103","430104","430105","430111","430121","430122","430124","430181","430200","430201","430202","430203","430204","430211","430221","430223","430224","430225","430281","430300","430301","430302","430304","430321","430381","430382","430400","430401","430405","430406","430407","430408","430412","430421","430422","430423","430424","430426","430481","430482","430500","430501","430502","430503","430511","430521","430522","430523","430524","430525","430527","430528","430529","430581","430600","430601","430602","430603","430611","430621","430623","430624","430626","430681","430682","430700","430701","430702","430703","430721","430722","430723","430724","430725","430726","430781","430800","430801","430802","430811","430821","430822","430900","430901","430902","430903","430921","430922","430923","430981","431000","431001","431002","431003","431021","431022","431023","431024","431025","431026","431027","431028","431081","431100","431101","431102","431103","431121","431122","431123","431124","431125","431126","431127","431128","431129","43100","431201","431202","431221","431222","431223","431224","431225","431226","431227","431228","431229","431230","431281","431300","431301","431302","431321","431322","431381","431382","433100","433101","433122","433123","433124","433125","433126","433127","433130"]
        first = random.choice(first_list)
        '''生成年份'''
        now = time.strftime('%Y')
        # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(2002,int(now) - 13)
        '''生成月份'''
        three = random.randint(1, 12)
        # 月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
        '''生成日期'''
        four = random.randint(1, 28)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
        '''生成身份证后四位'''
        # 后面序号低于相应位数，前面加上0填充
        five = random.randint(1, 9999)
        if five < 10:
            five = '000' + str(five)
        elif 10 < five < 100:
            five = '00' + str(five)
        elif 100 < five < 1000:
            five = '0' + str(five)
        IDcard = str(first) + str(second) + str(three) + str(four) + str(five)
        return IDcard
    def creat_parents_id(self):
        '''生成身份证前六位,n目前时湖南身份证号'''
        first_list = ["430000","430100","430101","430102","430103","430104","430105","430111","430121","430122","430124","430181","430200","430201","430202","430203","430204","430211","430221","430223","430224","430225","430281","430300","430301","430302","430304","430321","430381","430382","430400","430401","430405","430406","430407","430408","430412","430421","430422","430423","430424","430426","430481","430482","430500","430501","430502","430503","430511","430521","430522","430523","430524","430525","430527","430528","430529","430581","430600","430601","430602","430603","430611","430621","430623","430624","430626","430681","430682","430700","430701","430702","430703","430721","430722","430723","430724","430725","430726","430781","430800","430801","430802","430811","430821","430822","430900","430901","430902","430903","430921","430922","430923","430981","431000","431001","431002","431003","431021","431022","431023","431024","431025","431026","431027","431028","431081","431100","431101","431102","431103","431121","431122","431123","431124","431125","431126","431127","431128","431129","43100","431201","431202","431221","431222","431223","431224","431225","431226","431227","431228","431229","431230","431281","431300","431301","431302","431321","431322","431381","431382","433100","433101","433122","433123","433124","433125","433126","433127","433130"]
        first = random.choice(first_list)
        '''生成年份'''
        now = time.strftime('%Y')
        # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(1980, int(now) -30)
        '''生成月份'''
        three = random.randint(1, 12)
        # 月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
        '''生成日期'''
        four = random.randint(1, 28)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
        '''生成身份证后四位'''
        # 后面序号低于相应位数，前面加上0填充
        five = random.randint(1, 9999)
        if five < 10:
            five = '000' + str(five)
        elif 10 < five < 100:
            five = '00' + str(five)
        elif 100 < five < 1000:
            five = '0' + str(five)
        IDcard = str(first) + str(second) + str(three) + str(four) + str(five)
        return IDcard
    def Student_code(self):
        all_char = 'QAZWSXEDCRFVTGBYHNUJMIKOLPQAZWSXEDCRFVTGBYHNUJIKOLP'
        pre=sample(list(all_char),2)
        all_number="1234567890"
        five = random.randint(9999, 999999)
        return pre[0]+pre[1]+str(five)
    def Login(self):
        sees=requests.Session()

        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Host": "ischool.xiaogj.com"
        }
        cookie_location = {"location": "seesion"}
        url = "https://ischool.xiaogj.com/Pc.do?appid=1&action=login"
        request_data={'username': 'shaohui1@schooltest2', 'password': '123456', 'website': 'https://ischool.xiaogj.com', '_t_': 1611714114332}
        request_data = json.dumps(request_data)
        request_data = json.loads(request_data, encoding="utf-8")
        print(request_data)
        cur_time = int(round(time.time() * 1000))
        request_data["_t_"] = cur_time
        request_data = json.dumps(request_data)
        result = sees.post(url, data=request_data,headers=hearder, cookies=None)#登录接口
        result=result.text
        result = json.loads(result)
        print(result)
        authurl = result["authurl"]
        website = result["website"]
        token = result["token"]
        flag = result["result"]["msg"]
        if flag == "成功":
            flag_value = True
        returl = "&returl=https%3A%2F%2Fschooltest.xiaogj.com%2Findex.html"
        url = authurl + "?appid=1&website=" + website + "&auth_token="+token
        print(url)
        result=requests.head(url)
        # result = sees.post(url, cookies=None,
        #                   verify=False,allow_redirects=True)  # 重定向sso
        print(result)
        print(result.headers["Location"])
        url=result.headers["Location"]
        qrz_session="xgj_fulltime_session=session_Id="+url.split("=")[4]
        Cookie_handle().write_cookie(cookie_location["location"], qrz_session)
        # result = sees.post(url, data=request_data, headers=hearder, cookies=None)
        # print(result.headers)
    ##判断是否登录
    def is_login(self):
        sees = requests.Session()
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Host": "ischool.xiaogj.com"
        }
        url="http://ischool.xiaogj.com/Pc.do?appid=1&action=islogin"
        cookie = Cookie_handle().get_cookie("seesion")
        hearder["Cookie"] = cookie
        cur_time = int(round(time.time() * 1000))
        request_data={}
        request_data["_t_"] = cur_time
        try:
            result = sees.post(url, data=request_data, headers=hearder, cookies=None)
            result = result.text
            result = json.loads(result)
            flag = result["result"]["code"]
        except Exception as E:
            print(E)
            return False
        if flag ==20017:
            return True
        else:
            return False
if __name__=="__main__":

    # print(Action().createPhone())
    # print(Action().create_name())
    Action().Login()
    if(Action().is_login()):
        print("登录成功")
    else:
        print("登录失败")
