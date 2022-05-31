import time
import yaml
import os

from pyamlqt.create_widgets import create_widgets
# from pyamlqt.window_configure import init_window
import pyamlqt.qt6_switch as qt6_switch

qt6_mode = qt6_switch.qt6

if qt6_mode:
    from PyQt6.QtWidgets import QMainWindow
else:
    from PyQt5.QtWidgets import QMainWindow

class PyamlQtWindow(QMainWindow):
    def __init__(self, yaml_path:str = None):
        self.yaml_abs_path = os.path.abspath(yaml_path)
        self.number = 0
        self.time_val = int(time.time())
        self.start_flag = False

        super().__init__()


        if yaml_path != None:
            self.init_window()
            self.create_widgets()
        
        # geometry setting ---
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

    def __del__(self):
        pass
    
    def create_widgets(self):
        # Template ---
        self.widgets, self.stylesheet = self.create_all_widgets()
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ------------

    def init_window(self):
        with open(self.yaml_abs_path, 'r') as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # unique key = WINDOW
        window_data = yaml_data["WINDOW"]
        self.width = window_data["width"]
        self.height = window_data["height"]
        self.x = window_data["x"]
        self.y = window_data["y"]
        self.title = window_data["title"]

# Template ================================================================
    def create_all_widgets(self) -> dict:
        widgets, stylesheet_str = dict(), dict()
        
        with open(self.yaml_abs_path, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        
            for key in self.yaml_data:
                data = create_widgets.create(self, self.yaml_abs_path, key)
                widgets[key], stylesheet_str[key] = data[0], data[1]

        return widgets, stylesheet_str
# =========================================================================