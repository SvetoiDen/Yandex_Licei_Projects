from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QPushButton, QLabel
)
import sys


class Evelator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вычесление выражений')
        self.setGeometry(300, 300, 220, 110)

        self.label = QLabel('Выражение', self)
        self.label.setGeometry(5, 5, 100, 20)

        self.label1 = QLabel('Результат', self)
        self.label1.setGeometry(110, 5, 100, 20)

        self.first_value = QLineEdit(self)
        self.first_value.setGeometry(5, 30, 80, 20)

        self.second_value = QLineEdit(self)
        self.second_value.setGeometry(110, 30, 80, 20)

        self.trick_button = QPushButton('->', self)
        self.trick_button.setGeometry(88, 30, 20, 20)
        self.trick_button.clicked.connect(self.eval_app)

    def eval_app(self):
        text_app = self.first_value.text()
        res = eval(text_app)
        res = str(res)
        self.second_value.setText(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trick = Evelator()
    trick.show()
    sys.exit(app.exec())
