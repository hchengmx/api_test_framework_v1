import xlrd

# wb = xlrd.open_workbook("./test_user_data.xlsx")
# sh = wb.sheet_by_name("TestUserLogin")  # 按工作簿名定位工作表
# print(sh.nrows)  # 有效数据行数
# print(sh.ncols)  # 有效数据列数

def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1, sh.nrows):  #跳过标题行
        d =dict(zip(header, sh.row_values(i))) #将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  

# def get_test_data(data_list, case_name):
#     for case_data in data_list:
#         if