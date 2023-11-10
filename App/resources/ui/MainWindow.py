from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 310, 861, 271))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.conclusion = QtWidgets.QTextBrowser(self.centralwidget)
        self.conclusion.setGeometry(QtCore.QRect(0, 270, 861, 41))
        self.conclusion.setStyleSheet("background-color: rgb(125, 200, 200);\n"
"")
        self.conclusion.setObjectName("conclusion")
        self.reqText = QtWidgets.QTextEdit(self.centralwidget)
        self.reqText.setGeometry(QtCore.QRect(0, 40, 861, 192))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reqText.setFont(font)
        self.reqText.setStyleSheet("")
        self.reqText.setObjectName("textEdit_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 861, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(125, 200, 200);\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 229, 861, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reqButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reqButton.sizePolicy().hasHeightForWidth())
        self.reqButton.setSizePolicy(sizePolicy)
        self.reqButton.setMinimumSize(QtCore.QSize(39, 29))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.reqButton.setFont(font)
        self.reqButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.reqButton.setToolTipDuration(-1)
        self.reqButton.setAutoFillBackground(False)
        self.reqButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(148, 206, 120);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #81b369;\n"
"}")
        icon = QtGui.QIcon()
        script_dir = os.path.dirname(__file__)[:-2]
        rel_path = "ChatGPT_logo.svg.png"
        abs_db_path = os.path.join(script_dir, rel_path)
        icon.addPixmap(QtGui.QPixmap(abs_db_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reqButton.setIcon(icon)
        self.reqButton.setAutoExclusive(False)
        self.reqButton.setAutoDefault(False)
        self.reqButton.setDefault(False)
        self.reqButton.setObjectName("reqButton")
        self.horizontalLayout.addWidget(self.reqButton)
        self.AskGPTButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AskGPTButton.sizePolicy().hasHeightForWidth())
        self.AskGPTButton.setSizePolicy(sizePolicy)
        self.AskGPTButton.setMinimumSize(QtCore.QSize(39, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.AskGPTButton.setFont(font)
        self.AskGPTButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(148, 206, 120);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #81b369;\n"
"}")
        self.AskGPTButton.setIcon(icon)
        self.AskGPTButton.setObjectName("AskGPTButton")
        self.horizontalLayout.addWidget(self.AskGPTButton)
        self.rewriteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rewriteButton.sizePolicy().hasHeightForWidth())
        self.rewriteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rewriteButton.setFont(font)
        self.rewriteButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(148, 206, 120);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #81b369;\n"
"}")
        self.rewriteButton.setIcon(icon)
        self.rewriteButton.setObjectName("rewriteButton")
        self.horizontalLayout.addWidget(self.rewriteButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conclusion.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Исправленный текст:</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Текст:</span></p></body></html>"))
        self.reqButton.setText(_translate("MainWindow", "Запросы"))
        self.AskGPTButton.setText(_translate("MainWindow", "Спросить у GPT"))
        self.rewriteButton.setText(_translate("MainWindow", "Исправить текст"))