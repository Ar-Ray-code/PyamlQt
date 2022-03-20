import sys
import datetime
import time
import yaml
import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyamlqt5.create_widgets import create_widgets

TITLE = "Pyaml-Qt"
WIDTH = 1280
HEIGHT = 720
FONT = "Ubuntu"

YAML = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")

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
        pass
    
    def create_widgets(self):
        self.widgets, self.stylesheet = self.create_all_widgets(YAML)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])

        self.widgets["start_stop_button"].clicked.connect(self.button_update)

        self.widgets["exit_button"].clicked.connect(self.exit)
        self.widgets["spinbox"].valueChanged.connect(self.spinbox_update)

        self.widgets["progressbar"].setMaximum(100)
        self.widgets["progressbar"].setMinimum(0)
        self.widgets["progressbar"].setValue(50)

        self.widgets["lcd_number"].display(334)
        self.widgets["lineedit"].setText("qawsedrftgyhujikolp")

        # create timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start(1000)
    
    def spinbox_update(self):
        self.value = self.widgets["spinbox"].value()
    
    def button_update(self):
        if self.start_flag == False:
            self.start_flag = True
            self.widgets["start_stop_button"].setText('Stop')
            self.widgets["start_stop_button"].setStyleSheet(self.stylesheet["exit_button"])
            
            self.time_val = int(time.time()) + 5
        else:
            self.start_flag = False
            self.widgets["start_stop_button"].setText('Start')
            self.widgets["start_stop_button"].setStyleSheet(self.stylesheet["start_stop_button"])

    def exit(self):
        # ask
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                  "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                                    QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()

    def timer_update(self):
        self.time_val = int(time.time())
        
        if self.start_flag == True:
            self.number += 1
            if self.number >= 100:
                self.number = 0
        else:
            pass

        self.widgets["lcd_number"].display(self.number)
        self.widgets["progressbar"].setValue(self.number)
        self.widgets["spinbox"].setValue(self.number)
        self.widgets["slider"].setValue(self.number)

        self.widgets["time_label"].setText("Unixtime: " + str(self.time_val))
        self.widgets["datetime_label"].setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.update()
        self.show()
        self.timer.start(10)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
