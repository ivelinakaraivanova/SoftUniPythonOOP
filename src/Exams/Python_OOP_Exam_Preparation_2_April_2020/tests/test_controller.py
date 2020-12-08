import unittest

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_add_player(self):
        self.assertEqual(self.controller.player_repository.count, 0)
        result = self.controller.add_player("Beginner", 'Begi')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(result, "Successfully added player of type Beginner with username: Begi")

    def test_add_card(self):
        self.assertEqual(self.controller.card_repository.count, 0)
        result = self.controller.add_card("Magic", "M")
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(result, "Successfully added card of type MagicCard with name: M")

    def test_add_player_card(self):
        self.controller.add_player("Beginner", 'Begi')
        self.controller.add_card("Magic", "M")
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(self.controller.card_repository.count, 1)
        result = self.controller.add_player_card("Begi", "M")
        self.assertEqual(result, "Successfully added card: M to user: Begi")

    def test_fight(self):
        self.controller.add_player("Advanced", "Adi")
        self.controller.add_player("Beginner", "Bobi")
        result = self.controller.fight("Adi", 'Bobi')
        self.assertEqual(result, "Attack user health 250 - Enemy user health 90")

    def test_report(self):
        player1 = Advanced('Adi')
        player2 = Beginner('Bobi')
        t_card_1 = TrapCard('TA')
        m_card_2 = MagicCard("ME")
        player2.card_repository.add(t_card_1)
        player1.card_repository.add(m_card_2)
        self.controller.player_repository.add(player2)
        self.controller.player_repository.add(player1)
        result = self.controller.report()
        self.assertEqual(result, "Username: Bobi - Health: 50 - Cards 1\n### Card: TA - Damage: 120\n"
                                 "Username: Adi - Health: 250 - Cards 1\n### Card: ME - Damage: 5\n")
