# creating the window
import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget): # creating window class 

    def __init__(self):
        super().__init__()
        self.title = "PyQT5 simple window - pythonspot.com" # initilize title
        self.left = 10 # left side
        self.top = 10 # top side
        self.width = 640 # width of the box
        self.height = 480 # height of the box
        self.initUI() # init ui vairable class

    def initUI(self): # creating ui
        self.setWindowTitle(self.title) # creating window
        self.setGeometry(self.left, self.top, self.width, self.height) # geometry
        self.show() # show window

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    ex = App()
    sys.exit(app.exec_())   