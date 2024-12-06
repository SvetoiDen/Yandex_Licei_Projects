from PyQt6.QtGui import QKeyEvent, QPixmap
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer
from config.function_project.SQLite_Class import SQLite_project
from Widgets.Widget_Log import Widget_Log
import datetime

itogLog = {'Показано рекламы': 0, 'Удалено билбордов': 0, 'Начало показа': '', 'Конец показа': ''}


class Widget_FullScreen(QWidget):
    def __init__(self):
        super().__init__()
        global isLog, itogLog
        self.setWindowTitle("FullScreen BuildBoard")
        self.resize(200, 200)
        self.label = QLabel(self)
        self.label.setFixedSize(1980, 1080)

        itogLog['Начало показа'] = datetime.datetime.now().strftime('%d-%m-%Y : %X')
        self.image_index = 0
        self.img_data = {}
        self.get_dict_data_img()

        self.load_image()
        self._timer = QTimer(self)
        self._timer.start(60000)
        self._timer.timeout.connect(self.load_image)

    def keyPressEvent(self, event: QKeyEvent):
        # закрытие полноэкранного показа через Escape
        if event.key() == Qt.Key.Key_Escape:
            global isLog, itogLog
            self._timer.stop()
            itogLog['Конец показа'] = datetime.datetime.now().strftime('%d-%m-%Y : %X')
            self.widget_log = Widget_Log(itogLog)
            self.widget_log.show()
            self.close()

    def get_itogLog(self):
        return self.itogLog

    def get_dict_data_img(self):
        # создание начального словаря со всеми билбордами
        cur = SQLite_project()
        self.img_src = cur.select_gets("SELECT image_src, timer FROM buildboards")
        cur.close()

        i = 0
        for row in self.img_src:
            if i == 0:
                self.img_data[f"{row[0]}"] = 1
            else:
                self.img_data[f"{row[0]}"] = 0
            i += 1

    def load_image(self):
        global isLog, itogLog
        # функция по загрузке картинок через интервал времени
        cur = SQLite_project()
        self.img_src = cur.select_gets("SELECT image_src, timer FROM buildboards")
        self.timer_data = cur.select_get(
            f"SELECT id, timer, money FROM timers WHERE id = {self.img_src[self.image_index][1]}")
        self.len_src_image = len(self.img_src) - 1
        cur.close()

        pixmap = QPixmap()
        self.label.setPixmap(pixmap)
        pixmap.load(self.img_src[self.image_index][0])
        self.label.setPixmap(pixmap)

        if self.img_data.get(self.img_src[self.image_index][0]) >= self.timer_data[1]:
            self.img_data.__delitem__(self.img_src[self.image_index][0])
            cur = SQLite_project()
            cur.commit_query(f"DELETE FROM buildboards WHERE image_src = '{self.img_src[self.image_index][0]}'")
            cur.close()
            itogLog['Удалено билбордов'] = itogLog.get('Удалено билбордов') + 1
            if self.image_index < self.len_src_image:
                self.image_index += 1
            else:
                self.image_index = 0
            return

        if self.image_index == self.len_src_image:
            self.image_index = 0
            self.img_data[self.img_src[self.image_index][0]] = self.img_data.get(self.img_src[self.image_index][0]) + 1
            return

        self.img_data[self.img_src[self.image_index][0]] = self.img_data.get(self.img_src[self.image_index][0]) + 1
        self.image_index += 1
        itogLog['Показано рекламы'] = itogLog.get('Показано рекламы') + 1
