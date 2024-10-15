import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSlider, QLabel
)
from PyQt6.QtGui import QImage, QPixmap, QMouseEvent


class AlphaManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('А вот все')
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(500, 400)

        self.orig = QImage()
        self.orig.load('orig.jpg')
        self.img = QLabel(self)

        self.img.setGeometry(60, 20, 300, 300)
        self.img.setPixmap(QPixmap(self.orig))

        self.alpha = QSlider(self)
        self.alpha.setMaximum(255)
        self.alpha.setMinimum(0)
        self.alpha.setValue(255)
        self.alpha.valueChanged.connect(self.slider_alpha)
        self.alpha.setGeometry(5, 10, 20, 200)

    def slider_alpha(self):
        self.orig.set
        self.orig.save('new.jpg')

        self.orig.load('new.jpg')
        self.img.setPixmap(QPixmap(self.orig))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = AlphaManagement()
    m.show()
    sys.exit(app.exec())