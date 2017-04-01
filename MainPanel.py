from PyQt5 import QtWidgets,QtCore
from ui.first import Ui_MainWindow
from core.HandleSourceData import SourceDataHandler
import sys

class TaskThread(QtCore.QThread):
    workSignal = QtCore.pyqtSignal()
    workEndSignal = QtCore.pyqtSignal()

    def __init__(self, file_first, file_second, parent=None):
        super(TaskThread, self).__init__(parent)
        self.file_first = file_first
        self.file_second = file_second

    def run(self):
        handler = SourceDataHandler()
        handler.run(self.file_first, self.file_second)
        self.workEndSignal.emit()
        pass

class ManelPanel(QtWidgets.QWidget,Ui_MainWindow):

    def __init__(self):
        super(ManelPanel,self).__init__()
        self.setupUi(self)
        self.btn_file_one.clicked.connect(self.first_file)
        self.btn_file_two.clicked.connect(self.second_file)
        self.btn_create.clicked.connect(self.create_excel)

    def first_file(self):
        self.file_name_first, filetype_first = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                         "选取文件",
                                                                         "C:/",
                                                                         "All Files (*);;Text Files (*.txt)")
        self.edt_file_one.setText(self.file_name_first)
        pass

    def second_file(self):
        self.file_name_second, filetype_second = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                         "选取文件",
                                                                         "C:/",
                                                                         "All Files (*);;Text Files (*.txt)")
        self.edt_file_two.setText(self.file_name_second)
        pass

    def working(self):
        self.btn_file_one.setEnabled(False)
        self.btn_file_two.setEnabled(False)
        self.btn_create.setEnabled(False)
        self.btn_create.setText("运行中...")
        pass

    def work_end(self):
        self.btn_file_one.setEnabled(True)
        self.btn_file_two.setEnabled(True)
        self.btn_create.setEnabled(True)
        self.btn_create.setText("生成excel")
        pass

    def create_excel(self):
        self.working()
        self.task = TaskThread(self.file_name_first, self.file_name_second)
        self.task.workEndSignal.connect(self.work_end)
        self.task.start()
        pass


app=QtWidgets.QApplication(sys.argv)
myshow=ManelPanel()
myshow.show()
sys.exit(app.exec_())