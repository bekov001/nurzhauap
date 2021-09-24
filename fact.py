import xlsxwriter
import xlrd

workbook = xlrd.open_workbook('C:\\Users\\atheelm\\Documents\\python excel mission\\errors1.xlsx')
workbook = xlrd.open_workbook('C:\\Users\\atheelm\\Documents\\python excel mission\\errors1.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] # The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
# tronsform the workbook to a list of dictionnary
data =[]
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    data.append(elm)
print(data)




# try:
#     if any(not el for key, el in self.statics.items()):
#         print("\033[33mСтатиски пока нет")
#     else:
#         workbook = xlsxwriter.Workbook('docs/test.xlsx')
#         for key, (item, count) in enumerate(self.statics.items()):
#             name = dec[item].replace(" ", "_")
#             worksheet = workbook.add_worksheet(name)
#             if isinstance(count, list):
#                 count = func1(count)
#                 for index, (amount, el) in enumerate(count):
#                     worksheet.write(index, 0, el)
#                     worksheet.write(index, 1, int(amount))
#                     chart = workbook.add_chart({'type': 'pie'})
#
#                 # Строим по нашим данным
#                 chart.add_series({'values': f'={name}!B1:B{index + 1}',
#                                   'categories': f"={name}!A1:A{index + 1}"})
#
#                 worksheet.insert_chart('C3', chart)
#             else:
#                 worksheet.write(0, 0, dec[item])
#                 worksheet.write(0, 1, count)
#
#         # # Тип диаграммЫ
#
#         workbook.close()
# except Exception:
#     print("файл пустой")