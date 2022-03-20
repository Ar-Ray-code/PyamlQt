import sys
import os

from pyamlqt5.create_widgets import create_widgets
from PyQt5.QtWidgets import QApplication, QMainWindow

YAML = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")

class MainWindow(QMainWindow):
    def __init__(self):
        self.number = 0
        super().__init__()

        # geometry setting ---
        self.setWindowTitle("Simple GUI")
        self.setGeometry(0, 0, 800, 720)
        
        # Template ( Don't have to edit ) ==============
        self.widgets, self.stylesheet = self.create_all_widgets(YAML)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ==============================================

        # --- Your code ----
        # -*-*-*-*-*-*-*-*-*
        # -----------------
        
        self.show()

    # Template ( Don't have to edit ) ==============
    def create_all_widgets(self, yaml_path: str) -> dict:
        import yaml
        widgets, stylesheet_str = dict(), dict()
        with open(yaml_path, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        
            for key in self.yaml_data:
                data = create_widgets.create(self, yaml_path, key, os.path.abspath(os.path.dirname(__file__)) + "/../")
                widgets[key], stylesheet_str[key] = data[0], data[1]

        return widgets, stylesheet_str
    # ==============================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
