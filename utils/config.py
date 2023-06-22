import yaml

class Config:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get(self, key):
        keys = key.split('.')
        value = self.config
        for key in keys:
            value = value[key]
        return value
    