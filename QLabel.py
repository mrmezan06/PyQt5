from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Label"
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
        vbox = QVBoxLayout()
        label = QLabel("This is PyQt5 Label")
        vbox.addWidget(label)
        l2 = QLabel("PyQt5 GUI App Development")
        l2.setFont(QtGui.QFont("Sanserif", 20))
        l2.setStyleSheet('color:red')
        vbox.addWidget(l2)
        self.setLayout(vbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
