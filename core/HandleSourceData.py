from excelutils import ExcelHandler
from .Creator import WorkExcelCreator
class SourceDataHandler():
    # 获得排序key
    def get_sort_key(self, row):
        return row[1]

    # 合并数据
    def merge_data(self, row1, row2, filename, sheetname):
        workbook = ExcelHandler.create_work(filename)
        sheet = ExcelHandler.get_worksheet(workbook, ExcelHandler.get_worksheet_namse_from_workbook(workbook)[0])

        result = []
        for row1_1 in row1:
            self.survival(result, row1_1)

        for row2_2 in row2:
            self.survival(result, row2_2)

        result.sort(key=self.get_sort_key, reverse=True)

        # result.insert(0, ['来源名称', '访客数',  '收藏人数', '加购人数', '支付买家数'])

        creator = WorkExcelCreator()

        creator.work("test.xlsx", result)
        # for row in result:
        #     sheet.append(row)
        #
        # ExcelHandler.save(workbook, filename)

    # 查找在数组中的位置
    def index_of_list(self, list, row):
        i = 0

        while i < len(list):
            cell = list[i]
            if cell[0] == row[0].value:
                return i
            i = i + 1

        return -1

    # 合并单元行
    def survival(self, lists, row):

        indexs = [0, 1, 6, 7, 11]
        index = 1
        result = []
        indexolist = self.index_of_list(lists, row)
        if indexolist == -1:
            result.append(row[0].value)
            while index < len(indexs):
                result.append(float(row[indexs[index]].value))
                index = index + 1
            lists.append(result)
        else:
            while index < len(indexs):
                lists[indexolist][index] = float(lists[indexolist][index]) + float(row[indexs[index]].value)
                index = index + 1

    def get_tuple_of_data(self, file_name):
        workbook = ExcelHandler.get_workbook(file_name)
        names = ExcelHandler.get_worksheet_namse_from_workbook(workbook)
        sheet = ExcelHandler.get_worksheet(workbook, names[0])

        # 获得所有元组
        rows = ExcelHandler.get_sheet_all_rows(sheet)
        # 剪切需要的元组
        cells = ExcelHandler.get_cells(sheet, 'A7', 'M' + str(len(rows)))
        return cells

    def run(self, file_first, file_second):
        cells = self.get_tuple_of_data(file_first)
        cells2 = self.get_tuple_of_data(file_second)
        self.merge_data(cells, cells2, "result_oo.xlsx", "tst")


