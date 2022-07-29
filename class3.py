from player import Class3
from high_class import AssassinCross


class RuneKnight(Class3):
    def __init__(self, level: int, is_transcended: bool = False):
        super().__init__(level, is_transcended)

    def get_rune_creation_success_rate(self) -> float:
        # todo: enhance this formula
        return 71 + self.status['DEX'] / 30 + self.status['LUK'] / 10 + 14 / 10 + 2 - 5


class GuillotineCross(Class3, AssassinCross):
    def __init__(self, level: int, is_transcended: bool = False):
        super().__init__(level, is_transcended)
