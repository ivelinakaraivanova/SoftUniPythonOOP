from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        players_usernames = [p.username for p in self.players]
        if player.username in players_usernames:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        pl = [p for p in self.players if p.username == player][0]
        self.players.remove(pl)
        self.count -= 1

    def find(self, username: str):
        pl = [p for p in self.players if p.username == username][0]
        return pl
