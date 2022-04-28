import time
import yaml
import os

from pyamlqt.create_widgets import create_widgets
import pyamlqt.qt6_switch as qt6_switch

qt6_mode = qt6_switch.qt6

if qt6_mode:
    from PyQt6.QtWidgets import QMainWindow
else:
    from PyQt5.QtWidgets import QMainWindow

class PyamlQtWindow(QMainWindow):
    def __init__(self, title: str, x: int, y: int, width: int, height: int, yaml_path:str = None):
        self.number = 0
        self.time_val = int(time.time())
        self.start_flag = False

        super().__init__()

        # geometry setting ---
        self.setWindowTitle(title)
        self.setGeometry(x, y, width, height)

        if yaml_path != None:
            self.create_widgets(yaml_path)

    def __del__(self):
        pass
    
    def create_widgets(self, yaml_path: str):
        # Template ---
        self.widgets, self.stylesheet = self.create_all_widgets(yaml_path)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ------------

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