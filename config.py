# Creates a config object
# Can be read & updated
import json
from time import time 

class Config:

    def __init__(self, config_file_path):
        self.file_path = config_file_path
        self.read_config()

    def read_config(self):
        # Reads the config file and sets the config of the instance
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.config = config

    def update_config(self):
        # Update the config file to values stored in memory
        config_json = json.dumps(self.config)
        f = open(self.file_path, "w")
        f.write(config_json)
        f.close()

    # Getters & Setters
    def set_cols(self, cols):
        self.config["cols"] = cols

    def set_rows(self, rows):
        self.config["rows"] = rows

    def set_time_delay(self, time_delay):
        self.config["time_delay"] = time_delay