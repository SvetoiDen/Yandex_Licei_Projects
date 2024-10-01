from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QPushButton, QCheckBox
)
import sys


class WidgetsHideNSeek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Прятки')
        self.setGeometry(300, 300, 200, 100)

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.setGeometry(5, 5, 50, 20)

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.setGeometry(5, 25, 50, 20)

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.setGeometry(5, 45, 50, 20)

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.setGeometry(5, 65, 50, 20)

        self.edit1 = QLineEdit('поле edit1', self)
        self.edit1.setGeometry(60, 5, 80, 20)

        self.edit2 = QLineEdit('поле edit2', self)
        self.edit2.setGeometry(60, 25, 80, 20)

        self.edit3 = QLineEdit('поле edit3', self)
        self.edit3.setGeometry(60, 45, 80, 20)

        self.edit4 = QLineEdit('поле edit4', self)
        self.edit4.setGeometry(60, 65, 80, 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    trick = WidgetsHideNSeek()
    trick.show()
    sys.exit(app.exec())
