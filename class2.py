from player import Class2


class Alchemist(Class2):
    def __init__(self, level: int):
        super().__init__(level)

    def get_potion_creation_success_rate(self) -> float:
        # todo: enhance this formula
        return 40 + 70 * 0.2 + self.status['DEX'] * 0.1 + self.status['LUK'] * 0.1 + self.status['INT'] * 0.05
