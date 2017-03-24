from excelutils import ExcelHandler

workbook = ExcelHandler.create_work("D:/pyCode/DSHelper/test.xlsx")
ExcelHandler.create_sheet(workbook, "test")
names = ExcelHandler.get_worksheet_namse_from_workbook(workbook)
sheet = ExcelHandler.get_worksheet(workbook,names[0])

sheet["A1"].value = 1
sheet["B1"] = 2
c = sheet["C"]
a = sheet["A"]
b = sheet["B"]


ExcelHandler.save(workbook, "D:/pyCode/DSHelper/test.xlsx")
print(workbook)
print(names)
