import sys
import os

from pyamlqt.mainwindow import PyamlQtWindow
import pyamlqt.qt6_switch as qt6_switch

qt6_mode = qt6_switch.qt6

if qt6_mode:
    from PyQt6.QtWidgets import QApplication
else:
    from PyQt5.QtWidgets import QApplication

PLUS = -2
EQUAL = -3

YAML = os.path.join(os.path.dirname(__file__), "../yaml/calculator.yaml")

class MainWindow(PyamlQtWindow):
    def __init__(self):
        self.number = 0
        super().__init__(YAML)

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

        for key in self.widgets.keys():
            if key == "lcd":
                self.widgets[key].setStyleSheet(self.stylesheet[key])
            else:
                self.widgets[key].setStyleSheet(self.stylesheet["style_common"])

        self.show()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
