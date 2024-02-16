import sys
import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_game import MainGame
import json

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>739</width>
    <height>407</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>140</y>
      <width>261</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>Начать игру</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>20</y>
      <width>331</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:26pt; font-weight:600;&quot;&gt;Ball Bounce&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>801</width>
      <height>581</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(222, 255, 225);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>150</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:12pt; font-weight:600;&quot;&gt;Размер коробки&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>220</y>
      <width>31</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>ок</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>122</x>
      <y>220</y>
      <width>51</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>62</x>
      <y>220</y>
      <width>51</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>180</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>от 100 до 1000</string>
    </property>
   </widget>
   <zorder>label_2</zorder>
   <zorder>pushButton</zorder>
   <zorder>label</zorder>
   <zorder>label_3</zorder>
   <zorder>pushButton_2</zorder>
   <zorder>lineEdit</zorder>
   <zorder>lineEdit_2</zorder>
   <zorder>label_4</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>739</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class mainmenu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.show()
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.size)

    def start(self):
        self.hide()
        QApplication.exit(0)
        MainGame.run()

    def size(self):
        import json
        with open('size.json') as f:
            data = json.load(f)
        data['size'][1] = self.lineEdit.text()
        data['size'][0] = self.lineEdit_2.text()
        with open('size.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    application = QApplication(sys.argv)
    window = mainmenu()
    sys.exit(application.exec())

if __name__ == '__main__':
    main()