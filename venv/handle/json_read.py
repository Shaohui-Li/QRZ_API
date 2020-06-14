#coding=utf-8
import json
import os
# from deepdiff import DeepDiff
base_path=os.path.dirname(os.getcwd())
class Json_read:
    def load_json(self,file_name=None):
        if file_name==None:
            file_path=base_path+"\\config\\cookie.json"
        else:
            file_path=base_path+file_name
        with open(file_path,encoding="utf-8") as f:
            data=json.load(f)
        return data
    def get_url_value(self,key,file_name=None):
        data=self.load_json(file_name)
        return data.get(key)
    def get_element_value(self,key,element,file_name=None):
        data=self.get_url_value(key,file_name)
        if data !=None:
            for i in data:
                code_value=i.get(str(element))
                if code_value!=None:
                    return code_value
        return None
    def check_jsonvalue(self,dict1,dict2):
        cmd_res = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmd_res.get("dictionary_item_added"):
            return False
        else:
            return True
    def write_json_value(self,filepath,data):
        with open(filepath,"w") as f:
            f.write(data)
if __name__=="__main__":
    js=Json_read()
    # a=js.load_json("/cofig/fiddler_data.json")
    b=js.load_json("/cofig/fiddler_data2.json")
    print(js.get_url_value("action=usercenter.index&appid=3","/cofig/mitmdata.json"))
