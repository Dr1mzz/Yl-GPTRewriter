import sys
import g4f
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from resources.ui.MainWindow import Ui_MainWindow
from resources.ui.LoginDialog import Ui_LoginDialog
from database import UserDao
import hashlib


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id) -> None:
        super(MainWindow, self).__init__()
        self.user_id = user_id
        self.setupUi(self)
        self.initUI()

    def initUI(self) -> None:
        self.rewriteButton.clicked.connect(self.ask_gpt)
        self.AskGPTButton.clicked.connect(self.ask_gpt)

    def ask_gpt(self) -> None:
        flag = False
        sender = self.sender()
        if sender == self.rewriteButton:
            if self.reqText.toPlainText():
                prompt = (
                    "Исправь грамматические и пунктационные ошибки, не изменяй формулировки и смысл слов, "
                    "в ответе запиши исправленный текст и ничего больше. Сам текст:"
                    + self.reqText.toPlainText()
                )
                self.text_browser_rewriter_style(True)
            else:
                self.text_browser_rewriter_style(True)
                self.textEdit_2.setText("Кажется вы ничего не ввели. Попробуйте снова!")
                flag = True
        else:
            if self.reqText.toPlainText():
                prompt = self.reqText.toPlainText()
                self.text_browser_rewriter_style(False)
            else:
                self.text_browser_rewriter_style(False)
                self.textEdit_2.setText("Кажется вы ничего не ввели. Попробуйте снова!")
                flag = True
        if not (flag):
            try:
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_35_turbo,
                    messages=[{"role": "user", "content": prompt}],
                    timeout=120,
                )
            except RuntimeError:
                self.textEdit_2.setText("Произошла ошибка. Попробуйте снова!")
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
            self.set_error('Error: Invalid login or password.')

    def is_user_valid(self, login, password):
        user = self.dao.get(login)
        return user[0] if user is not None and user[3] == hashlib.md5(password.encode()).hexdigest() else -1

    def create_user(self):
        login = self.login_input.text()
        password = self.pass_input.text()
        if self.check_login(login) and self.check_pass(password):
            try:
                self.dao.save(login, login, password)
                self.log_in()
            except Exception:
                self.set_error('Error: this login is already occupied.')

    def check_pass(self, password):
        if not 8 <= len(password) <= 30:
            self.set_error('Error: Password must be 8 to 30 characters long.')
            return False
        return True

    def check_login(self, login):
        if not 3 <= len(login) <= 20:
            self.set_error('Error: Login must be 3 to 20 characters long.')
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
