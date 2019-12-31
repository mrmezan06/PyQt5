from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QVBoxLayout,QGridLayout
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQT5 Grid Layout"
        self.left = 500
        self.top = 200
        self.width = 540
        self.height = 360
        self.iconName = "male.png"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What is your favourite programming language?")
        gridLayout = QGridLayout()

        button0 = QPushButton("Java", self)
        button0.setIcon(QtGui.QIcon("java.jpg"))
        button0.setIconSize(QtCore.QSize(40, 40))
        button0.setMinimumHeight(40)
        gridLayout.addWidget(button0, 0, 0)

        button1 = QPushButton("Python", self)
        button1.setIcon(QtGui.QIcon("python.png"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("Swift", self)
        button2.setIcon(QtGui.QIcon("swift.png"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 0, 2)

        button3 = QPushButton("C# (C-Sharp)", self)
        button3.setIcon(QtGui.QIcon("csharp.png"))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 0)

        button4 = QPushButton("C++", self)
        button4.setIcon(QtGui.QIcon("cplusplus.png"))
        button4.setIconSize(QtCore.QSize(40, 40))
        button4.setMinimumHeight(40)
        gridLayout.addWidget(button4, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())