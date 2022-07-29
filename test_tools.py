import unittest

from tools import SimsTool


class TestTools(unittest.TestCase):
    def test_rune_knight_status(self):
        status: dict[str, int] = SimsTool.get_rune_mastery_best_status(102, False)
        self.assertLessEqual(status['DEX'], 130)
        self.assertLessEqual(status['LUK'], 130)

    def test_rune_knight_status_transcended(self):
        status: dict[str, int] = SimsTool.get_rune_mastery_best_status(102, True)
        self.assertLessEqual(status['DEX'], 130)
        self.assertLessEqual(status['LUK'], 130)

    def test_assassin_cross_status(self):
        status: dict[str, int] = SimsTool.get_poison_creation_best_status(99)
        self.assertLessEqual(status['DEX'], 99)
        self.assertLessEqual(status['LUK'], 99)

    def test_guillotine_status(self):
        status: dict[str, int] = SimsTool.get_poison_creation_best_status(102)
        self.assertLessEqual(status['DEX'], 130)
        self.assertLessEqual(status['LUK'], 130)

    def test_alchemist_status(self):
        status: dict[str, int] = SimsTool.get_potion_creation_best_status(99)
        self.assertLessEqual(status['DEX'], 99)
        self.assertLessEqual(status['LUK'], 99)
