import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QFont

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

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        if user:
            if password == user[1]:
                self.hide()
                feedback_window.show()
            else:
                QMessageBox.warning(self, 'Login Failed', 'Invalid password. Please try again.')
        else:
            create_new_user = QMessageBox.question(self, 'User Not Found', 'User does not exist. Do you want to create a new user?', QMessageBox.Yes | QMessageBox.No)
            if create_new_user == QMessageBox.Yes:
                create_user_window.show()
        self.username_input.clear()
        self.password_input.clear()

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

class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create User")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Create a new username and password:")
        self.label.setFont(QFont('Arial', 12))

        self.new_username_input = QLineEdit()
        self.new_username_input.setPlaceholderText("New Username")

        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("New Password")
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.create_user_button = QPushButton("Create User")
        self.create_user_button.clicked.connect(self.create_user)

        layout.addWidget(self.label)
        layout.addWidget(self.new_username_input)
        layout.addWidget(self.new_password_input)
        layout.addWidget(self.create_user_button)

        self.setLayout(layout)

    def create_user(self):
        new_username = self.new_username_input.text()
        new_password = self.new_password_input.text()

        if not new_username or not new_password:
            QMessageBox.warning(self, 'Invalid Input', 'Both a new username and password are required to create a user.')
            return

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (new_username, new_password))
        conn.commit()
        QMessageBox.information(self, 'User Created', 'New user created successfully.')
        self.new_username_input.clear()
        self.new_password_input.clear()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    feedback_window = FeedbackWindow()
    create_user_window = CreateUserWindow()

    login_window.show()
    sys.exit(app.exec_())
