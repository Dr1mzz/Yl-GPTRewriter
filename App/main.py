import sys
import g4f
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from resources.ui.MainWindow import Ui_MainWindow
from widgets import RequestWidget
from resources.ui.LoginDialog import Ui_LoginDialog
from database import UserDao, ReqDao, ReqException
import hashlib


NO_TEXT_ERROR = "Кажется вы ничего не ввели. Попробуйте снова!"
CHATGPT_ERROR = "Произошла ошибка. Попробуйте снова!"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id) -> None:
        super(MainWindow, self).__init__()
        self.user_id = user_id
        self.cursor = 0
        self.setupUi(self)
        self.request_widget = RequestWidget(self.user_id)
        self.request_dao = ReqDao()
        self.initUI()

    def initUI(self) -> None:
        self.rewriteButton.clicked.connect(self.ask_gpt)
        self.AskGPTButton.clicked.connect(self.ask_gpt)
        self.reqButton.clicked.connect(self.get_requests)

    def ask_gpt(self) -> None:
        flag = False
        sender = self.sender()
        request = self.reqText.toPlainText()
        if sender == self.rewriteButton:
            if request:
                prompt = (
                    "Исправь грамматические и пунктационные ошибки, не изменяй формулировки и смысл слов, "
                    "в ответе запиши исправленный текст и ничего больше. Сам текст:"
                    + request
                )
                self.add_request(request)
                self.text_browser_rewriter_style(True)
            else:
                self.text_browser_rewriter_style(True)
                self.textEdit_2.setText(NO_TEXT_ERROR)
                flag = True
        else:
            if request:
                prompt = request
                self.add_request(request)
                self.text_browser_rewriter_style(False)
            else:
                self.text_browser_rewriter_style(False)
                self.textEdit_2.setText(NO_TEXT_ERROR)
                flag = True
        if not (flag):
            try:
                response = g4f.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    provider=g4f.Provider.GeekGpt,
                    messages=[{"role": "user", "content": prompt}],
                )
            except RuntimeError:
                self.textEdit_2.setText(CHATGPT_ERROR)
            self.textEdit_2.setText(response)

    def text_browser_rewriter_style(self, flag: bool) -> None:
        _translate = QtCore.QCoreApplication.translate
        if flag:
            self.conclusion.setHtml(
                _translate(
                    "MainWindow",
                    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                    '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600; color:#ffffff;">Исправленный текст:</span></p></body></html>',
                )
            )
        else:
            self.conclusion.setHtml(
                _translate(
                    "MainWindow",
                    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                    '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600; color:#ffffff;">Ответ GPT:</span></p></body></html>',
                )
            )
    
    def add_request(self, request):
        try:
            self.request_dao.save(self.user_id, request)
        except ReqException:
            pass

    def get_requests(self):
        self.request_widget.initUI()
        self.request_widget.show()


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.player = None
        self.setupUi(self)
        self.dao = UserDao()
        self.log_in_button.clicked.connect(self.log_in)
        self.reg_button.clicked.connect(self.create_user)

    def log_in(self):
        login = self.login_input.text()
        password = self.pass_input.text()
        user_id = self.is_user_valid(login, password)
        if user_id > 0:
            self.player = MainWindow(user_id)
            self.hide()
            self.player.show()
        else:
            self.set_error("Error: Invalid login or password.")

    def is_user_valid(self, login, password):
        user = self.dao.get(login)
        return (
            user[0]
            if user is not None
            and user[3] == hashlib.md5(password.encode()).hexdigest()
            else -1
        )

    def create_user(self):
        login = self.login_input.text()
        password = self.pass_input.text()
        if self.check_login(login) and self.check_pass(password):
            try:
                self.dao.save(login, login, password)
                self.log_in()
            except Exception:
                self.set_error("Error: this login is already occupied.")

    def check_pass(self, password):
        if not 8 <= len(password) <= 30:
            self.set_error("Error: Password must be 8 to 30 characters long.")
            return False
        return True

    def check_login(self, login):
        if not 3 <= len(login) <= 20:
            self.set_error("Error: Login must be 3 to 20 characters long.")
            return False
        return True

    def set_error(self, msg):
        if msg is None:
            self.error_label.hide()
        else:
            self.error_label.setText(msg)
            self.error_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginDialog()
    window.show()
    sys.exit(app.exec_())
