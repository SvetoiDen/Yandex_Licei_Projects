from Widgets.Widgets_CreateBuildBoard import Create_BuildBoard
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QMessageBox, QWidget, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont, QIcon
from Widgets.Widget_FullScreenBuildBoard import Widget_FullScreen
from config.function_project.SQLite_Class import SQLite_project
import sys


class Project_BuildBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        # вызываем стили и вставляем в проект
        with open('./config/style.css', 'r') as file:
            self.setStyleSheet(file.read())
        self.setWindowIcon(QIcon('config/image_project/icon.ico'))

        # вызываем второе и третье окно, которое неактивно
        self.openCrt = Create_BuildBoard()
        # создаем вертикальный Layout для кнопок и помещаем
        widget_layout = QWidget()
        self._layoutmain = QVBoxLayout()
        self._layoutmain.setContentsMargins(25, 20, 25, 20)
        self._layoutmain.setSpacing(20)
        widget_layout.setLayout(self._layoutmain)
        # создаем основное окно
        self.setWindowTitle('Редактор Билбортов')
        self.setFixedSize(330, 300)
        self.btn_buildboard = QPushButton('Создать билборд')
        self.btn_buildboard.setProperty("class", "btn_main")
        font = QFont()
        font.setFamily('config/font_project/Bitter-ExtraBold.ttf')
        self.btn_buildboard.setFont(font)
        # Прописываем класс кнопке
        self.btn_fullScreen = QPushButton('Начать показ билбордов')
        self.btn_fullScreen.setProperty("class", "btn_main")
        self.btn_fullScreen.setFont(font)
        self.btn_buildboard.clicked.connect(self.open_createBuildBoard)
        self.btn_fullScreen.clicked.connect(self.open_fullscreenwidget)
        # Добавляем таблицу об отображения билдбордов
        self.tablebuildboard = QTableWidget()
        self.sqlite_buildboard_get()

        self._layoutmain.addWidget(self.btn_buildboard, 1)
        self._layoutmain.addWidget(self.btn_fullScreen, 2)
        self._layoutmain.addWidget(self.tablebuildboard, 3)
        self.setCentralWidget(widget_layout)

    # Пишем функцию вызова второго окна
    def open_createBuildBoard(self):
        if self.openCrt.isVisible():
            self.openCrt.hide()
        else:
            self.openCrt.show()

    def sqlite_buildboard_get(self):
        cur = SQLite_project()
        data = cur.select_gets("SELECT name, image_src FROM buildboards")
        cur.close()

        self.tablebuildboard.setRowCount(0)
        self.tablebuildboard.setColumnCount(2)
        for i, row in enumerate(data):
            self.tablebuildboard.setRowCount(self.tablebuildboard.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tablebuildboard.setItem(i,j, QTableWidgetItem(elem))

    def open_fullscreenwidget(self):
        cur = SQLite_project()
        if not cur.select_get("SELECT * FROM buildboards") is None:
            # вызываем третье окно, и сразу в фулл экран
            self.openFullScreen = Widget_FullScreen()
            self.openFullScreen.showFullScreen()

        else:
            qmb = QMessageBox()
            btn = qmb.warning(self, 'Ошибка!', 'У вас нету записей. Воспроизведение не может быть')
        cur.close()

    # ивент закрытия всех окон
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()

# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    main = Project_BuildBoard()
    main.showNormal()
    sys.exit(app.exec())
