from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.lab = QLabel("Chosen Option : Swift")
        self.lab.setFont(QtGui.QFont("Sanserif", 18))
        self.radioBtn1 = QRadioButton("Swift")
        self.radioBtn2 = QRadioButton("Java")
        self.radioBtn3 = QRadioButton("C#")
        self.radioBtn4 = QRadioButton("Python")
        self.groupBox = QGroupBox("What Is Your Favourite Programming Language ?")
        self.title = "PyQT5 Radio Button"
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
        self.radioButton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.lab)
        self.setLayout(vbox)
        self.show()

    def radioButton(self):

        self.groupBox.setFont(QtGui.QFont("Sanserif", 15))
        hbxly = QHBoxLayout()

        self.radioBtn1.setChecked(True)

        icon1 = QtGui.QIcon("swift.png")
        icon2 = QtGui.QIcon("java.jpg")
        icon3 = QtGui.QIcon("csharp.png")
        icon4 = QtGui.QIcon("python.png")
        self.radioBtn1.setIcon(icon1)
        self.radioBtn2.setIcon(icon2)
        self.radioBtn3.setIcon(icon3)
        self.radioBtn4.setIcon(icon4)

        size = QtCore.QSize(40, 40)
        self.radioBtn1.setIconSize(size)
        self.radioBtn2.setIconSize(size)
        self.radioBtn3.setIconSize(size)
        self.radioBtn4.setIconSize(size)

        # Event Action
        self.radioBtn1.toggled.connect(self.OnRBClick)
        self.radioBtn2.toggled.connect(self.OnRBClick)
        self.radioBtn3.toggled.connect(self.OnRBClick)
        self.radioBtn4.toggled.connect(self.OnRBClick)

        hbxly.addWidget(self.radioBtn1)
        hbxly.addWidget(self.radioBtn2)
        hbxly.addWidget(self.radioBtn3)
        hbxly.addWidget(self.radioBtn4)

        self.groupBox.setLayout(hbxly)

    def OnRBClick(self):
        rbtn = self.sender()
        if rbtn.isChecked():
            self.lab.setText("Chosen Option : " + rbtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
