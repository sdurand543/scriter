import os

class serial_dict():
    def __init__(self, dict_path):
        self.dict_path = dict_path

    def contains_key(self, key):
        entry_path = os.path.join(self.dict_path, key)
        return os.path.isfile(entry_path)
        
    def __getitem__(self, key):
        entry_path = os.path.join(self.dict_path, key)
        key_file = open(entry_path, "r")
        value_data = key_file.read()
        key_file.close()
        return value_data
    
    def __setitem__(self, key, value_data):
        entry_path = os.path.join(self.dict_path, key)
        key_file = open(entry_path, "w")
        key_file.write(str(value_data))
        key_file.close()
