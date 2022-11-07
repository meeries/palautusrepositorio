import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_search_finds(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")

    def test_search_doesnt_find(self):
        self.assertAlmostEqual(self.statistics.search("Eiole"), None)

    def test_team_works(self):
        players = self.statistics.team("PIT")
        self.assertEqual(players[0].name, "Lemieux")

    def test_top(self):
        list = self.statistics.top(3)
        self.assertEqual(list[0].name, "Gretzky")
