from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from .label_configure import label_configure

# object list ---------------------------------------------------------------
# create_lcdnumber    create_slider
# create_checkbox     create_lineedit 
# create_combobox     create_progressbar
# create_label        create_pushbutton
# create_spinbox
# ----------------------------------------------------------------------------

def create_stylesheet_str(yaml_path: str, key: str, script_dir:str = "") -> str:
    configure = label_configure(yaml_path, key, script_dir)
    stylesheet_str = str()

    if configure.font_color != "":
        stylesheet_str += "color: " + configure.font_color + ";"
    if configure.font_bold:
        stylesheet_str += "font-weight: bold;"
    if configure.background_color != "":
        stylesheet_str += "background-color: " + configure.background_color + "; "
    if configure.path != "":
        stylesheet_str += "background-image: url(" + configure.path + "); "
    
    return stylesheet_str

class create_widgets:
    def __init__(self):
        pass

    # return qpushbutton, str
    def create_pushbutton(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QPushButton, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QPushButton(self)
        target.setText(config.text)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_label(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QLabel, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QLabel(self)
        target.setText(config.text)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_lcdnumber(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QLCDNumber, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QLCDNumber(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_progressbar(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QProgressBar, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QProgressBar(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_combobox(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QComboBox, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QComboBox(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_lineedit(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QLineEdit, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QLineEdit(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_checkbox(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QCheckBox, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QCheckBox(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_slider(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QSlider, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QSlider(self)
        target.resize(config.width, config.height)
        
        if config.height > config.width:
            target.setOrientation(QtCore.Qt.Vertical)
        else:
            target.setOrientation(QtCore.Qt.Horizontal)
        
        target.setMinimum(config.min)
        target.setMaximum(config.max)
        target.setValue(config.default)

        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    def create_spinbox(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QSpinBox, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QSpinBox(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        return tuple((target , stylesheet_str))

    # QComboBox
    def create_combobox(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QComboBox, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QComboBox(self)

        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        # set target items
        for items in config.items:
            target.addItem(items)
        return tuple((target , stylesheet_str))
    
    # QLineEdit
    def create_lineedit(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QLineEdit, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QLineEdit(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        # AlignTop
        target.setAlignment(QtCore.Qt.AlignTop)
        return tuple((target , stylesheet_str))
    
    # QCheckBox
    def create_checkbox(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QCheckBox, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QCheckBox(self)
        target.resize(config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        # target.setAlignment(QtCore.Qt.AlignCenter)
        stylesheet_str = create_stylesheet_str(yaml_path, key)
        # set text
        target.setText(config.text)
        return tuple((target , stylesheet_str))
    # Qlabel
    def create_imagelabel(self, yaml_path: str, key: str, script_dir:str="") -> tuple((QtWidgets.QLabel, str)):
        config = label_configure(yaml_path, key)
        target = QtWidgets.QLabel(self)
        target.setGeometry(config.x, config.y, config.width, config.height)
        target.move(config.x, config.y)
        target.setFont(QtGui.QFont(config.font, config.font_size))
        target.setAlignment(QtCore.Qt.AlignCenter)
        
        stylesheet_str = create_stylesheet_str(yaml_path, key, script_dir)
        return tuple((target , stylesheet_str))


    # # Template ================================================================
    # def create_all_widgets(self, yaml_path: str) -> dict:
    #     widgets = dict()
    #     stylesheet_str = dict()
    #     data = tuple()

    #     with open(yaml_path, 'r') as f:
    #         self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        
    #         for key in self.yaml_data:
    #             if self.yaml_data[key]['type'] == 'pushbutton':
    #                 data = create_widgets.create_pushbutton(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'label':
    #                 data = create_widgets.create_label(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'lcdnumber':
    #                 data = create_widgets.create_lcdnumber(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'spinbox':
    #                 data = create_widgets.create_spinbox(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'progressbar':
    #                 data = create_widgets.create_progressbar(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'combobox':
    #                 data = create_widgets.create_combobox(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'lineedit':
    #                 data = create_widgets.create_lineedit(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'checkbox':
    #                 data = create_widgets.create_checkbox(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'slider':
    #                 data = create_widgets.create_slider(self, yaml_path, key)
    #             elif self.yaml_data[key]['type'] == 'image':
    #                 data = create_widgets.create_imagelabel(self, yaml_path, key, os.path.abspath(os.path.dirname(__file__)) + "/../")
                    
    #             else:
    #                 print ('missing type')
    #             widgets[key] = data[0]
    #             stylesheet_str[key] = data[1]

    #     return widgets, stylesheet_str
    # # =========================================================================