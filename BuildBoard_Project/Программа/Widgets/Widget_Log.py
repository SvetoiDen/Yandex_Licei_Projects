from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class Widget_Log(QWidget):
    def __init__(self, itogLog):
        super().__init__()
        self.setWindowTitle('Log_Buildboard')
        self.setWindowIcon(QIcon('./config/image_project/icon.ico'))
        self.setFixedSize(350, 320)
        self.itogLog = itogLog

        list_label = []

        QFontDatabase.addApplicationFont('./config/font_project/Bitter-ExtraBold.ttf')
        new_famaly = QFontDatabase.applicationFontFamilies(0)
        self._fontCreate = QFont(new_famaly, 12)
        self._fontCreate.setBold(True)
        self.Layout_Itog = QVBoxLayout()

        for name, value in self.itogLog.items():
            label = QLabel(f'{name} - {value}', self)
            label.setObjectName(name)
            label.setFont(self._fontCreate)
            list_label.append(label.objectName())
            self.Layout_Itog.addWidget(label)

        self.setLayout(self.Layout_Itog)
