from database import ReqDao
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QHeaderView
from resources.ui.ReqWidget import Ui_RequestWidget


class RequestWidget(QMainWindow, Ui_RequestWidget):
    def __init__(self, user_id):
        super(RequestWidget, self).__init__()
        self.user_id = user_id
        self.setupUi(self)
        self.db = ReqDao()
        self.initUI()

    def initUI(self):
        horHeaders = []
        self.data = self.db.get_all(self.user_id)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, row in enumerate(self.data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                horHeaders.append(elem)
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        header = self.tableWidget.horizontalHeader()
        header.setStretchLastSection(True)