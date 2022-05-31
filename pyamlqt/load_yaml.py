import sys
import os

from pyamlqt.mainwindow import PyamlQtWindow
from PyQt6.QtWidgets import QApplication

class MainWindow(PyamlQtWindow):
    def __init__(self, args):
        self.number = 0
        print(args)
        if (len(args) == 2):
            super().__init__(args[1])
            self.show()
        else:
            print("No args.")
            sys.exit()

def entry_point():
    app = QApplication(sys.argv)
    window = MainWindow(sys.argv)
    sys.exit(app.exec())

if __name__ == '__main__':
    entry_point()
