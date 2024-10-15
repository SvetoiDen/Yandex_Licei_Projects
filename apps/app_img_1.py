import io
import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QButtonGroup
)
from PyQt6.QtGui import QPixmap, QTransform, QImage
from PyQt6 import uic

patent = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>526</width>
    <height>446</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>50</y>
      <width>151</width>
      <height>271</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QPushButton" name="red">
       <property name="text">
        <string>R</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="green">
       <property name="text">
        <string>G</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="blue">
       <property name="text">
        <string>B</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="all_color">
       <property name="text">
        <string>ALL</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>330</y>
      <width>421</width>
      <height>51</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="left_image">
       <property name="text">
        <string>Против часовой стрелки</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="right_image">
       <property name="text">
        <string>По часовой стелки</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="img_label">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>160</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        p = io.StringIO(patent)
        uic.loadUi(p, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Картинка')
        self.setFixedSize(526, 446)

        self.file = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'Рисунок (*.jpg);;ПНГ (*.png)')[0]
        self.curr_image = QImage()
        self.curr_image.load(self.file)

        self.channelButtons = QButtonGroup(self)
        self.channelButtons.addButton(self.red)
        self.channelButtons.addButton(self.green)
        self.channelButtons.addButton(self.blue)

        self.red.clicked.connect(partial(self.set_color, self.red))
        self.green.clicked.connect(partial(self.set_color, self.green))
        self.blue.clicked.connect(partial(self.set_color, self.blue))

        self.rotateButtons = QButtonGroup(self)
        self.rotateButtons.addButton(self.left_image)
        self.rotateButtons.addButton(self.right_image)

        self.left_image.clicked.connect(partial(self.set_rsize, self.left_image))
        self.right_image.clicked.connect(partial(self.set_rsize, self.right_image))

        self.img = QPixmap(self.curr_image)

        self.img_label.setGeometry(220, 100, 200, 200)
        self.img_label.setPixmap(self.img)

    def set_color(self, btn: QPushButton):
        if btn.text() == 'R':
            self.curr_image.setPixelColor(255, 0, 0)
            self.curr_image.save('r.jpg')

            self.curr_image.load('r.jpg')
            self.img_label.setPixmap(QPixmap(self.curr_image))
        elif btn.text() == 'G':
            self.curr_image.setPixelColor(0, 255, 0)
            self.curr_image.save('r.jpg')

            self.curr_image.load('r.jpg')
            self.img_label.setPixmap(QPixmap(self.curr_image))
        elif btn.text() == 'B':
            self.curr_image.setPixelColor(0, 0, 255)
            self.curr_image.save('r.jpg')

            self.curr_image.load('r.jpg')
            self.img_label.setPixmap(QPixmap(self.curr_image))

    def set_rsize(self, btn: QPushButton):
        if btn.text() == 'Против часовой стрелки':
            self.curr_image.setDevicePixelRatio(45)
            self.curr_image.save('r.jpg')

            self.curr_image.load('r.jpg')
            self.img_label.setPixmap(QPixmap(self.curr_image))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MyPillow()
    m.show()
    sys.exit(app.exec())