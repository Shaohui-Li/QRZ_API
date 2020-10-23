#coding=utf-8
import requests
import json
import pdfkit
import datetime,time
import wkhtmltopdf
import sys
import os
import base64
import hashlib
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
class Reboat_request():
    def reboat_markdown_test(self,case_number=None,success_number=None,fail_number=None):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": "测试执行用例总数：<font color='comment'>%s</font>例；\n"
                           "执行成功用例数：<font color='info'>%s</font>例；\n"
                           "执行失败用例数: <font color='warning'>%s</font>例。"%(case_number,success_number,fail_number)
            }
        }
        request_data = json.dumps(data)
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",

        }
        result = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99",
            data=request_data, headers=hearder)
        return print(result)
    def reboat_upload_file(self,filename):
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=c1d60a22-b682-493e-839c-5dd8bcc30d99&type=file"
        hearder = {
            "Content-Type": "multipart/form-data",
            "Connection": "keep-alive",
            "Content-Length": "220",
        }
        files = {'file': open(filename, 'rb')}
        # data={
        #     "Content-Disposition": "form-data",
        #     "filelength": "6",
        #     "name": "media",
        #     "file_name": "D:/project/quanrizhi/venv/case/report.html",
        #     "Content - Type": "application / octet - stream",
        # }
        # request_data = json.dumps(data)
        result = requests.post(url,files=files,headers=hearder).text
        print(result)
        result=json.loads(result)
        media_id=result["media_id"]
        return media_id
    def reboat_fileadress(self,media_id):
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99"
        data={
            "msgtype": "file",
            "file": {
            "media_id": "%s"%(media_id)
                    },
            }
        hearder = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
        }
        request_data = json.dumps(data)
        result=requests.post(url,data=request_data,headers=hearder).text
        return result
    def html_to_pdf(self,filename):
        report_date = datetime.datetime.now().strftime("%Y{y}%m{m}%d{d}%H{h}%M{s}").format(y="年",m="月",d="日",h="时",s="秒",)
        report_name = report_date + "冒烟报告.pdf"
        report_path=filename.split("\\")
        report_path.pop(5)
        report_path.pop(4)
        report_path="/".join(report_path)+"/Report/"+report_name
        config = pdfkit.configuration(wkhtmltopdf=r'D:\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdfkit.from_file(filename, report_path,configuration=config)
            # css = ['static/css/main.css']
        return report_path
    def html_to_img(self,filename):
        try:
            report_date = datetime.datetime.now().strftime("%Y{y}%m{m}%d{d}%H{h}%M{s}").format(y="年", m="月", d="日",
                                                                                               h="时",
                                                                                               s="秒", )
            report_name = report_date + "冒烟报告.jpg"
            report_path = filename.split("\\")
            report_path.pop(5)
            report_path.pop(4)
            report_path = "/".join(report_path) + "/Report/" + report_name
            config = pdfkit.configuration(wkhtmltopdf=r'D:\wkhtmltox\bin\wkhtmltoimage.exe')
            pdfkit.from_file(filename, report_path, configuration=config)
            return report_path
        except Exception as e:
            return report_path
    def upload_img(self,file_name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c1d60a22-b682-493e-839c-5dd8bcc30d99"
        # report_date = datetime.datetime.now().strftime("%Y{y}%m{m}%d{d}%H{h}%M{s}").format(y="年", m="月", d="日", h="时",                                                                                 s="秒", )
        # report_name = report_date + "冒烟报告"
        hearders = {"Content-Type": "application/json"}
        with open(file_name, 'rb') as f:
            data = f.read()
            encodestr = base64.b64encode(data)
            image_data = str(encodestr, 'utf-8')
        with open(file_name, 'rb') as file:  # 图片的MD5值
            md = hashlib.md5()
            md.update(file.read())
            image_md5 = md.hexdigest()
        data = {
            "msgtype": "image",
            "image":{
                        "base64":image_data,
                        "md5": image_md5
                     }
                }
        request_data = json.dumps(data)
        result = requests.post(url, data=request_data, headers=hearders).text
        return result
    def reboat_upload_img(self, filename):
        url="https://fs.xiaogj.com/FileService"
        files = {'file': open(filename, 'rb')}
        hearder = {
            "Content-Type": "multipart/form-data;boundary = ----WebKitFormBoundaryHtTMWAtarPYy17vx",

            "Connection": "keep-alive",
        }
        timestamp = int(time.time())
        url1='https://schooltest.xiaogj.com/Pc.do?appid=1&action=getuploadtoken'
        data1={'timestamp': timestamp}
        request_data=json.dumps(data1)
        result=requests.post(url1,data=request_data).text
        return result

        params = {
            'timestamp': timestamp,
            'nonceStr': '62lhAiWdY3siWo4a',
            'apikey': 'ba97cc58-6b24-42df-96fd-c952e9f7d629',
            'signature': 'db855c4acc01f096c0c39f226583c471',
            'eventId':''
        }
        result = requests.post(url, files=files,params=params, headers=hearder).text
        print(result)


if __name__=="__main__":
    # print(Reboat_request().reboat_fileadress(media_id))
    # file_name="D:\project\quanrizhi\\venv\Report\\10-15_23-52-01全日智冒烟测试结果.html"
    file_name="D:\project\quanrizhi\\venv\Report\\10-16_16-55-21全日智冒烟测试结果.html"
    # report_path = file_name.split("\\")
    # report_path.pop(5)
    # report_date = datetime.datetime.now().strftime( "%Y-%m-%d %H:%M")
    # report_name = "/"+report_date + ".docx"
    # report_path="/".join(report_path)+report_name
    # print(report_path)
    # Reboat_request().reboat_test(10, 8, 2)
    # media_id = Reboat_request().reboat_upload_file(file_name)
    path=Reboat_request().html_to_img(file_name)
    print(Reboat_request().upload_img(path))
    