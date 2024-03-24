import openpyxl as excel

book = excel.load_workbook('C:\\Users\\satol\\Downloads\\java\\code\\udemy_Web_developer\\openxl\\hizumidata.xlsx')
#sheet = book.active
sheet = book.active

for row in sheet["B5":"B31"]:
    print([c.value for c in row])


