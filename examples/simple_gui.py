import sys
import os

from pyamlqt.mainwindow import PyamlQtWindow
from PyQt6.QtWidgets import QApplication

YAML = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")

class MainWindow(PyamlQtWindow):
    def __init__(self):
        self.number = 0
        super().__init__("title", 0, 0, 800, 720, YAML)
        self.show()

def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    entry_point()