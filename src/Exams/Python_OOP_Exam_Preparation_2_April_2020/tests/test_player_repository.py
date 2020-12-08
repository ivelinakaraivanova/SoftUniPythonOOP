import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pl_rep = PlayerRepository()

    def test_init(self):
        self.assertEqual(self.pl_rep.count, 0)
        self.assertEqual(self.pl_rep.players, [])

    def test_add_player_raises_value_error(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        with self.assertRaises(ValueError) as err:
            self.pl_rep.add(beginner)
        self.assertEqual(str(err.exception), "Player Riki already exists!")

    def test_add_player(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        self.assertEqual(self.pl_rep.players, [beginner])

    def test_add_player_count(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        self.assertEqual(self.pl_rep.count, 1)

    def test_remove_player_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.pl_rep.remove("")
        self.assertEqual(str(err.exception), "Player cannot be an empty string!")

    def test_remove_player(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        self.pl_rep.remove("Riki")
        self.assertEqual(self.pl_rep.players, [])

    def test_remove_player_count(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        self.pl_rep.remove("Riki")
        self.assertEqual(self.pl_rep.count, 0)

    def test_find_player(self):
        beginner = Beginner('Riki')
        self.pl_rep.add(beginner)
        self.assertEqual(self.pl_rep.find("Riki"), beginner)
