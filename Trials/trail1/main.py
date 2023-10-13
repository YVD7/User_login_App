import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QGridLayout, QMessageBox, QPushButton 

# Login form

class loginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User Login')
        self.resize(500, 100)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> User name </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Please enter your username")
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size = "4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Plase enter your password")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_passwrod(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exce_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)

    form = loginForm()
    form.show()

    sys.exit(app.exec_())