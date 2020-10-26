#coding=utf-8
import sys
sys.path.append(r"D:\project\quanrizhi\venv\lib\site-packages")
sys.path.append(r"D:\project\quanrizhi\venv\config")
import openpyxl
import os
base_path=os.path.dirname(os.getcwd())
class Excel_handle:
    def load_excel(self,file_path=None):
        if file_path==None:
            self.file_path=base_path+"\\config\\login_test_case.xlsx"
        else:
            self.file_path=base_path+file_path
        open_excel=openpyxl.load_workbook(self.file_path)
        return open_excel
    def get_sheet_data(self,index=None):
        """获取表格数据"""
        sheet_name=self.load_excel().sheetnames
        if index==None:
            index=0
        data=self.load_excel()[sheet_name[index]]
        return data
    def get_value(self,row,cols,index=None):
        """获取单元格值"""
        data=self.get_sheet_data(index).cell(row=row,column=cols).value
        return data
    def get_rows(self,index=None):
        """获取行数"""
        rows=self.get_sheet_data(index).max_row
        return rows
    def get_rows_value(self,row,index=None):
        """获取行数值"""
        row_list=[]
        for i in self.get_sheet_data(index)[row]:
            row_list.append(i.value)
        return row_list
    def write_cell_value(self,row,col,value,sheetname=None):
        """写入单元格值"""
        if sheetname==None:
            sheetname="login"
        excel=self.load_excel()
        data=excel[sheetname]
        data.cell(row,col,value)
        excel.save(self.file_path)
    def get_col_value(self,case_id,col=None,index=None):
        """获取某一列所有数据"""
        if col==None:
            col="A"
        col_data=self.get_sheet_data(index)[col]
        col_value={}
        b=1
        try:
            for i in col_data:
                col_value[i.value]=b
                b+=1
            col_value.pop("用例编号")
            return col_value[case_id]
        except:
            return None
    def get_rowlist_data(self,index=None):
        """获取列表所有行数据"""
        rows=self.get_rows(index)
        data=[]
        for i in range(rows):
            if (i+2)>rows:
                break
            data.append(self.get_rows_value(i+2))
        return data
    def delete_row(self,i,index=None):
        """删除行"""
        wb=self.load_excel(index)
        ws=wb.active
        ws.delete_rows(i)