import json

def read_config():
    # Function to read the configuration file
    # Should probably refactor into a class in the future
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
    


if __name__ == '__main__':
    run_game()