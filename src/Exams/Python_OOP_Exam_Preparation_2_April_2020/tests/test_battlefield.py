import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.player1 = Advanced('Adi')
        self.player2 = Beginner('Bobi')
        self.battle_field = BattleField()

    def test_fight_player_is_dead(self):
        self.player1.health = 0
        with self.assertRaises(ValueError) as err:
            self.battle_field.fight(self.player1, self.player2)
        self.assertEqual(str(err.exception), "Player is dead!")

    def test_fight_player_health_in_fight(self):
        self.battle_field.fight(self.player2, self.player1)
        self.assertEqual(self.player2.health, 90)
        self.assertEqual(self.player1.health, 250)

    def test_players_cards_damage_points(self):
        t_card_1 = TrapCard('TA')
        m_card_2 = MagicCard("ME")
        self.player2.card_repository.add(t_card_1)
        self.player1.card_repository.add(m_card_2)
        self.battle_field.fight(self.player2, self.player1)
        self.assertEqual(self.player2.health, 90)
        self.assertEqual(self.player1.health, 180)

    def test_fight_player_dies(self):
        t_card_1 = TrapCard('TA')
        m_card_2 = MagicCard("ME")
        self.player2.card_repository.add(t_card_1)
        self.player1.card_repository.add(m_card_2)
        self.battle_field.fight(self.player2, self.player1)
        self.assertEqual(self.player2.health, 90)
        self.assertEqual(self.player1.health, 180)
        self.battle_field.fight(self.player2, self.player1)
        self.assertEqual(self.player2.health, 130)
        self.assertEqual(self.player1.health, 80)
        with self.assertRaises(ValueError) as err:
            self.battle_field.fight(self.player2, self.player1)
        self.assertEqual(str(err.exception), "Player's health bonus cannot be less than zero.")
