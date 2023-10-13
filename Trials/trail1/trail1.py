import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QPushButton, QTextEdit, QMessageBox, QVBoxLayout, QLabel

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create the username and password widgets
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Create the login and view/update buttons
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        self.view_update_button = QPushButton('View/Update Details')
        self.view_update_button.clicked.connect(self.view_update_details)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.view_update_button)
        self.setLayout(layout)

    def login(self):
        # Get the username and password from the widgets
        username = self.username.text()
        password = self.password.text()

        # Check if the user exists in the database
        conn = sqlite3.connect('user_feedback.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()

        # If the user exists, open the feedback form
        if user:
            self.feedback_form = FeedbackForm(username)
            self.feedback_form.show()

        # Otherwise, show an error message
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password.')

    def view_update_details(self):
        # Get the username and password from the widgets
        username = self.username.text()
        password = self.password.text()

        # Check if the user exists in the database
        conn = sqlite3.connect('user_feedback.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()

        # If the user exists, open the user details form
        if user:
            self.user_details = UserDetailsForm(user[0])
            self.user_details.show()

        # Otherwise, show an error message
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password.')

class FeedbackForm(QDialog):
    def __init__(self, username):
        super().__init__()

        # Create the feedback text box
        self.feedback = QTextEdit()

        # Create the submit button
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.feedback)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

        # Store the username
        self.username = username

    def submit(self):
        # Get the feedback from the text box
        feedback = self.feedback.toPlainText()

        # Insert the feedback into the database
        conn = sqlite3.connect('user_feedback.db')
        c = conn.cursor()
        c.execute('INSERT INTO feedback (username, feedback) VALUES (?, ?)', (self.username, feedback))
        conn.commit()

        # Close the form
        self.close()

class UserDetailsForm(QDialog):
    def __init__(self, username):
        super().__init__()

        # Get the user details from the database
        conn = sqlite3.connect('user_feedback.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        # Create the username, email, and password widgets
        self.username = QLineEdit(user[0])
        self.email = QLineEdit

        # next code

        self.password = QLineEdit(user[2])
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # Create the update button
        self.update_button = QPushButton('Update')
        self.update_button.clicked.connect(self.update)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Username'))
        layout.addWidget(self.username)
        layout.addWidget(QLabel('Email'))
        layout.addWidget(self.email)
        layout.addWidget(QLabel('Password'))
        layout.addWidget(self.password)
        layout.addWidget(self.update_button)
        self.setLayout(layout)

    def update(self):
        # Get the updated user details from the widgets
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()

        # Update the user details in the database
        conn = sqlite3.connect('user_feedback.db')
        c = conn.cursor()
        c.execute('UPDATE users SET email = ?, password = ? WHERE username = ?', (email, password, username))
        conn.commit()

        # Close the form
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the login dialog
    login_dialog = LoginDialog()
    login_dialog.show()

    app.exec_()
