import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Nim Strikes Back")

        self.X = random.randint(10, 50)  # Начальное значение X
        self.Y = random.randint(1, 10)  # Значение для увеличения
        self.Z = random.randint(1, 10)  # Значение для уменьшения
        self.turns_left = 10

        # Создание виджетов
        self.layout = QVBoxLayout()

        self.xlabel = QLabel(f"Текущее значение: {self.X}", self)
        self.layout.addWidget(self.xlabel)

        self.turns_label = QLabel(f"Осталось ходов: {self.turns_left}", self)
        self.layout.addWidget(self.turns_label)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)

        # Кнопка для увеличения на Y
        self.btnp = QPushButton(f"Увеличить на {self.Y}", self)
        self.btnp.clicked.connect(self.increase_value)
        self.layout.addWidget(self.btnp)

        # Кнопка для уменьшения на Z
        self.btnm = QPushButton(f"Уменьшить на {self.Z}", self)
        self.btnm.clicked.connect(self.decrease_value)
        self.layout.addWidget(self.btnm)

        self.setLayout(self.layout)

    def update_labels(self):
        self.xlabel.setText(f"Текущее значение: {self.X}")
        self.turns_label.setText(f"Осталось ходов: {self.turns_left}")
        self.result_label.setText("")

    def increase_value(self):
        if self.turns_left > 0:
            self.X += self.Y
            self.turns_left -= 1
            self.check_win_loss()
        else:
            self.end_game("Проигрыш! Попробуйте снова.")
        self.update_labels()

    def decrease_value(self):
        if self.turns_left > 0:
            self.X -= self.Z
            self.turns_left -= 1
            self.check_win_loss()
        else:
            self.end_game("Проигрыш! Попробуйте снова.")
        self.update_labels()

    def check_win_loss(self):
        if self.X == 0:
            self.end_game("Поздравляем, вы выиграли!")
        elif self.turns_left == 0:
            self.end_game("Проигрыш! Попробуйте снова.")

    def end_game(self, message):
        print(message)
        self.result_label.setText(message)

        self.X = random.randint(10, 50)  # Начальное значение X
        self.Y = random.randint(1, 10)  # Значение для увеличения
        self.Z = random.randint(1, 10)  # Значение для уменьшения
        self.turns_left = 10
        self.update_labels()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = NimStrikesBack()
    game.show()
    sys.exit(app.exec())
