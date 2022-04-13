from .label_configure import label_configure
import pyamlqt.qt6_switch as qt6_switch

qt6_mode = qt6_switch.qt6

if qt6_mode:
    from PyQt6 import QtCore, QtWidgets, QtGui
    print("qt6 mode")
else:
    from PyQt5 import QtCore, QtWidgets, QtGui
    print("qt5 mode")


# object list ---------------------------------------------------------------
# create_lcdnumber    create_slider
# create_checkbox     create_lineedit
# create_combobox     create_progressbar
# create_label        create_pushbutton
# create_spinbox
# ----------------------------------------------------------------------------

class create_widgets:
    def __init__(self):
        pass

    def create(self, yaml_path: str, key: str, script_dir: str = ""):
        config = label_configure(yaml_path, key, script_dir)

        if config.type == "qpushbutton":
            target = QtWidgets.QPushButton(self)
            target.setText(config.text)
            target.setFont(QtGui.QFont(config.font, config.font_size))

        elif config.type == "qlabel":
            target = QtWidgets.QLabel(self)
            target.setText(config.text)
            target.setFont(QtGui.QFont(config.font, config.font_size))

            if qt6_mode:
                target.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                target.setAlignment(QtCore.Qt.AlignCenter)

        elif config.type == "qlcdnumber":
            target = QtWidgets.QLCDNumber(self)
            target.setFont(QtGui.QFont(config.font, config.font_size))

        elif config.type == "qprogressbar":
            target = QtWidgets.QProgressBar(self)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            if qt6_mode:
                target.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                target.setAlignment(QtCore.Qt.AlignCenter)

        elif config.type == "qlineedit":
            target = QtWidgets.QLineEdit(self)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            if qt6_mode:
                target.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            else:
                target.setAlignment(QtCore.Qt.AlignTop)

        elif config.type == "qcheckbox":
            target = QtWidgets.QCheckBox(self)
            target.resize(config.width, config.height)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            target.setText(config.text)

        elif config.type == "qslider":
            target = QtWidgets.QSlider(self)
            target.resize(config.width, config.height)

            if config.height > config.width:
                if qt6_mode:
                    target.setOrientation(QtCore.Qt.Orientation.Vertical)
                else:
                    target.setOrientation(QtCore.Qt.Vertical)
            else:
                if qt6_mode:
                    target.setOrientation(QtCore.Qt.Orientation.Horizontal)
                else:
                    target.setOrientation(QtCore.Qt.Horizontal)
            target.setMinimum(config.min)
            target.setMaximum(config.max)
            target.setValue(config.default)
            target.setFont(QtGui.QFont(config.font, config.font_size))

        elif config.type == "qspinbox":
            target = QtWidgets.QSpinBox(self)
            target.resize(config.width, config.height)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            if qt6_mode:
                target.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                target.setAlignment(QtCore.Qt.AlignCenter)

        elif config.type == "qcombobox":
            target = QtWidgets.QComboBox(self)
            target.resize(config.width, config.height)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            for items in config.items:
                target.addItem(items)

        elif config.type == "image":
            target = QtWidgets.QLabel(self)
            target.setGeometry(config.x, config.y, config.width, config.height)
            target.setFont(QtGui.QFont(config.font, config.font_size))
            if qt6_mode:
                target.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                target.setAlignment(QtCore.Qt.AlignCenter)

        elif config.type == "stylesheet":
            target = QtWidgets.QLabel(self)
            target.setHidden(True)

        else:
            print(config.type + " is not defined")
            exit(1)

        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        stylesheet_str = config.stylesheet_str
        # stylesheet_str
        return tuple((target, stylesheet_str))

# # Template  ================================================================
#     def create_all_widgets(self, yaml_path: str) -> dict:
#         widgets, stylesheet_str = dict(), dict()
#         with open(yaml_path, 'r') as f:
#             self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)

#             for key in self.yaml_data:
#                 data = create_widgets.create(self, yaml_path, key, os.path.abspath(os.path.dirname(__file__)) + "/../")
#                 widgets[key], stylesheet_str[key] = data[0], data[1]

#         return widgets, stylesheet_str
# # =========================================================================
