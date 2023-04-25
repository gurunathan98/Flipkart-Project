# yaml_function.py

# program to read a YAML file and get the data out of YAML file

from yaml import load
from yaml.loader import SafeLoader

class Guru_YAML:
   
    def __init__(self, file_name):
        self.file = file_name

    # read the YAML file
    def yaml_reader(self):
        with open(self.file) as file:
            data = load(file, Loader=SafeLoader)
        return data
