from handle import excel_handle
import openpyxl
import os
from handle import action
import random
base_path=os.path.dirname(os.getcwd())
class Name_tel:
    def __init__(self):
        self.ac = action.Action()
        self.he = excel_handle.Excel_handle("\config\\name_tel.xlsx")
    def name_teacher(self):
        for i in range(1,100):
            phone = self.ac.createPhone()  # 生成随机手机号码
            name = self.ac.create_name()
            self.he.write_cell_value(i,1,name,"Sheet1")
            self.he.write_cell_value(i,2,phone,"Sheet1")
    def test_add_clue(self):
        for i in range(2,4502):
            phone = self.ac.createPhone()  # 生成随机手机号码
            name = self.ac.create_name()
            father_name=self.ac.create_name()
            mother_name=self.ac.create_name()
            father_phone=self.ac.createPhone()
            mother_phone=self.ac.createPhone()
            student_id_card = self.ac.creat_sutdent_id()  # 生成身份证号
            mother_id_card=self.ac.creat_parents_id()#妈妈身份证号
            father_id_card=self.ac.creat_parents_id()#父亲身份证号
            id_type_list1 = ["博士", "硕士", "本科", "专科", "高中", "初中", "小学", "其他"]
            mother_id_type=random.choice(id_type_list1)
            id_type_list2 = ["博士", "硕士", "本科", "专科", "高中", "初中", "小学", "其他"]
            father_id_type = random.choice(id_type_list2)
            post_grade_list=["中专2020级","中专2019级"," 中专2018级","大专2020级","大专2019级","大专2018级 "]
            post_grade = random.choice(post_grade_list)
            sex_list=["男","女"]
            sex = random.choice(sex_list)
            birthday=student_id_card[6:10]+"/"+student_id_card[10:12]+"/"+student_id_card[12:14]
            nation_list = ["汉族", "蒙古族", "回族", "藏族", "维吾尔族", "苗族", "彝族", "壮族", "布依族", "朝鲜族", "满族", "侗族", "瑶族", "白族",
                           "土家族",
                           "哈尼族", "哈萨克族", "傣族", "黎族", "傈僳族", "佤族", "畲族", "高山族", "拉祜族", "水族", "东乡族", "纳西族", "景颇族",
                           "柯尔克孜族",
                           "土族", "达斡尔族", "仫佬族", "羌族", "布朗族", "撒拉族", "毛难族", "仡佬族", "锡伯族", "阿昌族", "普米族", "塔吉克族", "怒族",
                           "乌孜别克族", "俄罗斯族", "鄂温克族", "崩龙族", "保安族", "裕固族", "京族", "塔塔尔族", "独龙族", "鄂伦春族", "赫哲族", "门巴族",
                           "珞巴族",
                           "基诺族"]
            nation = random.choice(nation_list)
            nationality_list=["中国","中国（香港）","中国（澳门）","中国（台湾）","海外"]
            nationality=random.choice(nationality_list)
            # clue_from_list=["熟人推荐","学校宣传","媒体"]
            # clue_from = random.choice(clue_from_list)
            major_list = ["航空服务","民航安全技术管理","城市轨道交通运营管理","机务维修","机务"]
            major=random.choice(major_list)
            teacher_list=["田凯","贾东旭","李晓燕","甘平","纪苏恩"]
            teacher=random.choice(teacher_list)
            Political_outlook_list=["共青团员","共产党员","其他"]
            Political_outlook=random.choice(Political_outlook_list)
            education_level_list=["小学","初中","高中","中级","高级","中专","大专","其他"]
            education_level=random.choice( education_level_list)
            now_level_list=["初中一年级","初中二年级","初中三年级","高中一年级","高中二年级","高中三年级"]
            now_level=random.choice( now_level_list)
            accommodation_list=["是","否"]
            accommodation = random.choice(accommodation_list)
            body_status_list=["健康或良好","一般或较弱","一般或较弱","有慢性病","有生理缺陷","残疾"]
            body_status = random.choice(body_status_list)
            student_code=self.ac.Student_code()
            relationship_list=["自己","父母","祖父母/外祖父母","其他亲属"]
            relationship = random.choice(relationship_list)
            post_grauate_list=["2021年 - 春季","2021年 - 秋季"]
            post_grauate=random.choice(post_grauate_list)
            yixiang=random.choice(range(1,5))
            print(student_id_card,mother_id_card,father_id_card,mother_id_type,father_id_type,birthday,
                  post_grade,sex,nationality,major,teacher,Political_outlook,education_level,now_level,accommodation,body_status,student_code,relationship)
            self.he.write_cell_values(i,1,name,phone,student_id_card,birthday,father_name,father_phone,mother_id_card,post_grade,sex,major,teacher,nation,nationality,yixiang,post_grauate,"Sheet1")
            # self.he.write_cell_value(i,1,name,"Sheet1")
            # self.he.write_cell_value(i,2,phone,"Sheet1")
            # self.he.write_cell_value(i, 3, father_name, "Sheet1")
            # self.he.write_cell_value(i, 4, mother_name, "Sheet1")
            # self.he.write_cell_value(i, 5, student_id_card, "Sheet1")
            # self.he.write_cell_value(i, 6, mother_id_card, "Sheet1")
            # self.he.write_cell_value(i, 7, father_id_card, "Sheet1")
            # self.he.write_cell_value(i, 8, mother_id_type, "Sheet1")
            # self.he.write_cell_value(i, 9, father_id_type, "Sheet1")
            # self.he.write_cell_value(i, 10, post_grade, "Sheet1")
            # self.he.write_cell_value(i, 11, sex, "Sheet1")
            # self.he.write_cell_value(i, 12, birthday, "Sheet1")
            # self.he.write_cell_value(i, 13, nation, "Sheet1")
            # self.he.write_cell_value(i, 15, nationality, "Sheet1")
            # # self.he.write_cell_value(i, 16, clue_from, "Sheet1")
            # self.he.write_cell_value(i, 17, major, "Sheet1")
            # self.he.write_cell_value(i, 18, teacher, "Sheet1")
            # self.he.write_cell_value(i, 19, Political_outlook, "Sheet1")
            # self.he.write_cell_value(i, 20, education_level, "Sheet1")
            # self.he.write_cell_value(i, 21, now_level, "Sheet1")
            # self.he.write_cell_value(i, 22, accommodation, "Sheet1")
            # self.he.write_cell_value(i, 23, body_status, "Sheet1")
            # self.he.write_cell_value(i, 24, student_code, "Sheet1")
            # self.he.write_cell_value(i, 25, relationship, "Sheet1")
            # self.he.write_cell_value(i, 26, father_phone, "Sheet1")
            # self.he.write_cell_value(i, 27, mother_phone, "Sheet1")



if __name__=="__main__":
    Name_tel().test_add_clue()