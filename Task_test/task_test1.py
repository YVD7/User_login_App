import sys
import os
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Window(QDialog):

    # constructor
    def __init__(self):
        super(Window, self).__init__()

        # setting window title
        self.setWindowTitle("Python")

        # setting geomentry to the window 
        self.setGeometry(100, 100, 300, 400)

        # create a group box 
        self.formGroupBox = QGroupBox("From 1")

        # creating a group box to select age
        self.ageSpinBar = QSpinBox()
        
        # creating combo box to select degree
        self.degreeComobox = QComboBox()

        # adding items to combo box
        self.degreeComobox.addItems(["BTech", "MTech", "PhD"])

        # creating a line edit
        self.nameLineEdit = QLineEdit()

        # creating the mothod that create the form 
        self.createForm()

        # creating a dialog button of ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.rejected)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

    # get info method called when form is accepted
    def getInfo(self):

        # printing the form information
        print("Person Name: {0}".format(self.nameLineEdit.text()))
        print("Degree: {0}".format(self.degreeComobox.currentText()))
        print("Age : {0}".format(self.ageSpinBar.text()))

        # closing the window
        self.close()

    # creating form method
    def createForm(self):

        # creating a from layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name"), self.nameLineEdit)

        # for degree and adding spin box
        layout.addRow(QLabel("Age"), self.ageSpinBar)

        # setting layout
        self.formGroupBox.setLayout(layout)

# main method
if __name__ == '__main__':

    # Create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our window
    window = Window()
    
    # show the window
    window.show()

    # start the app
    sys.exit(app.exec())