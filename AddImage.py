from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Add Image"
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
        image = QLabel(self)
        pxmap = QPixmap("swift.png")
        image.setPixmap(pxmap)
        vbox.addWidget(image)
        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
