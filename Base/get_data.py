import yaml, os


class Get_Data():
    def get_yaml_data(self, file_name):
        with open("./Data" + os.sep +file_name,'r') as f:
           return yaml.load(f)
