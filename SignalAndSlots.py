from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui, QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Events and Signals"
        self.top = 500
        self.left = 200
        self.width = 300
        self.height = 250
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("male.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateButton()
        self.show()

    def CreateButton(self):
        button = QPushButton("Click Me", self)
        # button.move(100, 100)
        button.setGeometry(QRect(100, 100, 111, 50))
        button.setIcon(QtGui.QIcon("male.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print("Hello World!")
        sys.exit()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
