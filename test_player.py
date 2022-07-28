import unittest

from class2 import Alchemist
from class3 import RuneKnight
from high_class import AssassinCross


class TestPlayer(unittest.TestCase):
    class_1_2_max_status = 99
    class_3_max_status = 130

    def test_class_1_2_can_up_status(self):
        sim = Alchemist(60)
        expected: bool = sim.up_status('STR', 1)
        self.assertTrue(expected)

    def test_class3_can_up_status(self):
        sim: RuneKnight = RuneKnight(102, False)
        expected: bool = sim.up_status('STR', 1)
        self.assertTrue(expected)

    def test_class_1_2_cannot_up_excess_max_status(self):
        sim: AssassinCross = AssassinCross(60)
        sim.status['STR'] = self.class_1_2_max_status
        expected: bool = sim.up_status('STR', 1)
        self.assertFalse(expected)

    def test_class3_cannot_up_excess_max_status(self):
        sim: RuneKnight = RuneKnight(102, False)
        sim.status['STR'] = self.class_3_max_status
        expected: bool = sim.up_status('STR', 1)
        self.assertFalse(expected)

    def test_has_correct_data(self):
        al: Alchemist = Alchemist(60)
        class_level: int = al.class_level
        self.assertEqual(class_level, 2)

        ac: AssassinCross = AssassinCross(60)
        class_level: int = ac.class_level
        self.assertEqual(class_level, 2)

        rk: RuneKnight = RuneKnight(102, False)
        class_level: int = rk.class_level
        self.assertEqual(class_level, 3)


if __name__ == '__main__':
    unittest.main()
