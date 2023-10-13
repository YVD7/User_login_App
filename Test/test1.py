# Importing the libraries
# for application, widget , pushbutton, box layout
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout #,QLabel
from PyQt5.QtCore import Qt # importing core 
from PyQt5.QtGui import QPalette, QColor # 
app = QApplication([])

# label = QLabel("Hello World!")
# label.show()
# app.exec()

# Creating the top and buttom buttons
# window = QWidget() # for creating window with the help of QWidget
# layout = QVBoxLayout() # creating layout of the box
# layout.addWidget(QPushButton('Top')) # Adding the top button with QPushbutton
# layout.addWidget(QPushButton('Bottom')) # adding bottom button with QPushbutton
# window.setLayout(layout) # sestting the layout 
# window.show() # showing window
# app.exec() # finally executing the application

# Custom colors and styles
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.buttonText, arc=QPalette.ColorRole, acolor=QColor())
app.setPalette(palette)
button = QPushButton("Hello World!")
button.show()
app.exec()

