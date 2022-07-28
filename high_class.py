from player import Class2, TranscendedClass


class AssassinCross(Class2, TranscendedClass):
    def __init__(self, level: int):
        super().__init__(level)

    def get_poison_creation_success_rate(self) -> float:
        # todo: enhance this formula
        return 20 + self.status['DEX'] * 0.4 + self.status['LUK'] * 0.2
