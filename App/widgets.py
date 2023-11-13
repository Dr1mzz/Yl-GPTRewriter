from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect
import sqlite3
from database import ReqDao
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMainWindow
from resources.ui.ReqWidget import Ui_RequestWidget


class RequestWidget(QMainWindow, Ui_RequestWidget):
    def __init__(self, user_id):
        super(RequestWidget, self).__init__()
        self.user_id = user_id
        self.setupUi(self)
        self.db = ReqDao()
        self.initUI()
        # self.connection = sqlite3.connect("")
        # self.db = QSqlDatabase.addDatabase()

    def initUI(self):
        self.data = self.db.get_all(self.user_id)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))