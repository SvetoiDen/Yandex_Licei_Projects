from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QLineEdit, QTableWidgetItem, QLayout
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
        self.total.setGeometry(50, 500, 200, 20)

        self.load_csv()
        self.tableWidget.cellChanged.connect(self.set_price)

    def load_csv(self):
        with open('price.csv', encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            title = next(reader) + ['Количество']
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = InteractiveReceipt()
    m.show()
    sys.exit(app.exec())
