import sys
import os
import yaml

from pyamlqt5.create_widgets import create_widgets

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

TITLE = "calc"
WIDTH = 700
HEIGHT = 920

PLUS = -2
EQUAL = -3

YAML = os.path.join(os.path.dirname(__file__), "../yaml/calculator.yaml")

class MainWindow(QMainWindow):
    def __init__(self):
        self.number = 0
        super().__init__()

        # geometry setting ---
        self.setWindowTitle(TITLE)
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.create_widgets()

    def __del__(self):
        pass
    
    def create_widgets(self):
        # Template ---
        self.widgets, self.stylesheet = self.create_all_widgets(YAML)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ------------

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
        widgets, stylesheet_str = dict(), dict()
        with open(yaml_path, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        
            for key in self.yaml_data:
                data = create_widgets.create(self, yaml_path, key, os.path.abspath(os.path.dirname(__file__)) + "/../")
                widgets[key], stylesheet_str[key] = data[0], data[1]

        return widgets, stylesheet_str
# =========================================================================

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
