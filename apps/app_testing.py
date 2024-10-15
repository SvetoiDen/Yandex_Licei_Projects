import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,100,300,100)
        self.setWindowTitle('program')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())