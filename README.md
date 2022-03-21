# PyamlQt（ぴゃむるきゅーと）

[![PyPI version](https://badge.fury.io/py/PyamlQt.svg)](https://badge.fury.io/py/PyamlQt)

- [Zenn「最もシンプルなGUI設計パッケージPyamlQtについて」](https://zenn.dev/array/articles/9617ae0bbd8a80)

PyQt6 configuration in yaml format providing the most simple script.

## Requirements

- yaml
- PyQt6, ( PyQt5 )

## Installation

```bash
pip install PyamlQt
```

<!-- ```bash
git clone https://github.com/Ar-Ray-code/PyamlQt.git
cd PyamlQt
pip3 install -v -e . 
``` -->

## Demo

```bash
python3 examples/chaos.py
```

## Template

See `examples/simple_gui.py`.

```python
import sys
import os

from pyamlqt.create_widgets import create_widgets
import pyamlqt.qt6_switch as qt6_switch

qt6_mode = qt6_switch.qt6

if qt6_mode:
    from PyQt6.QtWidgets import QApplication, QMainWindow
else:
    from PyQt5.QtWidgets import QApplication, QMainWindow

YAML = os.path.join(os.path.dirname(__file__), "../yaml/chaos.yaml")

class MainWindow(QMainWindow):
    def __init__(self):
        self.number = 0
        super().__init__()

        # geometry setting ---
        self.setWindowTitle("Simple GUI")
        self.setGeometry(0, 0, 800, 720)
        
        # Template ==========================================
        self.widgets, self.stylesheet = self.create_all_widgets(YAML)
        for key in self.widgets.keys():
            self.widgets[key].setStyleSheet(self.stylesheet[key])
        # ==============================================

        # --- Your code ----
        # -*-*-*-*-*-*-*-*-*
        # -----------------
        
        self.show()

    # Template ==========================================
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
    # sys.exit(app.exec_())
    sys.exit(app.exec())
```

<!-- Run `python3 <path-to-script>/simple_gui.py`. -->
![](image/simple-gui-480p.png)

## Elements (dev)
In yaml, you can add the following elements defined in PyQt.Widgets This may be added in the future.

- pushbutton : definition of QPushButton
- qlabel : definition of QLabel 
- qlcdnumber : definition of QLCDNumber
- qprogressbar : definition of QProgressBar
- qlineedit : definition of QLineEdit
- qcheckbox : definition of QCheckbox
- qslider : definition of QSlider
- qspinbox : definition of QSpinBox
- qcombobox : definition of QCombobox
- image : definition of QLabel (using image path)
- stylesheet : definition of Stylesheet (define as QLabel and `setHidden=True`)

### YAML format

PyamlQt defines common elements for simplicity. Not all values need to be defined, but if not set, default values will be applied

```yaml
key: # key name (Required for your scripts)
  type: slider # QWidgets
  x_center: 500 # x center point
  y_center: 550 # y center point
  width: 200 # QWidgets width
  height: 50 # QWidgets height
  max: 100 # QObject max value
  min: 0 # QObject min value
  default: 70 # QObject set default value
  text: "Slider" # Text
  font_size: 30 # Text size [px]
  font_color: "#ff0000" # Text color
  font: "Ubuntu" # Text font
  font_bold: false # bold-text option
  items: # Selectable items( Combobox's option )
    - a
    - b
    - c
```

### PyQt5 Mode
If you want to use PyQt5, you have to change the `qt6_switch.py` file.

- Open the file and change the `qt6_mode` variable to `False`.
- `pip3 install PyQt5`
- `pip3 install -v -e .`
