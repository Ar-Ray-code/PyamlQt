import PyQt5
import sys
import datetime
import time
import os

from pyamlqt5.create_widgets import create_widgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import yaml

# FONT = "Chilanka"
TITLE = "calc"
WIDTH = 700
HEIGHT = 920
FONT = "Ubuntu"

PLUS = -2
EQUAL = -3

YAML = os.path.join(os.path.dirname(__file__), "../yaml/calculator.yaml")

class MainWindow(QMainWindow):
    def __init__(self):
        self.stylesheet = {}
        self.element_dict = {}
        self.number = 0

        self.time_val = int(time.time())
        self.start_flag = False

        super().__init__()

        self.setWindowTitle(TITLE)
        self.setGeometry(0, 0, WIDTH, HEIGHT)

        self.create_widgets()

    def __del__(self):
        self.timer.stop()
        pass
    
    def create_widgets(self):
        self.widgets, self.stylesheet = self.create_all_widgets(YAML)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])

        # start-stop button
        self.widgets["button_1"].clicked.connect(lambda: self.button_update(1))
        self.widgets["button_2"].clicked.connect(lambda: self.button_update(2))
        self.widgets["button_3"].clicked.connect(lambda: self.button_update(3))
        self.widgets["button_4"].clicked.connect(lambda: self.button_update(4))
        self.widgets["button_5"].clicked.connect(lambda: self.button_update(5))
        self.widgets["button_6"].clicked.connect(lambda: self.button_update(6))
        self.widgets["button_7"].clicked.connect(lambda: self.button_update(7))
        self.widgets["button_8"].clicked.connect(lambda: self.button_update(8))
        self.widgets["button_9"].clicked.connect(lambda: self.button_update(9))
        self.widgets["button_0"].clicked.connect(lambda: self.button_update(0))
        self.widgets["button_plus"].clicked.connect(lambda: self.button_update(PLUS))
        self.widgets["button_equal"].clicked.connect(lambda: self.button_update(EQUAL))

        # show
        self.show()

# Template ================================================================
    def create_all_widgets(self, yaml_path: str) -> dict:
        widgets = dict()
        stylesheet_str = dict()
        data = tuple()

        with open(yaml_path, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        
            for key in self.yaml_data:
                if self.yaml_data[key]['type'] == 'pushbutton':
                    data = create_widgets.create_pushbutton(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'label':
                    data = create_widgets.create_label(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'lcdnumber':
                    data = create_widgets.create_lcdnumber(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'spinbox':
                    data = create_widgets.create_spinbox(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'progressbar':
                    data = create_widgets.create_progressbar(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'combobox':
                    data = create_widgets.create_combobox(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'lineedit':
                    data = create_widgets.create_lineedit(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'checkbox':
                    data = create_widgets.create_checkbox(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'slider':
                    data = create_widgets.create_slider(self, yaml_path, key)
                elif self.yaml_data[key]['type'] == 'image':
                    data = create_widgets.create_imagelabel(self, yaml_path, key, os.path.abspath(os.path.dirname(__file__)) + "/../")
                    
                else:
                    print ('missing type')
                widgets[key] = data[0]
                stylesheet_str[key] = data[1]

        return widgets, stylesheet_str
    # =========================================================================
    # 1~9
    def button_update(self, number:int = -1):
        if number >= 0:
            self.number = number
        else:
            if number == PLUS:
                self.cache = self.number
                self.number = 0
            elif number == EQUAL:
                self.number = self.cache + self.number
                self.cache = 0
            else:
                pass
        self.widgets["lcd"].display(self.number)

    def exit(self):
        # ask
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                  "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                                    QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
