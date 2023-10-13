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
            QMessageBox.warning(self, 'Login Failed', 'User does not exist. Please sign up.')

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
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("User Management Options:")
        self.label.setFont(QFont('Arial', 12))

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.create_user_button = QPushButton("Create User")
        self.create_user_button.clicked.connect(self.create_user)

        self.update_user_button = QPushButton("Update User")
        self.update_user_button.clicked.connect(self.update_user)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.create_user_button)
        layout.addWidget(self.update_user_button)

        self.setLayout(layout)

    def create_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, 'Invalid Input', 'Both username and password are required to create a user.')
            return

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        if user:
            QMessageBox.warning(self, 'User Exists', 'Username already exists. Please choose a different username.')
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            QMessageBox.information(self, 'User Created', 'New user created successfully.')
            self.username_input.clear()
            self.password_input.clear()

    def update_user(self):
        username = self.username_input.text()
        new_password = self.password_input.text()

        if not username or not new_password:
            QMessageBox.warning(self, 'Invalid Input', 'Both username and new password are required to update a user.')
            return

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        if user:
            cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
            conn.commit()
            QMessageBox.information(self, 'User Updated', 'User password updated successfully.')
            self.username_input.clear()
            self.password_input.clear()
        else:
            QMessageBox.warning(self, 'User Not Found', 'User does not exist. Please sign up or enter an existing username.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    feedback_window = FeedbackWindow()
    user_management_window = UserManagementWindow()

    login_window.show()
    sys.exit(app.exec_())
