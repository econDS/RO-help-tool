from config import Config


class Player:
    class_1_2_max_status: int = 99
    class_3_max_status: int = 130

    def __init__(self, level: int, is_transcended: bool = False):
        self.config = Config()
        self.level: int = level
        self.is_transcended: bool = is_transcended
        self.class_level: int = 1
        self.status_points: int = self.get_status_points()
        self.status: dict[str, int] = {'STR': 1, 'AGI': 1, 'VIT': 1, 'INT': 1, 'DEX': 1, 'LUK': 1}
        self.max_status = self.get_max_status()

    def get_status_points(self):
        if self.is_transcended:
            return self.config.status_point_transcended[self.level]
        return self.config.status_point[self.level]

    def get_max_status(self):
        if self.class_level < 3:
            return self.class_1_2_max_status
        return self.class_3_max_status

    def up_status(self, stat: str, amount: int = 1) -> bool:
        for a in range(amount):
            status_point_required = self.config.raise_status_cost[self.status[stat]]
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

    def reset_status(self):
        self.status = {'STR': 1, 'AGI': 1, 'VIT': 1, 'INT': 1, 'DEX': 1, 'LUK': 1}

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
