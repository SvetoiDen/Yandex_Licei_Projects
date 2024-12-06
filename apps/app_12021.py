from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
import sys
import random


class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btnx = 150
        self.btny = 150

        self.setMouseTracking(True)

        self.setFixedSize(400,400)
        self.btn = QPushButton('Нажми на меня', self)
        self.btn.setGeometry(self.btnx, self.btny, 90, 40)

    def mouseMoveEvent(self, event):
        mousex = event.pos().x()
        mousey = event.pos().y()

        if self.btnx + 15 == mousex or self.btny + 15 == mousey:
            print(1)
            self.btnx = random.randint(50, 200)
            self.btny = random.randint(50, 200)

            self.btn.move(self.btnx,self.btny)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMain()
    main.show()
    sys.exit(app.exec())