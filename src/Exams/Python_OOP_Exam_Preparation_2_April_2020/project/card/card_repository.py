from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        cards_names = [c.name for c in self.cards]
        if card.name in cards_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        cr = [c for c in self.cards if c.name == card][0]
        self.cards.remove(cr)
        self.count -= 1

    def find(self, name: str):
        cr = [c for c in self.cards if c.name == name]
        if cr:
            return cr[0]
