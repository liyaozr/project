"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import openpyxl


class ReadExcel():
    def __init__(self, filename, sheet_name):
        self.filename = filename
        # 打开工作簿
        self.wb = openpyxl.load_workbook(filename)
        # 打开工作簿中的表格
        self.sh = self.wb[sheet_name]

    def read_data(self):
        # 获取数据，注意！！！要转换为列表格式，否则无法循环
        datas = list(self.sh.rows)
        # print(datas[0])
        # 获取标题
        title = [i.value for i in datas[0]]
        cases = []
        # 通过循环获取表格中的数据并保存在空列表中
        for data in datas[1:]:
            values = [i.value for i in data]
            case = dict(zip(title, values))
            cases.append(case)
        return cases

    def write_data(self, row, column, value):
        # 写入数据
        self.sh.cell(row=row, column=column, value=value)
        # 保存表格
        self.wb.save(self.filename)
