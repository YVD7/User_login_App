import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Create a SQLite database to store user information
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your username and password:")
        self.label.setFont(QFont('Arial', 12))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        if user:
            self.hide()
            feedback_window.show()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password. Please try again.')

class FeedbackWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Feedback Form")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your feedback:")
        self.label.setFont(QFont('Arial', 12))

        self.feedback_input = QTextEdit()

        self.submit_button = QPushButton("Submit Feedback")
        self.submit_button.clicked.connect(self.submit_feedback)

        layout.addWidget(self.label)
        layout.addWidget(self.feedback_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_feedback(self):
        feedback = self.feedback_input.toPlainText()
        QMessageBox.information(self, 'Feedback Received', 'Thank you for your feedback!')
        self.feedback_input.clear()

class UserManagementWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Management")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("User Management Options:")
        self.label.setFont(QFont('Arial', 12))

        self.view_users_button = QPushButton("View Users")
        self.view_users_button.clicked.connect(self.view_users)

        layout.addWidget(self.label)
        layout.addWidget(self.view_users_button)

        self.setLayout(layout)

    def view_users(self):
        cursor.execute('SELECT username FROM users')
        users = cursor.fetchall()
        user_list = '\n'.join([user[0] for user in users])
        QMessageBox.information(self, 'Users', f'List of Users:\n{user_list}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    feedback_window = FeedbackWindow()
    user_management_window = UserManagementWindow()

    login_window.show()
    sys.exit(app.exec_())
