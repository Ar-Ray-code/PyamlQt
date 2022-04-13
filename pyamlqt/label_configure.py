import sys
import os
import yaml
import re
import urllib.request

DEBUG_FLAG = True


class label_configure:
    def is_url(self, path: str) -> bool:
        pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if re.match(pattern, path):
            return True
        else:
            return False

    def __init__(self, yaml_file: str, target_key: str, script_dir: str = "") -> None:
        self.stylesheet_str = str()
        self.yaml_file = yaml_file
        self.target_key = target_key

        self.debug = DEBUG_FLAG

        with open(self.yaml_file, 'r') as f:
            self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # exit when no yaml data
        if self.yaml_data is None:
            print("no yaml data")
            sys.exit()
        self.yaml_data = self.yaml_data[self.target_key]

    # include yaml from yaml ---------------------------------------------------
        if "include" in self.yaml_data:
            path = self.yaml_data["include"]["path"]
            key = self.yaml_data["include"]["key"]
            # is url or path
            if self.is_url(path):
                # is url -> save to ~/.cache/pyamlqt/yaml/***.yaml and load it
                # exists ~/.cache/pyamlqt/yaml/***.yaml ?
                if not os.path.exists(os.path.expanduser("~/.cache/pyamlqt/yaml/" + os.path.basename(path))):
                    os.makedirs(os.path.expanduser(
                        "~/.cache/pyamlqt/yaml"), exist_ok=True)
                    urllib.request.urlretrieve(path, os.path.expanduser(
                        "~/.cache/pyamlqt/yaml/") + os.path.basename(path))
                    print("download yaml file: " + path)
                else:
                    print("yaml file is already downloaded (Please delete ~/.cache/pyamlqt/yaml/" +
                          os.path.basename(path) + " to download again)")
                path = os.path.expanduser(
                    "~/.cache/pyamlqt/yaml/") + os.path.basename(path)

            with open(path, 'r') as f:
                self.yaml_data = yaml.load(f, Loader=yaml.FullLoader)
            self.yaml_data = label_configure(path, key, script_dir).yaml_data
            print("yaml_data: " + str(self.yaml_data))
            # return force
            return

    # Using common tag --------------------------------------------------------

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
            self.font_size = 10

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

    # StyleSheet ---------------------------------------------------------------
        if "style" in self.yaml_data:
            # if include key
            if "include" in self.yaml_data["style"]:
                path = self.yaml_data["style"]["include"]["path"]
                key = self.yaml_data["style"]["include"]["key"]
                # is url or path
                if self.is_url(path):
                    # is url -> save to ~/.cache/pyamlqt/yaml/***.yaml and load it
                    # exists ~/.cache/pyamlqt/yaml/***.yaml ?
                    if not os.path.exists(os.path.expanduser("~/.cache/pyamlqt/yaml/" + os.path.basename(path))):
                        os.makedirs(os.path.expanduser(
                            "~/.cache/pyamlqt/yaml"), exist_ok=True)
                        urllib.request.urlretrieve(path, os.path.expanduser(
                            "~/.cache/pyamlqt/yaml/") + os.path.basename(path))
                        print("download yaml file: " + path)
                    else:
                        print("yaml file is already downloaded (Please delete ~/.cache/pyamlqt/yaml/" +
                              os.path.basename(path) + " to download again)")
                    path = os.path.expanduser(
                        "~/.cache/pyamlqt/yaml/") + os.path.basename(path)

                with open(path, 'r') as f:
                    self.stylesheet_str = yaml.load(f, Loader=yaml.FullLoader)
                self.stylesheet_str = label_configure(
                    path, key, script_dir).stylesheet_str
                print("stylesheet_str: " + str(self.stylesheet_str))

            else:
                for key, value in self.yaml_data["style"].items():
                    self.stylesheet_str += key + ": " + str(value) + "; "
        else:
            self.stylesheet_str = ""

    # Label Rect ---------------------------------------------------------------
        if "rect" in self.yaml_data:
            # if include key
            if "include" in self.yaml_data["rect"]:
                path = self.yaml_data["rect"]["include"]["path"]
                key = self.yaml_data["rect"]["include"]["key"]
                # is url or path
                if self.is_url(path):
                    # is url -> save to ~/.cache/pyamlqt/yaml/***.yaml and load it
                    # exists ~/.cache/pyamlqt/yaml/***.yaml ?
                    if not os.path.exists(os.path.expanduser("~/.cache/pyamlqt/yaml/" + os.path.basename(path))):
                        os.makedirs(os.path.expanduser(
                            "~/.cache/pyamlqt/yaml"), exist_ok=True)
                        urllib.request.urlretrieve(path, os.path.expanduser(
                            "~/.cache/pyamlqt/yaml/") + os.path.basename(path))
                        print("download yaml file: " + path)
                    else:
                        print("yaml file is already downloaded (Please delete ~/.cache/pyamlqt/yaml/" +
                              os.path.basename(path) + " to download again)")
                    path = os.path.expanduser(
                        "~/.cache/pyamlqt/yaml/") + os.path.basename(path)

                with open(path, 'r') as f:
                    self.rect_width = yaml.load(f, Loader=yaml.FullLoader)
                self.rect_width = label_configure(path, key, script_dir).rect_width
                self.rect_height = label_configure(path, key, script_dir).rect_height
            else:
                self.rect_width = self.yaml_data["rect"]["width"]
                self.rect_height = self.yaml_data["rect"]["height"]
        else:
            pass
            self.rect_width = self.width
            self.rect_height = self.height

        self.width = self.rect_width
        self.height = self.rect_height

    # debug ---------------------------------------------------------------
        if "debug" in self.yaml_data:
            self.debug = self.yaml_data["debug"]
        else:
            self.debug = False

        self.x = self.x_center - self.width // 2
        self.y = self.y_center - self.height // 2

        # print all
        if self.debug:
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
            print("stylesheet_str: " + str(self.stylesheet_str))
            print("==========================================================")
