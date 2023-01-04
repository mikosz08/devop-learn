
from characters.player.Player import Player
from characters.player.PlayerStats import PlayerStats
from data.default_statistics import *
from utils.Logger import Logger

import unittest


class TestCharacter(unittest.TestCase):

    def test_character_stats(self):
        player = Player(PlayerStats())
        player_stats = player.get_stats()
        self.assertEqual(player_stats.CHARACTER_CLASS,
                         DEFAULT_CHARACTER_CLASS,
                         f"Should be {DEFAULT_CHARACTER_CLASS}")
        self.assertEqual(player_stats.ATT, DEFAULT_ATT,
                         f"Should be {DEFAULT_ATT}")
        self.assertEqual(player_stats.DEF, DEFAULT_DEF,
                         f"Should be {DEFAULT_DEF}")
        self.assertEqual(player_stats.HP, DEFAULT_HP,
                         f"Should be {DEFAULT_HP}")
        self.assertEqual(player_stats.MP, DEFAULT_MP,
                         f"Should be {DEFAULT_MP}")
        self.assertEqual(player_stats.LEVEL, DEFAULT_LEVEL,
                         f"Should be {DEFAULT_LEVEL}")
        self.assertEqual(player_stats.RACE, DEFAULT_RACE,
                         f"Should be {DEFAULT_RACE}")
        self.assertEqual(player_stats.SPD, DEFAULT_SPD,
                         f"Should be {DEFAULT_SPD}")


if __name__ == '__main__':
    unittest.main()
