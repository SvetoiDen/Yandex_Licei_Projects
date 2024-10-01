from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QPushButton
)
import sys


class WordTrick(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Фокус со словами')
        self.setGeometry(300, 300, 200, 100)

        self.first_value = QLineEdit(self)
        self.first_value.setGeometry(5, 10, 80, 20)

        self.second_value = QLineEdit(self)
        self.second_value.setGeometry(110, 10, 80, 20)

        self.trick_button = QPushButton('->', self)
        self.trick_button.setGeometry(88, 10, 20, 20)
        self.trick_button.clicked.connect(self.trick)

    def trick(self):
        if self.trick_button.text() == '->':
            if self.first_value.text():
                self.second_value.setText(self.first_value.text())
                self.first_value.clear()
                self.trick_button.setText('<-')
            else:
                self.second_value.clear()
                self.first_value.setText("")
                self.trick_button.setText('<-')
        elif self.trick_button.text() == '<-':
            if self.second_value.text():
                self.first_value.setText(self.second_value.text())
                self.second_value.clear()
                self.trick_button.setText('->')
            else:
                self.first_value.clear()
                self.second_value.setText("")
                self.trick_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trick = WordTrick()
    trick.show()
    sys.exit(app.exec())
