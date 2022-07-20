import json

__author__ = "Damian Mann, Sarah Puglisi, William Todd, Vinh Phuc Hoang"
__copyright__ = "Copyright 2022, Griffith University"
__license__ = "MIT"
__version__ = "0.1"

def read_config():
    # Function to read the configuration file
    # Should probably refactor into a class in the future
    # A class would allow us to have read/write/update methods
    # Returns: Dictionary or False
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        config = config[0] #change from list to dict
        return config
    except:
        return False

def run_game():
    config = read_config()
    if (not config):
        print("Error reading config file")
        exit()
    # Run game
    


if __name__ == '__main__':
    run_game()