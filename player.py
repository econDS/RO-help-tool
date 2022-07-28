import json

# load config files
with open('config/point_gain.json') as f:
    point_gain_raw: dict[str, int] = json.load(f)
    point_gain: dict[int, int] = {int(k): v for k, v in point_gain_raw.items()}
with open('config/status_point.json') as f:
    status_point_raw: dict[str, int] = json.load(f)
    status_point: dict[int, int] = {int(k): v for k, v in status_point_raw.items()}
with open('config/status_point_transcended.json') as f:
    status_point_transcended_raw: dict[str, int] = json.load(f)
    status_point_transcended: dict[int, int] = {int(k): v for k, v in status_point_transcended_raw.items()}
with open('config/raise_status_cost.json') as f:
    raise_status_cost_raw: dict[str, int] = json.load(f)
    raise_status_cost: dict[int, int] = {int(k): v for k, v in raise_status_cost_raw.items()}


class Player:
    class_1_2_max_status: int = 99
    class_3_max_status: int = 130

    def __init__(self, level: int, is_transcended: bool = False):
        self.level: int = level
        self.is_transcended: bool = is_transcended
        self.class_level: int = 1
        self.status_points: int = self.get_status_points()
        self.status: dict[str, int] = {'STR': 1, 'AGI': 1, 'VIT': 1, 'INT': 1, 'DEX': 1, 'LUK': 1}
        self.max_status = self.get_max_status()

    def get_status_points(self):
        if self.is_transcended:
            return status_point_transcended[self.level]
        return status_point[self.level]

    def get_max_status(self):
        if self.class_level < 3:
            return self.class_1_2_max_status
        return self.class_3_max_status

    def up_status(self, stat: str, amount: int = 1) -> bool:
        for a in range(amount):
            status_point_required = raise_status_cost[self.status[stat]]
            if self.status[stat] >= self.class_3_max_status:
                print('Max status reached')
                return False
            if self.class_level < 3 and self.status[stat] >= self.class_1_2_max_status:
                print('Max status reached')
                return False
            if status_point_required > self.status_points:
                print('Not enough status points')
                return False
            self.status[stat] += 1
            self.status_points -= status_point_required
        return True


class Class1(Player):
    def __init__(self, level: int):
        super().__init__(level)
        self.class_level: int = 1


class Class2(Player):
    def __init__(self, level: int):
        super().__init__(level)
        self.class_level: int = 2


class Class3(Player):
    def __init__(self, level: int, is_transcended: bool = False):
        super().__init__(level, is_transcended)
        self.class_level: int = 3


class TranscendedClass(Player):
    def __init__(self, level: int):
        super().__init__(level, True)
