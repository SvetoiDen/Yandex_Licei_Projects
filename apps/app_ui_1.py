from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLineEdit,
    QPushButton, QButtonGroup
)
from PyQt6 import uic
import sys, io

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>616</width>
    <height>439</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Текстовый флаг</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>150</y>
      <width>139</width>
      <height>131</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>23</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет #1</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_1">
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>150</y>
      <width>139</width>
      <height>131</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="font">
        <font>
         <pointsize>23</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет #2</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_5">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_6">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>150</y>
      <width>139</width>
      <height>131</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QLabel" name="label_3">
       <property name="font">
        <font>
         <pointsize>23</pointsize>
        </font>
       </property>
       <property name="text">
        <string>Цвет #3</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Синий</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Красный</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_9">
       <property name="text">
        <string>Зелёный</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="make_flag">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>310</y>
      <width>121</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Создать Флаг</string>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>360</y>
      <width>400</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цвета:</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.setFixedSize(567, 450)
        self.color_group_1 = QButtonGroup(self)
        self.color_group_1.addButton(self.radioButton_1)
        self.color_group_1.addButton(self.radioButton_2)
        self.color_group_1.addButton(self.radioButton_3)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_2.addButton(self.radioButton_4)
        self.color_group_2.addButton(self.radioButton_5)
        self.color_group_2.addButton(self.radioButton_6)
        self.color_group_3 = QButtonGroup(self)
        self.color_group_3.addButton(self.radioButton_7)
        self.color_group_3.addButton(self.radioButton_8)
        self.color_group_3.addButton(self.radioButton_9)

        self.make_flag.clicked.connect(self.set_flag)

    def set_flag(self):
        text = ''
        for but in self.color_group_1.buttons():
            if but.isChecked():
                text += f"{but.text()}, "

        for but in self.color_group_2.buttons():
            if but.isChecked():
                text += f"{but.text()} и "

        for but in self.color_group_3.buttons():
            if but.isChecked():
                text += f"{but.text()}"

        self.result.setText(f'Цвета: {text}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = FlagMaker()
    f.show()
    sys.exit(app.exec())
