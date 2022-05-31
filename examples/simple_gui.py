import sys
import os

from pyamlqt.mainwindow import PyamlQtWindow
from PyQt6.QtWidgets import QApplication

class MainWindow(PyamlQtWindow):
    def __init__(self):
        self.number = 0
        yaml_path = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")
        super().__init__(yaml_path)
        self.show()

def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    entry_point()