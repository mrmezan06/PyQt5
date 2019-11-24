from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "QPush Button"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "male.png"
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.UIComponent()
        self.show()

    def UIComponent(self):
        button = QPushButton("Click Me", self)
        # button.move(100, 100)
        button.setGeometry(QRect(100, 100, 111, 50))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
