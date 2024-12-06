import shutil
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox, QFileDialog, QRadioButton, QHBoxLayout, QButtonGroup
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QFontDatabase, QIcon
from config.function_project.SQLite_Class import SQLite_project


class Create_BuildBoard(QWidget):
    def __init__(self):
        super().__init__()
        with open('./config/style.css', 'r') as file:
            self.setStyleSheet(file.read())
        self.setWindowIcon(QIcon('./config/image_project/icon.ico'))

        QFontDatabase.addApplicationFont('config/font_project/Bitter-ExtraBold.ttf')
        self.new_famaly = QFontDatabase.applicationFontFamilies(0)
        self._fontCreate = QFont(self.new_famaly, 11)

        # создаем второе окно для создания нового билдборда
        # присваиваем шрифт и стили к кнопке и тексту
        # добавляем вертикальный Layout и добавляем к нему виджеты
        # добавляем другие Layout

        self._imagebuildboard = {}

        self.layoutCreate = QVBoxLayout()
        self.layoutCreate.setContentsMargins(30, 10, 30, 10)
        self.layoutCreate.setSpacing(7)
        self.setWindowTitle('Создание билборта')
        self.setFixedSize(475, 200)
        self.label1 = QLabel('Создание Билбордов')

        self._font1 = QFont()
        self._font1.setPointSize(18)
        self._font1.setFamily('TT Commons Bold')

        self.label1.setFont(self._font1)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._linkimg = QPushButton('Добавить изображение')
        self._linkimg.setFont(self._fontCreate)
        self._namebuildboard = QLineEdit()
        self._namebuildboard.setFont(self._fontCreate)
        self._namebuildboard.setPlaceholderText('Введите название билборда')
        self._linkimg.clicked.connect(self.getImagebuildboard)

        self._buttonready = QPushButton('Создать билдборд', self)
        self._buttonready.setFont(self._fontCreate)
        self._buttonready.clicked.connect(self.readybuildboard)

        self.label2 = QLabel('Выберите таймер:', self)
        self.label2.setFont(self._fontCreate)
        self._radiotimer1 = QRadioButton('12Д 12Ч', self)
        self._radiotimer2 = QRadioButton('16Д 12Ч', self)
        self._radiotimer3 = QRadioButton('24Д 12Ч', self)
        self._radiotimer1.setFont(self._fontCreate)
        self._radiotimer2.setFont(self._fontCreate)
        self._radiotimer3.setFont(self._fontCreate)
        self.layoutradiobut = QHBoxLayout()
        self.groupraduibut = QButtonGroup()

        self.groupraduibut.addButton(self._radiotimer1)
        self.groupraduibut.addButton(self._radiotimer2)
        self.groupraduibut.addButton(self._radiotimer3)
        self.groupraduibut.buttonClicked.connect(self.clickedradiobutton)

        self.layoutradiobut.addWidget(self.label2)
        self.layoutradiobut.addWidget(self._radiotimer1)
        self.layoutradiobut.addWidget(self._radiotimer2)
        self.layoutradiobut.addWidget(self._radiotimer3)

        self.layoutCreate.addWidget(self.label1)
        self.layoutCreate.addWidget(self._linkimg)
        self.layoutCreate.addWidget(self._namebuildboard)
        self.layoutCreate.addLayout(self.layoutradiobut, 1)
        self.layoutCreate.addWidget(self._buttonready)
        self.setLayout(self.layoutCreate)

        self._linkimg.setProperty('class', 'btn_widget')
        self._buttonready.setProperty('class', 'btn_widget')

    # функция добавления файла
    def getImagebuildboard(self):
        self.file = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'Рисунок (*.jpg)')[0]

        if not self.file == '':
            self._namefile = self.file.split('/')[len(self.file.split('/')) - 1]
            self._imagebuildboard.clear()

            pixmap_check = QPixmap(self.file)
            if pixmap_check.width() == 1920 and pixmap_check.height() == 1080:
                self.file_check = self.file.split(sep='/')
                if 'image_buildboard' in self.file_check and 'config' in self.file_check:
                    dlg = QMessageBox(self)
                    btn = dlg.warning(self, 'Ошибка!', 'Вы берете этот же файл из директории программы.')
                    return

                self._imagebuildboard[self._namefile] = f'config/image_buildboard/{self._namefile}'

                dlg = QMessageBox(self)
                dlg.setWindowTitle("Изображение добавлено")
                dlg.setText(f"Ваше изображение {self._namefile} было добавлено в список билбордов")
                shutil.copy(self.file, 'config/image_buildboard')
                button = dlg.exec()
                return
            else:
                dlg = QMessageBox(self)
                btn = dlg.warning(self, 'Ошибка!',
                                  f'Размер изображения должен быть 1920 на 1080.\nВаша же картинка имеет размер {pixmap_check.width()} на {pixmap_check.height()}')
                return

    # функция добавления id по нажатии на RadioButton
    def clickedradiobutton(self):
        button = self.groupraduibut.checkedButton()
        if button == self._radiotimer1:
            self._imagebuildboard['but_check'] = 1
        elif button == self._radiotimer2:
            self._imagebuildboard['but_check'] = 2
        elif button == self._radiotimer3:
            self._imagebuildboard['but_check'] = 3

    # функция добавления записи в BD билдборд
    def readybuildboard(self):
        db = SQLite_project()

        try:
            if len(self._imagebuildboard) < 2 or self._namebuildboard.text() == "" or not self.groupraduibut.checkedButton().isChecked():
                dlg_error = QMessageBox(self)
                but = dlg_error.warning(self, "Ошибка!", "Не все данные были добавлены\nИли не был выбран таймер")
                return
        except Exception:
            dlg_error = QMessageBox(self)
            but = dlg_error.warning(self, "Ошибка!", "Не все данные были добавлены\nИли не был выбран таймер")
            return

        db.commit_query("INSERT INTO buildboards (name, image_src, timer) VALUES ('{}','{}',{})".format(
            self._namebuildboard.text(),
            self._imagebuildboard[self._namefile],
            self._imagebuildboard['but_check']
        ))

        self._imagebuildboard.clear()
        self._namebuildboard.clear()

        # регистрация и закрытие виджета
        db.close()
        dlg_access = QMessageBox(self)
        dlg_access.setWindowTitle("Ваш билдборд готов")
        dlg_access.setText(f"билдборд сохранен в базу данных")
        button = dlg_access.exec()
        self.hide()
