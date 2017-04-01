from excelutils import ExcelHandler

class WorkExcelCreator():

    def work(self, file_name, data):
        workbook = ExcelHandler.create_work(file_name)
        sheetnames =  ExcelHandler.get_worksheet_namse_from_workbook(workbook)
        sheet = ExcelHandler.get_worksheet(workbook, sheetnames[0])
        self.write_title(sheet)
        self.append_data(sheet, data)
        ExcelHandler.save(workbook, file_name)



    def write_title(self, sheet):
        flow_title_1 = ['宝贝搜索词', '访客数', '收藏数', '加购数', '支付买家数', '总价值', '价值比']

        for x in range(len(flow_title_1)):
            # print(x)
            sheet.cell(row=1, column=x+1, value=flow_title_1[x])
            pass

    def append_data(self, sheet, datas):
        columns = [1, 2, 3, 4, 5]
        for x in range(len(datas)):
            for col in columns:
                sheet.cell(row=x + 2, column=col, value=datas[x][col-1])
            print("=IF(A"+str(x+2)+"<>\"\",C"+str(x+2)+"+D"+str(x+2)+"+10*E"+str(x+2)+",\"\")")
            sheet.cell(row=x + 2, column=6, value="=IF(A"+str(x+2)+"<>\"\",C"+str(x+2)+"+D"+str(x+2)+"+10*E"+str(x+2)+",\"\")")
            sheet.cell(row=x + 2, column=7, value="=IF(B"+str(x+2)+">0,F"+str(x+2)+"/B"+str(x+2)+","")")

