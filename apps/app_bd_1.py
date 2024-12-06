import random

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QLineEdit, QTableWidgetItem, QPushButton
)
import csv
import sys


class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hel')
        self.setFixedSize(600, 600)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 500, 450)
        self.total = QLineEdit(self)
        self.total.setGeometry(150, 500, 200, 20)
        self.updateButton = QPushButton('обновить', self)
        self.updateButton.setGeometry(10, 500, 80, 40)

        self.load_csv()
        self.color_top()
        self.tableWidget.cellChanged.connect(self.set_price)
        self.updateButton.clicked.connect(self.color_top)

    def load_csv(self):
        with open('price.csv', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            title = next(reader) + ['Количество']
            reader = sorted(reader, key=lambda x: int(x[1]), reverse=True)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
                self.tableWidget.setItem(i, j, QTableWidgetItem("0"))
        self.tableWidget.resizeColumnsToContents()

    def set_price(self):
        itog = 0
        for i in range(self.tableWidget.rowCount()):
            price = int(self.tableWidget.item(i, 1).text())
            cnt = int(self.tableWidget.item(i, 2).text())

            itog += price * cnt
        self.total.setText(str(itog))

    def color_top(self):
        for i in range(self.tableWidget.rowCount()):
            if i > 4:
                break
            qc = QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.item(i, j).setBackground(qc)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = InteractiveReceipt()
    m.show()
    sys.exit(app.exec())
