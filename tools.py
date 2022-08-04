from itertools import product
from typing import TypeVar

from class2 import Alchemist
from class3 import RuneKnight, GuillotineCross, Genetic
from high_class import AssassinCross
from player import Class2

PlayerFamily = TypeVar('PlayerFamily', Class2, Alchemist, RuneKnight, GuillotineCross, AssassinCross, Genetic)


def simulate(status_list: list[str], max_status: int, sim: PlayerFamily) -> tuple[list[PlayerFamily], list[float]]:
    sims: list[PlayerFamily] = []
    probs: list[float] = []
    for status_combination in product(range(max_status), repeat=len(status_list)):
        klass = globals()[type(sim).__name__]
        sim = klass(sim.level, sim.is_transcended)
        for status in status_list:
            sim.up_status(status, status_combination[status_list.index(status)])
            sims.append(sim)
            if type(sim).__name__ == 'RuneKnight':
                probs.append(sim.get_rune_creation_success_rate())
            elif type(sim).__name__ == 'AssassinCross':
                probs.append(sim.get_poison_creation_success_rate())
            elif type(sim).__name__ == 'Alchemist':
                probs.append(sim.get_potion_creation_success_rate())
    return sims, probs


class SimsTool:
    @staticmethod
    def get_rune_mastery_best_status(level: int, is_transcended: bool = False) -> dict[str, int]:
        rk: RuneKnight = RuneKnight(level, is_transcended)
        sims, probs = simulate(['LUK', 'DEX'], rk.get_max_status(), rk)
        print(f"Max probability of Rune Mastery creation at {(best_prob :=  max(probs)):.2f}%")
        print(f"Best status for Rune Knight level {level} and transcended {rk.is_transcended} is:")
        print(best_status := sims[probs.index(best_prob)].status)
        return best_status

    @staticmethod
    def get_poison_creation_best_status(level: int,
                                        is_transcended: bool = False,
                                        is_class3: bool = False) -> dict[str, int]:
        sim = GuillotineCross(level, is_transcended) if is_class3 else AssassinCross(level)
        sims, probs = simulate(['LUK', 'DEX'], sim.get_max_status(), sim)
        print(f"Max probability of Deathly poison creation at {(best_prob := max(probs)):.2f}%")
        print(f"Best status for Assassin Cross level {level} and transcended {sim.is_transcended} is:")
        print(best_status := sims[probs.index(best_prob)].status)
        return best_status

    @staticmethod
    def get_potion_creation_best_status(level: int,
                                        is_transcended: bool = False,
                                        is_class3: bool = False) -> dict[str, int]:
        sim = GuillotineCross(level, is_transcended) if is_class3 else Alchemist(level)
        sims, probs = simulate(['STR', 'INT'], sim.get_max_status(), sim)
        print(f"Max probability of Potion creation at {(best_prob := max(probs)):.2f}%")
        print(f"Best status for Alchemist level {level} and transcended {sim.is_transcended} is:")
        print(best_status := sims[probs.index(best_prob)].status)
        return best_status
