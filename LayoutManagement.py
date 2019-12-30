from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQT5 Layout Management"
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
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupBox)
        self.setLayout(vboxLayout)
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What is your favourite sport?")
        hboxLayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon("football.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        hboxLayout.addWidget(button)

        button1 = QPushButton("Cricket", self)
        button1.setIcon(QtGui.QIcon("cricket.png"))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        hboxLayout.addWidget(button1)

        button2 = QPushButton("Tennis", self)
        button2.setIcon(QtGui.QIcon("tennis.png"))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        hboxLayout.addWidget(button2)

        self.groupBox.setLayout(hboxLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

