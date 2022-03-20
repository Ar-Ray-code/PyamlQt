import sys
import os
import yaml

DEBUG_FLAG = False

class label_configure:
    def __init__(self, yaml_file: str, target_key: str, script_dir:str="") -> None:
        self.stylesheet_str = str()
        self.yaml_file = yaml_file
        self.target_key = target_key

        with open(self.yaml_file, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # exit when no yaml data
        if self.yaml_data is None:
            print("no yaml data")
            sys.exit()
        self.yaml_data = self.yaml_data[self.target_key]

        if "type" in self.yaml_data:
            self.type = self.yaml_data["type"]
        else:
            print("type is undefined.")
            sys.exit()

        if "x_center" in self.yaml_data:
            self.x_center = self.yaml_data["x_center"]
        else:
            self.x_center = 0

        if "y_center" in self.yaml_data:
            self.y_center = self.yaml_data["y_center"]
        else:
            self.y_center = 0
        
        if "width" in self.yaml_data:
            self.width = self.yaml_data["width"]
        else:
            self.width = 50

        if "height" in self.yaml_data:
            self.height = self.yaml_data["height"]
        else:
            self.height = 50

        if "text" in self.yaml_data:
            self.text = self.yaml_data["text"]
        else:
            self.text = ""
        if "font_size" in self.yaml_data:
            self.font_size = self.yaml_data["font_size"]
        else:
            self.font_size = 0

        if "font_color" in self.yaml_data:
            self.font_color = self.yaml_data["font_color"]
        else:
            self.font_color = "#000000"
        
        if "background_color" in self.yaml_data:
            self.background_color = self.yaml_data["background_color"]
        else:
            self.background_color = ""
        
        if "font" in self.yaml_data:
            self.font = self.yaml_data["font"]
        else:
            self.font = "Arial"
        
        if "font_bold" in self.yaml_data:
            self.font_bold = self.yaml_data["font_bold"]
        else:
            self.font_bold = False
        
        if "items" in self.yaml_data:
            self.items = self.yaml_data["items"]
        else:
            self.items = []
        
        if "max" in self.yaml_data:
            self.max = self.yaml_data["max"]
        else:
            self.max = 100
        
        if "min" in self.yaml_data:
            self.min = self.yaml_data["min"]
        else:
            self.min = 0
        
        if "step" in self.yaml_data:
            self.step = self.yaml_data["step"]
        else:
            self.step = 1
        
        if "default" in self.yaml_data:
            self.default = self.yaml_data["default"]
        else:
            self.default = 0
        
        if "path" in self.yaml_data:
            self.path = self.yaml_data["path"]
            if script_dir != "":
                self.path = script_dir + self.path
                self.path = os.path.abspath(self.path)
        else:
            self.path = ""

        self.x = self.x_center - self.width // 2
        self.y = self.y_center - self.height // 2

        # print all
        if DEBUG_FLAG:
            print("==========================================================")
            print("loading " + yaml_file)
            print("type:" + str(self.type))
            print("x_center: " + str(self.x_center))
            print("y_center: " + str(self.y_center))
            print("width: " + str(self.width))
            print("height: " + str(self.height))
            print("text: " + str(self.text))
            print("font_size: " + str(self.font_size))
            print("font_color: " + str(self.font_color))
            print("background_color: " + str(self.background_color))
            print("font: " + str(self.font))
            print("font_bold: " + str(self.font_bold))
            print("items: " + str(self.items))
            print("max: " + str(self.max))
            print("min: " + str(self.min))
            print("step: " + str(self.step))
            print("default: " + str(self.default))
            print("path: " + str(self.path))
            print("==========================================================")