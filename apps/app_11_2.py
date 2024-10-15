import sys
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QTextEdit, QApplication
)


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('program')

        self.button = QPushButton('Получить', self)
        self.text_field = QTextEdit(self)

        self.button.clicked.connect(self.get_slovo)

        self.button.setGeometry(5, 10, 70, 20)
        self.text_field.setGeometry(90, 10, 200, 20)

    def get_slovo(self):
        import random

        with open('lines.txt', 'r', encoding='utf-8') as file:
            f = file.readlines()

        try:
            l1 = f[random.randint(0, len(f) - 1)]
            self.text_field.setText(l1)
        except ValueError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomString()
    window.show()
    sys.exit(app.exec())
