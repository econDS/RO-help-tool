from class2 import Alchemist
from class3 import RuneKnight
from high_class import AssassinCross
from player import Player


class SimsTool:
    @staticmethod
    def get_rune_mastery_best_status(level: int, is_transcended: bool = False) -> dict[str, int]:
        sims: list[Player] = []
        rune_probs: list[float] = []
        rk: RuneKnight = RuneKnight(level, is_transcended)
        for luk in range(1, rk.get_max_status()):
            for dex in range(1, rk.get_max_status()):
                sim = RuneKnight(level, is_transcended)
                sim.up_status('LUK', luk)
                sim.up_status('DEX', dex)
                print(f"simulated for RuneKnight: LUK{sim.status['LUK']} DEX{sim.status['DEX']}")
                sims.append(sim)
                rune_probs.append(sim.get_rune_creation_success_rate())
        best_prob = max(rune_probs)
        best_sim = sims[rune_probs.index(best_prob)]
        print(f"Max probability of Rune Mastery creation at {best_prob:.2f}%")
        print(f"Best status for Rune Knight level {level} and transcended {rk.is_transcended} is:")
        print(best_sim.status)
        return best_sim.status

    @staticmethod
    def get_poison_creation_best_status(level: int) -> dict[str, int]:
        sims: list[Player] = []
        poison_probs: list[float] = []
        ac: AssassinCross = AssassinCross(level)
        for luk in range(1, ac.get_max_status()):
            for dex in range(1, ac.get_max_status()):
                sim = AssassinCross(level)
                sim.up_status('DEX', dex)
                sim.up_status('LUK', luk)
                print(f"simulated for AssassinCross: DEX{sim.status['DEX']} LUK{sim.status['LUK']}")
                sims.append(sim)
                poison_probs.append(sim.get_poison_creation_success_rate())
        best_prob = max(poison_probs)
        best_sim = sims[poison_probs.index(best_prob)]
        print(f"Max probability of Deathly poison creation at {best_prob:.2f}%")
        print(f"Best status for Assassin Cross level {level} and transcended {ac.is_transcended} is:")
        print(best_sim.status)
        return best_sim.status

    @staticmethod
    def get_potion_creation_best_status(level: int) -> dict[str, int]:
        sims: list[Player] = []
        potion_probs: list[float] = []
        al: Alchemist = Alchemist(level)
        for luk in range(1, al.get_max_status()):
            for dex in range(1, al.get_max_status()):
                for intel in range(1, al.get_max_status()):
                    sim = Alchemist(level)
                    sim.up_status('DEX', dex)
                    sim.up_status('LUK', luk)
                    sim.up_status('INT', intel)
                    print(f"simulated for Alchemist: DEX{sim.status['DEX']}"
                          + f" LUK{sim.status['LUK']} INT{sim.status['INT']}")
                    potion_probs.append(sim.get_potion_creation_success_rate())
                    sims.append(sim)
        best_prob = max(potion_probs)
        best_sim = sims[potion_probs.index(best_prob)]
        print(f"Max probability of Potion creation at {best_prob:.2f}%")
        print(f"Best status for Alchemist level {level} and transcended {al.is_transcended} is:")
        print(best_sim.status)
        return best_sim.status
