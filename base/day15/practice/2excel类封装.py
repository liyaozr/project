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
        self.wb = openpyxl.load_workbook(filename)
        self.sh = self.wb[sheet_name]

    def read_data(self):
        datas = self.sh.rows
        title = [i.value for i in datas[0]]
        cases = []
        for data in datas[1:]:
            values = [i.value for i in data]
            case = dict(zip(title, values))
            cases.append(case)
        return cases

    def write_excel(self, row, column, value):
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)
