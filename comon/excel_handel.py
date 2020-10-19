from openpyxl import load_workbook
from comon.config import con
class Excel:
    # 传入对应的excel的路径
    def __init__(self,file_path):
        self.file_path = file_path
        self.excel = load_workbook(file_path)

    def sheet(self,sheet):
        try:
            if isinstance(sheet,int):
                return self.excel.worksheets[sheet]
            elif isinstance(sheet,str):
                return self.excel.get_sheet_by_name(sheet)
        except AssertionError as error:
            return (error)
       # 读取一行的数据
    def one_row_data(self,sheet,row):
        try:
            sheet = self.sheet(sheet)
            data = sheet[row]
            data_list = []
            for i in data:
                data_list.append(i.value)
            return data_list
        except AssertionError as error:
            return (error)
        # 读取一行的数据
    def one_data(self,sheet,row,line):
        sheet = self.sheet(sheet)
        data = sheet[row][line]
        return data.value
      # 读取全部的数据
    def all_data(self,sheet):
        try:
            one = self.one_row_data(sheet,1)
            sheet = self.sheet(sheet)
            data = sheet.rows
            data_li = list(data)[1:]
            data_list =[]
            for i in data_li:
                da_li = []
                for c in i:
                    da_li.append(c.value)
                    da_dict = dict(zip(one,da_li))
                data_list.append(da_dict)
            return data_list
        except AssertionError as error:
            return error

    def write(self,sheet,row,line,zhi):
        try:
            sheet = self.sheet(sheet)
            data = sheet[row][line]
            data.value = zhi
            self.excel.save(self.file_path)
            self.excel.close()
            print('写入成功')
        except AssertionError as error:
            print(error)










if __name__ == '__main__':
    co = con.article('excle_path','excel_path')
    ex = Excel(co)
    # print(ex.one_row_data(0,1))
    # # print(ex.all_data(0))
    # print(ex.write(0,1,1,'three'))
    print(ex.one_data(0,1,1))