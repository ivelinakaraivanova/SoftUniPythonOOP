from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker_bonus = sum([c.health_points for c in attacker.card_repository.cards])
        attacker.health += attacker_bonus
        enemy_bonus = sum([c.health_points for c in enemy.card_repository.cards])
        enemy.health += enemy_bonus

        for c in attacker.card_repository.cards:
            enemy.take_damage(c.damage_points)
            if enemy.is_dead:
                return

        for c in enemy.card_repository.cards:
            attacker.take_damage(c.damage_points)
            if attacker.is_dead:
                return
