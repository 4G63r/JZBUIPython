import xlrd


# excel = xlrd.open_workbook('/Volumes/SAMSUNG/TP_Rush/jiazhangbang/config/case.xlsx')
# print(excel.sheet_names())  # 获取工作表名称
# sheet1 = excel.sheets()[0]  # 获取第一个工作表对象print(sheet1)
# print(sheet1)
# print(sheet1.nrows)  # 获取行数
# print(sheet1.row_values(0))  # 获取第一行数据
# print(sheet1.col_values(0))  # 获取第一列数据
# print(sheet1.cell(3, 4).value)  # 获取第4行第5列元素


class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path == None:
            file_path = '/Volumes/SAMSUNG/TP_Rush/jiazhangbang/config/case.xlsx'
        if i == None:
            i = 0
        self.excel = self.get_excel(file_path)
        self.data = self.get_sheet(i)

    def get_excel(self, file_path):
        """获取excel对象"""
        excel = xlrd.open_workbook(file_path)
        return excel

    def get_sheet(self, i):
        """获取sheet"""
        sheet = self.excel.sheets()[i]
        return sheet

    def get_lines(self):
        """获取excel行数"""
        lines = self.data.nrows
        return lines

    def get_cell(self, row, col):
        """获取单元格内容"""
        data = self.data.cell(row, col).value
        return data


if __name__ == '__main__':
    o = OperaExcel()
    print(o.get_cell(4, 5))
