from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QPushButton, QLabel, QLCDNumber
)
import sys


class MiniCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Миникалькулятор')
        self.setGeometry(300, 300, 220, 210)

        self.label = QLabel('Первое число (целое)', self)
        self.label.setGeometry(5, 5, 200, 20)

        self.label1 = QLabel('Второе число (целое)', self)
        self.label1.setGeometry(5, 50, 200, 20)

        self.label2 = QLabel('Сумма', self)
        self.label2.setGeometry(5, 100, 200, 20)

        self.label3 = QLabel('Разность', self)
        self.label3.setGeometry(5, 120, 200, 20)

        self.label4 = QLabel('Произведения', self)
        self.label4.setGeometry(5, 140, 200, 20)

        self.label5 = QLabel('Частное', self)
        self.label5.setGeometry(5, 160, 200, 20)

        self.number_1 = QLineEdit(self)
        self.number_1.setGeometry(5, 30, 80, 20)

        self.number_2 = QLineEdit(self)
        self.number_2.setGeometry(5, 70, 80, 20)

        self.result_sum = QLCDNumber(self)
        self.result_sum.setGeometry(70, 100, 100, 20)

        self.result_sub = QLCDNumber(self)
        self.result_sub.setGeometry(70, 120, 100, 20)

        self.result_mul = QLCDNumber(self)
        self.result_mul.setGeometry(100, 140, 100, 20)

        self.result_div = QLCDNumber(self)
        self.result_div.setGeometry(70, 160, 100, 20)

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.setGeometry(88, 30, 20, 20)
        self.calculate_button.clicked.connect(self.calc_app)

    def calc_app(self):
        t1 = int(self.number_1.text())
        t2 = int(self.number_2.text())

        self.result_sum.display(str(eval(f"{t1}+{t2}")))
        self.result_sub.display(str(eval(f"{t1}-{t2}")))
        self.result_mul.display(str(eval(f"{t1}*{t2}")))
        try:
            self.result_div.display(str(round(eval(f"{t1}/{t2}"), 3)))
        except Exception:
            self.result_div.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trick = MiniCalculator()
    trick.show()
    sys.exit(app.exec())
