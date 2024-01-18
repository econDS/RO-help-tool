import json


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.init_config()
        return cls._instance

    def init_config(self):
        self.point_gain = self.load_config('config/point_gain.json')
        self.status_point = self.load_config('config/status_point.json')
        self.status_point_transcended = self.load_config('config/status_point_transcended.json')
        self.raise_status_cost = self.load_config('config/raise_status_cost.json')

    @staticmethod
    def load_config(file_path):
        with open(file_path) as f:
            return {int(k): v for k, v in json.load(f).items()}
